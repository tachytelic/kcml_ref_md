Return values

Most methods return a value upon completion so that the method can return information back to the program. In most cases the return value is used simply to inform the programmer that the request has passed or failed. Normally a value of zero signifies that the request passed and any other non-zero value is returned to signify a fail. The return value from a method can be used in place of a numeric function, for example:

IF (Form1.listControl1.Add(text\$)) ‘DisplayError() END IF

The above example would call the *‘DisplayError()* routine if the attempt to add an item to the control *listControl1* failed.

Although most methods return numeric values some also return string values, for example list boxes have the

*GetString\$()* method which is used to retrieve the specified string from a list box.
