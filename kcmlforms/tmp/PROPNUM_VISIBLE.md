Visible (generic control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (boolean property)

**Makes the control visible/invisible**

If set to *True* the control is visible and can therefore be used. Controls can be made invisible by setting the this property to *FALSE*. This can be useful if you want to temporarily hide a control from the user. For example to temporarily remove a list box from view you could use the following: .listControl1.Visible=FALSE

And to find out if the list box is currently visible the following could be used: ListBoxState = .listControl1.Visible

Though this is a style and so would not normally be available at run time, there is special support at runtime for setting and inspecting .[.Enabled](PROPNUM_ENABLED.htm) and [.Visible](PROPNUM_VISIBLE.htm).

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
