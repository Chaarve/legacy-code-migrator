# Migrated from BankAccount.java using AI Migration Agent
"""BankAccount module migrated from Java to Python.

This module defines the :class:`BankAccount` class, preserving the original
business logic while using idiomatic Python constructs such as type hints,
properties, and f‑strings. A minimal :class:`Transaction` helper is also
included to keep the code functional without requiring the original Java
implementation.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Transaction:
    """Simple representation of a financial transaction.

    The original Java code only stored a type, amount and description, so we
    replicate that structure. ``timestamp`` is added for completeness.
    """

    type: str
    amount: float
    description: str
    timestamp: datetime = datetime.now()

    def __str__(self) -> str:
        # Mimic the Java ``toString`` output used in the original code.
        return f"{self.timestamp.isoformat()} | {self.type:<12} | ${self.amount:,.2f} | {self.description}"


class BankAccount:
    """Pythonic version of the Java ``BankAccount`` class.

    All business rules from the original implementation are retained:

    * Accounts start active and can be deactivated.
    * Deposits and withdrawals must be positive and respect the account's
      active status.
    * Transfers are performed as a withdrawal from the source followed by a
      deposit into the target, with appropriate transaction records.
    """

    def __init__(
        self,
        account_number: str,
        holder_name: str,
        initial_deposit: float,
        account_type: str,
    ) -> None:
        self._account_number: str = account_number
        self._holder_name: str = holder_name
        self._balance: float = initial_deposit
        self._account_type: str = account_type  # e.g., "SAVINGS", "CHECKING"
        self._transaction_history: List[Transaction] = []
        self._is_active: bool = True

        if initial_deposit > 0:
            self._transaction_history.append(
                Transaction("DEPOSIT", initial_deposit, "Initial deposit")
            )

    # ---------------------------------------------------------------------
    # Core operations
    # ---------------------------------------------------------------------
    def deposit(self, amount: float) -> bool:
        """Deposit *amount* into the account.

        Returns ``True`` on success, ``False`` otherwise. Errors are printed to
        standard output to mirror the original Java behaviour.
        """
        if not self._is_active:
            print(f"ERROR: Account {self._account_number} is inactive.")
            return False
        if amount <= 0:
            print("ERROR: Deposit amount must be positive.")
            return False
        self._balance += amount
        self._transaction_history.append(
            Transaction("DEPOSIT", amount, "Cash deposit")
        )
        print(f"Deposited ${amount} to account {self._account_number}")
        return True

    def withdraw(self, amount: float) -> bool:
        """Withdraw *amount* from the account.

        Returns ``True`` on success, ``False`` otherwise.
        """
        if not self._is_active:
            print(f"ERROR: Account {self._account_number} is inactive.")
            return False
        if amount <= 0:
            print("ERROR: Withdrawal amount must be positive.")
            return False
        if amount > self._balance:
            print(f"ERROR: Insufficient funds. Balance: ${self._balance}")
            return False
        self._balance -= amount
        self._transaction_history.append(
            Transaction("WITHDRAWAL", amount, "Cash withdrawal")
        )
        print(f"Withdrew ${amount} from account {self._account_number}")
        return True

    def transfer_to(self, target: "BankAccount", amount: float) -> bool:
        """Transfer *amount* from this account to *target*.

        The operation succeeds only if the withdrawal from the source account
        succeeds. Both accounts receive appropriate transaction records.
        """
        if self.withdraw(amount):
            target.deposit(amount)
            self._transaction_history.append(
                Transaction(
                    "TRANSFER_OUT",
                    amount,
                    f"Transfer to {target.account_number}",
                )
            )
            target._transaction_history.append(
                Transaction(
                    "TRANSFER_IN",
                    amount,
                    f"Transfer from {self._account_number}",
                )
            )
            print(
                f"Transferred ${amount} from {self._account_number} to {target.account_number}"
            )
            return True
        return False

    def print_statement(self) -> None:
        """Print a formatted account statement to standard output."""
        print("\n========== ACCOUNT STATEMENT ==========")
        print(f"Account : {self._account_number}")
        print(f"Holder  : {self._holder_name}")
        print(f"Type    : {self._account_type}")
        print(f"Status  : {'Active' if self._is_active else 'Inactive'}")
        print(f"Balance : ${self._balance:,.2f}")
        print("----------------------------------------")
        print("TRANSACTIONS:")
        for t in self._transaction_history:
            print(f"  {t}")
        print("========================================\n")

    def deactivate(self) -> None:
        """Mark the account as inactive."""
        self._is_active = False
        print(f"Account {self._account_number} has been deactivated.")

    # ---------------------------------------------------------------------
    # Property accessors (read‑only – mirrors Java getters)
    # ---------------------------------------------------------------------
    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def holder_name(self) -> str:
        return self._holder_name

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def account_type(self) -> str:
        return self._account_type

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def transaction_history(self) -> List[Transaction]:
        # Return a copy to prevent external mutation, preserving encapsulation.
        return list(self._transaction_history)

    # ---------------------------------------------------------------------
    # Representation helpers
    # ---------------------------------------------------------------------
    def __repr__(self) -> str:
        return (
            f"BankAccount(account_number={self._account_number!r}, "
            f"holder_name={self._holder_name!r}, balance={self._balance!r}, "
            f"account_type={self._account_type!r}, is_active={self._is_active!r})"
        )
