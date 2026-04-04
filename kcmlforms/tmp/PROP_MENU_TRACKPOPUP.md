TrackPopup (menu control method)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> TrackPopup(int, int) Method

**Pops up the menu at the specified coordinates**

***Int1***      Specifies the *x* coordinate of the popup menu\
***Int2***      Specifies the *y* coordinate of the popup menu

This method is used to display a popup menu at the specified coordinates. Popup menus are created separately via the [Menu editor](/FormsDesignerMenubars.htm) in the [KCML Forms Designer](/TheKCMLFormsDesigner.htm). This method is only useful when called by the [*Click()* Picture control event handler or the](PROP_PICBUTTON_CLICK.htm) [*LeftClick()* and](PROP_GRID_LEFTCLICK.htm) [*RightClick()* Grid control or Tree control event handlers as the mouse pointer coordinates at the time of the click automatically passed into these handlers.](PROP_GRID_RIGHTCLICK.htm)

The mouse pointer co-ordinates are returned by the [*MouseX* and](PROP_BUTTON_MOUSEX.htm) [*MouseY* properties. These can be used with *TrackPopup()* to place the menu at the exact location of the click. For example, the following grid control event handler displays the menu *Popup1* at the location of the last mouse click: -DEFEVENT Form1.GridControl1.LeftClick() .menu1.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top) END EVENT](PROP_BUTTON_MOUSEY.htm)

Note that when working with the Grid control, the [*LeftClick()* and](PROP_GRID_LEFTCLICK.htm) [*RightClick()* event handlers can only be used if the](PROP_GRID_RIGHTCLICK.htm) [*LeftAction* and](PROP_GRID_LEFTACTION.htm) [*RightAction* properties are set accordingly.](PROP_GRID_RIGHTACTION.htm)

##### See also:

Other [menu](menu.htm) properties, methods and events, [menuitem](menuitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
