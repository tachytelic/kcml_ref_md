Magna Falcon

KTERM=magna

This terminal, which is available in both a monochrome and a color version, works in a dual mode. It is normally a VT100 terminal (set in the set-up menu for the terminal) but it can be switched under program control into a Wang personality with the same functionality as a 2536 terminal. KCML will do this automatically when it starts executing and restore the original VT100 personality on exit or when escaping to UNIX with the [SHELL](SHELL.htm) statement or with the exclamation mark '!' from the KCML immediate mode prompt. This allows KCML based applications to coexist with other UNIX applications such as MS Word, Word Perfect, OfficePower or Uniplex, all of which use the VT100 personality. For this to work the environment variable *TERM* that UNIX applications use to discover the type of terminal would be set to 'vt100' and *KTERM*, used by KCML, would be set to 'magna'.

The Magna Falcon will work with both XON/XOFF and Wang flow control and when in XON/XOFF mode it uses a special convention so that KCML can recognise all the function keys including SF17 and SF19. It is not necessary to set Wang flow control in order to use the Wang personality.

The color version of the Falcon automatically maps attributes such as bright or blink into different colors. All color terminals and also the late model monochrome screens have the capability of saving screens and windows in the terminal memory thus speeding up the KCML [WINDOW OPEN/CLOSE](WINDOW.htm) statement. This feature is automatically enabled by KCML.

The keyboard contains 16 function keys plus all the other required editing keys. Because the [HALT](TextTermHalt.htm) key sends XOFF this key must not be used. Instead [HALT](TextTermHalt.htm) should be redefined as CTRL-Y and [RESET](TextTermHalt.htm) as CTRL-R using the UNIX *stty* in each users *.profile*

stty intr '^y' quit '^r'

This command is automatically added to the *.profile* file created by the *kcmladmin* installation program.

Both shift and Ctrl need to be pressed together in order to get CTRL combinations.
