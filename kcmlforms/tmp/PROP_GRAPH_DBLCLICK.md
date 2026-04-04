DblClk (graph control event)

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

**Double click on graph data**

The DblClk() event is triggered when the user double clicks onto a bar element, pie sector or legend. The data set and index are found in [ClickSet](PROP_GRAPH_CLICKSET.htm) and [ClickIndex](PROP_GRAPH_CLICKINDEX.htm) and allow the programmer to take an action based on the element clicked such as bring up further information or drilling down into the data. On pie charts elements may be highlighted using the [Explode()](PROP_GRAPH_EXPLODE.htm) method.

Note that the [*Click()* event handler is called prior to this event handler when the user double clicks on a graph.](PROP_GRAPH_CLICK.htm)

##### Example:


     DEFEVENT Form1.graphControl.DblClk()

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
