import threading

import rumps
from algosdk.v2client.algod import AlgodClient
from tinyman.v2.client import (
    BaseTinymanClient,
    TinymanV2MainnetClient,
    TinymanV2TestnetClient,
)

from src.common.constants import (
    ALGO,
    LEDGER_TYPE,
    TINYBAR_ASSETS_DB,
    TINYBAR_DATA_PATH,
    USDC,
)
from src.common.models import ASA
from src.common.utils import save_tinybar_data

ICON_PATH = "icon.png"
ALGOD_URL = "https://mainnet-api.algonode.cloud"

algod = AlgodClient("", ALGOD_URL, headers={"User-Agent": "algosdk"})


class TinyBar(rumps.App):
    def __init__(self):
        super(TinyBar, self).__init__(name="TinyBar")

        ### Clients setup
        self.tinyman_client: BaseTinymanClient = (
            TinymanV2MainnetClient(
                algod,
            )
            if LEDGER_TYPE.lower() == "mainnet"
            else TinymanV2TestnetClient()
        )

        self.asas = TINYBAR_ASSETS_DB
        self.asa: ASA = TINYBAR_ASSETS_DB[0]

        ### Menu setup
        self.search_menuitem: rumps.MenuItem = rumps.MenuItem("➕ Add ASA")
        self.menu.add(self.search_menuitem)

        self.explorer_menuitem: rumps.MenuItem = rumps.MenuItem("🔎 Explorer")
        self.menu.add(self.explorer_menuitem)

        for asa in self.asas:
            self.menu.add(rumps.MenuItem(asa.unit_name, callback=self._changeAsa))

        self.about_menuitem: rumps.MenuItem = rumps.MenuItem("ℹ️ About")
        self.menu.add(self.about_menuitem)

    def _changeAsa(self, sender):
        self.title = f" 🔍 {sender.title}"
        self.asa = [asa for asa in self.asas if asa.unit_name == sender.title][0]
        self.getAsaPrice()

    def _save_asa_data(self, asa: ASA):
        self.asas.append(asa)
        save_tinybar_data(TINYBAR_DATA_PATH, self.asas)

    @rumps.clicked("➕ Add ASA")
    def search(self, sender):
        window = rumps.Window(
            f"Current: {self.asa.unit_name} ({self.asa.id})",
            "Enter asset ID (aka ASA ID)...",
        )
        window.icon = ICON_PATH
        response = window.run()

        try:
            asa_info = self.tinyman_client.algod.asset_info(int(response.text))
            self.asa = ASA(
                id=asa_info["index"],
                decimals=asa_info["params"]["decimals"],
                unit_name=asa_info["params"]["unit-name"],
                name=asa_info["params"]["name"],
            )
            self._save_asa_data(self.asa)
            self.getAsaPrice()
        except Exception:
            self.title = "Invalid ASA, try again..."
            self.asa = TINYBAR_ASSETS_DB[0]

    @rumps.clicked("🔎 Explorer")
    def search(self, sender):
        window = rumps.Window(
            f"Current: {self.asa.unit_name} ({self.asa.id})",
            "Enter asset ID (aka ASA ID)...",
        )
        window.icon = ICON_PATH
        response = window.run()

        try:
            asa_info = self.tinyman_client.algod.asset_info(int(response.text))
            asa = ASA(
                id=asa_info["index"],
                decimals=asa_info["params"]["decimals"],
                unit_name=asa_info["params"]["unit-name"],
                name=asa_info["params"]["name"],
                manager=asa_info["params"]["manager"],
                reserve=asa_info["params"]["reserve"],
                freeze=asa_info["params"]["freeze"],
                creator=asa_info["params"]["creator"],
                total=asa_info["params"]["total"],
                url=asa_info["params"]["url"],
            )
            message = (
                f"ID: {asa.id}\n"
                f"Unit Name: {asa.unit_name}\n"
                f"Name: {asa.name}\n"
                f"Total: {asa.total}\n"
                f"URL: {asa.url}\n"
                f"Creator: {asa.creator}\n"
                f"Reserve: {asa.reserve}\n"
                f"Manager: {asa.freeze}\n"
                f"Manager: {asa.manager}\n"
                f"https://algoscan.app/asset/{asa.id}"
            )
            rumps.alert(
                title="AlgoScan URL",
                message=message,
                ok=None,
                cancel=None,
                icon_path=ICON_PATH,
            )
        except Exception:
            self.title = "Invalid ASA, try again..."
            self.asa = TINYBAR_ASSETS_DB[0]

    @rumps.clicked("ℹ️ About")
    def about(self, _):
        rumps.alert(
            title="TinyBar App",
            message="Version 0.4.0 - Apr 2023 by @aorumbayev\nhttps://github.com/aorumbayev/tinybar\n\nTracking TinyMan asset prices from your MacOS menu bar\nhas never been easier!\n\n* The base currency is ALGO, app always displays USDC equivalent to selected ALGO amount from selected ASA/ALGO pair.\n\n* Refresh rate is every 60 seconds.\n\nUpdates are currently manual, refer to repo to get latest...\n\nLicensed under MIT.\n\nrumps licensed under BSD 3-Clause.",
            ok=None,
            cancel=None,
            icon_path=ICON_PATH,
        )

    @rumps.timer(360)
    def updateAsaPrice(self, _):
        thread = threading.Thread(target=self.getAsaPrice)
        thread.start()

    def getAsaPrice(self):
        try:
            algo = self.tinyman_client.fetch_asset(ALGO.id)
            asset = self.tinyman_client.fetch_asset(self.asa.id)
            usdc = self.tinyman_client.fetch_asset(USDC.id)

            # Fetch the pool for selected asa and get output algo value
            pool = self.tinyman_client.fetch_pool(algo, asset)
            quote = pool.fetch_fixed_input_swap_quote(
                asset(1 * pow(10, asset.decimals)), slippage=0.01
            )
            price_in_algo = quote.amount_out.amount

            # Fetch usdc pool and get usdc equivalent of algo
            algo_usdc_pool = self.tinyman_client.fetch_pool(algo, usdc)
            usdc_quote = algo_usdc_pool.fetch_fixed_input_swap_quote(
                algo(price_in_algo), slippage=0.01
            )
            price = round(usdc_quote.amount_out.amount / 1e6, 4)

            self.title = f"|{self.asa.unit_name}|{algo.unit_name}: ${price}|"
        except Exception:
            self.title = "Tinyman error, please retry"
            if not self.asa:
                self.asa = TINYBAR_ASSETS_DB[0]


if __name__ == "__main__":
    TinyBar().run()
