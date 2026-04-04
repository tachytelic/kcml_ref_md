'KCMLCommandLine(bmark\$)

This function is used in [bookmarking](whatisabookmark.htm) to allow the server to get the -C arguments from clients command line. The buffer passed must be large enough to hold the returned string otherwise the client may crash. It is permitted to pass 0 instead of a string buffer in order to get the length.

Syntax

\$DECLARE 'KCMLCommandLine(RETURN STR())

Returns

The function returns the length of the command line in bytes.

Example

\$DECLARE 'KCMLCommandLine(RETURN STR()) DIM a\$0 DIM len REM By passing 0 for the string, we just get its length len = 'KCMLCommandLine(0) IF (len \> 0) REM Knowing the length we can MAT REDIM REM to exactly the size we need MAT REDIM a\$len REM This time fetch the string into a\$ 'KCMLCommandLine(STR(a\$)) PRINT "Command line is ",a\$ END IF
