# Migrated from Customer.java using AI Migration Agent
"""Customer module migrated from Java to Python.

This module defines the :class:`Customer` class, preserving the original business
logic while using idiomatic Python constructs.  The original Java class managed
customer information, a list of ``BankAccount`` objects, and provided operations
such as opening/closing accounts and printing a summary.

The migration follows these principles:
- All business rules are kept exactly the same.
- Java static fields become class variables.
- Java collections become Python ``list`` with appropriate type hints.
- String formatting uses f‑strings.
- ``System.out.println`` calls are replaced with ``print``.
- Accessor methods are provided as properties where appropriate.
"""

from __future__ import annotations

from typing import List

# Assuming ``BankAccount`` is defined in the same package or importable module.
# If it resides in a different module, adjust the import accordingly.
# from .bank_account import BankAccount


class Customer:
    """Represents a bank customer.

    Attributes
    ----------
    customer_id: str
        Unique identifier generated automatically.
    name: str
        Customer's full name.
    email: str
        Contact email address.
    phone: str
        Contact phone number.
    accounts: List[BankAccount]
        Collection of the customer's bank accounts.
    """

    # Class‑level counter to mimic the static ``customerCounter`` in Java.
    _customer_counter: int = 0

    def __init__(self, name: str, email: str, phone: str) -> None:
        """Create a new ``Customer`` instance.

        The ``customer_id`` is generated using the pattern ``CUST####`` where
        ``####`` is a zero‑padded sequential number.
        """
        # Increment the class counter and generate the ID.
        type(self)._customer_counter += 1
        self.customer_id: str = f"CUST{self._customer_counter:04d}"
        self.name: str = name
        self.email: str = email
        self.phone: str = phone
        self.accounts: List[BankAccount] = []

    def open_account(self, account_type: str, initial_deposit: float) -> BankAccount:
        """Open a new bank account for the customer.

        Parameters
        ----------
        account_type: str
            Type of the account (e.g., "Checking", "Savings").
        initial_deposit: float
            Starting balance for the new account.

        Returns
        -------
        BankAccount
            The newly created account instance.
        """
        # Build an account number similar to the Java implementation.
        acc_num = (
            f"{self.customer_id}-"
            f"{account_type[:3].upper()}-"
            f"{len(self.accounts) + 1}"
        )
        account = BankAccount(acc_num, self.name, initial_deposit, account_type)
        self.accounts.append(account)
        print(f"Opened {account_type} account {acc_num} for {self.name}")
        return account

    def close_account(self, account_number: str) -> None:
        """Close an existing account if its balance is zero.

        The method searches the customer's accounts for the given ``account_number``.
        If the account has a non‑zero balance, a warning is printed and the operation
        is aborted.  If the account is not found, an error message is printed.
        """
        for acc in self.accounts:
            if acc.get_account_number() == account_number:
                if acc.get_balance() > 0:
                    print(
                        f"WARNING: Account has balance ${acc.get_balance():.2f}. "
                        "Please withdraw first."
                    )
                    return
                acc.deactivate()
                print(f"Account {account_number} closed for customer {self.name}")
                return
        print(f"ERROR: Account {account_number} not found for customer {self.name}")

    def get_total_balance(self) -> float:
        """Calculate the total balance across all *active* accounts."""
        total = 0.0
        for acc in self.accounts:
            if acc.is_active():
                total += acc.get_balance()
        return total

    def print_customer_summary(self) -> None:
        """Print a formatted summary of the customer and all accounts."""
        print("\n+======================================+")
        print("|         CUSTOMER SUMMARY            |")
        print("+======================================+")
        print(f"  ID    : {self.customer_id}")
        print(f"  Name  : {self.name}")
        print(f"  Email : {self.email}")
        print(f"  Phone : {self.phone}")
        print(f"  Accounts: {len(self.accounts)}")
        print(f"  Total Balance: ${self.get_total_balance():.2f}")
        print("+======================================+")

        for acc in self.accounts:
            acc.print_statement()

    # ---------------------------------------------------------------------
    # Accessor properties – these replace the explicit getter methods in Java.
    # ---------------------------------------------------------------------
    @property
    def customer_id(self) -> str:
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value: str) -> None:
        self._customer_id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def accounts(self) -> List[BankAccount]:
        return self._accounts

    @accounts.setter
    def accounts(self, value: List[BankAccount]) -> None:
        self._accounts = value

    # ``phone`` is not used elsewhere in the original code, but we expose it for
    # completeness.
    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        self._phone = value

# Note: The original Java class relied on the ``BankAccount`` class for many
# operations (e.g., ``get_balance``, ``is_active``, ``print_statement``).  Those
# methods must exist on the Python ``BankAccount`` implementation for this
# migration to function correctly.
