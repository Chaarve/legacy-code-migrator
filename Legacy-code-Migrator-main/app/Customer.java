package com.bank.core;

import java.util.ArrayList;
import java.util.List;

public class Customer {
    private String customerId;
    private String name;
    private String email;
    private String phone;
    private List<BankAccount> accounts;
    private static int customerCounter = 0;

    public Customer(String name, String email, String phone) {
        this.customerId = "CUST" + String.format("%04d", ++customerCounter);
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.accounts = new ArrayList<>();
    }

    public BankAccount openAccount(String accountType, double initialDeposit) {
        String accNum = customerId + "-" + accountType.substring(0, 3).toUpperCase() + "-" + (accounts.size() + 1);
        BankAccount account = new BankAccount(accNum, name, initialDeposit, accountType);
        accounts.add(account);
        System.out.println("Opened " + accountType + " account " + accNum + " for " + name);
        return account;
    }

    public void closeAccount(String accountNumber) {
        for (BankAccount acc : accounts) {
            if (acc.getAccountNumber().equals(accountNumber)) {
                if (acc.getBalance() > 0) {
                    System.out.println("WARNING: Account has balance $" + acc.getBalance() + ". Please withdraw first.");
                    return;
                }
                acc.deactivate();
                System.out.println("Account " + accountNumber + " closed for customer " + name);
                return;
            }
        }
        System.out.println("ERROR: Account " + accountNumber + " not found for customer " + name);
    }

    public double getTotalBalance() {
        double total = 0;
        for (BankAccount acc : accounts) {
            if (acc.isActive()) {
                total += acc.getBalance();
            }
        }
        return total;
    }

    public void printCustomerSummary() {
        System.out.println("\n+======================================+");
        System.out.println("|         CUSTOMER SUMMARY             |");
        System.out.println("+======================================+");
        System.out.println("  ID    : " + customerId);
        System.out.println("  Name  : " + name);
        System.out.println("  Email : " + email);
        System.out.println("  Phone : " + phone);
        System.out.println("  Accounts: " + accounts.size());
        System.out.println("  Total Balance: $" + String.format("%.2f", getTotalBalance()));
        System.out.println("+======================================+");

        for (BankAccount acc : accounts) {
            acc.printStatement();
        }
    }

    // Getters
    public String getCustomerId() { return customerId; }
    public String getName() { return name; }
    public String getEmail() { return email; }
    public List<BankAccount> getAccounts() { return accounts; }
}
