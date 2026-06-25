# Migrated from Customer.java using AI Migration Agent
"""Customer module migrated from Java to Python.

This module defines the :class:`Customer` class, preserving the original business
logic while using idiomatic Python constructs.

The original Java class relied on a static ``customerCounter`` to generate a
unique ``customerId``. In Python we use a class variable ``_customer_counter``
for the same purpose. All methods have been translated to Pythonic equivalents
with type hints and docstrings.
"""

from __future__ import annotations

from typing import List

# Assuming ``BankAccount`` is defined in the same package or imported appropriately.
# If it resides in another module, replace the import path accordingly.
try:
    from .bank_account import BankAccount  # type: ignore
except ImportError:
    # Placeholder for static analysis; the actual implementation should be provided.
    class BankAccount:  # pragma: no cover
        """Placeholder BankAccount class.

        The real implementation must provide the following interface used by
        :class:`Customer`:

        * ``__init__(self, account_number: str, owner_name: str, initial_deposit: float, account_type: str)``
        * ``get_account_number() -> str``
        * ``get_balance() -> float``
        * ``is_active() -> bool``
        * ``deactivate() -> None``
        * ``print_statement() -> None``
        """

        def __init__(self, account_number: str, owner_name: str, initial_deposit: float, account_type: str):
            self.account_number = account_number
            self.owner_name = owner_name
            self.balance = initial_deposit
            self.account_type = account_type
            self.active = True

        def get_account_number(self) -> str:
            return self.account_number

        def get_balance(self) -> float:
            return self.balance

        def is_active(self) -> bool:
            return self.active

        def deactivate(self) -> None:
            self.active = False

        def print_statement(self) -> None:
            print(f"Statement for {self.account_number}: balance=${self.balance:.2f}")


class Customer:
    """Represents a bank customer.

    Attributes
    ----------
    customer_id: str
        Unique identifier generated from a class‑level counter.
    name: str
        Customer's full name.
    email: str
        Contact e‑mail address.
    phone: str
        Contact phone number.
    accounts: List[BankAccount]
        Collection of the customer's bank accounts.
    """

    # Class variable to mimic the static ``customerCounter`` in Java.
    _customer_counter: int = 0

    def __init__(self, name: str, email: str, phone: str) -> None:
        """Create a new ``Customer`` instance.

        Parameters
        ----------
        name: str
            Customer's name.
        email: str
            Email address.
        phone: str
            Phone number.
        """
        # Increment the counter and generate a formatted ID, e.g., CUST0001.
        type(self)._customer_counter += 1
        self.customer_id: str = f"CUST{type(self)._customer_counter:04d}"
        self.name: str = name
        self.email: str = email
        self.phone: str = phone
        self.accounts: List[BankAccount] = []

    def open_account(self, account_type: str, initial_deposit: float) -> BankAccount:
        """Open a new bank account for the customer.

        The account number follows the pattern ``{customer_id}-{TYPE}-{N}`` where
        ``TYPE`` is the first three characters of ``account_type`` (upper‑cased) and
        ``N`` is the sequential index of the account for this customer.
        """
        prefix = account_type[:3].upper()
        acc_num = f"{self.customer_id}-{prefix}-{len(self.accounts) + 1}"
        account = BankAccount(acc_num, self.name, initial_deposit, account_type)
        self.accounts.append(account)
        print(f"Opened {account_type} account {acc_num} for {self.name}")
        return account

    def close_account(self, account_number: str) -> None:
        """Close an existing account if its balance is zero.

        If the account has a non‑zero balance a warning is printed and the
        operation is aborted. If the account cannot be found an error message is
        displayed.
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
        return sum(acc.get_balance() for acc in self.accounts if acc.is_active())

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

    # Getters – retained for API compatibility with the original Java code.
    @property
    def customer_id(self) -> str:
        return self.customer_id

    @property
    def name(self) -> str:
        return self.name

    @property
    def email(self) -> str:
        return self.email

    @property
    def accounts(self) -> List[BankAccount]:
        return self.accounts

    # Note: Direct attribute access is idiomatic in Python; the above
    # properties are provided only to mirror the Java getters.

# End of migrated module
