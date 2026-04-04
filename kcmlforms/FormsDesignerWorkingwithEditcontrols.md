Forms Designer - Working with Edit controls

------------------------------------------------------------------------

To add an Edit control to a form click on the <img src="bitmaps/form0040.gif" data-align="BOTTOM" data-border="0" alt="Edit control tool" /> icon on the controls palette.

The Edit control is possibly the most widely used control of all as it allows the user to enter all types of data into the form. The control can be programmed to restrict the amount of information and the type of information that is entered, this is done with the [*Type\$* property. In most cases the control is displayed as an edit control although special properties are available to allow for combo box and check box styles, see the](tmp/PROPSTR_TYPE.htm) [*DropDown* and](tmp/PROP_EDIT_DROPDOWN.htm)

*DropStyle* properties for more information.

If a database object has been defined then you can drag columns from the database directly onto the form. Edit controls created by this method are automatically sized and will inherit the description and type information directly from the data dictionary associated to the table.

Generally an edit control will have some static text associated with it as a prompt. The best way to do this is not with a separate control but with the [.Label\$](tmp/PROP_EDIT_EDITLABEL.htm) string property introduced in KCML 5.03. KCML will then take on responsibility for alignment in some circumstances (see [Introduction to Edit Groups](IntroEditGroup.htm)). When adding controls to a form they ought to be dropped on an [Edit Group](FormsDesignerWorkingWithEditGroups.htm) to facilitate automatic alignment.

Other useful Edit control properties

[*CanConvert*\
](tmp/PROP_KCMLEDIT_CANCONVERT.htm)[*Help\$\
[DropDown](tmp/PROP_EDIT_DROPDOWN.htm)\
[DropStyle](tmp/PROP_EDIT_DROPSTYLE.htm)\
[DropDownFilled](tmp/PROP_KCMLEDIT_DROPDOWNDIRTY.htm)\
[Type\$](tmp/PROPSTR_TYPE.htm)\
[ValidateText\$](tmp/PROP_KCMLEDIT_VALIDATETEXT.htm)*\
](tmp/PROP_GENERIC_HELP.htm)[Label\$](tmp/PROP_EDIT_EDITLABEL.htm)

Useful Edit control event handlers:

[*Click()\
[DropDown()](tmp/PROP_KCMLEDIT_DROPEVENT.htm)\*
](tmp/PROP_KCMLEDIT_CLICK.htm)

*MaxText()\
[Validate()](tmp/PROP_KCMLEDIT_VALIDATE.htm)*

 
