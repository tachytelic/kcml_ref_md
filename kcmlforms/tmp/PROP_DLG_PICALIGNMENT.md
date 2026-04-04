PictureAlignment (form control property)

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
*(Default, TopLeft, TopCenter, TopRight, MiddleLeft, MiddleCenter, MiddleRight, BottomLeft, BottomCenter, BottomRight, Tile, Stretch, Fit)*

**Specifies the alignment of the background picture**

Used to specify the alignment of a picture as used by the picture control, grid control cells, the tree control and form backgrounds. The picture itself is specified by setting the [Picture](PROP_GENERIC_PICTURE.htm) property either at design time or within the program. The available options are as follows:

|            |              |             |
|------------|--------------|-------------|
| TopLeft    | TopCenter    | TopRight    |
| MiddleLeft | MiddleCenter | MiddleRight |
| BottomLeft | BottomCenter | BottomRight |
| Default    | Tile         | Stretch     |
| Fit        |              |             |

For example, the following would place the CD icon at the bottom left hand corner of the form: .form.Picture = &.CD .form.PictureAlignment = &.BottomLeft

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
