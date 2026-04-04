Forms Designer - Working with Combo boxes

------------------------------------------------------------------------

To add a combo box to the current form click on the <img src="bitmaps/form0037.gif" data-align="BOTTOM" data-border="0" alt="Combo box tool" /> icon on the controls palette.

Combo boxes are used to offer the user with a list of information from which they can select an item. The mouse or the keyboard navigation keys are used to move up and down through the list. Three types of combo boxes are available by setting the

*Type* property. The types are as follows:

**Simple**\
A simple Combo Box displays a permanently visible list of items. The user is able to enter some text in the edit portion of the control. As the text is entered the list is automatically adjusted to show the items following the entered text as if they were in sorted order. Clicking on an item from the list places the selected item into the edit control portion of the combo box.

**Drop List**\
A drop list combo box has no edit control portion. It only allows the user to select an item from the list. As the user clicks on the control the drop down portion of the list is displayed. The user can then use the mouse to select an item from the list.

**Drop Down**\
A drop down combo box is a combination of the simple and the drop list types. The list is only displayed if the user clicks on the down arrow to the right of the edit control portion of the combo box. The user is able to enter text into the edit control portion of the combo box. If the list portion is in view then the list will adjust to sort the list to the nearest string matching the entered text.

By default, scroll bars are not added to the list. These should be added by setting the

*VertScroll* property.

The

*Sort* property can be set so that items in the list are automatically sorted as they are added.

Note: The KCML edit control can also be used to provide a drop down list. Because of the extended functionality of this control it is recommended that you use it in place of the regular combo box.

Other useful Combo box properties

*Help\$*

Useful Combo Box Event Handlers:

*Click()\
[DblClick()](tmp/PROP_COMBO_DBLCLK.htm)\
[GetFocus()](tmp/PROP_COMBO_SETFOCUS.htm)\
[LoseFocus()](tmp/PROP_COMBO_KILLFOCUS.htm)\
[DropDown()](tmp/PROP_COMBO_DROPDOWN.htm)*\
