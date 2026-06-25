       IDENTIFICATION DIVISION.
       PROGRAM-ID. INTEREST-CALC.
       AUTHOR. LEGACY-BANK-SYSTEM.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-PRINCIPAL           PIC 9(9)V99.
       01 WS-ANNUAL-RATE         PIC 9(3)V9999.
       01 WS-MONTHS              PIC 9(3).
       01 WS-MONTHLY-RATE        PIC 9V9(8).
       01 WS-MONTHLY-PAYMENT     PIC 9(9)V99.
       01 WS-TOTAL-PAYMENT       PIC 9(9)V99.
       01 WS-TOTAL-INTEREST      PIC 9(9)V99.
       01 WS-REMAINING-BAL       PIC 9(9)V99.
       01 WS-INTEREST-PART       PIC 9(9)V99.
       01 WS-PRINCIPAL-PART      PIC 9(9)V99.
       01 WS-MONTH-CTR           PIC 9(3).
       01 WS-NUMERATOR           PIC 9(15)V9(8).
       01 WS-DENOMINATOR         PIC 9(15)V9(8).
       01 WS-POWER-RESULT        PIC 9(15)V9(8).
       01 WS-TEMP                PIC 9(15)V9(8).

       01 WS-COMPOUND-RESULT.
          05 WS-COMPOUND-BAL     PIC 9(9)V99.
          05 WS-COMPOUND-INT     PIC 9(9)V99.

       01 WS-SIMPLE-RESULT.
          05 WS-SIMPLE-INT       PIC 9(9)V99.
          05 WS-SIMPLE-TOTAL     PIC 9(9)V99.

       01 WS-RATE-TYPE           PIC X(10).

       PROCEDURE DIVISION.
       MAIN-LOGIC.
           DISPLAY "========================================"
           DISPLAY "    INTEREST CALCULATION ENGINE v1.0"
           DISPLAY "========================================"

           PERFORM CALC-SIMPLE-INTEREST
           PERFORM CALC-COMPOUND-INTEREST
           PERFORM CALC-LOAN-EMI
           PERFORM CALC-FIXED-DEPOSIT
           PERFORM COMPARISON-REPORT

           DISPLAY " "
           DISPLAY "All calculations completed successfully."
           STOP RUN.

       CALC-SIMPLE-INTEREST.
           DISPLAY " "
           DISPLAY "--- SIMPLE INTEREST ---"
           MOVE 10000.00 TO WS-PRINCIPAL
           MOVE 8.5000   TO WS-ANNUAL-RATE
           MOVE 24        TO WS-MONTHS

           COMPUTE WS-SIMPLE-INT =
               WS-PRINCIPAL * WS-ANNUAL-RATE *
               (WS-MONTHS / 12) / 100

           COMPUTE WS-SIMPLE-TOTAL =
               WS-PRINCIPAL + WS-SIMPLE-INT

           DISPLAY "Principal    : $" WS-PRINCIPAL
           DISPLAY "Rate         : " WS-ANNUAL-RATE "%"
           DISPLAY "Period       : " WS-MONTHS " months"
           DISPLAY "Interest     : $" WS-SIMPLE-INT
           DISPLAY "Total Amount : $" WS-SIMPLE-TOTAL.

       CALC-COMPOUND-INTEREST.
           DISPLAY " "
           DISPLAY "--- COMPOUND INTEREST (Quarterly) ---"
           MOVE 10000.00 TO WS-PRINCIPAL
           MOVE 8.5000   TO WS-ANNUAL-RATE
           MOVE 24        TO WS-MONTHS

           COMPUTE WS-TEMP =
               1 + (WS-ANNUAL-RATE / 100 / 4)

           COMPUTE WS-POWER-RESULT =
               WS-TEMP ** (4 * WS-MONTHS / 12)

           COMPUTE WS-COMPOUND-BAL =
               WS-PRINCIPAL * WS-POWER-RESULT

           COMPUTE WS-COMPOUND-INT =
               WS-COMPOUND-BAL - WS-PRINCIPAL

           DISPLAY "Principal    : $" WS-PRINCIPAL
           DISPLAY "Rate         : " WS-ANNUAL-RATE
                   "% compounded quarterly"
           DISPLAY "Period       : " WS-MONTHS " months"
           DISPLAY "Final Amount : $" WS-COMPOUND-BAL
           DISPLAY "Interest     : $" WS-COMPOUND-INT.

       CALC-LOAN-EMI.
           DISPLAY " "
           DISPLAY "--- LOAN EMI CALCULATION ---"
           MOVE 250000.00 TO WS-PRINCIPAL
           MOVE 6.5000    TO WS-ANNUAL-RATE
           MOVE 60         TO WS-MONTHS

           COMPUTE WS-MONTHLY-RATE =
               WS-ANNUAL-RATE / 100 / 12

           IF WS-MONTHLY-RATE = 0
               COMPUTE WS-MONTHLY-PAYMENT =
                   WS-PRINCIPAL / WS-MONTHS
           ELSE
               COMPUTE WS-NUMERATOR =
                   WS-MONTHLY-RATE *
                   (1 + WS-MONTHLY-RATE) ** WS-MONTHS
               COMPUTE WS-DENOMINATOR =
                   (1 + WS-MONTHLY-RATE) ** WS-MONTHS - 1
               COMPUTE WS-MONTHLY-PAYMENT =
                   WS-PRINCIPAL *
                   (WS-NUMERATOR / WS-DENOMINATOR)
           END-IF

           COMPUTE WS-TOTAL-PAYMENT =
               WS-MONTHLY-PAYMENT * WS-MONTHS

           COMPUTE WS-TOTAL-INTEREST =
               WS-TOTAL-PAYMENT - WS-PRINCIPAL

           DISPLAY "Loan Amount     : $" WS-PRINCIPAL
           DISPLAY "Annual Rate     : " WS-ANNUAL-RATE "%"
           DISPLAY "Term            : " WS-MONTHS " months"
           DISPLAY "Monthly EMI     : $" WS-MONTHLY-PAYMENT
           DISPLAY "Total Payment   : $" WS-TOTAL-PAYMENT
           DISPLAY "Total Interest  : $" WS-TOTAL-INTEREST

           DISPLAY " "
           DISPLAY "  First 5 months breakdown:"
           MOVE WS-PRINCIPAL TO WS-REMAINING-BAL
           PERFORM VARYING WS-MONTH-CTR FROM 1 BY 1
               UNTIL WS-MONTH-CTR > 5
               COMPUTE WS-INTEREST-PART =
                   WS-REMAINING-BAL * WS-MONTHLY-RATE
               COMPUTE WS-PRINCIPAL-PART =
                   WS-MONTHLY-PAYMENT - WS-INTEREST-PART
               SUBTRACT WS-PRINCIPAL-PART FROM WS-REMAINING-BAL
               DISPLAY "  Month " WS-MONTH-CTR
                       " | EMI: $" WS-MONTHLY-PAYMENT
                       " | Principal: $" WS-PRINCIPAL-PART
                       " | Interest: $" WS-INTEREST-PART
                       " | Balance: $" WS-REMAINING-BAL
           END-PERFORM.

       CALC-FIXED-DEPOSIT.
           DISPLAY " "
           DISPLAY "--- FIXED DEPOSIT MATURITY ---"
           MOVE 50000.00 TO WS-PRINCIPAL
           MOVE 7.2500   TO WS-ANNUAL-RATE
           MOVE 36        TO WS-MONTHS

           COMPUTE WS-TEMP =
               1 + (WS-ANNUAL-RATE / 100 / 4)
           COMPUTE WS-POWER-RESULT =
               WS-TEMP ** (4 * WS-MONTHS / 12)
           COMPUTE WS-COMPOUND-BAL =
               WS-PRINCIPAL * WS-POWER-RESULT
           COMPUTE WS-COMPOUND-INT =
               WS-COMPOUND-BAL - WS-PRINCIPAL

           DISPLAY "FD Amount    : $" WS-PRINCIPAL
           DISPLAY "Rate         : " WS-ANNUAL-RATE "%"
           DISPLAY "Period       : " WS-MONTHS " months"
           DISPLAY "Maturity Amt : $" WS-COMPOUND-BAL
           DISPLAY "Interest     : $" WS-COMPOUND-INT.

       COMPARISON-REPORT.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "  INTEREST COMPARISON ($10,000 / 24mo)"
           DISPLAY "========================================"
           DISPLAY "  Simple Interest   : $" WS-SIMPLE-INT
           DISPLAY "  Compound Interest : $" WS-COMPOUND-INT
           DISPLAY "  Difference        : $"
           COMPUTE WS-TEMP =
               WS-COMPOUND-INT - WS-SIMPLE-INT
           DISPLAY "    " WS-TEMP
           DISPLAY "========================================".
