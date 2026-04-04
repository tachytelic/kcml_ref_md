Assigning font sets to controls

To assign a font set to a control the pointer to the font set is assigned to the controls

*Font* property. Both stock fonts and new fonts created within the forms designer can be assigned to a control. For example, the following could be used to change the font used by the control *Edit1* to use a large bold font:

.Edit1.Font = &.HugeBold

Note that the actual font used by a [stock font](Acompletelistofstockfonts.htm) is based on the font used by the actual form. It is therefore recommended that you always use stock fonts to ensure that your forms retain the standard Windows look and feel.

Many controls can have the same font set assigned. If this is the case then any changes to the font will automatically be reflected by each control. For example, the following would change the font name used by the font set *dlgfont1* and assign it to a list box, a combo box and a button:

.dlgfont1.name\$ = "Arial" .listControl1.font = &.dlgfont1 .comboControl1.font = &.dlgfont1 .btnControl1.font = &.dlgfont1
