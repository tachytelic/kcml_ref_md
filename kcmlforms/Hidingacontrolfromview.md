Hiding a control from view

------------------------------------------------------------------------

To temporarily hide a form control from the user, either set the [*Visible* property to *FALSE* within the](tmp/PROPNUM_VISIBLE.htm) [Forms Designer](TheKCMLFormsDesigner.htm) or change the *Visible* property within the program, for example the following would be used to hide the controls *btnControl1, listControl1* and *comboControl1*:

.btnControl1.visible = FALSE .edit1.visible = FALSE .comboControl1.visible = FALSE

and to find out the current *Visible* state of a control you could use the following:

BtnState = .btnControl1.Visible
