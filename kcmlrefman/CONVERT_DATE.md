CONVERT DATE

------------------------------------------------------------------------

General Forms:\

1.  CONVERT DATE numeric_expression TO alpha_receiver

2.  CONVERT DATE alpha_expression TO numeric_receiver

------------------------------------------------------------------------

CONVERT DATE can be used to convert between [ISO-8601](http://www.iso.ch/markete/8601.pdf) dates in CCYY-MM-DD format and [Julian dates](JulianDate.htm). The ISO-8601 date format of "CCYY-MM-DD" is the same as the format used in the KCML ODBC driver. The full CCYY year must be used and it is not permitted to abbreviate to just the YY part. For example:

CONVERT DATE "1997-02-11" TO Julian\
CONVERT DATE Vbdate + 2415019 TO VBdate\$

Note that the date form of the KCML Edit control ([.Type\$](mk:@MSITStore:kcmlforms.chm::/tmp/PROPSTR_TYPE.htm)="D") receives and returns the date as a Julian value, therefore to initialize the Edit control to a specific date the following could be used:

CONVERT DATE Idate\$ TO JDate\
.editControl1.Type\$ = "D"\
.editControl1.Text\$ = JDate

See Also

[\#DATE](_DATE.htm)\
[DATE](DATE.htm)\
[CONVERT TIME](CONVERT_TIME.htm)\
[ISO date standard](http://www.iso.ch/markete/8601.pdf)
