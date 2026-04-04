TabSkip (generic control property)

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
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(None, Forward, Back)*

**Skip this control when tabbing**

The **TabSkip** property is used to specify how controls respond to the Tab key. .EditControl1.TabSkip = &.Forward

The following TabSkip options are available.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>None</th>
<td>Default tab operation applies.<br />
Pressing Tab moves focus to the control from the previous one. Pressing Shift-Tab moves focus back to the control from the next one.</td>
</tr>
<tr>
<th>Forward</th>
<td>The control refuses focus from the previous control and passes it to the next control that doesn't have <strong>TabSkip</strong> set to <strong>Forward</strong>. If no other control accepts focus, the focus will not change. Pressing Shit-Tab to move focus back to the control from the next control is unaffected.</td>
</tr>
<tr>
<th>Back</th>
<td>The control accepts a Tab forward from the previous control but will refuse focus coming back from the next control via Shift-Tab and pass it the previous tab that doesn't have <strong>TabSkip</strong> set to <strong>Back</strong>.</td>
</tr>
</tbody>
</table>

**Note:** Some controls such as Rich Edit controls process the Tab key. In these controls pressing Tab will not move the focus.

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
