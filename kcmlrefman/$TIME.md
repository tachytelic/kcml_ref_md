\$TIME function

------------------------------------------------------------------------

General Form:\

\$TIME

------------------------------------------------------------------------

The \$TIME alpha function is used to return the current time in terms of the number of seconds since 0000 GMT on 1 January 1970. This is in the form of a 4 byte unsigned binary string. This function is mainly used as a timestamp for timing events. Event duration can be computed by subtraction using [SUBC](SUB.htm).

Syntax example:

tm\$ = \$TIME SUBC tm\$\
test\$ = \$TIME

This time stamp will be with respect to GMT and not local time on systems that understand [timezones](timezone.htm).

See also:

[TIME](TIME.htm)\
[\#TIME](_TIME.htm) [\$TIMESTAMP]($TIMESTAMP.htm)
