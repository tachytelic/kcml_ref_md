## Editor

While most of the editing capabilities of the old editor have been preserved, some new features are available:

- The client is now responsible for line oriented editing which should make the editor more responsive on slow connections as less text needs to be sent from the server to the client.
- The editor window has a scroll bar which supports a mouse wheel if you have one.
- Keywords and variables are now colored. This can be configured by the user using a palette from which colors can be dragged and dropped onto syntax elements in the editor window. Use the [Color Options](coloropts.htm) menu item on the Config menu to bring up the palette. This dialog can also be used to change the font used. Colors are no longer limited to the 16 DOS VGA colors and can be customized from any color supported by the display. The default colors are more subtle than the green on black of the previous KCML4 editor.
- Variables that have not been declared in a DIM or LOCAL DIM are underlined.
- Line numbers are supressed by default to save space on the screen. They can be toggled on or off using the Line Numbers toggle on the [Line menu](Line_Menu.htm).
- [Auto-completion](wbsuggestion.htm#autocomplete) is available for IF, WHILE, SELECT CASE, ERROR DO and FOR statements.
- A similar [suggestion](wbsuggestion.htm) prompting mechanism allows autocompletion of variable names based on what is in the symbol table. If you have typed part of a variable name you can then press ALT-cursor-down to get a list of matching symbols in a popup window from which you can pick the one you want to complete the current item. If there is only one match then pressing RETURN in that popup will pick it. It can also prompt with suggested method or events for a partly completed form or object expression based on an evaluation of what has beeen typed thus far and what can legally complete it.
- Form components can be dragged from the [form browser](wbbrowseforms.htm).
- The forms editor is now invoked from a right click context menu and not by right double clicking on the DEFFORM. It can also be invoked from the [forms browser](wbbrowseforms.htm).
- The forms editor can be used in read-only mode while debugging and for with forms that reside in shared memory. The controls will be marked in red and any changes made in the editor will be discarded.
- Event handler code in the global can now be expanded or contracted with either the toolbar buttons, which expand and contract all handlers, or by clicking or using F5 on a particular DEFEVENT keyword for one handler. Previously handlers in the global were always expanded and could not be collapsed.
- [Blank lines](BlankLines.htm) are allowed in programs to improve readability.
