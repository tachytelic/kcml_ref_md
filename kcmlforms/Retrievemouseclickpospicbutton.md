Retrieving the position of a mouse click within a picture button

------------------------------------------------------------------------

If a [*Click()* event handler exists for the picture button, the exact location where the mouse clicked on the control is passed into the event handler with the](tmp/PROP_PICBUTTON_CLICK.htm) [*MouseX* and](tmp/PROP_BUTTON_MOUSEX.htm) [*MouseY* properties. These properties can then be used by the event handler to place a control at the point where the mouse clicked. For example, the following event handler would move the static text control *txtControl1* to the location of the mouse click on the picture button. Note that the](tmp/PROP_BUTTON_MOUSEY.htm) [*MouseX* and](tmp/PROP_BUTTON_MOUSEX.htm) [*MouseY* values are relative to the top left corner of the picture button, therefore to place the static text correctly the static text controls](tmp/PROP_BUTTON_MOUSEY.htm) [*Left* and](PROPNUM_X.htm) [*Top* properties are added to](tmp/PROPNUM_Y.htm) [*MouseX* and](tmp/PROP_BUTTON_MOUSEX.htm)

*MouseY*.

\- DEFEVENT Form1.picControl1.Click() .txtControl1.Left = ..Left + ..MouseX .txtControl1.Top = ..Top + ..MouseY END EVENT
