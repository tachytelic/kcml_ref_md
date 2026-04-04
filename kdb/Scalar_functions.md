Set and Scalar functions

The KISAM ODBC driver supports all the set functions and scalar numeric, string and date functions defined in Appendix F of the Microsoft ODBC 2.0 Programmers Reference.

The scalar functions can be invoked using the ODBC conventions for functions of { fn *function()* }. e.g.

SELECT {fn UCASE(NAME)} FROM CUSTOMERS Both the Set and Scalar functions are acceptible in inline SQL as in SELECT UCASE(NAME) FROM CUSTOMERS

[Set functions](Set_functions.htm)

[String functions](Scalar_string_functions.htm)

[Numeric functions](Numeric_functions.htm)

[Date functions](Date_functions.htm)

[System functions](System_functions.htm)

[Type conversion](Type_conversion.htm)
