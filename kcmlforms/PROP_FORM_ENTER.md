Enter() (Form event handler)

This event is called before the form is actually displayed. This event handler is usually used to initialize form controls before the form is actually displayed. Because the form has not actually been created within Windows at this time, any OCX controls it contains have yet to be instantiated and so cannot be referenced here. However the standard KCML controls do exist and can be inspected or modified at this time.
