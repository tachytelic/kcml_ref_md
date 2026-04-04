Explode (graph control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Explode(int, int, int) Method

**Show graph item in exploded form**

The **Explode()** method allows a particular element of the graph to be highlighted in some manner. It currently applies only to pie charts and highlights the element by showing the pie sector slightly removed from the pie circle. The first two parameters are the data set and dat index; the last parameter should be TRUE to show the item as exploded and FALSE to show it as normal. Any number of items may be shown as exploded at any time.

Note that exploding items using the 3D pie chart style is not recommended because only the curved edge is shown in 3D and not the pie sector sides (which are never seen unless items are exploded).

##### Example:


     .graphControl.Explode(i, j, k)

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
