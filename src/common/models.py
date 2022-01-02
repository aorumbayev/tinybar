from pydantic import BaseModel


class TinymanPoolStats(BaseModel):
    price: str
    price_with_slippage: str
    swap_type: str
    swap_fees: str
    slippage: str


class ASA(BaseModel):
    id: int
    decimals: int
    unit_name: str
    name: str
