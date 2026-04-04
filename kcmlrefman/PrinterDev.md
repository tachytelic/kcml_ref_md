Working with printers

KCML programs traditionally treat printers as character devices. Printing can be done by the terminal or client (called [local printing](LocalPrinters.htm)) or can be sent to a printer attached to the server. A further option is to connect to a network printer like [Kprint](kprint.htm).

The program generates printed output using the [PRINT](PRINT.htm) and [PRINTUSING](PRINTUSING.htm) statments having first SELECTed the required print device with [SELECT PRINT](SELECT_PRINT.htm). The device should have been previously defined by [\$DEVICE]($DEVICE.htm) and locked with [\$OPEN]($OPEN.htm) e.g.

\$DEVICE /015="LPT1"\
SELECT \#9/015 \$OPEN \#9\
SELECT PRINT \#9\
PRINT "Hello"\
SELECT PRINT /005\
\$CLOSE \#9\

Locking with \$OPEN is necessary because

- On a directly connected printer it ensures that that two processes do not write at the same time
- If the printer is spooled, the \$CLOSE tells KCML to close the print job and allow the spooler to print it

The normal line terminating character in KCML is the HEX(0D) carriage return. Some older printers had hardware support for this but today most printers will expect the application to terminate lines with HEX(0D0A). KCML supports a mechanism to control the line terminator by setting the first digit of the device address to '0' (for automatic addition of a HEX(OA) or '2' to just pass the HEX(0D) through. The example above uses '0 to achieve this. For more about using the first digit to set the line terminator see the [PRINT](PRINT.htm#DevType) statement.

See Also

[Working with local printers](LocalPrinters.htm)\
[Printing on NT servers](NTPrinting.htm)\
[Printing on Unix servers](UnixPrinting.htm)\
[Network printing with Kprint](kprint.htm)\
