SELECT PASSWORD command

------------------------------------------------------------------------

General Form:

SELECT PASSWORD \[! \[challenge\$\]\]

------------------------------------------------------------------------

The SELECT PASSWORD command is used to scramble a program that is to be [SAVEd](SAVE.htm) with the [SAVE \<!\>](SAVE.htm) command. SELECT PASSWORD is a separate command, and cannot be combined with other SELECT parameters. It prompts on the console device if not scripted with LOAD ASCII or SELECT CI.

If the command has been executed from the console, KCML will prompt twice for a password. Echoing of characters as they are entered is suppressed, so the password has to be entered identically to avoid mistakes. If the command is scripted then no prompt for input will be made and the next string entered will be the password used. The password is saved with the scrambled program. The password stays in effect for further [SAVEs](SAVE.htm) until a [CLEAR](CLEAR.htm) is issued.

When KCML is executing a scrambled program, all [LISTing](LIST.htm), editing, and [TRACEing](TRACE.htm) is disabled. Pressing the interrupt key (Ctrl+BREAK) will stop the program, but the only actions available are [CLEAR](CLEAR.htm) and [LOAD RUN](LOAD_RUN.htm). For protected programs the editor displays the message "Protected Program".

The program may be revealed by specifying the original password with the SELECT PASSWORD command immediately after the program is [LOADed](LOAD.htm). As an aid to support of scrambled programs, it is possible to temporarily reveal the executing program without giving away the master password. The SELECT PASSWORD ! command will display a random string of characters as a challenge and prompt for a response. The user can then contact the author who can use SELECT PASSWORD ! challenge\$ to generate the response string. The command will prompt the author for the master password.

See also:

[SAVE](SAVE.htm), [RESAVE](RESAVE.htm)
