DropDown (kcmledit control property)

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
*(NoDrop, DropFocus, DropEnabled, DropAlways)*

**Used to set the DBEdit control to act as a regular edit control or as a drop down list box**

Used to instruct the Edit control or grid cell to act as either a regular edit control or as a drop down list box. This property is a design time only property and can therefore not be changed under program control.

Available styles are as follows:

|  |  |
|----|----|
| NoDrop | Setting this style means that the control will act as a standard Edit control with no drop down capabilities. |
| DropFocus | Setting this style means that the control can have a drop down list but the down arrow used to signify that the control has drop down capabilities is not displayed until the control gets focus. |
| DropEnabled | Setting this style means that the control can have a drop down list. The down arrow used to signify that the control has drop down capabilities is only displayed if the control is enabled. |
| DropAlways | Setting this style will display the down arrow at all times. |

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
