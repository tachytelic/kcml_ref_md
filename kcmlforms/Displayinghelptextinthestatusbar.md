Displaying help text in the status bar

Certain controls are able to display help information in the status bar when the control gets focus. The help information is specified with the [*Help\$* property. Note that a status bar must exist on the form before information can be displayed. Also note that changes to the](tmp/PROP_GENERIC_HELP.htm) [*Help\$* property are not reflected until the current event handler has finished processing. To instantly update the text in the status bar after](tmp/PROP_GENERIC_HELP.htm) [*Help\$* has been modified you should call the](tmp/PROP_GENERIC_HELP.htm)

*Form.Flush()* method.

Note that the contents of

*Help\$* will also be used as a tooltip when the mouse pointer hovers over the control.
