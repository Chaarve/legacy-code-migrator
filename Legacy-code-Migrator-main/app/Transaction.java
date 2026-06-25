package com.bank.core;

import java.text.SimpleDateFormat;
import java.util.Date;

public class Transaction {
    private String transactionId;
    private String type;
    private double amount;
    private String description;
    private Date timestamp;
    private static int idCounter = 1000;

    public Transaction(String type, double amount, String description) {
        this.transactionId = "TXN" + (++idCounter);
        this.type = type;
        this.amount = amount;
        this.description = description;
        this.timestamp = new Date();
    }

    public String getTransactionId() { return transactionId; }
    public String getType() { return type; }
    public double getAmount() { return amount; }
    public String getDescription() { return description; }
    public Date getTimestamp() { return timestamp; }

    @Override
    public String toString() {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        return String.format("[%s] %s | %-12s | $%.2f | %s",
                sdf.format(timestamp), transactionId, type, amount, description);
    }
}
