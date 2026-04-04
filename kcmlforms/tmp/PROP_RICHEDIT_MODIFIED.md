Modified (richedit control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Set when text is modified by the user**

This property is set to ***TRUE*** when the contents of the control have been modified. It can also be used to enable and disable the [*Modified()* event handler. If this property is ***FALSE*** then the](PROP_RICHEDIT_MODIFIEDEVENT.htm) [*Modified()* event handler is called.](PROP_RICHEDIT_MODIFIED.htm)

This property when used in conjunction with the [*Modified()* event handler is quite useful for enabling and disabling other controls when and if the contents of the RTF control are modified. For example you may wish to enable the "Save" and "Clear" buttons to allow the user to save or clear the contents of the control and at the same time you may want to disable the "Load" button. - DEFEVENT Form1.rtfControl1.Modified() .btnSave.Enabled = .RTFControl1.Modified .btnClear.Enabled = .RTFControl1.Modified .btnLoad.Enabled = 1 - .RTFControl1.Modified END EVENT](PROP_RICHEDIT_MODIFIED.htm)

 

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
