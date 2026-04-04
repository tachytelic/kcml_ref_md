TextAlignment (generic property)

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

**Specifies the alignment of the text on picture button**

This property is used to align the text on a KCML picture button. Available settings are as follows:

|                               |                    |                   |
|-------------------------------|--------------------|-------------------|
| ***TopLeft***                 | ***TopCenter***    | ***TopRight***    |
| ***MiddleLeft***              | ***MiddleCenter*** | ***MiddleRight*** |
| ***BottomLeft***              | ***BottomCenter*** | ***BottonRight*** |
| ***Default (Middle Center)*** |                    | ****              |

***\***
For example the following could be used to change the alignment of the text on the control picControl1: .picControl1.TextAlignment = &.TopLeft

##### See also:

Other [picbutton](picbutton.htm) properties, methods and events and [generic](generic.htm) properties and methods.
