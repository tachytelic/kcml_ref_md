CONVERT TIME

------------------------------------------------------------------------

General Forms:

1.  CONVERT TIME numeric_expression TO alpha_receiver

2.  CONVERT TIME alpha_expression TO numeric_receiver

------------------------------------------------------------------------

CONVERT TIME can be used to convert between ISO times in HH:MM:SS format and KCML times. KCML times are d count of seconds since midnight [local time](timezone.htm) and are used by the KCML database TIME data type which stores the number as a 4 byte integer ("B4" format). For example:

CONVERT TIME "23:15:00" TO itime

Date values must be in the range 0 to 86399, i.e. up to 23:59:59, or an X71 error will result. A negative date value, specifically a value of -1, is considered to mean NULL and will be converted to a blank string and vice versa. Thus if used to convert time differences the max difference allowed is +23:59:59.

Note that the time form of the KCML edit control ([.Type\$](mk:@MSITStore:kcmlforms.chm::/tmp/PROPSTR_TYPE.htm)="T") receives and returns the time as a number, therefore to initialize the edit control to a specific time the following could be used:

CONVERT TIME Itime\$ TO itime\
.editControl1.Type\$ = "T"\
.editControl1.Text\$ = itime

See Also

[\#TIME](_TIME.htm)\
[TIME](TIME.htm)\
[CONVERT DATE](CONVERT_DATE.htm)
