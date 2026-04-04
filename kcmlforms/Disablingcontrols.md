Disabling controls

To disable a control, either set the [*Enabled* property to FALSE within the](tmp/PROPNUM_ENABLED.htm) [Forms Designer](TheKCMLFormsDesigner.htm) or change the *Enabled* property directly within the program, for example the following would be used to disable the controls *cbControl1, listControl1 and editControl1*:

.cbControl1.Enabled = FALSE .listControl1.Enabled = FALSE .editControl1.Enabled = FALSE

and to re-enable the controls set the *Enabled* property to TRUE, for example:

.cbControl1.Enabled = TRUE .listControl1.Enabled = TRUE .editControl1.Enabled = TRUE

If a number of controls are to be enabled or disabled as a group then they should be grouped in the Forms Designer with the [Group Tool](FormsDesignerGroupingControls.htm) and then if the group is enabled or disabled, all the controls will be changed automatically. See [Disabling groups of controls](Disablingandenablingagroupofcontrols.htm).
