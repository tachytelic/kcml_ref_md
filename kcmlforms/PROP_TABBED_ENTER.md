Enter() (Tab control event handler)

This event handler is called on the new tab page each time the specific tab page is exposed. This event handler would normally be used to initialize various controls on the tab page prior to the tab page being exposed. It is recommended that tab controls with many tabs each containing many controls do their initialization using this event rather than doing it in the form's [Enter()](PROP_FORM_ENTER.htm) event so that there is less of a delay when the form is first created.

DEFEVENT WizForm.tabControl1.tab1.Enter() ..tab1.DisableNext = TRUE; END EVENT

Tab control event handlers are created for each tab using the [Tab Control editor](FormsDesignerTabcontrols.htm) within the [Forms designer](TheKCMLFormsDesigner.htm).

Note that the event will not be generated if the tab is clicked or tabbed onto when it is already the active tab. It is only called for the new active tab page when the active tab page is switched to another tab page on the same tab control.

Also it will not be generated when the form is opened with the tab already enabled. To be consistent and have this event triggered for all tab pages, it may be necessary to disable the tab control at design time and explicitely enable it in the forms show() event.

There is also a [Exit()](PROP_TABBED_EXIT.htm) event that can be triggered for the previous tab when a new tab is activated.
