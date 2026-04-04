Modified (richedit control event)

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
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when the user first modified text**

This event handler is called when the contents of an RTF control have been modified. This event handler is only called if the *Modified* property is set to ***FALSE***. The *Modified* property is automatically set to ***TRUE*** when the contents of the control are modified.

This event handler is quite useful for enabling and disabling other controls when and if the contents of the RTF control are modified. For example you may wish to enable the "Save" and "Clear" buttons to allow the user to save or clear the contents of the control and at the same time you may want to disable the "Load" button. - DEFEVENT Form1.rtfControl1.Modified() .btnSave.Enabled = .rtfControl1.Modified .btnClear.Enabled = .rtfControl1.Modified .btnLoad.Enabled = 1 - .rtfControl1.Modified END EVENT

 

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
