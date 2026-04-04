## Color options dialog

This dialog allows the colors and fonts used in the editor and debugger to be changed. This is done in an interactive way by dragging the color or font required from this palette and dropping it on top of an example of the text element you wish to change.

Any changes will only be permanent if you click the OK button. You can still revert to the original factory default colors and fonts by clicking the Default button.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/coloropts.png" data-border="0" alt="Color options dialog" />

</div>

### Components of the dialog

Along the top of the dialog are a palette of the 16 standard Windows colors. Below that are another 16 custom colors which are initially all white. On the third row are four drop zones. The first two act together to allow colors for the debug window to be re-mapped. This is explained further below. The third drop zone is used to define a custom color and the fourth is used to define a custom font.

### Changing editor colors

You may first wish to set up some special custom colors, see [below](#CustomColor). Pick the color from the built in or custom palette and drag it onto the element of the editor to be colored. For background colors drag using the right mouse button. Elements that can be colored include

|                              |
|------------------------------|
| Program text                 |
| Comments (REMs)              |
| Variables                    |
| Objects                      |
| Numeric and string constants |

### Changing editor fonts

This first requires that you have set up some custom fonts using the option described [below](#CustomFont). You have up to three custom fonts in the palette which can then be dragged onto the appropriate window. Only one font can be used per window. Fonts are stored by scene however. <span id="CustomColor"></span>

### Defining a custom color

Pick one of the custom color pads in the custom color palette on the second row and drag it down onto the third drop zone marked 'Drag colors here to customize colour' Choosers will bring up a standard Windows dialog allowing you to select exactly the color required. If you pick a color and exit the dialog with the OK button then the color will appear in the chosen pad of the custom color palette augmenting the built in standard colors. This has been done for the first color of the custom palette which has been set to a light purple. <span id="CustomFont"></span>

### Defining a custom font

Pick one of the three custom fonts pads (which are initially set to 15pt FixedSys) and drag it onto the fourth drop zone marked 'Drag fonts here to customize fonts'. This will bring up the standard Windows Font Chooser dialog allowing you to pick a new font, font style and font size. This will then appear in the custom font palette. In the example dialog the first two pads have been changed to Lucida Console 15pt Italic and Courier New. Note that only monospaced fonts are selectable.

### Re-mapping debug colors

This uses the first two drop zones to re-map colours used in the editor to alternative colors for the debugger. By default the white background of the editor is set to a pink color when the editor is active. This indicates visually the mode. To re-map a particular editor color drop an example from the palette onto the first zone and drop the new color onto the second zone. All instances of the first color will then be transformed into the second.
