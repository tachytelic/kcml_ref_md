NoItemClick (graph control event)

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

**Click on non data area in graph**

The NoItemClick() event is triggered when the user clicks onto an area of the graph not occupied by a bar element, pie sector or legend. If the user clicks on one of these items the [Click](PROP_GRAPH_CLICK.htm) event is triggered instead.

##### Example:


     DEFEVENT Form1.graphControl.NoItemClick()

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
