Popup menus within Grids

------------------------------------------------------------------------

It is possible to display a popup menu on the grid at the exact point where the user clicked. For popup menus to work you must set either the [*LeftAction* or](tmp/PROP_GRID_LEFTACTION.htm) [*RightAction* properties for the cells that can call a popup menu. The program must also contain an appropriate event handler for the mouse action, for example if you require a left mouse click to display the popup menu then the program must contain a](tmp/PROP_GRID_RIGHTACTION.htm) [*LeftClick()* event handler. When the event handler is called the](tmp/PROP_GRID_LEFTCLICK.htm) [*MouseX* and](tmp/PROP_BUTTON_MOUSEX.htm) [*MouseY* properties are set to the location of the mouse click that triggered the event. The](tmp/PROP_BUTTON_MOUSEY.htm) [*TrackPopup()* menu method is used to display the menu. The menu must have previously been created by the](tmp/PROP_MENU_TRACKPOPUP.htm) [Menu Editor](FormsDesignerMenubars.htm) within the [Forms designer](TheKCMLFormsDesigner.htm). Note that the position returned by *MouseX* and *MouseY* is relative to the top left hand corner of the grid control. Therefore to place a control at the exact location where the user clicked you must add the [*Top* and](tmp/PROPNUM_Y.htm)

*Left* positions of the control to the *MouseX* and *MouseY* properties. The following event handler could be used to display the menu *Popup1* at the location of the last left mouse click:

-DEFEVENT Form1.GridControl1.LeftClick() .popup1.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top) END EVENT

[Click here](ExamplePopupmenus.htm) for an example program.
