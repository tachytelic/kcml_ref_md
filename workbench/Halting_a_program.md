## Halting a program

The halt key in the Workbench is always CTRL BREAK. When a program is halted KCML displays the Workbench debug screen with the current statement centered. This is the statement that was about to be executed when interrupted. It is indicated by being displayed in reverse video. If a form was being displayed at the time then the DEFFORM for that form is the statement notionally being executed.

If the executing program is blocked waiting for input from the keyboard on a KEYIN, INPUT or LINPUT then it usually be necessary to supply the input before the HALT will take effect. For [KEYIN](mk:@MSITStore:kcmlrefman.chm::/KEYIN.htm) only a single character is needed but with [LINPUT](mk:@MSITStore:kcmlrefman.chm::/LINPUT.htm) the whole line must be supplied.
