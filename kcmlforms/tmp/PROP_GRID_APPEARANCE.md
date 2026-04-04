Appearance (grid control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only enumerated property)\
*(Default, Flat, Raised, Sunken, Plain, EditStyle, ReadOnly)*

**Specifies the appearance of the grid**

Used to specify the default appearance of a Grid control. Possible choices are

|  |  |
|----|----|
| Default | The same as Flat |
| Flat | Standard 3D look with a white background and grey lines separating cells. |
| Raised | The background color is the same as dialog background. Lines are grey. |
| Sunken | The background color is the same as dialog background. Lines are white. |
| Plain | The background color is the same as dialog background. Lines are black. |
| EditStyle | Grid is drawn with the editable background color set in the clients [forms preferences](mk:@MSITStore:kclient.chm::/formprefs.htm) |
| ReadOnly | Grid is drawn with the read only background color set in the clients [forms preferences](mk:@MSITStore:kclient.chm::/formprefs.htm) |

Fixed row and column cells are always drawn the same way and are unaffected by this setting.

This property is a design time only property that has no effect if changed under program control.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
