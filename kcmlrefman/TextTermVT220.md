Generic VT220

KTERM=vt220 or KTERM=vt320 or KTERM=vt420

This is also a very common terminal which has 20 function keys as well as editing keys. The VT320, VT420 and VT510 can all be considered the same and aliases are provided in TERMINFO allowing KTERM values of vt320 and vt420 to be used. Again many other terminals (e.g. the Wyse 185) provide VT220 emulations, although they very rarely provide the soft font capability. The generic VT220 has a limited soft font capability which can allow a limited box graphics emulation (see [VT220 with boxes](TextTermVT220box.htm)). A default [\$SCREEN]($SCREEN.htm) file SCREEN.vt220 is supplied which maps all the block graphic characters to a single solid graphic. A wide range of multinational characters are available between 0x80 and 0xFF.

Be aware that on most VT220s the key in the place where backspace should be actually sends DEL or \x7F. KCML will cope with this provided that DEL is not defined as [HALT](TextTermHalt.htm) so *stty* should be used to define [HALT](TextTermHalt.htm) as some other key e.g. CTRL-C

stty intr '^c' quit '^r'

This command is automatically added to the *.profile* file created by the *kcmladmin* installation program.

The standard function keys will give access to SF 1 to 20 and the editing pad is mapped as follows:

| KCML Key | VT220 Equivalent |
|----------|------------------|
| RECALL   | FIND             |
| EDIT     | SELECT           |
| INSERT   | INSERT           |
| DELETE   | REMOVE           |
| NEXT     | NEXT             |
| PREV     | PREV             |

The shifted function keys are normally only available for local user programming but if the supplied *vt220key* file is cat'ed into the terminal in *.profile* it will reprogram those keys to make them available. The standard TERMINFO definition assumes this has been done.
