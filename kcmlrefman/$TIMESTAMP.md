\$TIMESTAMP function

General Form:\

\$TIMESTAMP

------------------------------------------------------------------------

The \$TIMESTAMP alpha function is used to return the current date and time in terms of the number of milliseconds since 0000 GMT year 0000 (one day before 1 January 0001). This is in the form of a 6 byte unsigned binary string. This function is mainly used as a timestamp for timing events. Event duration can be computed by subtraction using [SUBC](SUB.htm).

This time stamp will be with respect to GMT and not local time on systems that understand [timezones](timezone.htm).

The TIMESTAMP packing format can be used to timestamp database rows.

Here is an example of how \$TIMESTAMP could be used to time a loop:


    DIM ts_start$6, ts_diff$6, n=1000
    ts_start$ = $TIMESTAMP

    FOR i = 1 TO n
    a$ = s.echo$("hello")
    NEXT i

    ts_diff$ = $TIMESTAMP SUBC ts_start$
    PRINT "Each loop took";VAL(STR(ts_diff$, 3, 4), 4) / n / 1000;"seconds"

Syntax example:

tm\$ = \$TIMESTAMP SUBC tm\$\
test\$ = \$TIMESTAMP

See also:

[TIME](TIME.htm)\
[\#TIME](_TIME.htm) [\$TIME]($TIME.htm)
