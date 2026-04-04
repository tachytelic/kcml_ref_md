Set functions supported

The KISAM ODBC driver supports all the set functions defined the Microsoft ODBC 2.0 Programmers Reference.

These functions can be invoked as inline SQL functions in queries that have GROUP BY clauses. e.g.

SELECT AccountCode, COUNT(AccountCode), SUM(AmountPaid) FROM ACCOUNTS, TRANSACTIONS WHERE TRANSACTIONS.AccountCode = ACCOUNTS.AccountCode GROUP BY AccountCode

| Function | Description                                               |
|----------|-----------------------------------------------------------|
| COUNT( ) | Returns the number of rows in the group.                  |
| SUM( )   | Returns the sum of the column within the group.           |
| AVG( )   | Returns the average value of the column within the group. |
| MIN( )   | Returns the minimum value of the column within the group. |
| MAX( )   | Returns the maximum value of the column within the group. |
