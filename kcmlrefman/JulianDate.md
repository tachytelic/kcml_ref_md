Julian dates

Julian dates are day numbers counted from a standard date of 1200 GMT on January 1, 4716BCE in the Gregorian calendar. This date standard is widely used in astronomy and other sciences as it makes relative date calculations simple. To get the number of days elapsed between two events it is simply necessary to subtract two numbers without having to worry about leap years and the length of a month. The day of the week (assuming Monday to be zero) can be easily found by reducing the date [modulo](MODfn.htm) 7.

Julian dates are used by KCML database DATE [data types](mk:@MSITStore:kdb.chm::/datatypes.htm) which stores the number as a 3 byte integer ('B3' format). Because KCML uses an integer representation ignoring any fractional part, it differs from the astronomical definition in that it counts from midnight. It also uses local time for the [timezone](timezone.htm) rather than GMT. The difference between local timezone and GMT is available in bytes 43 and 44 of [\$MACHINE]($MACHINE.htm#BYTE43).

They are very similar to the date type used in Microsoft applications such as VB, Excel and Access which counts from 0000 on 1899-12-30 Note that Excel for the Macintosh uses a different date scheme based on 1904. To convert a Microsoft date to a Julian date just add 2415019.

[CONVERT DATE](CONVERT_DATE.htm) can be used to convert between ISO dates in CCYY-MM-DD format and Julian dates.

CONVERT DATE "1997-02-11" TO Julian\
CONVERT DATE Vbdate + 2415019 TO VBdate\$

The date form of the KCML Edit control ([.Type\$](mk:@MSITStore:kcmlforms.chm::/tmp/PROPSTR_TYPE.htm)="D") receives and returns the date as a Julian value, therefore to initialize the Edit control to a specific date the following could be used:

CONVERT DATE Idate\$ TO JDate\
.editControl1.Type\$ = "D"\
.editControl1.Text\$ = JDate

See Also

[\#DATE](_DATE.htm)\
[DATE](DATE.htm)\
[CONVERT TIME](CONVERT_TIME.htm)\
[CONVERT DATE](CONVERT_DATE.htm)\
[\$MACHINE]($MACHINE.htm)\
