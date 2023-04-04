from typing import Optional

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
    creator: Optional[str] = None
    manager: Optional[str] = None
    reserve: Optional[str] = None
    freeze: Optional[str] = None
    total: Optional[int] = None
    url: Optional[str] = None
