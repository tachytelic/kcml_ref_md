ShowValues (graph control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Show values on graph**

If set to TRUE, then data values are displayed above the columns on bar charts and next to pie sectors on pie charts. On crowded pie charts values are omitted if they overlap other values. On bar charts, if space is limited, the values may be truncated to only a few significant digits and trailing zeroes omitted.

##### Example:


     IF (.graphControl.ShowValues)
       ...
     END IF

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
