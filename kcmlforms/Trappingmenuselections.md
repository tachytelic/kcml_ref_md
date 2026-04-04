Trapping menu selections (The Select() event handler)

------------------------------------------------------------------------

To trap a menu selection the [*Select()* event handler is used for the option. Event handlers are best created by setting the "Create KCML Event" option within the](tmp/PROP_MENU_SELECT.htm) [Menu Editor](FormsDesignerMenubars.htm). The [*Select()* event handler can also be used to set and unset a check mark from a menu option. Check marks are set with the](tmp/PROP_MENU_SELECT.htm)

*Checked* property. For example, the following would set and unset the check from the "Test" option within the "File" menu each time the option is selected:

\- DEFEVENT Form1.menu1.FileTest.Select() IF (..FileTest.Checked) ..FileTest.Checked = FALSE ELSE ..FileTest.Checked = TRUE END IF END EVENT
