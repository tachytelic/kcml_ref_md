GetDataField (generic control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> GetDataField() Method

**Returns the SYM of the data source, datafield and occurs value**

This method can be used to retrieve the data aware information for any control or grid cell. If the information is retrieved successfully then the result is TRUE. If the control is not data aware (or the control does not support data awareness) then the result is FALSE.

If the function succeeds, then it returns in the 3 BYREF parameters the SYM of the data source string (as set by [*DataSource* , the SYM of the data field (as set by](PROP_DATASOURCE.htm) [*DataField*) and the value of the occurs (if there is no explicit occurs the value is 1).](PROP_DATAFIELD.htm)


    IF (.control.GetDataField(BYREF strsym, BYREF fieldsym, BYREF occurs)
        REM Validate this control
        ...
    ENDIF

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
