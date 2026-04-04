Alternative naming

Like properties it may not always be necessary to specify the main object name, in this case *Form1,* as it is likely that these statements would appear within the scope of the DEFFORM and FORM END statements. Therefore the statement from the example above could be written as:

IF (.listControl1.Add(text\$)) ‘DisplayError() END IF

It is also possible to drop the control name itself from the statement if the control is being referenced from within its own event handler. For example:

IF (..Add(text\$)) ‘DisplayError() END IF
