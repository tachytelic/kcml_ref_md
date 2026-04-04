Duplicate (generic control method)

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
<td>Advanced</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Duplicate(int, int, string) Method

**Duplicate control with title**

|      |                                            |
|------|--------------------------------------------|
| Int1 | The horizontal position of the new control |
| Int2 | The vertical position of the new control   |
| Str  | The text label for the new control         |

This method is used within the [*Create()* event handler to duplicate a control to a new location on the current form and set its text. It is a generalization of the Duplicate(int, int) method used to copy generic controls. As in that method the first parameters specify the new location of the control relative to the top left hand corner of the form. The third string parameter allows the controls label to be changed.](PROP_FORM_CREATE.htm)

The method returns a [sym](PROPNUM_SYM.htm) pointer to the newly created control to allow the program to later reference the controls properties and methods.

For example: .btnControl2.Duplicate(5, 12, "Click Me")

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
