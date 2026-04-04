Setting the tab stops in a list box

By default tab stops within a list box are placed every 32 [Dialog Box Units](DialogBoxUnitsDLUs.htm). Alternative settings can be specified at design time by double clicking on the list box within the forms designer. To set the tab positions within a program the new positions can be set by assigning a string of comma separated positions to the

*TabStop\$* property. For example:

.listControl1.TabStop\$ = "50, 100, 150, 200"

This can also be done with the \$FMT( function, for example:

Tabs\$ = \$FMT("###, \###, \###, \###", 40, 80, 140, 200) .listControl1.TabStop\$ = Tabs\$

When adding strings to a list box the HEX(09) character is used to signify the position of a Tab, see [Adding strings to a list box](Addingstringstoalistbox.htm) for more information.

To disable the expansion of the HEX(09) character set the

*UseTabs* property to *FALSE*.
