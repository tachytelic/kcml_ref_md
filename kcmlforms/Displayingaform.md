Displaying a form

------------------------------------------------------------------------

A form gets created when the

*Open()* method is invoked for that form. This is very much like a subroutine and an entry is placed on the top of the return stack. A data structure describing the form and it properties is created at this time (this is called instantiation). Until the *Open()* method is invoked the properties, methods etc. of a form do not exist. Similarly the data structure for the object will be destroyed when the *Open()* method is exited and those properties will then no longer exist. Because forms can be nested, it is possible to refer to the properties of a previously opened form from with an event handler belonging to a child form.

Locally DIMed variables belonging to the form also get created by the *Open()* method and any initialization code that immediately follows the DEFFORM will be executed up to the FORM END or the first DEF EVENT. Local variables declared this way may be shared by any of the forms event handlers while the form is open.

The *Open()* method returns an integer value which will be 0 if the CANCEL button dismissed the form and 1 if the OK button dismissed it. If the

*Terminate()* method was explicitly invoked then it will be the integer argument passed to this method.

 
