Forms Designer - Setting the tab order

------------------------------------------------------------------------

The Tab order is the order in which the user can move between controls when the Tab and Shift Tab keys are pressed. It is important that the order is set correctly and in a logical manner so that the user does not get confused. To set the tab order click on the [<img src="bitmaps/forms_de.gif" data-align="BOTTOM" data-border="0" alt="tab order button" />](TheEditMenuSetTaborderoption.htm) tool bar button, this will then show the current tab order. To change the order simply click on the controls in the order in which you require. Notice that Tab controls have their own separate ordering so controls on a tab are shown in a different color.

When setting accelerator keys in static text controls, the control in the tab order immediately following the static text will be the control that gets focus if the accelerator is pressed.

<img src="bitmaps/inherit.gif" data-align="BASELINE" data-border="0" width="355" height="217" alt="Example of setting the tab order on a form with an embedded tab control" />  

This order cannot be set or changed at runtime. Controls can be left out of the tab order by setting their [TabStop](tmp/PROPNUM_TABSTOP.htm) style to FALSE however.
