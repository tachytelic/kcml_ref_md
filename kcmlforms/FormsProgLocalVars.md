Defining local variables for forms

Statements entered between the DEFFORM and FORM END statements are only executed when the form is opened. Normally only the event handlers for the form would appear within the definition. However, it may also be useful to locally define any variables required by the definition and its event handlers etc. For example:

-DEFFORM Form1() LOCAL DIM Temp\$1000, Flag\$1, Sort_Temp\$1000 . . . FORM END
