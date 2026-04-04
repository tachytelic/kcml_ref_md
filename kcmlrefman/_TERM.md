\#TERM function

------------------------------------------------------------------------

General Form:\
\
     \#TERM\
\

------------------------------------------------------------------------

The \#TERM function returns a small integer uniquely identifying the client or terminal owning the KCML process. All KCML processes started from that terminal or client will be guaranteed the same value for \#TERM allowing it to be used to track or identify physical location or terminal attributes such as type of local printer. The \#TERM function is valid wherever a numeric expression is valid.

If the standard input to KCML is not a terminal then the value of \#TERM is zero.

The normal range for \#TERM is 1 to 1024 but this can be extended to 1 to 32768 using the -y switch to [bkstat](bkstat.htm) e.g. bkstat -y 8000. This must be done before any KCML process has run and so should be inserted into a Unix script executed before the system goes multi-user during the boot.

The maximum value of \#TERM and [\#PART](_PART.htm) can be restricted to a value less tha the default with the [BCDPART](EnvVars.htm#BCDPART) environment variable.

When KCML is starting it uses the terminal name to identify the terminal (see [Compatibility](#compat) below) and looks this up in the TERMFILE file. This is a simple text file located in the same directory as the KCML executable however if the environment variable [TERMFILE](EnvVars.htm#TERMFILE) was set and given the value of the name of another file, perhaps in another directory, then that file will be used. It contains a line for each allocated \#TERM value with the terminal name and the \#TERM value separated by a tab. If the name is not found then the lowest value for \#TERM not already in the table is allocated for it and a new line is added to the end of the file to make the mapping permanent. It is possible to edit this file with a text editor to predefine the \#TERM allocations. Blank lines and whitespace characters are ignored. Comments are allowed between a \# and the end of the line. Generally a KCML process will get the same \#PART value as \#TERM provided \#TERM is non-zero and that value has not been given to another process. It is possible to control the allocation of \#PART for secondary processes using extra comma separated values after the initial \#TERM number.

Compatibility

Prior to KCML5 the default maximum \#TERM was 512.

In KCML4 either the tty name (e.g. /dev/tty01) or, in the case of WDW connected over a network, the IP address was used to identify the terminal in TERMFILE. For KCML5 kclients this has been changed to the PC computer name as IP addresses can change if DHCP is used to allocate them.

Syntax examples:

terminal(count) = \#TERM\
IF \#TERM \< 40 THEN BREAK

See also:

[\#PART](_PART.htm)
