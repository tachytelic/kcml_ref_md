RightClick (graph control event)

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

**Right click on graph data**

The RightClick() event is triggered when the user right-clicks onto a bar element, pie sector or legend. The data set and index are found in [ClickSet](PROP_GRAPH_CLICKSET.htm) and [ClickIndex](PROP_GRAPH_CLICKINDEX.htm) and allow the programmer to take an action based on the element clicked such as bring up further information or drilling down into the data. If the user clicks on a legend item, the values returned will depend on whether the graph has a singal or mutliple sets of data. On a single set graph, each legend represents a data item, so the ClickSet will be the single set of the graph and the ClickIndex wil be the item of the legend. On a multiple set graph, each legend item represents a data set, so the ClickSet will be the legend clicked and the ClickIndex will be 0 as no particular item is accessed. On pie charts elements may be highlighted using the [Explode()](PROP_GRAPH_EXPLODE.htm) method.

Note that this event handler can be used to display popup menus by calling the [*TrackPopup()* menu control method. Use the](PROP_MENU_TRACKPOPUP.htm) [MouseX](PROP_GENERIC_MOUSEX.htm) and [MouseY](PROP_GENERIC_MOUSEY.htm) properties to position the popup menu at the point on the control surface the click occurred.

##### Example:


     DEFEVENT Form1.graphControl.RightClick()

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
