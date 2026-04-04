NoItemRightClick (graph control event)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Right click on non data area in graph**

The NoItemRightClick() event is triggered when the user right-clicks onto an area of the graph not occupied by a bar element, pie sector or legend. If the user clicks on one of these items the [RightClick](PROP_GRAPH_RIGHTCLICK.htm) event is triggered instead.

Note that this event handler can be used to display popup menus by calling the [*TrackPopup()* menu control method. Use the](PROP_MENU_TRACKPOPUP.htm) [MouseX](PROP_GENERIC_MOUSEX.htm) and [MouseY](PROP_GENERIC_MOUSEY.htm) properties to position the popup menu at the point on the control surface the click occurred.

##### Example:


     DEFEVENT Form1.graphControl.NoItemRightClick()

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
