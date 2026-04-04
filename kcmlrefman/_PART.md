\#PART function

------------------------------------------------------------------------

General Form:\
\
     \#PART\
\

------------------------------------------------------------------------

The \#PART function returns a number, counted from 1, which uniquely identifies the running instance of KCML. It will usually have the same value as that of the [\#TERM](_TERM.htm) function, unless [\#TERM](_TERM.htm) is set to zero or there are multiple KCML processes owned by that terminal. The \#PART function is valid wherever a numeric expression is valid.

Further invocations of KCML on the same terminal, either via [SHELL](SHELL.htm), [\$RELEASE]($RELEASE.htm) or another kclient session, take their partition number from a dynamically allocated list of available partitions starting from the maximum, by default 1024, and counting downward.

To increase the maximum value of \#PART beyond 1024 run [bkstat](bkstat.htm) with the -x flag e.g. bkstat -x 3000. This must be done before any KCML process has run and so should be inserted into a Unix script executed before the system goes multi-user during the boot. The maximum allowed value is 32768.

The maximum (and minimum) value of \#PART can be restricted with the [BCDPART](EnvVars.htm#BCDPART) environment variable which must be set before KCML starts. The value should be the maximum partition number required. The maximim and minimum values used can be found in [\$OPTIONS RUN]($OPTIONS_RUN.htm) bytes 55-56 and 25-26 respectively.

The maximum partition number available for the system can be discovered at run time from bytes 36 and 37 of [\$MACHINE]($MACHINE.htm). This might well be greater than the maximum value set by the BCDPART mechanism for a particular KCML process.

Compatibility

Prior to KCML5 the default maximum was 512.

Syntax examples:

partition = \#PART\
IF (#PART \<=50)

See also:

[\#TERM](_TERM.htm)
