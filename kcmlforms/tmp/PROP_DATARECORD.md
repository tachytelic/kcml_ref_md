Record (DataBind control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Data-aware property

**Specifies the name of the DEFRECORD bound to the object**

This [DataBind](DataBind.htm) control property contains the name of the KCML [DEFRECORD](mk:@MSITStore:kcmlrefman.chm::/DEFRECORD.htm) record associated with the control. It describes the layout of the bound row buffer or structure specified by the [.Bind](PROP_DATASOURCE_BIND.htm) property.

A DataBind control is created in the KCML Workbench by dragging the bound record from the record browser and dropping it onto the form's DEFFORM definition in the editor window. This creates a DataBind object with a name of the record name prefixed by 'data\_'. The [.Record](PROP_DATARECORD.htm) property will be set to the name of the record and the [.Bind](PROP_DATASOURCE_BIND.htm) property will be defaulted to the record name with a \$ sign appended.

The property can be set either with the forms designer or programmatically. In the forms designer click on the ellipsis associated with the DataBind property on a form control. In a program this property can be set at .Create() event time.

See [here](/DataBinding.htm) for more on data binding.

##### Example:


     .data.Record

##### See also:

Other [DataBind](DataBind.htm) properties, methods and events and [generic](generic.htm) properties and methods.
