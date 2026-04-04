## Stepping through a program

A halted program can have its execution traced by stepping through one statement at a time with the space bar. Each time space is pressed the program will execute the current statement and halt again. The reverse video bar representing the current statement is updated as it goes allowing the programmer to see exactly where in the program it is. Any output from the program goes to the execute screen which can be inspected at any time with F4. If the statement being executed requires keyboard input such as [<u>LINPUT</u>](mk:@MSITStore:kcmlrefman.chm::/linput)) or [<u>KEYIN</u>](mk:@MSITStore:kcmlrefman.chm::/keyin)) then the execute screen is displayed until the characters are entered whereupon the debug screen is represented.

When stepping with space any [<u>REM</u>](mk:@MSITStore:kcmlrefman.chm::/rem)), [<u>DIM</u>](mk:@MSITStore:kcmlrefman.chm::/dim)) or [<u>COM</u>](mk:@MSITStore:kcmlrefman.chm::/com)) statements are skipped automatically as they do not have any effect at runtime.

Execution of subroutines will proceed in one step. To descend into a subroutine and execute each line therein the **I** key should be used instead of the spacebar to ensure that execution continues into subroutines rather than over them.

To step through an event handler on a form, break into the form with the [HALT key](Halting_a_program.htm) which will interrupt the program and make the DEFFORM the current statement. If you then press **I** (to step into a subroutine) the form will be redisplayed allowing you to trigger the event by pressing the button or tabbing out of the edit or whatever. The debugger will then get control with the current line on the DEFEVENT for the event handler allowing you to step through its code. When you RETURN from the handler control will pass to the form again.

If the [Current Variables](WinCurrentVars.htm) window is displayed (as in the default scene A) then any variables on the line being stepped will be temporarily displayed in that window both on entry and, if modified, on exit in red.
