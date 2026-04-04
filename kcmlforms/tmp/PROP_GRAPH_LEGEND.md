Legend (graph control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Legend(int, string) Method

**Graph legend (index and text)**

The graph **Legend()** method allows the provision of a legend for pie charts and multiple data set graphs. In both cases, elements are distinguished by color, and the legend colors are displayed in a list on the right-hand side of the graph together with the supplied description. The two parameters are the index number and a description string.

The [XLabel()](PROP_GRAPH_XLABEL.htm) method is used to provide descriptions along the X-axis.

##### Example:


     .graphControl.Legend(i, a$)

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
