Key (generic property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Specifies the accelerator key for the button**

The **Key** property is used to define a short cut key for a button. See the analogous [Key](PROP_MENU_KEY.htm) property for menu items for more information about how accelerator keys are defined.

This example shows how the shift F6 key may be used as an accelerator for a button


    Form1.ActionIt.key = 0x7501

##### See also:

Other [picbutton](picbutton.htm) properties, methods and events and [generic](generic.htm) properties and methods.
