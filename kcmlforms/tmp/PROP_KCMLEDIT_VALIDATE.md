Validate (kcmledit control event)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called if the contents of the control were modified by the user**

This event handler is used to validate text entered into an Edit control by the client. This event handler is only called if the text in the control has changed and the control is about to lose focus. Text set programmatically at the server is considered to be valid initially. It becomes invalid only if changed at the client. The modified text is available to the routine in the [ValidateText\$](PROP_KCMLEDIT_VALIDATETEXT.htm) property while the original, presumably valid, text is stored in the [Text\$](PROPSTR_TITLE.htm) property.

The changed text is only accepted if the event handler completes succesfully, i.e. a RETURN FALSE statement is not executed. KCML will set the .text\$ property to be the same as the ValidateText\$ property. If the handler declares the text to be invalid by returning FALSE then the text is still considered modified and .Text\$ is not changed. In order to shift focus to another control, the user must either enter valid text or press any Cancel button.

The [AlwaysValidate](PROP_KCMLEDIT_VALIDATEPROP.htm) property can be used to force the Validate() event to trigger on loss of focus even if the value of the control has not altered thus acting like the deprecated .LoseFocus() event in KCML 5.

Validate() events and dropdown lists

Note that on edit controls with a dropdown list, the Text\$ field is set when the list entry changes in preparation for a [SelChange()](PROP_EDIT_SELCHANGE.htm) event. Thus in a Validate event (which will always happen after the SelChange event), both the Text\$ and ValidateText\$ will reflect the new selection. In these cases Validate makes little sense in terms of validation as the user is presented with a given list of presumably valid selections in the first place. The Validate event is still generated for the benefit of applications that prefer to fill in other fields on the form only after the user moves away rather than on every selection change.

Validate() events and menus

The validate event is only triggered when the control loses focus. If the form has a menu or toolbar, then selecting a menu item will not cause the control to lose focus. However, in this case the validate event is triggered first (assuming the contents have been changed) and only if the return from the handler is TRUE will the menu selection will occur.

It is possible to have individual menu items that do not force the validation to take place, for instance if the menu item will perform some sort of lookup based on the current value. This can be done programatically in the [Create()](PROP_FORM_CREATE.htm) event with


     .menu.menuitem.Flag = .menu.menuitem.Flag + 0x80000000

Validate() events and Return() events

If a control has both a .Validate() event handler and an enabled [.Return()](PROP_KCMLEDIT_RETURN.htm) event handler then the Validate() event gets priority if RETURN is pressed. The Return() event will not trigger if the text has been modified and the Validate() event will be called. Only if the text is considered valid as a result of being set by the server or having passed a previous validation will the Return() event get called.

Note that in the case of modified text, focus will not actually leave the control in response to the RETURN even if .Validate() returns TRUE in order to be compatible with the normal rules for Return() events.

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
