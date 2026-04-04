Positioning forms

------------------------------------------------------------------------

To position a form under program control, the [*Placement, [Left](PROPNUM_X.htm)* and](tmp/PROP_DLG_PLACEMENT.htm) [*Top* properties are used. The](tmp/PROPNUM_Y.htm) [*Placement* property is used to specify the new position from a selection of preset values, while](tmp/PROP_DLG_PLACEMENT.htm) [*Left* and](PROPNUM_X.htm)

*Top* are used to explicitly specifiy the new position. For example, the following would move the specified form to the center of the screen:

.form.Placement = &.MiddleCenter

For a list of available placement settings see

*Placement.*

When using the [*Left* and](PROPNUM_X.htm)

*Top* properties the new position is specified in screen pixels, for example:

.form.Left = 100 .form.Top = 100

To allow the [*Left* and](PROPNUM_X.htm) [*Top* properties to be specified in Dialog Box Units (](tmp/PROPNUM_Y.htm)[DLUs](DialogBoxUnitsDLUs.htm)) the placement property should be set to *RelativeToParent.*
