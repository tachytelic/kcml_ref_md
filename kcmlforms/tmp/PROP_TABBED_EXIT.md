Exit (tabbeditem control event)

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
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when the user exits the tab**

The Tab control *Exit()* event is called each time the specific tab is deactivated because the user selects another tab page on the same control. This event is useful for verifying the users input is valid before allowing another tab to be selected. To prevent the user from leaving the current tab this event should return *FALSE*. Tab control event handlers are created for each tab using the [Tab Control editor](/FormsDesignerTabcontrols.htm) within the [Forms designer](/TheKCMLFormsDesigner.htm).

This event is not triggered if focus goes to another control. It is only relevant if the active tab on the control is changed.

There is also a [Enter()](PROP_TABBED_ENTER.htm) event that can be triggered for the new tab when it is activated.

##### Example:


     DEFEVENT Form1.tabbeditem.Exit()

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
