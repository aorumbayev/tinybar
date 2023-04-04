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
    ]
)
