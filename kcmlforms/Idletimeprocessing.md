Idle time processing

Each form can be instructed to continually perform a task at a given interval while the form is not processing any other event handlers. This feature can be used to perform background tasks such as polling a file for information or updating a clock on the form. To utilize this feature the [*Idle()* event handler must be created for the form and the](tmp/PROP_FORM_IDLE.htm) [*IdleTimer* property should be set to specify the interval in milliseconds at which the](tmp/PROP_FORM_IDLETIMER.htm)

*Idle()* event handler is to be called. For example, the following would set an interval of 60 seconds:

.form.IdleTimer = 60000

Setting

*IdleTimer* back to its default setting of -1 disables the *Idle()* event handler.

Note that calling the

*Idle()* event handler repeatedly will take up CPU time, therefore you should make sure that the interval specified by the *IdleTimer* property is sufficiently large.
