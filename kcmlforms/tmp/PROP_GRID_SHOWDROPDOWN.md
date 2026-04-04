ShowDropDown (grid control method)

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
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> ShowDropDown() Method

**Forces the display of the DBEdit dropdown**

Used to force the display of the drop down portion of a KCML Edit control within a Grid cell. This method may onyl be used when an edit is already instantiated on a grid (e.g. using MoveCursor() for an auto-edit cell or EditCell()) and will apply to the current edit cell. For example: REM this is an auto-edit grid. REM Move the cursor to start the edit, then immediately REM bring up the drop down list. .gridcontrol1.MoveCursor(2,1) .gridControl1.ShowDropDown()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
