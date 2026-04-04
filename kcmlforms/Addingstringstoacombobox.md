Adding strings to a combo box

------------------------------------------------------------------------

To add strings to a combo box the

*Add()* method is used. For example the following code reads in several items and adds them to the combo box *comboControl1*:

LOCAL DIM String\$20 WHILE TRUE DO READ String\$ IF (String\$==" ") THEN BREAK .comboControl1.Add(String\$) WEND DATA "Alan","Peter","Graham","Will","Steve","Dave","Phil","Rob"," "

Each string added to the list can have an associated tag which is specified by the second parameter of the [*Add()* method. The tag can be used as an alternative method of searching for items within the list (See](tmp/PROP_COMBO_ADD.htm)

*GetTag\$()).*
