# Migrated from Transaction.java using AI Migration Agent
"""Transaction module migrated from Java to Python.

This module defines a `Transaction` class that encapsulates transaction details.
The original Java implementation used a static counter for generating unique
transaction IDs, stored timestamps as `java.util.Date`, and formatted output
with `SimpleDateFormat`. The Python version mirrors this behavior using
class variables, `datetime.datetime`, and f‑strings.
"""

from __future__ import annotations

import datetime
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Transaction:
    """Represents a bank transaction.

    Attributes
    ----------
    transaction_id: str
        Unique identifier generated automatically.
    type: str
        Type of transaction (e.g., "deposit", "withdrawal").
    amount: float
        Monetary amount of the transaction.
    description: str
        Human‑readable description.
    timestamp: datetime.datetime
        Time when the transaction was created.
    """

    # Class variable to mimic the static `idCounter` in Java
    _id_counter: ClassVar[int] = 1000

    transaction_id: str = field(init=False)
    type: str
    amount: float
    description: str
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now)

    def __post_init__(self) -> None:
        """Generate a unique transaction ID after initialization.

        The ID follows the pattern ``TXN<counter>`` where the counter starts
        at 1001 (matching the Java pre‑increment behavior).
        """
        type(self)._id_counter += 1
        self.transaction_id = f"TXN{type(self)._id_counter}"

    def __str__(self) -> str:
        """Return a formatted string representation of the transaction.

        The format mirrors the Java `toString` method:
        ``[YYYY-MM-DD HH:MM:SS] TXNxxxx | TYPE          | $amount | description``
        """
        timestamp_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        # Align the type column to 12 characters, left‑justified
        return (
            f"[{timestamp_str}] {self.transaction_id} | "
            f"{self.type:<12} | ${self.amount:,.2f} | {self.description}"
        )
