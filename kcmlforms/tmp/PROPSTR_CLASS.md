Class\$ (generic control property)

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
<td>Read<br />
only</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Name of control type**

This read-only property returns the Windows class of the associated control. All the controls of the same type, buttons, edit boxes, grids etc. share the same class name. Generally the class name will only be of interest to Windows API programmers. KCML programmers should be careful about assuming that a class name for a given control will not change in a future version of KCML.

##### Example:


     a$ = .generic.Class$

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
