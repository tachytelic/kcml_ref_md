Forms Designer - Anchoring the controls on a form

To make sure that controls on a form remain in a tidy position if the form is resized you can set the controls anchor points. Once the controls have been placed on the form, select the [Edit Menu - Anchor Controls](TheEditMenuAnchorcontrolsoption.htm) option or the Anchor Controls Tool bar option [<img src="bitmaps/form0158.gif" data-align="BOTTOM" data-border="0" alt="Anchor tool" />](TheEditMenuAnchorcontrolsoption.htm). Once selected, the anchor points for the control are shown as white blocks on each side of the control. To set an anchor point simply click on the blocks and the block will change color.

To be able to resize a form at runtime you must set the forms [Resize](tmp/PROP_DLG_RESIZEDLG.htm) property to TRUE in the forms designer. For an example program showing anchored controls click [here](ExampleResize.htm).

The following examples show the effects of setting different combinations of anchor points:

1.  With no anchor points set, the button in the following example will remain in exactly the same position and will not change size if the form is resized.

    <img src="bitmaps/form0159.gif" data-align="BOTTOM" data-border="0" alt="No anchors" />

2.  If the top and right anchor points are set then the button will remain the same size and will remain the same distance from the top right hand corner regardless of how the form is resized.

    <img src="bitmaps/form0110.gif" data-align="BOTTOM" data-border="0" alt="Anchored to top right" />     <img src="bitmaps/form0111.gif" data-align="BOTTOM" data-border="0" alt="Anchored to top right and stretched" />

3.  If the left and right anchor points are set then the control is stretched.

    <img src="bitmaps/form0112.gif" data-align="BOTTOM" data-border="0" alt="Anchored on both sides" />     <img src="bitmaps/form0113.gif" data-align="BOTTOM" data-border="0" alt="Anchored on both sides and stretched" />
