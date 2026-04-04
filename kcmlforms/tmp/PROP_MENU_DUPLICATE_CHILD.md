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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Duplicate(string, int) Method

**Duplicate menu item with child flag**

There are three forms of the menu item duplicate method. They can only be used in the [Create()](PROP_FORM_CREATE.htm) event. The most general form takes two arguments.

If no argument is specified then a separator is created. The following are equivalent: .menu.menuitem1.Duplicate() .menu.menuitem1.Duplicate("")

If the second argument is not specified, or is FALSE then the new menu item will appear at the same level and immediately after the existing menu item. The following are equivalent: .menu.menuitem1.Duplicate("&New Item") .menu.menuitem1.Duplicate("&New Item", FALSE)

If the second argument is specified then it is a boolean value indicating whether the new item should be a child of the menu item (that is the menu item will produce a popup menu on which the new item will appear).

The result of each of these Duplicate() methods is the [sym](PROPNUM_SYM.htm) of the new menu item. This may also be used with the object notation. The following are ways of creating a "New" menu item on the file menu and adding a toolbar image: newsym = .menu1.File.Duplicate("&New", TRUE) .menu1.newsym.picture = &.FileNew OBJECT new = .menu1.File.Duplicate("&New", TRUE) new.picture = &.FileNew

Events on duplicated menu items are returned to the menu item's event handler (and this includes duplicates of duplicates). It is possible to use the Sym property of menu items to determine which menu item was actually selected. Thus, using the above example: IF (...Sym == newsym) REM New ... ENDIF IF (...Sym == new.sym) REM New ... ENDIF

##### See also:

Other [menuitem](menuitem.htm) properties, methods and events, [menu](menu.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
