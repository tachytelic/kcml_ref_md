Help\$ (generic control property)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Specifies the text displayed in the status bar when the control gets focus**

This property is used to provide additional help for the control in the form of tool tips or as a message in the status bar pane, if it exists. When the mouse pointer hovers over the control a small box appears containing the help text. If a Status bar exists on the form then the contents of *Help\$* are placed in the first pane of the Status bar when the control gets focus. The default help text for a control can be changed within the program, for example: .listControl1.Help\$ = "Used to enter useful information"

Note that the status bar is not updated until the current event handler has completed. To immediately update the status bar you should call the [*Flush()* method after the *Help\$* property has been changed.](PROP_DLG_FLUSH.htm)

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
