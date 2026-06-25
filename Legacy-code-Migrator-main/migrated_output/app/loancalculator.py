# Migrated from LoanCalculator.java using AI Migration Agent
"""Loan Calculator module migrated to Python.

This module provides a `LoanCalculator` class that encapsnates the same
business logic as the original Java implementation. All calculations are
identical, and the amortization schedule is printed to standard output.

The migration preserves the original method names (converted to snake_case
for Pythonic style) and adds type hints and docstrings for clarity.
"""

import math
from typing import Any


class LoanCalculator:
    """Calculate loan payments and print an amortization schedule.

    Parameters
    ----------
    principal_amount: float
        The total amount borrowed.
    annual_interest_rate: float
        Annual interest rate as a percentage (e.g., 5.5 for 5.5%).
    loan_term_months: int
        Length of the loan in months.
    """

    def __init__(self, principal_amount: float, annual_interest_rate: float, loan_term_months: int) -> None:
        self.principal_amount: float = principal_amount
        self.annual_interest_rate: float = annual_interest_rate
        self.loan_term_months: int = loan_term_months

    def calculate_monthly_payment(self) -> float:
        """Calculate the fixed monthly payment using the amortization formula.

        Returns
        -------
        float
            The monthly payment amount.
        """
        monthly_rate = self.annual_interest_rate / 100.0 / 12.0
        if monthly_rate == 0:
            return self.principal_amount / self.loan_term_months
        numerator = monthly_rate * math.pow(1 + monthly_rate, self.loan_term_months)
        denominator = math.pow(1 + monthly_rate, self.loan_term_months) - 1
        return self.principal_amount * (numerator / denominator)

    def calculate_total_payment(self) -> float:
        """Calculate the total amount paid over the life of the loan."""
        return self.calculate_monthly_payment() * self.loan_term_months

    def calculate_total_interest(self) -> float:
        """Calculate the total interest paid over the life of the loan."""
        return self.calculate_total_payment() - self.principal_amount

    def print_amortization_schedule(self) -> None:
        """Print a formatted amortization schedule to the console.

        The schedule mirrors the output format of the original Java version.
        """
        monthly_payment = self.calculate_monthly_payment()
        monthly_rate = self.annual_interest_rate / 100.0 / 12.0
        remaining_balance = self.principal_amount

        print("\n============ LOAN AMORTIZATION SCHEDULE ============")
        print(f"Principal: ${self.principal_amount:,.2f} | Rate: {self.annual_interest_rate:.2f}% | Term: {self.loan_term_months} months")
        print(f"Monthly Payment: ${monthly_payment:,.2f}")
        print("----------------------------------------------------")
        print(f"{'Month':<6} {'Payment':<12} {'Principal':<12} {'Interest':<12} {'Balance':<12}")
        print("----------------------------------------------------")

        for month in range(1, self.loan_term_months + 1):
            interest_payment = remaining_balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment
            # Guard against negative balance due to rounding
            if remaining_balance < 0:
                remaining_balance = 0.0

            print(f"{month:<6d} ${monthly_payment:>11.2f} ${principal_payment:>11.2f} ${interest_payment:>11.2f} ${remaining_balance:>11.2f}")

        print("----------------------------------------------------")
        print(f"Total Payment: ${self.calculate_total_payment():,.2f} | Total Interest: ${self.calculate_total_interest():,.2f}")
        print("====================================================\n")


# Example usage (uncomment for quick test)
# if __name__ == "__main__":
#     calculator = LoanCalculator(principal_amount=250000, annual_interest_rate=4.5, loan_term_months=360)
#     calculator.print_amortization_schedule()
