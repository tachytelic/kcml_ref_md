DropStyle (kcmledit control property)

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
*(DropDown, Ellipsis)*

**Determines whether the DBEdit control displays an down arrow or ellipses when acting as a dropdown control**

This property is used to determine whether the Edit control or grid cell displays a down arrow or ellipses on the right hand side of the control when acting as a drop down list. For this property to have any effect the [*DropDown* property should also be set to anything other than *NoDrop*. This property is a design time only property and can therefore not be changed under program control. Available settings are:](PROP_EDIT_DROPDOWN.htm)

DropDown

Used to display a down arrow on the right hand side of the control.

Ellipsis

Used to display ellipsis ("...") on the right hand side of the control. If set to ellipsis then the control will not display a drop down section, therefore the [*DropDown()* event handler will not be called, instead the](PROP_KCMLEDIT_DROPEVENT.htm)

*Click()* event handler is called. The ellipsis button is useful for displaying a special search dialog instead of a normal Combo box.

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
