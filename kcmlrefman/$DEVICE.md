\$DEVICE

------------------------------------------------------------------------

<div class="Generalform">

General Forms:\
\

<div class="indent">

1.  \$DEVICE /devaddr = nativefile\[, type \]
2.  alpha_receiver = \$DEVICE /devaddr

</div>

Where:

<div class="indent">

|  |  |  |
|----|----|----|
| nativefile | = | string expression yielding a native OS file name. This may contain an optionlist. |
| type | = | reserved words DISK, or TC. Exceptionally it may alpha expression yielding device information for a TC device. |

</div>

</div>

------------------------------------------------------------------------

KCML devices consists of character devices, files, disk platters, printers, serial line telecommunications devices and pipes. They are referenced using 3 digit hexadecimal device address which are mapped to the real devices by the Device Equivalence Table or DET. The \$DEVICE statement is used to add, amend or delete an entry from the list of currently defined devices in the DET, thus establishing a link between a native operating system file or device and a KCML device. KCML programs are thus insulated from the details of how these devices are named in the operating system.

If the right hand side of a \$DEVICE statement is a blank string then this will un-define a device by removing it from the table. A second \$DEVICE statement for a given device address redefines the first. A redefining \$DEVICE statement will first close the device currently open acting somewhat like [\$REWIND]($REWIND.htm).

The \$DEVICE statement can also be used as a function returning the name of the file corresponding to a given device. If the device has not previously been defined a blank is returned.

The type specifier is optional and need only be specified for TC devices or disk platters. In the case of disk image platters the keyword DISK should be used. However if there is no explicit type and the device address begins with \`D', \`3' or \`B' then DISK will be assumed. The keyword TC means a 2227B emulation. If there is a type string rather than a keyword then KCML will define a serial line device. See [Working with serial line devices](TCdevices.htm) for more about telecommunications support.

Device addresses are 3 hexadecimal digits. The first digit of a device address is disregarded and set to \`0' unless it is a \`D', \`3' or \`B' which are reserved for disk platters.

Certain devices are predefined:

| Device address | Purpose | Notes |
|----|----|----|
| /000 | null device | /dev/null for Unix and /DEV/NUL under Windows |
| /001 | input device | stdin |
| /005 | output device | stdout |
| /004 | local printer | The local printer is set to stdout and will use the printer port of the terminal if this capability is specified with PrintOn/PrintOff clauses in the terminals KCML TERMINFO database description. Kclient has local printing capability. If there is no local printer capability it will be initailzed to the same as the /015 device. |
| /015 | print device | Set to /dev/lp under Unix or a local printer under Windows. |

The first three devices are not strictly part of the DET and cannot be redefined with \$DEVICE. Under Windows the both the /004 and the /015 devices are initialized to be local printers.

Many device mappings have optional features that are controlled by an options clause appended to the native file name on the right hand side of the \$DEVICE. These are 3 character keywords which take boolean values of Y or N for ON and OFF respectively e.g.

\$DEVICE /019="/dev/tty98 ALF=Y"

These options are usually specific to a particular type of device and will generally be disregarded if applied to another type of device though this cannot be assumed. Unrecognized keywords will be ignored. Options are generally assumed to be N unless specified. Multiple space or comma separated options are supported.

| Keyword | Device class |  |
|----|----|----|
| ALF | Printers | Autolinefeed mode. If Y a HEX(0A) will be sent after every lone HEX(0D). HEX(0D0A) pairs are left unchanged. |
| AFF | Printers | Autoformfeed mode. If Y a HEX(0C) will be sent when the print job is closed by \$CLOSE provided at least one character was sent and the last character sent was not a HEX(0C). Applies only to Windows server printing through a printer driver. The default is Y but it can be suppressed with AFF=N. |
| BID | Printers | If set to Y then the printer is assumed to be capable of printing Arabic/Hebrew from right to left. |
| DIR | Printers | Affects [local printing](LocalPrinters.htm) (through the client) where the client is KClient (6.0 or greater). If a Y then printing is direct mode bypassing the printer driver which means printer specific control sequences may be used for compatibility with DOS and Unix. If an N then text mode printing through the Windows printer driver is used (all control codes will be ignored, but printing will work on the widest range of windows printers). The default is Y. |
| EXT | Disk platters | Extended format. Unnecessary and ignored as all KCML platters are extended. |
| LCL | Printers | If Y then this marks the printer device as local and output will be sent to the client. To maintain backwards compatability this mode also sets ALF=Y. If auto-linefeed is not required ALF=N must be specified **before** LCL=Y. See note on precedence. |
| LOG | Printers | If Y then raise an entry in the [event log](WRITE_LOG.htm) when the device is opened or close. This can be useful in determining if a spooled print request has been dispatched. |
| LPD | Printers | If Y the printer is to be considered a [KPRINT](kprint.htm) network LPD printer. |
| TMO | Character devices | On Unix only setting this to Y will produce a 0.1s delay between each character read. |
| RAW | Local printers | Setting RAW=Y will stop the client interpreting HEX(02) escape sequences. Set RAW=Y ALF=N to pass binary data, e.g. a PCL font, intact through to the printer. The default is RAW=N. |
| XLA | Printers | If Y then pass output through the \$PRINTER translate table. |

##### Note:

Options have a descending order of precedence. If conflicting options are specified the leftmost one will take effect.

Syntax examples:

\$DEVICE /019="/dev/tty98","EVEN,CS7,MIN0"\
\$DEVICE /219="\|lpr"\
PRINT \$DEVICE /219

See Also

[Working with printers](PrinterDev.htm)\
[Local printers](LocalPrinters.htm)\
[Working with pipes as devices](pipes.htm)\
[Working with serial line devices](TCdevices.htm)\
[SELECT](SELECT.htm)\
[LIST DT](LIST_DT.htm)\
