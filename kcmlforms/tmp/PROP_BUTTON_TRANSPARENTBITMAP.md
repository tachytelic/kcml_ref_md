TransparentBitmap (generic property)

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

**Specifies the transparent color**

This property is used to set the transparent color for a picture embedded on a picture enabled control such as a button. The pixels set to the transparent color in the picture are not drawn as the button is drawn thus allowing the background to bleed through. This makes the picture embed naturally on any background.

If the [*NoFill* property is set to *TRUE* then the background color or picture used by the form will replace the specified color, otherwise the background color of the picture as set by the](PROP_BUTTON_NOFILL.htm) [*BackColor* property is used.](PROP_GENERIC_BACKCOLOUR.htm)

The transparent color is set by specifying an existing color object. For example: .picButton1.TransparentBitmap = &.color1

##### See also:

Other [picbutton](picbutton.htm) properties, methods and events and [generic](generic.htm) properties and methods.
