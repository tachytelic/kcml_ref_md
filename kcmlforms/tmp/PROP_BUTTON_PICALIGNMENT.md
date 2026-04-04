PictureAlignment (generic property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, TopLeft, TopCenter, TopRight, MiddleLeft, MiddleCenter, MiddleRight, BottomLeft, BottomCenter, BottomRight, Tile, Stretch, Fit, Opposite)*

**Specifies the picture alignment**

The **PictureAlignment** property is used to determine where the picture is placed on the control. The default is to stretch the picture to fit the entire area of the control. The possible values are:

|  |  |
|----|----|
| Default | Same as Stretch |
| TopLeft | Positioned in top left corner |
| TopCenter | Centered horizontally at the top |
| TopRight | Positioned to top right corner |
| MiddleLeft | Vertically centered but on the left |
| MiddleCenter | Centered |
| MiddleRight | Vertically centered but on the right |
| BottomLeft | Positioned in bottom left corner |
| BottomCenter | Centered horizontally at the bottom |
| BottomRight | Positioned in bottom right corner |
| Tile | Picture drawn at normal size and repeated horizontally and vertically to cover the entire control |
| Stretch | Picture stretched to fit the entire control |
| Fit | Picture is stretched to cover as much of the control as possible without losing its aspect ratio |
| Opposite | In a picture button control only, the picture is placed opposite the button text, meaning that the picture is shown normal size and centered in the space left after the text is drawn |

.picControl1.PictureAlignment = &.MiddleCenter

##### See also:

Other [picbutton](picbutton.htm) properties, methods and events and [generic](generic.htm) properties and methods.
