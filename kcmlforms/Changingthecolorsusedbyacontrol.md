Changing the colors used by a control

------------------------------------------------------------------------

The colors used by a control can be set with the [*BackColor*](tmp/PROP_GENERIC_BACKCOLOUR.htm) and [*TextColor*](tmp/PROP_GENERIC_TEXTCOLOUR.htm) properties. If no color is set for a control by the program or within the Forms Designer then the default Windows background and text colors are used. If the colors for a control need to be changed by the program then a number of stock colors exist. For example, the following would change the text and background color of the control *Edit1* to green on white:

.EditControl1.TextColor = &.Green .EditControl1.BackColor = &.White

To return the colors back to the Windows default colors a value of default can be specified, for example:

.Edit1Control.TextColor = &.Default .Edit1Control.BackColor = &.Default

If you require a color other than one of the [stock colors](Acompletelistofstockcolors.htm) then a new color object can be create in the forms designer. Once the new object has been created the the color can then be adjusted directly by the program by changing its RGB values. For example, assuming that *color1* is being used as the background color for several controls on the form, then the following would set the background color for those controls to yellow.

.color1.red = 255 .color1.green = 255 .color1.blue = 0

Color sets created in this way can also be assigned to other controls. For example:

.listControl1.BackColor = &.color1 .comboControl1.BackColor = & color1

Note that most Windows applications tend to use the Windows standard colors so that if the user changes to a different color scheme the applications will continue to look the same. If you explicitly set the colors for controls then those colors may nave a different meaning in different color schemes. The KCML Forms designer allows colors from the Windows standard color list to be set for a control if required.
