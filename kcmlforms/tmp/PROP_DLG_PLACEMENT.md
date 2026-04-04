Placement (form control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, TopLeft, TopCenter, TopRight, MiddleLeft, MiddleCenter, MiddleRight, BottomLeft, BottomCenter, BottomRight, DefaultInParent, RelativeToParent, FullScreen, WorkingArea, SubForm, Stretch, NoFontCheck)*

**Specifies the default position of the form**

This property is used to specify the default positioning of new forms. If left unchanged the placement of forms is left to Windows. The available settings for this option are shown below. For example: - DEFEVENT Form1.Enter() .form.Placement = &.MiddleCenter END EVENT

Note that the [*Left*and](PROPNUM_X.htm) [*Top* properties can also be used to adjust the position of a form.](PROPNUM_Y.htm)

Most of the placement settings affect where the form appears on the screen. Some, however, also affect the size of the form. The *Stretch* setting moves and sizes all controls to fill out the form, but for the other settings controls will appear as designed, unless the [Anchoring option](/FormsDesignerAnchoringthecontrolsonaform.htm) is used in the form designer to scale and move certain controls.

If the Resize option is selected in the forms designer, a form may be enlarged by dragging the borders in the normal Windows fashion or by using the Maximize Box onthe caption bar which will be enabled. A form can never be dragged to smaller than its design size.

**Available placement settings:**

***Default***

Placement is left to system. Normally the position of forms is stored in the registry by user when the client terminates, so that each initial form appears in the same place. If this means that a form will spill off the side or bottom then it is moved so that all of the form is visible. If the form is too bug for the screen, then an attempt wil be made to use a smaller font so that the entire form will be visible. The [*Left*and](PROPNUM_X.htm) [*Top* properties are ignored.](PROPNUM_Y.htm)

***TopLeft, TopCenter, TopRight, MiddleLeft, MiddleCenter, MiddleRight, BottomLeft, BottomCenter, BottomRight***

Places the form at the specified position relative to the physical screen. The [*Left*and](PROPNUM_X.htm) [*Top* properties are ignored.](PROPNUM_Y.htm)

***DefaultInParent***

Placement is left to KCML. This will most likely be placed at the location of the last form displayed. The [*Left*and](PROPNUM_X.htm) [*Top* properties are ignored.](PROPNUM_Y.htm)

***RelativeToParent***

The form is positioned relative to the top left hand corner of the KCML Window, using the [*Left*and](PROPNUM_X.htm) [*Top* properties.](PROPNUM_Y.htm)

***FullScreen (5.03 and above)***

The form occupies the whole screen, overlapping any taskbar that may be visible. It is not maximized. The [*Left*and](PROPNUM_X.htm) [*Top* properties are ignored.](PROPNUM_Y.htm)

***WorkingArea (5.03 and above)***

The form occupies the entire screen area, exluding any taskbar. Note that the exact width and height of the form will depend on where the taskbar appears (it is nornally at the bottom, but may be against any side), and its current size. The [*Left*and](PROPNUM_X.htm) [*Top* properties are ignored.](PROPNUM_Y.htm)

***Stretch (5.03 and above)***

The form is stretched until it occupies the entire screen area, including the task bar. The font is scaled to its largest size such that the form stilll fits on the screen, and then the form and all the controls are stretched to fill the area. The [*Left*and](PROPNUM_X.htm) [*Top* properties are ignored.](PROPNUM_Y.htm)

***NoFontCheck (5.03 and above)***

The same as Default, but there is no check that the form will fit on the screen using the font specified (or default font if none specified). This is the behaviour of Default on versions prior to 5.03.

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
