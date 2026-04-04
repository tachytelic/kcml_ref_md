Programming function keys

Function keys can be programmed from the server using an extension to the VT220 escape sequences, originally introduced for the Magna terminal. This sequence can be issued directly in [VT220 mode](TextSeqVT.htm) and also in [KCML mode](TextSeqDW.htm) by prefixing it with a HEX(02).

ESC \[ ? *Fn* ; P1; ... ; Pn m

Where Fn is a number (0 to 39) defining the key to be programmed and P1 to Pn represent the decimal characters of the string to be sent when the key is pressed. This cannot contain zero. The numbers are separated by semicolons. E.g. To program F1 to send ? and RETURN you might code

PRINT HEX(021B);"\[?0;63;13m"

The function key numbers are in 4 blocks of 10 (corresponding to F1 to F10) for unshifted, shifted, with CTRL and with shift CTRL. Thus key 0 is F1, key 11 is F2 shifted etc.
