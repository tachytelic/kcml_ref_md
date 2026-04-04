Popup menus within RTF controls

------------------------------------------------------------------------

It is possible to display a popup menu within the RTF control at the exact point where the user issued a right mouse click. The program must contain a [*RightClick()* event handler for the control. When the event handler is called the](tmp/PROP_RICHEDIT_RCLICK.htm) [*MouseX* and](tmp/PROP_RICHEDIT_MOUSEX.htm) [*MouseY* properties are set to the location of the mouse click that triggered the event. The](tmp/PROP_RICHEDIT_MOUSEY.htm) [*TrackPopup()* menu method is then used to display the menu. The menu must have previously been created by the](tmp/PROP_MENU_TRACKPOPUP.htm) [Menu Editor](FormsDesignerMenubars.htm) within the [Forms designer](TheKCMLFormsDesigner.htm). The following event handler could be used to display the menu *Popup1* at the location of the last right mouse click:

-DEFEVENT Form1.rtfControl1.RightClick() .popup1.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top) END EVENT

 
