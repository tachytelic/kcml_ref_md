The Enter() event

At this point only server data structures exist and nothing has been sent to the client. If an [*Enter()* event handler exists in the program for the form KCML will then call that subroutine which can manipulate any properties and load any database records that may be required for data awareness. If at any point in this routine the program invokes the](tmp/PROP_FORM_ENTER.htm) [*Terminate()* method then the](tmp/PROP_DLG_TERMINATE.htm)

*Open()* method will return and the server-side data structures representing the form object will be destroyed. Because the client has not yet been sent the details of the form it is never visible to the user.

At the end of the user's [*Enter()* event handler KCML will call the internal default](tmp/PROP_FORM_ENTER.htm)

*Enter()* handler which will check if there are any data aware controls on the form and update the server-side properties from the database appropriately. It will then send instructions to the client to create and display the form using the current server-side properties. The user will now be able to see the form.

You cannot reference any OCX properties or methods in the Enter() event as the OCX has not yet been started. These must be deferred to the Show() event.
