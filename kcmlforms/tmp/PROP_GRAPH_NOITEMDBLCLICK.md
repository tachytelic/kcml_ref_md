NoItemDblClk (graph control event)

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

**Double click on non data area in graph**

The NoItemDblClk() event is triggered when the user double clicks onto an area of the graph not occupied by a bar element, pie sector or legend. If the user clicks on one of these items the [DblClk](PROP_GRAPH_DBLCLICK.htm) event is triggered instead.

Note that the [*Click()* event handler is called prior to this event handler when the user double clicks on a graph.](PROP_GRAPH_CLICK.htm)

##### Example:


     DEFEVENT Form1.graphControl.NoItemDblClk()

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
