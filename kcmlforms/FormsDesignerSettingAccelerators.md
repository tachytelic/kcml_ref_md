Forms Designer - Setting Accelerators

------------------------------------------------------------------------

To make it easier for the user to navigate around the form it is advisable to add accelerator keys to controls. Accelerator keys can be added to most controls by inserting an Ampersand (&) before the required character in the controls

*Text\$* property. When the form is displayed the controls label has the accelerator key underlined. The user can then use the Alt key followed by the specified key to move directly to the control. For example, for a check box you could set the *Text\$* property to "&CheckBox" which would add the letter "C" as an accelerator key. The user would then be able to press Alt+C to move directly to the control.

Not all controls have an associated text label, for example edit controls and list boxes etc. For these controls accelerator keys cannot be set directly. However, it is possible to add a Static text description next to the control that contains an accelerator key and since Static text controls can accept no input the focus is moved to the next control in the tab order. Therefore you must make sure that the Static text control appears before the control in the tab order. To check the tab order click on the [<img src="bitmaps/form0160.gif" data-align="BOTTOM" data-border="0" alt="form0160.gif" />](TheEditMenuSetTaborderoption.htm) tool bar button.

By including an accelerator key as part of a group box the key can be used to move to the first control within a group. Like static text labels, the group box must appear in the tab order before the first control in the group.

The [Tools Menu](TheToolsMenu.htm) - [Check Accelerators](ToolsMenuCheckAccelerators.htm) option can be used to verify accelerator keys. Normally accelerator keys are checked when the forms designer is closed. To stop accelerators from being checked modify the Check for Accelerator keys on exit option in the [Edit Menu](TheEditMenu.htm) - [Edit Options](TheEditMenuEditOptions.htm) - [Misc. Tab](EditOptionsMiscTab.htm).

Function keys can also be used to accelerate controls by specifying the function key as "&F&1" to "&F&12" for function keys 1 to 12.
