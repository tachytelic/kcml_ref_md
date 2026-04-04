Form control overview

The Form object is the parent of all the other controls that make up a form. The Form owns its child controls so if the form is moved then the other controls move too. The form is described by a DEF FORM statement in the program and is created by an Open() method applied to the named form. A number of server side events are triggered by the .Open(). These allow the programmer finer control over how the form is displayed and are described in the [form life cycle](ThelifehistoryofaForm.htm) page.

Forms can be [positioned](PositioningForms.htm) by setting design time properties or by setting those properties in an event handler. Forms can have a picture as a background by setting the [Picture](tmp/PROP_GENERIC_PICTURE.htm) property.

Forms can [inherit](FormsProgInherit.htm) controls and event handlers from template forms. This can make forms more consistent is appearance and can reuse code more effectively.

Forms can be created and modified dynamically. See [Dynamic Forms](DynamicForms.htm).
