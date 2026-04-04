DataSource (gridcell control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Data-aware property

**Specifies that variable name that is bound to a database table**

This property is contains the name of the KCML variable that has been bound to a database table. This property must be set within the Forms Designer and the variable will generally be defined previously with a [DEFOBJ](mk:@MSITStore:kcmlrefman.chm::/DEFOBJ.htm) statement so that it appears in the [Forms Designer Table List](/FormsDesignerWorkingwithTables.htm).

Controls are bound to columns within this buffer by setting their [DataField](/tmp/PROP_DATAFIELD.htm) property. Whenever a bound column in the row buffer is changed by KCML code in an event handler, the control in the client will be automatically updated by KCML at the end of the event. Often this is as a result of the whole row being updated by a database fetch operation. Similarly if an editable control in the client has its contents changed KCML will update the field in the row buffer when the next event (other than a Validate) is triggered.

In the case of a grid the property applies to the grid as a whole and not any cell, row or column.

The property can be inspected, but not set, at runtime with the value of the property being the SYM() of the name of the bound row buffer.


    PRINT "This control is bound to the row buffer ";SYMNAME(.editControl1.DataSource)

Starting with KCML 6.10 a new [Data Binding object](/DataBinding.htm) has been introduced which allows binding directly against [DEFRECORD](mk:@MSITStore:kcmlrefman.chm::/DEFRECORD.htm) records and dispenses with the DEFOBJ and its schema information. This uses the alternative [DataBind](PROP_DATABIND.htm) property on the control to specify the name of the [DataBind](DataBind.htm) object. If DataBind is set then DataSource is ignored. This new object is preferred over the original binding scheme and DataSource is now deprecated in new code.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
