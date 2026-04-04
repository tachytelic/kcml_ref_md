## Running a program

To run the current program in memory either type [<u>RUN</u>](mk:@MSITStore:kcmlrefman.chm::/run)) in immediate mode on the console window or press F11 in the editor or debugger window. KCML will switch focus to the form or to the text output screen when a program is running.

When the program terminates (e.g. on STOP, END or dropping off the last line) the KCML Workbench regains control and the program is displayed with a message on the status bar saying why the program stopped. Generally the debugger will be active unless it stopped on END or by falling off the end of the program in which case the program cannot be continued.
