Visible (menuitem control property)

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

**Makes a menu item visible/invisible**

If this property is set to the default setting of *TRUE* for a menu option the option will appear normally in the menu. However if set FALSE, either at design time or runtime, then the menu item will not appear at all and will not generate any select events. For example to completely suppress the Advanced options menu option: .ToolsMenu.Options.Visible = ('AdvancedUser() ? TRUE : FALSE)

To leave the option on the menu, but greyed out and inactive, use the [.Enabled](PROP_MENU_ENABLED.htm) property.

##### See also:

Other [menuitem](menuitem.htm) properties, methods and events, [menu](menu.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
