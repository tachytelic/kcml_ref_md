Forms Designer - Grouping Controls

------------------------------------------------------------------------

It is possible to assign a group name to a group of controls. This is particularly useful as groups of controls can then later be disabled and enabled or made invisible by the program. It is also possible to have group event handlers.

To place controls into a specific group you first need to create a new group in the Forms Designer which can be done with the [<img src="bitmaps/form0114.gif" data-align="BOTTOM" data-border="0" alt="group button" />](TheGroupingMenuMakeGroup.htm) tool bar button. Once the group has been created controls are added to the group be changing the *Group* design time property for the new control. Alternatively you can select a block of controls with the mouse and select the Make Group tool bar button and you will be prompted for the group name.

Note that the [Select Group](TheEditMenuSelectGroupOption.htm) option can be used to select all of the controls that are in the same group as the selected currently selected control.

The name you give the group will be the name of a pseudo-control at run time. For example if you put a number of buttons into a group called *bgrp* then at runtime you can make them all invisible together with a [.Visible()](tmp/PROP_GROUP_VISIBLE.htm) method call e.g. Form1.bgrp.Visible(FALSE)

See the [Group Control](IntroGroup.htm) reference for the available run time group methods.

There is also another type of grouping specific to KCML edit controls where KCML will guarantee the alignment of the controls and their labels. If such a control is enrolled in an [edit group](IntroEditGroup.htm) by setting the [.EditGroup](tmp/PROP_EDIT_EDITGROUP.htm) design time property then KCML will apply some heuristics to make sure the labels and the edit boxes of the edit group align vertically on the form. The labels
