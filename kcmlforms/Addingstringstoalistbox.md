Adding strings to a list box

To add strings to a list box the

*Add()* method is used. For example the following code reads in several items and adds them to the list box *listControl1*:

LOCAL DIM String\$20 WHILE TRUE DO READ String\$ IF (String\$==" ") THEN BREAK .listControl1.Add(String\$) WEND DATA "Alan", "Peter", "Graham", "Bill", "Steve", "Dave", "Sam", "Rob", " "

Each string added to the list can have an associated tag which is specified by the second parameter of the [*Add()* method. The tag can be used as an alternative method of searching for items within the list (See](tmp/PROP_LISTBOX_ADD.htm)

*GetTag\$()).*

If the

*UseTabs* property is set to *TRUE* then HEX(09) characters are automatically expanded as tabs within the list box. For example:

ListString\$ = Description\$ & HEX(09) & Part\$ & HEX(09) & Quantity\$ .listControl1.Add(ListString\$)

The PRINTUSING TO statement can be used to write information into a variable in the specified format, this is particularly useful for formatting strings that require tabulation. Setting byte 47 of \$OPTIONS RUN to HEX(03) changes the default behavior of PRINTUSING TO so that a HEX(09) is inserted at the first space that separates the formats. For example, the following would place the three values into the string with a HEX(09) separating each value, the string can the be added to the list box in the usual way:

STR(\$OPTIONS RUN,47,1) = HEX(03) PRINTUSING TO ListBox\$,"###### \###### \######",First, Second, Third .listControl1.Add(ListBox\$)

Note that changing the \$OPTIONS RUN byte in this way also disables the use of the count bytes that are normally stored in the first two bytes of the receiver variable. If you use PRINTUSING TO elsewhere in your applications then it is important that you reset this byte back to the default setting of HEX(00) immediately after use.

The actual tab positions can be set both at design time or within a program using the [*TabStop\$* property (See](tmp/PROP_LISTBOX_TABSTOP.htm) [Setting the tab stops in a list box](Settingthetabstopsinalistbox.htm) for more information).
