ANSI console on SCO UNIX

KTERM=ansi

This is used for the console screen on PC implementations of SCO UNIX. It is also available as a PC terminal emulation. It supports color. If KCML is using the DW device driver then it can display full box and block graphics. Otherwise it drives the screen in a text mode in which only type 1 boxes (see [\$BOXTABLE]($BOXTABLE.htm)) are possible.

A alternative font is supplied and installed by the *kcmladmin* program which can be used in text mode to reproduce the Wang character set. This font is loaded by the default *.profile* installed during the installation process.

The default keyboard layout for the ANSI console is

| KCML     | IBM PC            |
|----------|-------------------|
| SF1      | F1                |
| SF10     | F10               |
| SF11     | Shift + F1        |
| SF20     | Shift + F10       |
| SF21     | Ctrl + F1         |
| SF30     | Ctrl + F10        |
| SF31     | Alt + F1          |
| SF0      | Ctrl + Shift + F1 |
| EDIT     | Home              |
| RECALL   | End               |
| INSERT   | Ins               |
| DELETE   | Del               |
| NEXT     | PgDn              |
| PREV     | PgUp              |
| CONTINUE | Ctrl F            |
| EXECUTE  | Ctrl X            |

On enhanced keyboards with 12 function keys F11 returns SF11 normally, SF21 when shifted and SF31 when used with the Ctrl key. SF0 is also on Ctrl F12. Note due to an ambiguity in the ANSI terminal mapping shift tab and shift F2 send the same sequence.
