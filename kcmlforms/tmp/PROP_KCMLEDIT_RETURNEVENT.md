ReturnEvent (kcmledit control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Enable/disable the Return() event handler**

Used to enable and disable the [*Return()* event handler used by the Edit control. If set to *TRUE* then the](PROP_KCMLEDIT_RETURN.htm) [*Return()* event handler will be called if the user presses the RETURN key while in the Edit control. This overrides the normal behaviour for RETURN which is to action any default button. Focus will stay on the edit control. For example: .EditControl1.ReturnEvent = TRUE](PROP_KCMLEDIT_RETURN.htm)

If a [validate](PROP_KCMLEDIT_VALIDATE.htm) event handler also exists for the control then it will be called instead if the text has been modified.

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
