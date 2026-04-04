Changing the text on the face of a push button

To change the text that appears on the face of a button you can either set the [*text\$* directly within the](tmp/PROPSTR_TITLE.htm) [Forms Designer](TheKCMLFormsDesigner.htm) or you can modify this property within a program, for example:

.btnControl1.text\$ = "New Text"

The current button text can also be returned, for example:

ButtonText\$ = .btnControl1.text\$
