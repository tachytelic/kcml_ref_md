ON ... SELECT

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/onselect.gif" data-align="BOTTOM" data-border="0" alt="onselect.gif" />\
\
Where:\
\
     selopt           = a valid select option. See SELECT.\
\

------------------------------------------------------------------------

The ON ... SELECT statement is used to conditionally execute one of several possible [SELECT](SELECT.htm) statements. Transfer is made to the Nth [SELECT](SELECT.htm) statement in the list of devices if the integer value of the expression is N. One or more devices can be selected with the result of one expression, by separating each device in the list with a comma. A semi-colon separates each conditional device list.

For example if the variable ct is set to 3 then the following statement would select \#streams 1 and 2 to the device /D11:

00010 ON ct SELECT \#9 /D90;PRINT /204;#1 /D11, \#2 /D11

If the value of the expression is less than 1 or greater than the number of specified device lists, or the value of the expression points to a null device list, no [SELECT](SELECT.htm) operation is performed. Null device lists are indicated by consecutive semi-colons in the device list. If no select is made then the [ELSE](ELSE.htm) clause, if specified, is executed, otherwise the next statement in the program is executed.

The select value can also be specified with an alpha variable or string function. When an alpha variable or string function is used with the [ON ... GOSUB/GOTO](ONGOSUB.htm) statement, the binary value of the first byte in the alpha variable or function is used as the select variable.

For example, if the variable is\$ is set to HEX(02FFFFFF) then the following statement would select the [LIST](SELECT_LIST.htm) and [PRINT](SELECT_PRINT.htm) devices to /215:

ON is\$ SELECT \#1 /D99 ; LIST /215 , PRINT /215

Syntax examples:

ON temp SELECT RADIANS, TC /01C; \#1 /D11\
ON test SELECT \#1 /D90 ; ; ; \#40 /01C\
ON FLD(file\$.branch\$) SELECT \#1 /D90 ; DEGREES ; \#2 /D90, \#22 "/user1"

See also:

[SELECT](SELECT.htm)

 
