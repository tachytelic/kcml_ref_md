MultiLine (button control property)

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
<td>Advanced</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Wraps the text to multiple lines if the string is too long to fit on a single line**

This property is used to enable multiline text on push button controls. Normally text on push buttons is centered and any text that cannot fit onto the button face is automatically truncated, setting this property to ***TRUE*** will automatically wrap the text onto multiple lines. This property is most useful when writing multilingual applications as it means that words that wouldn't normally fit within the button space are automatically wrapped. However, you must make sure that the button is large enough for any wrapped text. This property is a design time only property that has no effect if changed under program control.

##### See also:

Other [button](button.htm) properties, methods and events and [generic](generic.htm) properties and methods.
