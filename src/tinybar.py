import threading
from typing import Dict, List

import rumps
from tinyman.v1.client import TinymanClient, TinymanMainnetClient, TinymanTestnetClient

from src.common.constants import LEDGER_TYPE, TinyBarAsaDb


class TinyBar(rumps.App):
    def __init__(self):
        super(TinyBar, self).__init__(name="TinyBar")

        self.tinyman_client: TinymanClient = (
            TinymanMainnetClient()
            if LEDGER_TYPE.lower() == "mainnet"
            else TinymanTestnetClient()
        )

        self.top_asas: List[Dict[str, TinyBarAsaDb]] = {
            "USDC": TinyBarAsaDb.USDC,
            "YLDLY": TinyBarAsaDb.YIELDLY,
            "AKITA": TinyBarAsaDb.AKITA_INU_TOKEN,
            "PLANETS": TinyBarAsaDb.PLANETS,
            "OPUL": TinyBarAsaDb.OPULOUS,
            "AWT": TinyBarAsaDb.AWT,
        }

        self.asa = self.top_asas["USDC"]
        self.asa_title = self.asa.name

        self.cur_sender = None

    @rumps.clicked("AWT")
    @rumps.clicked("OPUL")
    @rumps.clicked("PLANETS")
    @rumps.clicked("AKITA")
    @rumps.clicked("YLDLY")
    @rumps.clicked("USDC")
    def changeAsa(self, sender):
        self.title = f" 🔍 {sender.title}"
        self.asa = self.top_asas[sender.title]
        self.asa_title = sender.title
        self.getAsaPrice()

    @rumps.timer(60)
    def updateStockPrice(self, sender):
        thread = threading.Thread(target=self.getAsaPrice)
        thread.start()

    def getAsaPrice(self):
        algo = self.tinyman_client.fetch_asset(TinyBarAsaDb.ALGO.value)
        asa = self.tinyman_client.fetch_asset(self.asa.value)
        usdc = self.tinyman_client.fetch_asset(TinyBarAsaDb.USDC.value)

        # Fetch the pool for selected asa and get output algo value
        pool = self.tinyman_client.fetch_pool(algo, asa)
        quote = pool.fetch_fixed_input_swap_quote(
            asa(1 * pow(10, asa.decimals)), slippage=0
        )
        price_in_algo = quote.amount_out.amount / 1e6

        # Fetch usdc pool and get usdc equivalent of algo
        algo_usdc_pool = self.tinyman_client.fetch_pool(algo, usdc)
        usdc_quote = algo_usdc_pool.fetch_fixed_input_swap_quote(
            algo(price_in_algo * 1e6), slippage=0
        )
        price = round(usdc_quote.amount_out.amount / 1e6, 4)

        self.title = f"{self.asa_title}/{algo.name}: {price} 💰"


if __name__ == "__main__":
    TinyBar().run()
