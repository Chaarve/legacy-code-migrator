       IDENTIFICATION DIVISION.
       PROGRAM-ID. CUSTOMER-MGMT.
       AUTHOR. LEGACY-BANK-SYSTEM.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-CUSTOMER-RECORD.
          05 WS-CUST-ID           PIC X(10).
          05 WS-CUST-NAME         PIC X(30).
          05 WS-CUST-EMAIL        PIC X(40).
          05 WS-CUST-PHONE        PIC X(15).
          05 WS-CUST-BALANCE      PIC 9(9)V99.
          05 WS-CUST-STATUS       PIC X(8).
       01 WS-SEARCH-NAME          PIC X(30).
       01 WS-DEPOSIT-AMT          PIC 9(9)V99.
       01 WS-WITHDRAW-AMT         PIC 9(9)V99.
       01 WS-FOUND-FLAG           PIC 9 VALUE 0.
       01 WS-CUSTOMER-COUNT       PIC 99 VALUE 0.

       01 WS-CUSTOMER-TABLE.
          05 WS-CUST-ENTRY OCCURS 50 TIMES.
             10 CT-ID             PIC X(10).
             10 CT-NAME           PIC X(30).
             10 CT-EMAIL          PIC X(40).
             10 CT-PHONE          PIC X(15).
             10 CT-BALANCE        PIC 9(9)V99.
             10 CT-STATUS         PIC X(8).

       01 WS-IDX                  PIC 99.

       PROCEDURE DIVISION.
       MAIN-LOGIC.
           PERFORM INITIALIZE-SYSTEM
           PERFORM ADD-CUSTOMER-1
           PERFORM ADD-CUSTOMER-2
           PERFORM ADD-CUSTOMER-3
           PERFORM DEPOSIT-FUNDS
           PERFORM WITHDRAW-FUNDS
           PERFORM SEARCH-CUSTOMER
           PERFORM DISPLAY-ALL-CUSTOMERS
           PERFORM DISPLAY-TOTAL-ASSETS
           STOP RUN.

       INITIALIZE-SYSTEM.
           DISPLAY "========================================"
           DISPLAY "   CUSTOMER MANAGEMENT SYSTEM v1.0"
           DISPLAY "========================================"
           MOVE 0 TO WS-CUSTOMER-COUNT.

       ADD-CUSTOMER-1.
           ADD 1 TO WS-CUSTOMER-COUNT
           MOVE "C001"         TO CT-ID(WS-CUSTOMER-COUNT)
           MOVE "ALICE JOHNSON" TO CT-NAME(WS-CUSTOMER-COUNT)
           MOVE "alice@bank.com" TO CT-EMAIL(WS-CUSTOMER-COUNT)
           MOVE "555-0101"     TO CT-PHONE(WS-CUSTOMER-COUNT)
           MOVE 5000.00        TO CT-BALANCE(WS-CUSTOMER-COUNT)
           MOVE "ACTIVE"       TO CT-STATUS(WS-CUSTOMER-COUNT)
           DISPLAY "Added customer: ALICE JOHNSON".

       ADD-CUSTOMER-2.
           ADD 1 TO WS-CUSTOMER-COUNT
           MOVE "C002"         TO CT-ID(WS-CUSTOMER-COUNT)
           MOVE "BOB SMITH"    TO CT-NAME(WS-CUSTOMER-COUNT)
           MOVE "bob@bank.com" TO CT-EMAIL(WS-CUSTOMER-COUNT)
           MOVE "555-0202"     TO CT-PHONE(WS-CUSTOMER-COUNT)
           MOVE 3500.00        TO CT-BALANCE(WS-CUSTOMER-COUNT)
           MOVE "ACTIVE"       TO CT-STATUS(WS-CUSTOMER-COUNT)
           DISPLAY "Added customer: BOB SMITH".

       ADD-CUSTOMER-3.
           ADD 1 TO WS-CUSTOMER-COUNT
           MOVE "C003"         TO CT-ID(WS-CUSTOMER-COUNT)
           MOVE "CAROL DAVIS"  TO CT-NAME(WS-CUSTOMER-COUNT)
           MOVE "carol@bank.com" TO CT-EMAIL(WS-CUSTOMER-COUNT)
           MOVE "555-0303"     TO CT-PHONE(WS-CUSTOMER-COUNT)
           MOVE 12000.00       TO CT-BALANCE(WS-CUSTOMER-COUNT)
           MOVE "ACTIVE"       TO CT-STATUS(WS-CUSTOMER-COUNT)
           DISPLAY "Added customer: CAROL DAVIS".

       DEPOSIT-FUNDS.
           MOVE 2500.00 TO WS-DEPOSIT-AMT
           DISPLAY " "
           DISPLAY "--- Processing deposit for C001 ---"
           IF WS-DEPOSIT-AMT > 0
               ADD WS-DEPOSIT-AMT TO CT-BALANCE(1)
               DISPLAY "Deposited $" WS-DEPOSIT-AMT
                       " to ALICE JOHNSON"
               DISPLAY "New balance: $" CT-BALANCE(1)
           ELSE
               DISPLAY "ERROR: Deposit amount must be positive"
           END-IF.

       WITHDRAW-FUNDS.
           MOVE 1000.00 TO WS-WITHDRAW-AMT
           DISPLAY " "
           DISPLAY "--- Processing withdrawal for C002 ---"
           IF WS-WITHDRAW-AMT > CT-BALANCE(2)
               DISPLAY "ERROR: Insufficient funds"
               DISPLAY "Available: $" CT-BALANCE(2)
           ELSE
               SUBTRACT WS-WITHDRAW-AMT FROM CT-BALANCE(2)
               DISPLAY "Withdrew $" WS-WITHDRAW-AMT
                       " from BOB SMITH"
               DISPLAY "New balance: $" CT-BALANCE(2)
           END-IF.

       SEARCH-CUSTOMER.
           DISPLAY " "
           DISPLAY "--- Searching for BOB SMITH ---"
           MOVE "BOB SMITH" TO WS-SEARCH-NAME
           MOVE 0 TO WS-FOUND-FLAG
           PERFORM VARYING WS-IDX FROM 1 BY 1
               UNTIL WS-IDX > WS-CUSTOMER-COUNT
               IF CT-NAME(WS-IDX) = WS-SEARCH-NAME
                   MOVE 1 TO WS-FOUND-FLAG
                   DISPLAY "FOUND: " CT-NAME(WS-IDX)
                   DISPLAY "  ID     : " CT-ID(WS-IDX)
                   DISPLAY "  Email  : " CT-EMAIL(WS-IDX)
                   DISPLAY "  Balance: $" CT-BALANCE(WS-IDX)
                   DISPLAY "  Status : " CT-STATUS(WS-IDX)
               END-IF
           END-PERFORM
           IF WS-FOUND-FLAG = 0
               DISPLAY "Customer not found: " WS-SEARCH-NAME
           END-IF.

       DISPLAY-ALL-CUSTOMERS.
           DISPLAY " "
           DISPLAY "========================================"
           DISPLAY "        ALL CUSTOMERS REPORT"
           DISPLAY "========================================"
           PERFORM VARYING WS-IDX FROM 1 BY 1
               UNTIL WS-IDX > WS-CUSTOMER-COUNT
               DISPLAY "  " CT-ID(WS-IDX) " | "
                       CT-NAME(WS-IDX) " | $"
                       CT-BALANCE(WS-IDX) " | "
                       CT-STATUS(WS-IDX)
           END-PERFORM
           DISPLAY "========================================".

       DISPLAY-TOTAL-ASSETS.
           MOVE 0 TO WS-CUST-BALANCE
           PERFORM VARYING WS-IDX FROM 1 BY 1
               UNTIL WS-IDX > WS-CUSTOMER-COUNT
               ADD CT-BALANCE(WS-IDX) TO WS-CUST-BALANCE
           END-PERFORM
           DISPLAY " "
           DISPLAY "Total customers: " WS-CUSTOMER-COUNT
           DISPLAY "Total assets   : $" WS-CUST-BALANCE
           DISPLAY "========================================".
