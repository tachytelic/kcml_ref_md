Accelerator Keys

------------------------------------------------------------------------

Accelerator keys are used to make it easier for users to navigate forms with the keyboard. The accelerator key for a control is underscored in the controls label. The user can then hold the Alt key down and press the corresponding character to move to the control. It is important to make use of accelerator keys as not all users have access to a pointing device. Also some applications that require heavy keyboard use will be easier to use if the user can operate the entire form from the keyboard without having to use the mouse.

Accelerator keys are set by modifying the

*Text\$* property of a control. The accelerator key is specified by placing an ampersand (&) immediately before the character that is to be accelerated. For example, the following would make Alt+C the accelerator for the control:

.btnControl1.text\$ = "Please &Click Here"

Many controls, suct as Edit Controls, List boxes etc., do not have a direct label that is specified with the [*Text\$* property. With these controls](tmp/PROPSTR_TITLE.htm) [*Text\$* has a different meaning. To provide an accelerator key for such controls you need to place a static text label next to the control, the label for the static text can then specify the accelerator key for the control. However, for this to work the static text label must appear immediately before the control in the forms tab order (See](tmp/PROPSTR_TITLE.htm) [Setting the tab order for a form](FormsDesignerSettingthetaborder.htm) for more information).

<span id="Using_function_keys_as_accelerators" using_function_keys_as_accelerators=""></span>Using function keys as accelerators

Function keys can also be used as accelerator keys. This is done specifying the required function key as "&F&1" to "&F&12" for function keys 1 to 12 respectively, for example:

.btnControl1.Text\$ = "Press &F&12 to Continue"

 

 

 
