Enabled (menuitem control property)

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

**Enables/disables menu items**

If this property is set to the default setting of *TRUE* for a menu option the option will appear normally in the menu. However if set false, either at design time or runtime, then the menu item will appear greyed out and will not generate any select events. For example to disable the File menu's Save option: .FileMenu.SaveOpt.Enabled = ('DocModified() ? TRUE : FALSE)

To remove the option from the menu completely, rather than just greying it out, use the [.Visible](PROP_MENU_VISIBLE.htm) property.

##### See also:

Other [menuitem](menuitem.htm) properties, methods and events, [menu](menu.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
