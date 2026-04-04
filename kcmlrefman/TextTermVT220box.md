DEC VT220 with boxes

KTERM=vt220box or KTERM=vt320box or KTERM=vt420box

Use this particular *KTERM* if you have a genuine DEC VT220/320/420 or VT510. These terminals have a soft font capability that allows **KCML** to simulate box graphics using the supplied font. [Selfid](selfid.htm) should recognize such capabilities and return a KTERM with the box suffix. However some clones of the VT220 use a different size character cell to the original DEC terminal which may render the over scored characters unsatisfactory. If this is the case check your terminals set-up menu to see if the character cell size can be changed. Otherwise use the [generic VT220](TextTermVT220.htm) terminal type

The default *TERMINFO* assumes that the soft font has been loaded at login time by *cat*'ing the file *vt220font*. If you cannot use soft fonts with your terminal then you should use a *KTERM* of VT220 or edit the *TERMINFO*. Many emulations of the VT220 however do not support the soft font feature.

There are two fonts supplied, vt220font and vt420font which implement different cell sizes. The former has low resolution and should be used on the vt220 and vt320 and the latter on the vt420 and vt510 which support a higher resolution cell size.

The keyboard layout is the same as the [generic VT220](TextTermVT220.htm).
