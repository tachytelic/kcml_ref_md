The Show() event

If there is a [*Show()* event in the program then it will now be executed. This provides an opportunity for the program to reference any OCX controls which will have been instantiated before this event occurs or to raise any error messages in the context of the form as error messages in the](tmp/PROP_FORM_SHOW.htm) [*Enter()* event handler will not have a parent form. At the end of the users](tmp/PROP_FORM_ENTER.htm)

*Show()* event KCML will call the default handler which checks if any data aware controls have had their properties changed by the users handler and it will send any changes to the client to display.
