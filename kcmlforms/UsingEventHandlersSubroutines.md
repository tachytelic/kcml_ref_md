Calling event handlers as subroutines

Since an event handler is basically a subroutine it is possible to call them directly as if they were a method although the full name of the event handler must be specified. For example, to directly call the *Click()* event handler for the Help button the following could be used:

ReturnStatus = Form1.Help.Click()
