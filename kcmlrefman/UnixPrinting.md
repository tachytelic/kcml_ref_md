Unix server printing

There are two main ways to print on a Unix server, writing directly to a device as if it were a file, or printing through a spooler. The latter method is to be preferred as it avoid contention but in some circumstances, such as forms that need alignment, it may be better to print directly.

Direct printing

<span id="Direct"></span>

To print direct you need to know the name of a suitable device, the device should not be used for any other purpose and you will need write access. Naming schemes differ between versions of Unix. \$DEVICE /015="/dev/tty09 ALF=Y"

Most parallel printer drivers will enforce a locking scheme of their own which will cause a second attempt to open the printer to fail so it is desirable to use [\$OPEN]($OPEN.htm) and [\$CLOSE]($CLOSE.htm) around the print code. The [\$DEVICE]($DEVICE.htm) statement itself does not open the device but rather the first \$OPEN or PRINT will do so and rather than error trap the PRINT statments it is better to force the issue in one place with a \$OPEN.

Using spoolers

<span id="Spooler"></span>

All versions of Unix support print spooling with the *lp* program though there are some implementation differences particularly with BSD derived Unix versions such as HP-UX. In general you set up a pipe into the lp program for a particular print queue. The pipe gets opened when you \$OPEN the device and all printed output is logged to disk by the spooler. When you are finished printing you close the pipe with \$CLOSE and Unix will start to print to the device associated with the queue. There are numerous switches to lp to control the print process. Most spooler support network printing with the lpr protocol.

\$DEVICE /015="\|lp -d 3rdFloorLaser ALF=Y"

For more information about Unix spooling see the man pages for lp, lpstat and lpadmin.

See also

[Network printing with Kprint](kprint.htm)
