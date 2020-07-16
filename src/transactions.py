from dataclasses import dataclass
from datetime import date


@dataclass
class Transaction:
    """
    A dataclass representing a single transaction.

    Attributes:
        name (str): The name of the receiving or sending party
        amount (float): The amount sent or received (in € currently)
        date (date): The date of the transaction
        category (str): The category eg. 'Entertainment', 'Food' etc.
    """
    name: str
    amount: float
    date: date
    category: str
