\$ERR

------------------------------------------------------------------------

<div class="Generalform">

General Form:\

> \$ERR

</div>

------------------------------------------------------------------------

The \$ERR alphanumeric function is used to return the last error code as a string in the form cXX.YYY where c is a character representing the class of error, XX is the major error number in the range 00 to 99, and YYY is the minor number that uniquely identifies the particular error. Error classes are related to major error numbers thus:

| Class | Major errors | Description       |
|-------|--------------|-------------------|
| A     | 00 to 09     | System errors     |
| S     | 10 to 29     | Syntax errors     |
| O     | 30 to 30     | Object errors     |
| P     | 31 to 59     | Run time errors   |
| C     | 60 to 69     | Maths errors      |
| X     | 70 to 79     | Conversion errors |
| D     | 80 to 89     | Disk errors       |
| I     | 90 to 99     | Device errors     |

This function is valid anywhere a string expression is legal. Unlike [ERR](ERR.htm) it is not reset until the next error ocurs. A typical full codes might be:


    C62.001 Division by zero
    P57.017 Length of substring zero or negative
    P34.109 Reference to grid cell (10,11) in grid sized (10,10)

User errors signalled by [THROW ERR](THROW.htm) are returned as "I90.000" whatever their value.

Prior to KCML 6.0 \$ERR was implemented as [ERR\$(ERR)](ERR$(.htm). Prior to KCML 6.20 the full error text was not included if the error was handled by a ERROR clause as the text came from a separate berror.d file. As of 6.20 the text of all errors is included in KCML and is looked up for all classes of error in all circumstances. Note that for many errors the text is dynamic and reflects the components involved in the error (as in the P34 grid cell range error above.)

Do not assume that the error text or the minor error numbers will stay fixed in future versions of KCML.

Syntax examples:

major_err\$ = STR(\$ERR,2,2)\
minor_err\$ = STR(\$ERR,5,3)\

See also:

<div class="listing">

[ERR](ERR.htm), [ERR\$()](ERR$(.htm), [\$OSERR]($OSERR.htm), [ERROR](ERROR.htm)

</div>
