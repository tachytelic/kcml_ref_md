NoBorder (picbutton control property)

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

**Adds or removes the border from a picture button**

This property is used to determine if a border is to be added to the control. If set to *TRUE* then the border is removed. For example: .picControl1.NoBorder = TRUE

and to find out the current setting the following could be used: Border = .picPiccontrol1.NoBorder

<span style="font-family: Courier New,monospace; "> </span>The size of the drop down border that is displayed when the button is clicked can be changed with the [*Thickness* property. Setting *NoBorder* to *TRUE* and](PROP_BUTTON_THICKNESS.htm) [*Thickness* to zero will display no border around the picture.](PROP_BUTTON_THICKNESS.htm)

##### See also:

Other [picbutton](picbutton.htm) properties, methods and events and [generic](generic.htm) properties and methods.
