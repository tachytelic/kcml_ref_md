Using popup menus with picture buttons

------------------------------------------------------------------------

It is possible to display a popup menu on the picture at the exact point where the user clicked. The program must contain a [*Click()* event handler for the picture button. When the event handler is called the](tmp/PROP_PICBUTTON_CLICK.htm) [*MouseX* and](tmp/PROP_BUTTON_MOUSEX.htm) [*MouseY* properties are set to the location of the mouse click that triggered the event. The](tmp/PROP_BUTTON_MOUSEY.htm) [*TrackPopup()* menu method is then used to display the menu. The menu must have previously been created by the](tmp/PROP_MENU_TRACKPOPUP.htm) [Menu Editor](FormsDesignerMenubars.htm) within the [Forms designer](TheKCMLFormsDesigner.htm). The following event handler could be used to display the menu *Popup1* at the location of the last left mouse click:

-DEFEVENT Form1.picControl1.Click() .popup1.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top) END EVENT
