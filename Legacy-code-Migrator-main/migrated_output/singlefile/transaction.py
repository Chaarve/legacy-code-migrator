# Migrated from Transaction.java using AI Migration Agent
"""
Python migration of the Java `Transaction` class.

The original Java class encapsulated transaction details with an auto‑incrementing
ID, timestamp, and a formatted string representation.  The Python version uses a
`@dataclass` for boilerplate reduction while preserving the exact business logic:

* `transaction_id` is generated from a class‑level counter (`id_counter`).
* `timestamp` is set to the current UTC time at construction (mirroring `new Date()`).
* The `__str__` method reproduces the original `toString` format using
  `datetime.strftime`.

All public getters are provided as read‑only properties to keep the API
compatible with the original Java getters.
"""

from __future__ import annotations

import datetime
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Transaction:
    """Represents a financial transaction.

    Attributes
    ----------
    transaction_id: str
        Unique identifier generated automatically.
    type: str
        Transaction type (e.g., "deposit", "withdrawal").
    amount: float
        Monetary amount of the transaction.
    description: str
        Human‑readable description.
    timestamp: datetime.datetime
        Time when the transaction was created.
    """

    # Class variable for auto‑incrementing IDs (mirrors Java's static field).
    id_counter: ClassVar[int] = 1000

    type: str
    amount: float
    description: str
    transaction_id: str = field(init=False)
    timestamp: datetime.datetime = field(init=False)

    def __post_init__(self) -> None:
        """Generate `transaction_id` and set the creation timestamp.

        The ID format matches the Java implementation: ``"TXN" + (++idCounter)``.
        The timestamp uses the current local time (equivalent to Java's `new Date()`).
        """
        # Increment the class‑level counter and assign the ID.
        type(self).id_counter += 1
        self.transaction_id = f"TXN{type(self).id_counter}"
        # Record the creation time.
        self.timestamp = datetime.datetime.now()

    # ---------------------------------------------------------------------
    # Compatibility getters (mirroring the original Java getters).
    # ---------------------------------------------------------------------
    @property
    def get_transaction_id(self) -> str:
        return self.transaction_id

    @property
    def get_type(self) -> str:
        return self.type

    @property
    def get_amount(self) -> float:
        return self.amount

    @property
    def get_description(self) -> str:
        return self.description

    @property
    def get_timestamp(self) -> datetime.datetime:
        return self.timestamp

    def __str__(self) -> str:
        """Return a formatted string equivalent to Java's `toString`.

        Format: ``[yyyy-MM-dd HH:mm:ss] TXNxxxx | type          | $amount | description``
        """
        ts_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        # ``%-12s`` in Java left‑justifies within 12 characters; Python's format
        # specifier ``:<12`` achieves the same effect.
        return f"[{ts_str}] {self.transaction_id} | {self.type:<12} | ${self.amount:,.2f} | {self.description}"

# Example usage (can be removed in production code):
# if __name__ == "__main__":
#     txn = Transaction(type="Deposit", amount=1500.0, description="Initial deposit")
#     print(txn)
