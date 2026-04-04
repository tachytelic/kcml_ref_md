DataBind (generic property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Indexed property

**Binds the control to a table object**

The **DataBind** property was introduced in KCML 6.10 to replace the older [DataSource](PROP_DATASOURCE.htm) property. It applies to any data aware control that is bound to a KCML variable through a [DataBind](DataBind.htm) object containing a [DEFRECORD](mk:@MSITStore:kcmlrefman.chm::/DEFRECORD.htm) specification. Its value is the name of the DataBind object. This can be selected from a dropdown list of available objects in the Forms Designer. There is also an ellipsis against the property which can be used to inspect or edit the properties of the DataBind object.

See [here](/DataBinding.htm) for more on data binding.

##### Example:


     .editControl.DataBind

##### See also:

Other [edit](edit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
