NT server printing

There are two main ways to print on a Windows NT or Windows 9x server, writing directly to a device as if it were a file and using a printer driver in passthrough mode.

Direct printing

To print direct you need to know the name of a suitable device. The parallel printers are named LPT1, LPT2 etc and serial printers are named COM1, COM2 etc. You will need to use the Windows Control Panel to set the line speed for serial lines before you can use them. It is also possible that these devices might be locked by other users. To make a parallel printer available you can use \$DEVICE /015="LPT1"

It is also possible to print direct on a printer attached to another Windows computer on the LAN by using UNC file names e.g. \$DEVICE /015="\\Laptop\LPT1"

however this will only work if the device is shared. There are particular problems with a KCML server accessing network printer shares when the computers are in an NT Domain controlled by NT security. Because the KCML runs as an NT service it does not have security credentials that allow it access to network shares on other secure machines. See [Article Q124184](%20http://support.microsoft.com/support/kb/articles/Q124/1/84.asp%20) in the Microsoft Knowledge base about why they have this problem and some workaround.

Using printer drivers

Printer drivers written for Win32 should support a passthrough mode that allows raw text to be passed through unaltered to the printer. This is supported in KCML with the special grammar \$DEVICE *devaddr*="\>(*printername*)\[*docname*\]" where *printername* is the name of a printer as defined in the printers folder of Windows, the optional *docname* is your name for the document. If no *printername* is given then the current default printer will be used. For example:

\$DEVICE /015="\>(HP LaserJet 5Si/5Si MX PS)" \$DEVICE /016="\>(Epson Stylus Color 700)My report in color ALF=Y" \$DEVICE /017="\>()"

Note how you can still use options clauses even if you use the *docname* string.
