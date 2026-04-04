Forms Designer - Working with the Picture control

------------------------------------------------------------------------

To add a picture control to the form click on the <img src="bitmaps/form0093.gif" data-align="BOTTOM" data-border="0" alt="form0093.gif" /> icon on the controls palette.

Picture control can either act as a normal push button containing a picture or as a static picture. Once the control has been placed onto the form a picture can be selected by changing the [Picture](tmp/PROP_GENERIC_PICTURE.htm) property in the controls [properties list](TheFormsDesignerPropertieslist.htm). Note that initially at design time in the forms designer only files from the that PC client are available. At runtime, connected to the server, picture files can be loaded from the server directly from within the program by setting the [Cache\$](tmp/PROP_PICTURE_CACHE.htm)property.

The caption text for a picture control is set with the [Text\$](tmp/PROPSTR_TITLE.htm) property. To include an accelerator key in the caption text simply insert an ampersand (&) before the required character.

Normally pictures are automatically stretched when they are displayed. An alternative display method can be set with the [PictureAlignment](tmp/PROP_DLG_PICALIGNMENT.htm) property.

It is possible to set a transparent color within the bitmap with the [TransparentBitmap](tmp/PROP_BUTTON_TRANSPARENTBITMAP.htm) property. The specified color will then be replaced by the current background color of the control as specified by the [BackColor](tmp/PROP_GENERIC_BACKCOLOUR.htm) property. If the [NoFill](tmp/PROP_BUTTON_NOFILL.htm) property is set then the current background color or background picture of the form will replace the transparent color.

Using the control as a picture button

For the control to act as a picture button, that is to allow the button to go up and down when clicked, the [Thickness](tmp/PROP_BUTTON_THICKNESS.htm) property must be set to a value other than zero.

Using the control as a static picture control

To make the picture look like a static picture you should set the [Thickness](tmp/PROP_BUTTON_THICKNESS.htm) property to 0 to prevent the button from being moved up and down if it is clicked. The [NoFocusRect](tmp/PROP_BUTTON_NOFOCUSRECT.htm) property should be set to *TRUE* to remove the focus rectangle from the button face and to remove the text label from the picture the [Text\$](tmp/PROPSTR_TITLE.htm) should be set to blank. The border around the picture can be removed by setting [NoBorder](tmp/PROP_BUTTON_NOBORDER.htm) to *TRUE*.

Using a stock picture

To select a stock picture you need to double click on the [Picture](tmp/PROP_GENERIC_PICTURE.htm) property within the properties list for the control. Select the required stock picture from the *Picture Name* drop down. See [Stock Pictures](Acompletelistofstockpics.htm) for a complete list of available pictures.

**Other useful picture control properties**

\
[Enabled](tmp/PROPNUM_ENABLED.htm)\
[DropColor](tmp/PROP_BUTTON_DROPCOLOUR.htm)\
[ShadowColor](tmp/PROP_BUTTON_SHADOWCOLOUR.htm)\
[MouseX](tmp/PROP_BUTTON_MOUSEX.htm),\
[MouseY](tmp/PROP_BUTTON_MOUSEY.htm)

**Useful picture control Event handlers**

[Click()](tmp/PROP_PICBUTTON_CLICK.htm)
