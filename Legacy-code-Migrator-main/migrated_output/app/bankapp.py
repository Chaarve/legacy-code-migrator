# Migrated from BankApp.java using AI Migration Agent
"""Banking Application migrated to Python.

This module demonstrates account operations, transfers, and loan calculations.
It preserves the original business logic from the Java version.
"""

from __future__ import annotations

# Assuming equivalent Python modules exist for the legacy Java classes.
# Adjust import paths as necessary for your project structure.
from bank.core import BankAccount, Customer
from bank.services import LoanCalculator


def main() -> None:
    """Entry point for the Banking Application.

    Replicates the behavior of the original Java `BankApp.main` method.
    """
    print("+======================================+")
    print("|     WELCOME TO LEGACY BANK APP       |")
    print("+======================================+\n")

    # Create customers
    alice = Customer(name="Alice Johnson", email="alice@email.com", phone="555-0101")
    bob = Customer(name="Bob Smith", email="bob@email.com", phone="555-0202")

    # Open accounts
    alice_savings: BankAccount = alice.open_account(account_type="SAVINGS", initial_balance=5000.00)
    alice_checking: BankAccount = alice.open_account(account_type="CHECKING", initial_balance=2000.00)
    bob_savings: BankAccount = bob.open_account(account_type="SAVINGS", initial_balance=3000.00)

    # Perform transactions
    alice_savings.deposit(1500.00)
    alice_checking.withdraw(500.00)
    alice_savings.transfer_to(bob_savings, 1000.00)

    # Edge cases (expected to raise exceptions or be handled internally)
    try:
        alice_checking.withdraw(99999.00)  # Should fail - insufficient funds
    except Exception as e:
        print(f"Withdrawal failed as expected: {e}")

    try:
        alice_savings.deposit(-100)  # Should fail - negative amount
    except Exception as e:
        print(f"Deposit failed as expected: {e}")

    # Print summaries
    alice.print_customer_summary()
    bob.print_customer_summary()

    # Loan calculation
    print("\n--- LOAN CALCULATOR ---")
    home_loan = LoanCalculator(principal=250_000.00, annual_rate_percent=6.5, term_months=360)
    print(f"Home Loan Monthly Payment: ${home_loan.calculate_monthly_payment():.2f}")
    print(f"Total Interest: ${home_loan.calculate_total_interest():.2f}")

    car_loan = LoanCalculator(principal=30_000.00, annual_rate_percent=4.5, term_months=60)
    car_loan.print_amortization_schedule()

    print("\nBanking application completed successfully.")


if __name__ == "__main__":
    main()
