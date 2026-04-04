Form definitions

For each new form created by the [Forms Designer](TheKCMLFormsDesigner.htm) the form definition statements required to support the form are automatically inserted into the program, for example:

-DEFFORM Form1() FORM END Form1.Open()

The DEFFORM statement contains the complete description of the form (i.e. what it looks like). The editor suppresses the description as it is not readily intelligible, which is what the form editor is for. Because the editor shows only a limited amount of information the statement is shown in a different color and cannot be modified directly within the editor.

KCML will also insert a method to open the form when the program is executed. You may not want to display the form immediately, therefore the

*Open()* method should be moved to the relevant place within the program. Although the DEFFORM and FORM END statements are created automatically by the Forms designer, it is also possible to create a blank form directly by manually entering the DEFFORM and FORM END statements. The new blank form can then be edited by right double clicking on the form definition.
