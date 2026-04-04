Limiting the text entered into a Edit control

------------------------------------------------------------------------

By default if no type is specified by the [*Type\$* property the Edit control will work in much the same way as a regular Edit control. Normally a regular edit control uses the](tmp/PROPSTR_TYPE.htm) [*LimitText* property to restrict the number of characters entered. With the Edit control the](tmp/PROP_EDIT_LIMITTEXT.htm) [*Type\$* property is used to restrict the number of characters entered by specifying the type of control. For example, a type of "S25" would only allow the user to enter a string of 25 characters. Like the regular edit control, the](tmp/PROPSTR_TYPE.htm) [*MaxText()* event handler is called if the user attempts to enter any more than the limit. The type parameter can also be used to instruct the control to accept information in special format, for example a type of "D" would instruct the control to accept or display a date string in the local date format, see](tmp/PROP_DBEDIT_MAXTEXT.htm) [working with dates and the Edit control](WorkingwithdatesandEditcontrols.htm). The

*Type\$* property can be set within the program, for example the following would set the control up to accept a signed numeric value:

.EditControl1.Type\$ = "N-6.2"

The current type being used by the control can also be returned, for example:

CurType\$ = .EditControl.Type\$
