from dataclasses import dataclass


@dataclass
class TinymanPoolStats:
    price: str
    price_with_slippage: str
    swap_type: str
    swap_fees: str
    slippage: str
