INSERT

INSERT INTO table \[(column \[,column\]...)\] {VALUES (expression \[,expression\]..) \| subquery}

This statement will insert a row into the table. The values can be explicitly given for each column. If the columns are named in the initial optional column list then the vales must match. The values can be literals, expressions, functions or parameters

If a subquery supplies the values then as many rows as there are in the subqueries result set will be added. For more about subqueries see [SELECT](SELECT.htm).

Examples

INSERT INTO XX00test VALUES(1, 'red') INSERT INTO XX00test (Quantity, color) VALUES (5, 'green') INSERT INTO YY01test VALUES(?,?,?,?)
