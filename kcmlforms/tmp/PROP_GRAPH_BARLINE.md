BarLine (graph control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> BarLine(int, string) Method

**Draw set as line on bar chart, instead of columns**

The **BarLine()** method allows a data set to be displayed on the bar chart as horizontal lines rather than full columns. The lines are drawn across the columns and can be useful for show comparisons, limits or targets. Several data sets can be drawn in this style.

The first parameter describes the data set. The second parameter is a label for the data set, but is currently ignored.

##### Example:


     .graphControl.BarLine(i, a$)

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
