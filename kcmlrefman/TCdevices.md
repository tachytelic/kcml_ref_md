Working with serial line devices

There are two modes of serial support in KCML for RS232 type serial telecommunications devices. The first is 2227B emulation mode using \$GIO which is supported for compatibility only and is not documented here other than to say that this is a complete emulation and is supported under both Windows and Unix. To define a device as a 2227B emulator use the keyword TC as the type in [\$DEVICE]($DEVICE.htm).

The second mode is the preferred one and is enabled to supplying various keywords in a string as the optional type string. These keywords define parameters of the serial line, e.g. the speed, parity, flow control etc., and they are remembered in the device equivalence table. KCML will not switch the mode of the line to the specified state until a [\$OPEN]($OPEN.htm) statement is issued for that device. See the table [below](#table1) for a complete list of TC keywords. Blank strings are permitted.

By a long standing convention the devices addresses /01C to /01F are used for serial devices though this is not enforced or required by KCML.

On Unix the native filename to use will be character device names like /dev/tty01. The exact naming scheme depends on the version of Unix. You must have read and write access to the device to be able to open it. No other service should be using the port at the same time. Under NT and Windows 9x the names available are COM1 to COM9.

Keywords

The keywords used in the string must be separated by commas, and may be in any order and in any case. On Unix systems KCML will automatically turn on raw mode so that the Unix device driver does not interfere with any of the characters. Some communications controllers may not be able to support all of these features.

The default setting used with a blank TC string is 9600 baud, no parity, 8 data bits, 1 stop bit, no flow or modem control, minimum characters 1 and minimum delay 1 (corresponding to 0.1s).

<span id="table1"></span>

Keywords recognised by \$DEVICE

Keyword

Description

38400

Set baud rate to 38400.

19200

Set baud rate to 19200.

9600

Set baud rate to 9600.

4800

Set baud rate to 4800.

2400

Set baud rate to 2400.

1200

Set baud rate to 1200.

600

Set baud rate to 600.

300

Set baud rate to 300.

CS5

Set data bits to 5.

CS6

Set data bits to 6.

CS7

Set data bits to 7.

CS8

Set data bits to 8.

STOP1

Set stop bits to 1.

STOP2

Set stop bits to 2.

ODD

Set parity to odd.

EVEN

Set parity to even.

NONE

Set parity to none.

PARODD

Set parity to odd.

PARENB

Set parity to even.

IXON

React to flow control.

IXOFF

Generate flow control.

IXANY

Treat any character following an XOFF as an XON.

MODEM

Modem control.

LOCAL

No modem control.

MIN0

Set minimum characters to zero.

TIME0

Set maximum characters to zero.

RTSFLOW

RTS Flow control (SCO Unix versions only).

CTSFLOW

CTS Flow control (SCO Unix versions only).

See termio(7) in the Unix documentation for an explanation of the use of MIN0 and TIME0 which correspond to VMIN=0 and VTIME=0 so allowing a 0.1 second timeout.

Example:

\$DEVICE /01C = "/dev/tty0n","2400,odd,cs8" \$DEVICE /01F = "COM2",TC\
\$OPEN /01C
