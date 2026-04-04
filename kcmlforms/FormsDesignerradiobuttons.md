Forms Designer - Working with Radio buttons

------------------------------------------------------------------------

To add a Radio button to the current form click on the <img src="bitmaps/form0050.gif" data-align="BOTTOM" data-border="0" alt="form0050.gif" /> icon on the controls palette.

Radio buttons are used provide the user with a series of selection boxes where only on selection can be made. As a new selection is made the existing selection, if any, is cleared.

As each new Radio button is placed onto the form you will be prompted for a button set name. If no button set names exist then you will need to create a new one.

The caption text for a radio button is set with the [*Text\$* property. To include an accelerator key in the caption text simply insert an Ampersand before the required character. See](tmp/PROPSTR_TITLE.htm) [Working with Accelerators](FormsDesignerSettingAccelerators.htm) for more information.

The default state of the button is set with the

*State* property. A value of true fills the radio button. Obviously only one radio button within any button group can be filled.

**Other useful radio button properties**

*Enabled\
[LeftText](tmp/PROP_CHECK_LEFTTEXT.htm)\
[Visible](tmp/PROPNUM_VISIBLE.htm)*

**Useful Radio button event handlers**

*Click()*
