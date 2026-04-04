Spectrix SPX701

KTERM=spx701

Like the [Magna Falcon](TextTermMagna.htm) the SPX701 is a dual mode terminal capable of functioning as a VT100 or as a 2336 type terminal. In general you should set the terminal to VT100 mode and set the flow control to XON/XOFF. The environment variable *TERM* should be set to 'vt100' and *KTERM* to 'spx701' in your *.profile*. Then whenever KCML starts up it will switch the terminal automatically from VT100 to its Wang personality and switch it back again on exit or during shell escapes.

The SPX701 is capable of using either XON/XOFF or Wang flow control. In XON/XOFF mode it cannot send SF17 or SF19 as these keys respectively start and stop communications. It also implements an extended bi-directional flow control which has the side effect that lower case w's, x's and y's cannot be underscored in a [LINPUT](LINPUT.htm).

Like the Falcon this terminal is also available in a color model which can remap attributes like bright and blink into colors.

The keyboard contains 16 function keys plus all the other required editing keys. Because the HALThalt key sends XOFF this key must not be used. Instead [HALT](TextTermHalt.htm) should be redefined as CTRL-C and [RESET](TextTermHalt.htm) as CTRL-R using the UNIX *stty* command in the users *.profile*

stty intr '^c' quit '^r'

This command is automatically added to the *.profile* file created by the *kcmladmin* installation program.

Both shift and Ctrl need to be pressed together in order to get CTRL combinations.
