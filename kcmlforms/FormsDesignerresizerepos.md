Forms Designer - Sizing and positioning the form

The initial position of a form is normally left to Windows. Generally this is the best option. Normally the position of the last main form is stored in the registry, so that each form appears in the same place. If this means that a form will spill off the side or bottom then it is moved so that all of the form is visible. If the form is too big for the screen, then an attempt wil be made to use a smaller font so that the entire form will be visible. The form designer has boxes drawn on its background to allow you to see typical screen sizes so you can ensure your forms will fit the target monitor size.

If a more specific position is required then the [*Placement* property should be set accordingly. Options include the obvious TopLeft, TopCenter, TopRight, MiddleLeft, MiddleCenter, MiddleRight, BottomLeft, BottomCenter, BottomRight as well as FullScreen and RelativeToParent.](tmp/PROP_DLG_PLACEMENT.htm)

This property when used in conjunction with the [*Top* and](tmp/PROPNUM_Y.htm) [*Left* form properties gives full control over the forms position. These properties can be changed directly within the](PROPNUM_X.htm) [properties tab](TheFormsDesignerPropertieslist.htm).

To set the size of the form first click on the forms background then drag the sizing handles to the required size. When the size of the form is changed any controls that have had [anchor points](FormsDesignerAnchoringthecontrolsonaform.htm) set are automatically repositioned. You can also change the size by directly modifying the [*Height* and](tmp/PROPNUM_H.htm)

*Width* properties.

The forms designer status bar always displays the current size and position of the form.
