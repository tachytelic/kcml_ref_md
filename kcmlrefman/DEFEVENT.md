DEFEVENT

------------------------------------------------------------------------

General Form:\
\
     DEFEVENT eventname(\[\[\[argument\], argument\], ...\])\
     ...\
     END EVENT\
\
where *argument* is a string or numeric receiver.\
\

------------------------------------------------------------------------

A DEFEVENT statement marks the start of a subroutine called whenever an event is signalled back to KCML from a form executing in the client. Such subroutines are called **event handlers**. Each control on a form has zero or more possible events that can occur, e.g. the clicking of a button with a mouse will signal a .Click() event. When KCML opens a form in the client it searches the program for relevent event handlers and tells the client which events it wants to receive.

The event name is a dotted name constructed from the form name, the control name and the event name. Though it is conventional for event handlers to be defined with the scope of a DEFFORM ... END FORM block, it is equally possible for them to be defined elsewhere in the program as the name used in the DEFEVENT specifies the form to which it applies.

Though most events do not have any arguments it is possible to specify an argument list of string or numeric receivers for those that do. They must agree in type and number with the event definition.

Control returns to the form whenever a RETURN statement is executed

Syntax examples:

\
DEFEVENT Form1.btnOK.Click()

See also:

[DEFFORM](DEFFORM.htm)
