Working with Edit Groups

Edit Groups are rectangular containers for KCML edit controls. Provided each KCML edit control uses the [label\$](tmp/PROP_EDIT_EDITLABEL.htm) property for its static text label, the client will take responsibility for alignment of the controls and their labels within the edit group container. The alignment takes place at runtime to take account of setting the label\$ property at runtime and the possibility that the text is chevronned multilingual text and the language may be changed.

The alignment process is described in the [Introduction to Edit Groups](IntroEditGroup.htm) page.

An edit group is created in the Forms Designer by selecting the control from the palette using the <img src="bitmaps/EditGroupTool.png" data-border="0" alt="Edit Group Tool" /> button and dropping it on the form. This marks out a rectangular container on the form. Any KCML edit controls subsequently dropped on the container will be automatically enrolled in the group by having their .EditGroup property set to the name of the container.

Only KCML edit controls support the Edit Group concept. Any other controls dropped on the container will not be affected.

This screen shot shows a form in the Forms Designer with three edit controls within the rectangle of the edit group.

<img src="bitmaps/EditGroupFD.png" data-border="0" alt="An edit group container containing 3 edit controls in the forms designer" />

Note that the edits are all left-aligned so that KClient will move them as a single unit. At runtime this will look like:

<img src="bitmaps/EditGroupRun.png" data-border="0" alt="An edit group container containing 3 edit controls at runtime" />

This example is available as an [example program](ExampleEditGroup.htm) for you to try yourself.
