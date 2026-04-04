Terminating a form

------------------------------------------------------------------------

Normally a form is terminated when either of the OK and Cancel buttons are clicked. Once terminated, program control is returned to the statement immediately following the [*Open()* method for the form. The *Open()* method returns a value that can be used to determine how the form was terminated. The OK and Cancel buttons return a value of 1 (*TRUE*) and 0 (*FALSE*) respectively. The](OpenFormmethod.htm) [*Terminate()* method can be used to terminate a form prematurely and can pass a return value back to the](tmp/PROP_DLG_TERMINATE.htm)

*Open()* method. For example:

.form.Terminate(2)

Note that if you need to add an OK or Cancel button to a form you must set the

*Type* property accordingly.
