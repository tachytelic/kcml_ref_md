Defining local variables in an event handler

Event handlers inherit all existing variables including any variables defined locally for the form. It is also possible to define a new range of local variables for the event handler itself, this is done with the LOCAL DIM statement. For example:

\- DEFEVENT Form1.btnControl1.Click() LOCAL DIM Main\$1000, Temporary\$1000, Test ... END EVENT
