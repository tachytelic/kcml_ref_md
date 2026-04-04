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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Data(int, int, numeric) Method

**Graph data (index and set)**

The Data(set, index, data) method adds data to the graph. On pie charts, only one data set is displayed (the first), but on bar charts it is possible to have one data set (with each bar in a separate color) or multiple data sets (with each data set in a separate color, but all elements of each data set in the same color).

The index and set values are arbitrary values, which do not need to be declared first. Graphs are displayed in increasing order of data set and data index.

On simpler graphs, where only one data set is being displayed, the simpler form of [Data()](PROP_GRAPH_DATA2.htm) may be used.

##### Example:


     .graphControl.Data(i, j, a)

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
