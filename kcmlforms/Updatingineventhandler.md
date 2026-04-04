Updating control properties within an event handler

------------------------------------------------------------------------

When the properties of a control are changed within an event handler the actual change is not made until the event handler has finished. This is not always desirable as the event may need to constantly update controls on the form while it is processing. The [*Flush()* method can be used to force an update. A typical example is the KCML gauge control which is used to display a progress guage. Normally the progress of the event would not be updated until the event completed, therefore the gauge would jump straight to 100%. To constantly update the position the](tmp/PROP_DLG_FLUSH.htm)

*Flush()* method should be called each time the position is moved. For example:

-DEFEVENT Form1.ProcessData() WHILE (Count++ \< 100) DO 'ProcessRecords() .gaugeControl1.Position = Count .form.Flush() WEND END EVENT
