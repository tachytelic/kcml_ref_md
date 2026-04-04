Text\$ (generic control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Specifies or retrieves the text associated with the control**

This property supplies the text string representing the label of a control or the Title of the form. For example, to change the text on a button from Stop to Go you could do the following: .btnControl1.Text\$ = "Go"

<span style="font-family: Courier New,monospace; "> </span>And to retrieve the current label text from a button you could use: CurrentTitle\$ = .btnControl1.Text\$

<span style="font-family: Courier New,monospace; "> </span>For controls that support accelerator keys it is also possible to set the accelerator key for a control by inserting an ampersand before the required accelerator character. For example: .btnControl1.Text\$ = "&My Button"

**Note:** Escape sequences such as "\n" will be interpreted by kclient if set at design time. To avoid this escape the backslash using for example "\\n". This issue does not arise when setting Text\$ at run time.

<span style="font-family: Courier New,monospace; "> </span> 

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
