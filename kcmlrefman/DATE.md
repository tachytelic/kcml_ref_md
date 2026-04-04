DATE <span style="font-size: 16pt ; ">function</span>

------------------------------------------------------------------------

General Forms :\
\
     DATE\
\

------------------------------------------------------------------------

The DATE function is used to return the current system date in the local [timezone](timezone.htm). The date is returned as an alpha value in the format "YYMMDD". The DATE function is valid wherever an alpha expression is legal.

Note that use of this function should be avoided, as it does not return century information. The [\#DATE,](_DATE.htm) [CONVERT DATE](CONVERT_DATE.htm) and [\$TODAY]($TODAY.htm) instructions should be used when dealing with dates as these all cope with century information.

The [\$TODAY]($TODAY.htm) function is used to return today’s date including the current century.

Syntax example:

now\$ = DATE & TIME

See also:

[CONVERT DATE](CONVERT_DATE.htm), [\#DATE](_DATE.htm), [\$TIME]($TIME.htm), [TIME](TIME.htm), [\$TODAY]($TODAY.htm)
