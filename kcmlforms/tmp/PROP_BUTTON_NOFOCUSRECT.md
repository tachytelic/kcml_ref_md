NoFocusRect (picbutton control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Enables or disables the buttons focus rectangle**

This property is used to determine if a focus rectangle is to be placed onto the control if the control gets focus. Normally if the control is being used as a button then you would want a focus rectangle, therefore this property should be set to *FALSE*. However if the control is simply being used to display a picture then this property should be set to *TRUE*, for example: .picControl1.NoFocusRect = TRUE

and to find out the current setting the following could be used: Rectangle = .picControl1.NoFocusRect

##### See also:

Other [picbutton](picbutton.htm) properties, methods and events and [generic](generic.htm) properties and methods.
