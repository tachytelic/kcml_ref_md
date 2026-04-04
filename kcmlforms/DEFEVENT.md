DEFEVENT

------------------------------------------------------------------------

The DEFEVENT statement is used to define the start of an event handler. For each DEFEVENT statement a corresponding END EVENT statement must exist. The DEFEVENT statement is used to define event handlers for both database and form events. Normally event handlers are inserted by selecting the event in the [Forms Designer](TheKCMLFormsDesigner.htm) or from within the [Object Browser](TheKCMLObjectBrowser.htm). It is also possible to insert a new event by typing in the DEFEVENT and END EVENT statements. For Example, the following event would be called if the button control *btnControl1* was clicked.

-DEFEVENT Form1.btnControl1.Click()\
 . . .\
 END EVENT

It is also possible to call and event handler as a method, for example the following would call the above event handler:

 Form1.btnControl1.Click()
