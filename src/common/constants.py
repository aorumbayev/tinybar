from src.common.models import ASA
from src.common.utils import load_tinybar_data

LEDGER_TYPE = "MainNet"

ALGO = ASA(id=0, decimals=6, unit_name="ALGO", name="ALGO")
USDC = ASA(id=31566704, decimals=6, unit_name="USDC", name="USDC")

TINYBAR_DATA_PATH = "assets.tinybar"

_data = load_tinybar_data(TINYBAR_DATA_PATH)

TINYBAR_ASSETS_DB = (
    _data
    if _data
    else [
        USDC,
        ASA(id=384303832, decimals=6, unit_name="AKITA", name="AKITA INU TOKEN"),
        ASA(id=27165954, decimals=6, unit_name="PLANETS", name="PLANET"),
        ASA(id=287867876, decimals=6, unit_name="OPUL", name="OPULOUS"),
        ASA(id=233939122, decimals=6, unit_name="AWT", name="ALGOWORLD TOKEN"),
        ASA(id=226701642, decimals=6, unit_name="YLDY", name="YIELDLY"),

    ]
)
