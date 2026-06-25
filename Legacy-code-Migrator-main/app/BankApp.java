package com.bank;

import com.bank.core.BankAccount;
import com.bank.core.Customer;
import com.bank.services.LoanCalculator;

/**
 * Main entry point for the Banking Application.
 * Demonstrates account operations, transfers, and loan calculations.
 */
public class BankApp {

    public static void main(String[] args) {
        System.out.println("+======================================+");
        System.out.println("|     WELCOME TO LEGACY BANK APP       |");
        System.out.println("+======================================+\n");

        // Create customers
        Customer alice = new Customer("Alice Johnson", "alice@email.com", "555-0101");
        Customer bob = new Customer("Bob Smith", "bob@email.com", "555-0202");

        // Open accounts
        BankAccount aliceSavings = alice.openAccount("SAVINGS", 5000.00);
        BankAccount aliceChecking = alice.openAccount("CHECKING", 2000.00);
        BankAccount bobSavings = bob.openAccount("SAVINGS", 3000.00);

        // Perform transactions
        aliceSavings.deposit(1500.00);
        aliceChecking.withdraw(500.00);
        aliceSavings.transferTo(bobSavings, 1000.00);

        // Edge cases
        aliceChecking.withdraw(99999.00); // Should fail - insufficient funds
        aliceSavings.deposit(-100);       // Should fail - negative amount

        // Print summaries
        alice.printCustomerSummary();
        bob.printCustomerSummary();

        // Loan calculation
        System.out.println("\n--- LOAN CALCULATOR ---");
        LoanCalculator homeLoan = new LoanCalculator(250000.00, 6.5, 360);
        System.out.printf("Home Loan Monthly Payment: $%.2f%n", homeLoan.calculateMonthlyPayment());
        System.out.printf("Total Interest: $%.2f%n", homeLoan.calculateTotalInterest());

        LoanCalculator carLoan = new LoanCalculator(30000.00, 4.5, 60);
        carLoan.printAmortizationSchedule();

        System.out.println("\nBanking application completed successfully.");
    }
}
