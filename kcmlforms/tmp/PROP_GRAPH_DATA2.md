Data (graph control method)

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
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Data(int, numeric) Method

**Graph data (index)**

The Data(index, data) method is a simplified form of [Data()](PROP_GRAPH_DATA.htm) where all data belongs to the same data set. This will always be the case with pie charts (multiple pie charts are not currently supported) and often the case with bar charts.

The index values may be arbitrary values and the graph is displayed with index values in increasing order.

##### Example:


     .graphControl.Data(i, a)

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
