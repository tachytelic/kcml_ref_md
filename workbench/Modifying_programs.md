## Modifying programs

New text can be added to a program at the cursor by just typing it. In **Insert mode** as the text is typed the rest of the line is moved off to the right to leave space for the new characters but in **Overwrite mode** the new text overwrites existing text on the line. The default mode is Insert mode and the **Insert key** can be used to toggle between Insert mode and Overwrite mode. Whichever mode is in use text may be entered freely.

When the cursor is moved off a modified statement the line is syntax checked and the user alerted about any problems with a message on the status line. Statements failing the syntax check are displayed in a distinctive color (normally red). A program may be syntax checked at any time using the Show error command (F7) which searches from the current statement to the end of the program for statements that contain an error. SHIFT F7 will move the cursor to the last statement in the program with a syntax error.

Note that each individual statement is syntax checked independently, so it is possible for a portion of a line to be in error whilst surrounding statements on the same line are correct. This does not cause any compatibility problems with KCML versions prior to KCML 4.
