package com.bank.services;

public class LoanCalculator {
    private double principalAmount;
    private double annualInterestRate;
    private int loanTermMonths;

    public LoanCalculator(double principalAmount, double annualInterestRate, int loanTermMonths) {
        this.principalAmount = principalAmount;
        this.annualInterestRate = annualInterestRate;
        this.loanTermMonths = loanTermMonths;
    }

    public double calculateMonthlyPayment() {
        double monthlyRate = annualInterestRate / 100.0 / 12.0;
        if (monthlyRate == 0) {
            return principalAmount / loanTermMonths;
        }
        double numerator = monthlyRate * Math.pow(1 + monthlyRate, loanTermMonths);
        double denominator = Math.pow(1 + monthlyRate, loanTermMonths) - 1;
        return principalAmount * (numerator / denominator);
    }

    public double calculateTotalPayment() {
        return calculateMonthlyPayment() * loanTermMonths;
    }

    public double calculateTotalInterest() {
        return calculateTotalPayment() - principalAmount;
    }

    public void printAmortizationSchedule() {
        double monthlyPayment = calculateMonthlyPayment();
        double monthlyRate = annualInterestRate / 100.0 / 12.0;
        double remainingBalance = principalAmount;

        System.out.println("\n============ LOAN AMORTIZATION SCHEDULE ============");
        System.out.printf("Principal: $%.2f | Rate: %.2f%% | Term: %d months%n",
                principalAmount, annualInterestRate, loanTermMonths);
        System.out.printf("Monthly Payment: $%.2f%n", monthlyPayment);
        System.out.println("----------------------------------------------------");
        System.out.printf("%-6s %-12s %-12s %-12s %-12s%n",
                "Month", "Payment", "Principal", "Interest", "Balance");
        System.out.println("----------------------------------------------------");

        for (int month = 1; month <= loanTermMonths; month++) {
            double interestPayment = remainingBalance * monthlyRate;
            double principalPayment = monthlyPayment - interestPayment;
            remainingBalance -= principalPayment;

            if (remainingBalance < 0) remainingBalance = 0;

            System.out.printf("%-6d $%-11.2f $%-11.2f $%-11.2f $%-11.2f%n",
                    month, monthlyPayment, principalPayment, interestPayment, remainingBalance);
        }

        System.out.println("----------------------------------------------------");
        System.out.printf("Total Payment: $%.2f | Total Interest: $%.2f%n",
                calculateTotalPayment(), calculateTotalInterest());
        System.out.println("====================================================\n");
    }
}
