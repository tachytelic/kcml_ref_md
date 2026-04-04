Forms Designer - Working with List boxes

------------------------------------------------------------------------

To add a list box to the current form click on the <img src="bitmaps/form0069.gif" data-align="BOTTOM" data-border="0" alt="add listbox control" /> icon on the controls palette.

List boxes are used to provide a list of items to the user allowing the user to select one or more items. The items are added by the program and not via the Forms Designer.

Normally items are displayed in the list in the order in which they are added by the program. The list can automatically be sorted if the

*Sort* property is set.

There are three types of selection methods that can be presented to the user. The

*Selection* property is used to change the selection type. If the list box is set to allow multiple selections then the user is able to click on multiple items within the list box. The items are set as toggles, therefore clicking on an item a second time will unset the option. If the list box is set to allow extended selections then the user can select an item and drag down with the mouse to select a block of items. If the control key is held down then addition items can also be selected.

By default the list box has tab stops set at every 32 [Dialog Units](DialogBoxUnitsDLUs.htm), to change the tab positions you can double click on the control to call up the tab position editor. The column separators can be dragged around to change the tab stop positions. Once the modifications have been made the tick button <img src="bitmaps/form0061.gif" data-align="BOTTOM" data-border="0" alt="OK button" /> is selected to return to normal editing mode. The <img src="bitmaps/form0062.gif" data-align="BOTTOM" data-border="0" alt="revert button" /> button is used to return the tab stops back to the default setting of 32 [DLU's](DialogBoxUnitsDLUs.htm). The <img src="bitmaps/form0063.gif" data-align="BOTTOM" data-border="0" alt="default" /> button allows you to specify a new default tab stop setting.

<img src="bitmaps/form0064.gif" data-align="BOTTOM" data-border="0" alt="Setting columns in a listbox" /> 

**Other useful list box properties**

[*Enabled\
[Help\$](tmp/PROP_GENERIC_HELP.htm)*\
](tmp/PROPNUM_ENABLED.htm)

*MultiColumn\
[UseTabs](tmp/PROP_LISTBOX_USETABS.htm)\
[TabStops\$](tmp/PROP_LISTBOX_TABSTOP.htm)*

**Useful List box control event event handlers**

*Click()\
[DblClick()](tmp/PROP_LISTBOX_SELDBLCLK.htm)\
[GetFocus()](tmp/PROP_LISTBOX_SETFOCUS.htm)\
[LoseFocus()](tmp/PROP_LISTBOX_KILLFOCUS.htm)*
