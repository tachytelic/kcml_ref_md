Checked (menuitem control property)

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

**Used to check a menu item or determine the status of a menu item**

If this property is set to *TRUE* a tick is displayed by the menu option and any associated toolbar button stays depressed. For example:


     .menu1.fileoption1.Checked = TRUE

**Note:**

A menu option and related toolbar button can only be checked this way if the **Checkable** option is set in the forms designer.

The Checked property can be inspected and will be TRUE when the menu option is ticked and the toolbar button is down and FALSE otherwise. If the menu option is selected by the user, or the toolbar button is clicked, the state of both change and the Checked propery is updated in the client. However for the checked property to be updated on the server from user actions on the form, there **must** be a [Select()](PROP_MENU_SELECT.htm) event handler for the menu item, even if it contains no code.

##### See also:

Other [menuitem](menuitem.htm) properties, methods and events, [menu](menu.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
