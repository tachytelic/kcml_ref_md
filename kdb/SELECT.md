SELECT

SELECT \[ALL \| DISTINCT \] *selectlist*\
FROM *tablelist*\
\[WHERE *condition* \]\
\[GROUP BY *expression* \[, *expression*\] ...\]\
\[HAVING *condition*\]\
\[UNION \[ALL\] \[*subquery*\]\]\
\[ORDER BY {*expression* \| *position*} \[ASC\|DESC\] ... \]\

Where *selectlist* is

{ \* \| *table*.\* \| *expression* \[ AS *alias*\] \[, *expression* \[ AS *alias*\] \] ... }

And *tablelist* is

*table* \[*alias*\] \[, *table* \[*alias*\] \] ...

The components in italics above are defined as

| Component | Purpose |
|----|----|
| table | A named table in the database |
| alias | An alternative name for a table or an expression |
| expression | a column name, a literal value (either string or numeric), a built in function or an arithmetic expression involving other expressions |
| subquery | another SELECT statement |
| condition | a logical expression or multiple conditions connected by logical operators AND and OR possibly inside parentheses. Conditions can involve columns, functions, parameters or literals |
| position | the ordinal position, counted from 1, within the *selectlist* of the sort column |

Examples

SELECT \* FROM SL00trans SELECT color, qty\*10, UCASE(description) FROM SL00trans ORDER BY 1
