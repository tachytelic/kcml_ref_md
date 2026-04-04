GetIndex (gridcell control method)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> GetIndex(int) Method

**Used to test drop down index numbers for validity**

***Int***     The index of the item to test

Used to test index numbers for validity. If the specified index number no longer exists, i.e. the entry has been deleted, then a value of -1 is returned. For example: IF (.EditControl1.GetIndex(Position) = -1) ... END IF

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
