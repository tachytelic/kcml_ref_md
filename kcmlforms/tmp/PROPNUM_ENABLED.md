Enabled (generic control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (boolean property)

**Enables and disables a control**

This boolean property can be used to disable a control or menu option programmatically preventing it from receiving focus and generating events. Disabled controls are generally greyed out to make their status clear. Setting a value of TRUE means the control is enabled while a value of FALSE means it is disabled. In general a control will be enabled by default though controls can be disabled in the Forms Designer.

The Enabled property is implemented as a style but, unlike most other styles which can only be set at design time, this style can be inspected and changed at run time.

The [Enabled()](PROP_GROUP_ENABLED.htm) group method can enable and disable all the controls in a group together.

If Enabled is set FALSE for a tab control then it disables only navigation within the tab control. All the tab ears are greyed out and the user cannot switch to another tab page. The controls on the current visible tab page are not disabled.

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
