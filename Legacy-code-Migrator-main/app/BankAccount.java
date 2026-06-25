package com.bank.core;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class BankAccount {
    private String accountNumber;
    private String holderName;
    private double balance;
    private String accountType; // SAVINGS, CHECKING
    private List<Transaction> transactionHistory;
    private boolean isActive;

    public BankAccount(String accountNumber, String holderName, double initialDeposit, String accountType) {
        this.accountNumber = accountNumber;
        this.holderName = holderName;
        this.balance = initialDeposit;
        this.accountType = accountType;
        this.transactionHistory = new ArrayList<>();
        this.isActive = true;

        if (initialDeposit > 0) {
            transactionHistory.add(new Transaction("DEPOSIT", initialDeposit, "Initial deposit"));
        }
    }

    public boolean deposit(double amount) {
        if (!isActive) {
            System.out.println("ERROR: Account " + accountNumber + " is inactive.");
            return false;
        }
        if (amount <= 0) {
            System.out.println("ERROR: Deposit amount must be positive.");
            return false;
        }
        balance += amount;
        transactionHistory.add(new Transaction("DEPOSIT", amount, "Cash deposit"));
        System.out.println("Deposited $" + amount + " to account " + accountNumber);
        return true;
    }

    public boolean withdraw(double amount) {
        if (!isActive) {
            System.out.println("ERROR: Account " + accountNumber + " is inactive.");
            return false;
        }
        if (amount <= 0) {
            System.out.println("ERROR: Withdrawal amount must be positive.");
            return false;
        }
        if (amount > balance) {
            System.out.println("ERROR: Insufficient funds. Balance: $" + balance);
            return false;
        }
        balance -= amount;
        transactionHistory.add(new Transaction("WITHDRAWAL", amount, "Cash withdrawal"));
        System.out.println("Withdrew $" + amount + " from account " + accountNumber);
        return true;
    }

    public boolean transferTo(BankAccount target, double amount) {
        if (this.withdraw(amount)) {
            target.deposit(amount);
            this.transactionHistory.add(new Transaction("TRANSFER_OUT", amount, "Transfer to " + target.getAccountNumber()));
            target.transactionHistory.add(new Transaction("TRANSFER_IN", amount, "Transfer from " + this.accountNumber));
            System.out.println("Transferred $" + amount + " from " + accountNumber + " to " + target.getAccountNumber());
            return true;
        }
        return false;
    }

    public void printStatement() {
        System.out.println("\n========== ACCOUNT STATEMENT ==========");
        System.out.println("Account : " + accountNumber);
        System.out.println("Holder  : " + holderName);
        System.out.println("Type    : " + accountType);
        System.out.println("Status  : " + (isActive ? "Active" : "Inactive"));
        System.out.println("Balance : $" + String.format("%.2f", balance));
        System.out.println("----------------------------------------");
        System.out.println("TRANSACTIONS:");
        for (Transaction t : transactionHistory) {
            System.out.println("  " + t.toString());
        }
        System.out.println("========================================\n");
    }

    public void deactivate() {
        this.isActive = false;
        System.out.println("Account " + accountNumber + " has been deactivated.");
    }

    // Getters
    public String getAccountNumber() { return accountNumber; }
    public String getHolderName() { return holderName; }
    public double getBalance() { return balance; }
    public String getAccountType() { return accountType; }
    public boolean isActive() { return isActive; }
    public List<Transaction> getTransactionHistory() { return transactionHistory; }
}
