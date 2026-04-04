User editable Forms

KCML 5.02 introduced the [Create()](tmp/PROP_FORM_CREATE.htm) event and the [Duplicate()](tmp/PROP_GENERIC_DUPLICATE_2.htm) method which allowed a program to create a dynamic form by cloning controls already present on the template form. See [Dynamic Forms](DynamicForms.htm) for more information about this technique. Constructing a form this way may be too restrictive for some applications as the layout of the dynamic form is determined entirely by program logic. Generally this makes sense as program logic must be present to handle events. However sometimes what is required is the ability to add text or simple data aware KCML Edit controls to customize forms.

To allow end-users to modify forms directly and have the layout persist, KCML5.03 adds a new [Import()](tmp/PROP_FORM_IMPORT.htm) method which can be called inside the [Create()](tmp/PROP_FORM_CREATE.htm) event to pass a partial form definition to the kclient in a string variable allowing it to modify the form by adding new controls from the definition. This definition is similar to the ascii representation of a form normally hidden inside the DEFFORM statement.

The program will generally load the supplementary definition string from the database inside the forms [Create()](tmp/PROP_FORM_CREATE.htm) event and call [Import()](tmp/PROP_FORM_IMPORT.htm) passing it the string.

To generate a definition string the [EditForm()](tmp/PROP_FORM_EDIT.htm) method is provided which takes the [SYM()](mk:@MSITStore:kcmlrefman.chm::/SYM(.htm) of the string as its argument. This must be called also from within the [Create()](tmp/PROP_FORM_CREATE.htm) event for the form which may require a flag to be set to determine the mode in which it is to operate. The [EditForm()](tmp/PROP_FORM_EDIT.htm) method invokes the forms editor interpreting the string as a supplementary form definition. The properties of the base form itself, and any controls it might have, cannot be altered in the editor. Only controls defined in the string can be changed though new controls can also be added. In the following forms designer screen shot, taken from the dynamic forms [example](DynamicForms.htm), a static text control has been added and the original controls, which cannot be edited, are marked with a red cross.

<img src="bitmaps/dynform.png" data-border="0" alt="EditForm() example" />

The new definition is returned with the string redimensioned appropriately.

See the page on [dynamic forms](DynamicForms.htm) for an example program illustrating user editable forms.
