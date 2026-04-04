Local printing

KCML supports local printing from the client or from a suitable text mode terminal via the LCL=Y device specifier in [\$DEVICE]($DEVICE.htm). By default the device /004 is setup as a local printer as if it had been specified with \$DEVICE /004="stdout,LCL=Y,DIR=Y"

When the LCL=Y specifier is used the filename is disregarded and is only set to stdout as a convention. The actual printer used is set in the [client printer preferences](mk:@MSITStore:kclient.chm::/printerpreferences.htm).

The DIR=Y specifier means direct printing where the Windows printer driver is bypassed and the bytes are sent directly to the printer. This requires the application to take responsibility for setting page orientation, fonts etc with printer specific escape sequences if the printer defaults are not what is required. In particular with page printers such a LaserJet, the application must send a HEX(0C) to flush out the last page. Furthermore care must be taken with the code page used for text printing as HP printers do not use Latin-1 as their default for text printing and have to be programmed to use Latin-1/Roman-8. However this mode will give the best performance and may be mandated by older software which embeds control sequences..

Alternatively if DIR=N is specified then the client will send the print stream through the printer driver specified in the preferences. Any escape sequences will be ignored and the settings associated with that printer in Windows will be used. This mode should be used with special devices such as fax printers where the printer driver must be used.

Windows will, by default, spool all printer output so it is important that an application tell KCML when printing is complete so that KCML can, in turn, tell the client and therefore instruct Windows to stop spooling and start printing. To do this the print job should be enclosed within a [\$OPEN]($OPEN.htm) and a [\$CLOSE]($CLOSE.htm) grouping e.g. \$DEVICE /019="stdout,LCL=Y,DIR=N" \$OPEN /019 SELECT PRINT /019 PRINT "This will use default printer driver settings" SELECT PRINT /005 \$CLOSE /019

The print stream is multiplexed together with the screen stream on the connection to the client or terminal so if the printer is not spooled and goes off line this will hang the screen.

**Note**: The DIR=Y/N specifier was introduced with KCML 6.0 and was not available for KCML 5.x However with version 5.02 Kclient all printing can be done through the Windows print driver by creating a *login.ini* text file in the kclient directory. This can be created with notepad and should contain: \[printer\] TextMode=1
