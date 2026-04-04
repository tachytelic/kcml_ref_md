## Search Menu

These options are used for searching and replacing text in edit mode, navigating the program and inspecting variables.

<img src="bitmaps/searchmenu.png" data-align="BASELINE" data-border="0" alt="Search dialog" />

### Find ...

<span id="find"></span>

Used to search for the specified text or symbol. See [Searching for text and symbols](Searching_for_text.htm). You can also use the F3 function key or CTRL-F as a shortcut to bring up the search dialog.

### Replace ...

<span id="replace"></span>

Used to search for the specified text or symbol and replace it with the specified text or symbol. See [Searching and replacing text and symbols](Replacing_text.htm). You can also use the SHIFT-F3 function key as a shortcut.

### Search next

Used to find the next occurrence of the text or symbol currently being searched for. Also available with CTRL-N

### Search previous

Used to find the previous occurrence of the text or symbol currently being searched for. Also available with CTRL-P.

### Syntax check

Performs a syntax check of the program currently in memory. If errors are detected then the cursor is placed onto the first erroneous line. The F7 function key acts as a shortcut for this option.

### Select object

This option copies the variable, integer, function, subroutine label or text currently under the cursor into the command window. You can also use the F5 function key for this.

### Action object

Used to action the variable, line number, function, subroutine label or text currently in the status line. You can also use SHIFT-F2. Integer values are considered to be line numbers, therefore actioning an integer value will change to displaying the program from the actioned line number. If the line does not exists then the display will start from the next line in sequence. Actioning a subroutine label will change the display to list from the subroutine definition. If the subroutine exists within the currently selected global partition then the global text is displayed. Actioning a variable will display its dimensioning information and contents on the output window in [LIST DIM](mk:@MSITStore:relnotes.chm::/list_dim.htm) format.

### Revisit

After a line number or subroutine has been actioned, selecting **Revisit** returns to the place where the line or subroutine was actioned. [Revisting](Revisting.htm) can be nested. You can also use F6 as a shortcut.
