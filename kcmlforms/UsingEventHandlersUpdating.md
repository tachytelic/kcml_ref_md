Updating a forms controls within an event handler

To minimize network traffic, any changes made to the form and its controls while an event handler is processing are not sent to the client until the end of the event handler, i.e. when the END EVENT statement is reached. It is sometimes necessary to update controls on the form within an event handler. A common example of this is the Gauge control which is used to display a progress chart. To update the form and its controls within an event handler the

*Flush()* method is used.
