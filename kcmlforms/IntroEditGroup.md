Introduction to Edit Groups

Edit Groups are rectangular containers for KCML edit controls. Provided each KCML edit control uses the [label\$](tmp/PROP_EDIT_EDITLABEL.htm) property for its static text label, the client will take responsibility for alignment of the controls and their labels within the edit group container. The alignment takes place at runtime to take account of setting the label\$ property at runtime and the possibility that the text is chevronned multilingual text and the language may be changed.

Edit groups are created in the [Forms Designer](FormsDesignerWorkingWithEditGroups.htm).

The alignment process

The client will assume that the edit controls are already lined up vertically and horizontally by the Forms Designer. It will then find the longest label and define a rectangle of that width placed one space to the left of the left most edit control. Within the rectangle the labels will be left aligned. If the rectangle would fall outside the left margin of the edit control then the label text will be clipped. As a last resort, if text would otherwise be clipped, it will shift the edit controls as a group to the right, if is there is space to do so within the group box.

Only KCML edit controls which are members of an edit group are aligned this way and only those controls which are vertically aligned at design time will be aligned together at runtime.

Starting from KClient 6.20 an editgroup may contain multiple columns of edits. It is important in this case that the tab order within the group runs from left to right.

No vertical spacing adjustments are performed. That is still the responsibility of the designer. A future version of KCML will allow this through the addition of properties to the EditGroup control itself.

There is an [example program](ExampleEditGroup.htm) illustrating the use of label\$ and Edit Groups.
