XLabel (graph control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> XLabel(int, string) Method

**Graph x-axis label (index and text)**

The graph XLabel(index, string) method is used to provide labels along the X-axis of bar graphs. It has no use on pie charts. On graphs with multiple data sets, the elements with the same index from each of the data sets are grouped together and labelled.

For pie charts and to label each data set, see the [Legend()](PROP_GRAPH_LEGEND.htm) method.

##### Example:


     .graphControl.XLabel(i, a$)

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
