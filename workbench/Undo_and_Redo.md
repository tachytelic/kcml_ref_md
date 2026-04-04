## Undo and Redo

The editor has a multilevel Undo/Redo feature allowing previous editing operations performed to be undone. Pressing the Undo key (CTRL BACKSPACE or CTRL U) reverses the effect of the last operation that changed the program. This could be a simple change to one line, a multi line cut or paste, or a global replace effecting all the lines in the program. Pressing the undo key again will undo the previous change and so on. The last 100 changes made to the program with the editor are logged in an undo stack allowing a number of operations to be undone in reverse order.

Undo works in terms of entire statements.

The last changes undone can even be be redone if necessary by pressing the Redo key (SHIFT CTRL U).

The undo stack is cleared when a new program is loaded, the CLEAR command is executed or a line is modified in the console/immediate mode using the old editor.
