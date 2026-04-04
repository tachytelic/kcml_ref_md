Alternative naming

It is worth pointing out at this stage that in the example above it may not always be necessary to specify the main object name, in this case *Form1,* as it is likely that these statements would appear within the scope of the DEFFORM and FORM END statements. Therefore the statement could be rewritten as

.edit1.Text\$ = "New text"

It is also possible to drop the control name itself from the statement if the control is being referenced from within its own event handler. For example:

..Text\$ = "New text"

Alternative naming is particularly useful in the case of group event handlers where the event handler can be called by any of the controls in the group.
