MenuFirst (menu control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Read<br />
only</td>
<td>Advanced</td>
<td>KCML<br />
6.20+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Object property

**Get first menu item**

The MenuFirst property returns the first menu item of a menu control as an object. It may be used in conjunction with [MenuNext](PROP_MENUITEM_GETNEXT.htm) to programmatically move through the menu items on a menu control. Note that there is a single list of all the menu items, without regard to how they are displayed with submenus etc.

This example enumerates all the items on the menu, calling 'ProcessMenuItem() for each one.


    LOCAL DIM OBJECT m
    OBJECT m = .mnuControl1.MenuFirst
    WHILE (OBJECT m <> NULL)
        'ProcessMenuItem(OBJECT m)
        OBJECT m = m.MenuNext
    WEND

##### See also:

Other [menu](menu.htm) properties, methods and events, [menuitem](menuitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
