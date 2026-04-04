Duplicate (menuitem control method)

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
time</td>
<td>Run<br />
time</td>
<td>Advanced</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Duplicate(string) Method

**Duplicate menu item**

|     |                                |
|-----|--------------------------------|
| Str | The text for the new menu item |

The Duplicate() method can only be used in the [Create()](PROP_FORM_CREATE.htm) event. This form of the menu item duplicate method will place a new menu item immediately after the menu item.

The method returns a [sym](PROPNUM_SYM.htm) pointer to the newly created control to allow the program to later reference the controls properties and methods.

For example: newsym = .menu1.fileoption1.Duplicate("Open") newsym = .menu1.fileoption1.Duplicate("Close") newsym = .menu1.fileoption1.Duplicate("Print")

Would duplicate the menu option, *fileoption1*. While: .menu1.fileoption1.Duplicate("Child 1", 0) .menu1.fileoption1.Duplicate("Child 2", 0)

would create a child menu for the duplicated option. Furthermore .menu1.fileoption1.Duplicate()

would create a menu separator.

For more information on duplicating menu items and menu separators see [Duplicate(str, int)](PROP_MENU_DUPLICATE_CHILD.htm) and [Duplicate()](PROP_MENU_DUPLICATE_SEP.htm).

##### See also:

Other [menuitem](menuitem.htm) properties, methods and events, [menu](menu.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
