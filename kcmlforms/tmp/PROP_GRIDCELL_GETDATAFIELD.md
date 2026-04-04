GetDataField (gridcell control method)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Write<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> GetDataField() Method

**Returns the SYM of the data source, datafiled and occurs value**

This method can be used to retrieve the data aware information for a grid cell. If the information is retrieved the result is TRUE. If the cell is not data aware then the result is FALSE.

If the function succeeds, then it returns in the 3 BYREF parameters the SYM of the data source string (as set by [*DataSource* , the SYM of the data field (as set by](PROP_DATASOURCE.htm) [*DataField*) and the value of the occurs (if there is no explicit occurs the value is 1).](PROP_DATAFIELD.htm)


    IF (.control.GetDataField(BYREF strsym, BYREF fieldsym, BYREF occurs)
        REM Validate this control
        ...
    ENDIF

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
