ReadOnly (kcmledit control property)

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

**Enables/disables readonly mode for the control**

If set to *TRUE* the KCML edit control is marked as read only, preventing the text it contains from being altered or additional text from being entered. For example: .DbEdit1.ReadOnly = TRUE

The following could be used to determine the current *ReadOnly* state of the control: State = .DbEdit1.ReadOnly

Read-only text is drawn using a different background color. This color can be set as a [preference](mk:@MSITStore:kclient.chm::/formprefs.htm) in the client.

All the controls in a group and be marked readonly together using the [.ReadOnly()](PROP_GROUP_READONLY.htm) group method.

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
