Allowing the user to cancel event processing

------------------------------------------------------------------------

Normally an event handler will continue processing until the end of the event handler is reached or if a RETURN TRUE/FALSE statement is executed. Sometimes it is useful to allow the user to terminate a processing event. The

*EventPending()* method if executed will return *TRUE* if the user has triggered another event, then current event handler can then be exited with the RETURN TRUE/FALSE statement or by jumping to the end of the event handler. Once the event handler is exited the event handler for the pending event is then executed. For example the following event handler would continue processing until another event is triggered by the user.

-DEFEVENT Form1.ProcessData() .form.Busy() WHILE (Count \< MaxRecords) DO 'GetNextRecord() 'ProcessRecord() IF (.form.EventPending()) BREAK END IF WEND END EVENT
