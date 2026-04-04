Adding strings to the drop down portion of an Edit control

A normal combo box allows items to be added to the control before the control is used. With the Edit control items are only added when the user selects the down arrow to display the drop down. This can save time when the form is being drawn as the controls are only filled if the user attempts to display them. The drop down portion is only available if the

*DropDown* property has been set to anything other than *NoDrop* in the Forms Designer.

Each time the user clicks on the down arrow in order to display the drop down, the [*DropDown()* event handler is called. From within this event handler items are added with the](tmp/PROP_KCMLEDIT_DROPEVENT.htm) [*Add()* method. It is possible to prevent the](tmp/PROP_GCOMBO_ADD.htm) [*DropDown()* event handler from being called multiple times if the](tmp/PROP_KCMLEDIT_DROPEVENT.htm)

*DropDownFilled* property is set to *TRUE*. The following example shows an event handler for the control EditControl1 that fills the control with the numbers 1 to 20 if the user clicks on the down arrow.

\- DEFEVENT Form1.EditControl1.DropDown() FOR Count = 1 TO 20 CONVERT Count TO Tmp\$, (######) .EditControl1.Add(Tmp\$) NEXT Count .EditControl1.DropDownFilled = TRUE END EVENT

Each string added to the list can have an associated tag which is specified by the second parameter of the [*Add()* method. The tag can be used as an alternative method of searching for items within the list (See](tmp/PROP_GCOMBO_ADD.htm)

*GetTag\$()).* The tags themselves are displayed in the first column of the drop down list.
