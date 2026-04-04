DropDownFilled (kcmledit control property)

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

**Determines whether the drop down portion of the control has been filled**

This property is used to determine whether the drop down portion of a Edit control or Grid cell has been filled. This property should be set to *TRUE* after the drop down portion of the control has been filled, i.e. in the [*DropDown()*](PROP_KCMLEDIT_DROPEVENT.htm) event handler. If this property is set to *TRUE* then the *DropDown()* event handler will not be called again unless this property is set back to *FALSE* before the event occurs again. For example: -DEFEVENT Form1.EditControl1.DropDown() 'FillEditControl() .EditControl1.DropDownFilled = TRUE END EVENT

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
