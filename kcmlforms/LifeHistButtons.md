The OK and CANCEL buttons

The OK button is a special button with a design time type property of 'OK' which causes the client to always generate an event if Clicked even if there is no user event handler defined. The default KCML handler for this button will perform a

*Terminate(1)* method dismissing the form. A user event handler for this button can prevent the default handler being called by returning *FALSE*. A common technique is to validate text entered on the form in the OK button click event returning *FALSE* if any inconsistency is found and *TRUE* if correct.

The CANCEL button has a special design time property type of 'Cancel' which will cause the client to generate an event when clicked even if no server-side handler exists. The default handler performs a

*Terminate(0)* method dismissing the form.
