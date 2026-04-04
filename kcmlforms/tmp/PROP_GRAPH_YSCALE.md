YScale (graph control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> YScale(int, string) Method

**Scaling labels for y-axis**

The **YScale()** method is used to provide y-axis labelling and scaling information. Scaling is important where values may be large, and for instance, it would be better to have a y-axis label that was "millions", and the tick values to be displayed in millions rather than the actual value.

Repeated use of the method allows several different y-axis labels to be specified, each with a different scale; the graph chooses the appropriate scale and label based on the graph data. The first parameter is the scale (0 for no-scaling, 3 for thousand, 6 for millions and so on). For example, to display monetary values scaled appropriately, the following would be used: .graphcontrol1.YScale(0,"\$") .graphcontrol1.YScale(3,"\$Thousands") .graphcontrol1.YScale(6,"\$Millions") .graphcontrol1.YScale(9,"\$Billions")

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
