Open() (Form method)

Used to open and display a Form. Form objects must have preveiously been defined with the [DEFFORM](Formsprogramming.htm) statement For example:

-DEFFORM Form1() FORM END Form1.Open()

<span style="font-family: Courier New,monospace; "> </span>For form objects the *Open()* method returns TRUE if the OK button was selected or ***FALSE*** if the Cancel button was selected. Other values can be returned if the form

*Terminate()* method is used.
