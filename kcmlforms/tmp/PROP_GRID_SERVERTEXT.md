ServerText (grid control property)

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
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Enable server storage (and retrieval) of grid cell text**

In KCML 5.02 if this property is set to *TRUE* then a copy of the grids contents will be stored at the server side to allow the contents of edited grid cells to be retrieved by the program. This property was a design time only property that had no effect if changed under program control.

Starting with KCML 6.00 this property is always set to TRUE and it cannot be unset at design time or at run time.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
