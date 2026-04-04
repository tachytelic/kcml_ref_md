Tag\$ (generic control property)

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

**Free text field available to programmers**

This property is a free text field which can be referenced and modified by the program without effecting the appearance of the control. It is commonly used to associate labels to controls that don't have a [*Text\$* property. Control labels set with *Tag\$* can be used by group event handlers to determine which control triggered the event. See](PROPSTR_TITLE.htm) [Group events](../UsingEventHandlersGrouping.htm) for more information about group event handlers.

##### Example:


     a$ = .generic.Tag$

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
