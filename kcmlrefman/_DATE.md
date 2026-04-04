\#DATE

------------------------------------------------------------------------

General Form:\
\
     \#DATE\
\

------------------------------------------------------------------------

This function is used to return today's date as a Julian value. [Julian dates](JulianDate.htm) are day numbers counted from a standard date in 4716BCE. Julian dates are used by the KCML database DATE data type which stores the number as a 3 byte integer ("B3" format). They are very similar to the date type used in Microsoft applications such as VB, Excel and Access.

Note that the date form of the KCML DBEdit control (.Type\$="D") receives and returns the date as a Julian value, therefore to initialise the DBEdit control to today's date the following could be used:

.KCMLDBedit1.Type\$ = "D"\
.KCMLDBEdit1.Text\$ = \#DATE

See Also:

[CONVERT DATE](CONVERT_DATE.htm), [\#TIME](_TIME.htm)
