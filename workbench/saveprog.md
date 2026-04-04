## Saving Programs

Picking Save from the [file menu](File_Menu.htm) or pressing CTRL-S in the editor will bring up a dialog showing the status of the currently loaded programs. Because of overlaying there may be more than one program in memory. KCML tracks the source of each program and can tell if it has been altered by having a ststement modified, a line added or a line deleted. Lines added are assumed to belong program owning the previous line.

If a program has been modified then its summary will be in bold and a save button will be enabled. The workbench recorded the type of program (ascii or compiled) at the time the program was loaded and it will be saved the same way.

In the example below only the second program, V8/COMON, was altered by having a new line 9999 added so only that program can be saved.

<img src="bitmaps/savedlg.png" data-border="0" width="463" height="82" alt="save suggestion dialog" />

The columns in the summary are

|          |                                                                  |
|----------|------------------------------------------------------------------|
| Low      | The starting line number for the program                         |
| High     | The highest line number for that program                         |
| Original | The original line number range of the program when it was LOADed |
| Filename | The name of the program                                          |
| Type     | The type of program loaded (ascii or compiled)                   |
| Save     | There will be a button here for any modified programs            |
