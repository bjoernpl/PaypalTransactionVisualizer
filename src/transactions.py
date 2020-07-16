from dataclasses import dataclass
from datetime import date


@dataclass
class Transaction:
    name: str
    amount: float
    date: date
    category: str
