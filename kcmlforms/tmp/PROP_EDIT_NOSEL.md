NoSelectOnEntry (kcmledit control property)

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
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**The text is not automatically selected on tabbing in to the listbox**

Normally when an edit control gets focus, the current contents of the control are automatically selected. Although this action is the default for most Windows applications it can sometimes cause problems as the contents of the control are overwritten if the user accidentally presses a key. Setting this property to ***TRUE*** turns on the automatic selection of the control. This property is a design time only property that has no effect if changed under program control.

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
