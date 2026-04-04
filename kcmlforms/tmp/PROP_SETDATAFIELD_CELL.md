SetDataField (gridcell control method)

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
6.10+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> SetDataField(int, string) Method

**Sets the datafield property to the specified numeric field information**

This method can be used to set the data aware field information for a grid cell in an easier manner than setting [*DataField*](PROP_DATAFIELD.htm) directly. The grid must already have either [DataSource](PROP_DATASOURCE.htm) or [DataBind](PROP_DATABIND.htm) set. This method is polymorphic with two variants.

- The first parameter is the field start and the second the format of the string. This can be used for both numeric and string fields. If a field information is contained in a field variable, the [POS()](mk:@MSITStore:kcmlrefman.chm::/POS(.htm) and [PACK()](mk:@MSITStore:kcmlrefman.chm::/PACKfn.htm) functions may be used to deduce the start and format.

- The other variant applies only when bound against a [DataBind](DataBind.htm) object specified in the [DataBind](PROP_DATABIND.htm) property of the grid. It takes a single string argument corresponding to one of the [FLD](mk:@MSITStore:kcmlrefman.chm::/FLD.htm) names in the bound record.

The [*Type\$*](PROP_GRIDCELL_DBTYPE.htm) property is determined automatically based on the format given.

For more about data binding and the DataBind control see [here](/DataBinding.htm).


    REM Numeric field example
    .gridcell(2,2).SetDataField(POS(.nfld), PACK(.nfld))

    REM String field example
    .gridcell(2,3).SetDataField(POS(.sfld), PACK(.sld))

    REM explicit field
    .gridcell(2,4).SetDataField(10, "UNUM(10,2)")

    REM example using DataBind and a field name
    .gridcell(2,5).SetDataField("PARTNUM")

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
