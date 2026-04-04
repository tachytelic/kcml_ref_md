DataField (generic property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Indexed property

**Specifies the SYM of the column field name that is to be bound to the control. Deprecated.**

This property specifies the column name that is to be bound to the control. This column name must exist as a [field variable](mk:@MSITStore:kcmlrefman.chm::/TutorialFields.htm) in the program. This property would normally be set within the Forms Designer but it can also be set programmatically. This was made easier in 6.10 by the introduction of the [SetDataField()](PROP_SETDATAFIELD_CELL.htm) method; the example below shows this and an older way of doing this.

Note that either the [DataSource](PROP_DATASOURCE.htm) property or the [DataBind](PROP_DATABIND.htm) property must be set at design time to specify the name of the row buffer variable that has been bound to the database table. Both these properties are required for data awareness to work.

In a grid it is normal to set the property per column. The [DataAwareRow()](PROP_GRID_DATAAWAREROW.htm) method or the [DataPending](PROP_GRID_DATAPENDING2.htm) property can then be used to trigger a [RowRequest()](PROP_GRID_ROWREQUEST.htm) event in order fill on demand a row when the user scrolls to the bottom of the grid. As of KCML 6.00 it is possible to fill individual cells using the [WholeDataAware](PROP_GRID_WHOLEDATAAWARE.htm) style

The value returned from this property will be the [SYM](mk:@MSITStore:kcmlrefman.chm::/SYM(.htm) of the field as defined in the DEFFORM. This is the decorated name including any occurs and any trailing \$ for string variables. The name of the field can then be found using the [SYMNAME()](mk:@MSITStore:kcmlrefman.chm::/SYMNAME(.htm) function. To get the actual data source, data field and occurs, KCML 6.00 introduced the [GetDataField()](PROP_GETDATAFIELD.htm) method.

KCML 6.10 introduced the [SetDataField()](PROP_SETDATAFIELD_CELL.htm) method to allow the field packing information to be set directly without the use of a field.

In this example a grid is constructed to display the results of an SQL query using [KI_DESCRIBE_COL](mk:@MSITStore:kdb.chm::/tmp/KI_DESCRIBE_COL.htm) to find the column name and packing information and [KI_FLD](mk:@MSITStore:kdb.chm::/tmp/KI_FLD.htm) to count the columns and fill in the fields used in the form. The fields must be referenced somewhere in the program, ideally in a DIM statement. The recommended approach here is to use the KCML 6.10 SetDataField() method to avoid using fields entirely. Then the KI_FLD call could also be dispensed with as the column count and record length is also available from KI_PREPARE.


    prefix$="sqldemo_"
    REM instantiate fields
    CALL KI_FLD handle, prefix$ TO status, reclen, colcount
    FOR i = 1 TO colcount
        CALL KI_DESCRIBE_COL handle, i TO name$, type$, pack$, offset, status
        REM column heading
        .gridControl1.Cell(0, i).Text$ = name$
        REM Using tthe SetDataField() method introduced in KCML 6.10
        gridControl1.Cell(0, i).SetDataField(offset, pack$)
        REM The old method of setting DataField via the SYM of a variable containing the name of the field
        colname$ = "." & prefix$ & name$
        IF (STR(pack$,, 1) == "A") THEN colname$ = & "$"
        .gridControl1.Cell(0, i).DataField = SYM(colname$)
    NEXT i

##### See also:

Other [edit](edit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
