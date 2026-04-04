\$LIC(

------------------------------------------------------------------------

General Form:

strrecvr = \$LIC(section\$, key\$)

Where:

section\$ = alpha expression\
key\$ = alpha expression

------------------------------------------------------------------------

The \$LIC() function returns a key string from a specified section of a KCML license file. It will return a blank string if the key or section is not found in the license file. The key and section strings are not case sensitive. \$LIC() is legal only on the right hand side of a LET statement.

\$LIC() cannot be used to inspect the \[General\] section of the licence file.

Typical sections and their keys are:

| Section | Key   | Purpose                        |
|---------|-------|--------------------------------|
| KCML    | Users | Max allowed users              |
| Kclient | Users | Max allowed concurrent clients |
| ODBC    | Users | Max allowed ODBC users         |
| Kprint  | Users | Number of supported printers   |

Syntax examples:

count\$ = \$LIC("KCML", "Users")\
Licence\$ = \$LIC("Kprint", "Users")
