The Exit() event

This event occurs when the [*Terminate()* method is called either explicitly in the code of a handler or implicitly as a result of an OK button click or a CANCEL button click. If there is an user event handler for the](tmp/PROP_DLG_TERMINATE.htm) [*Exit()* event then it will be called after the client form has been destroyed but the server-side properties and local variables will still be available for inspection. On exit from the handler the object will be destroyed and KCML will return from the Open method. The](tmp/PROP_FORM_EXIT.htm)

*Exit()* event is intended to be used for tidy up code common to the other ways of exiting the form.

You cannot reference OCX controls in the Exit() event as they have already been shutdown by the client as part of the termination procedure before the server triggers this event.
