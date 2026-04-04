Validating the text entered into an Edit control

------------------------------------------------------------------------

If the text in a Edit control is changed and the control loses focus the [*Validate()* event handler is called, if it exists. Once called, the text entered by the user is passed into this routine in the](tmp/PROP_KCMLEDIT_VALIDATE.htm) [*ValidateText\$* property while the original contents of the control, i.e. the contents before the user made any changes, is stored in the](tmp/PROP_KCMLEDIT_VALIDATETEXT.htm)

*Text\$* property. Therefore if the user has entered an invalid value the original setting is still available to the program, for example:

-DEFEVENT EditControl1.Validate() IF (..ValidateText\$ \<\> CorrectValue\$) RETURN FALSE END IF .... END EVENT
