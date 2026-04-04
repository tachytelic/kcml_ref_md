# <span id="formwindowpreferences"></span> Form Window Preferences

This dialog controls colors and fonts on Forms.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

## <img src="bitmaps/formpref.gif" data-border="0" alt="Form preferences" />

</div>

| Element | Purpose |
|----|----|
| Default form font | This is the default font used for static text on forms. It will usually be a proportionally spaced sans serif font. Kclient will use the system defined font for the user. |
| Tag text color | Some list boxes and combo boxes allow a descriptitive text to be shown next to the value in the list. To distinguish this tag field it can be in a special color. The default is blue. |
| Read-only editbox background color | If this is left unchanged kclient will use normal Windows rules for distinguishing editable from read only fields. To make it more obvious when a field is editable it is possible to set a background color for a readonly control. |
| Editable field background color | See above. |
| Show help text on tooltip | If checked on then the kclient will display a tooltip box whenever the mouse cursor is hovered over a field that has a helpstring defined. |
| Show truncated text on tooltip | If checked on then kclient will display a tooltip with the full text whenever the mouse cursor is hovered over a field that is smaller than the text it contains. |
| Large toolbar | If checked on then the bitmaps on toolbars will be displayed in 24x24 pixel size rather than 16x16 and they will be underwritten with a title à la IE4 |

There may be extra color selections beyond the built in tag color, read-only background and editable background if the application has made use of user defined colors. Developers may wish to look at the client object method [.UserColor()](mk:@MSITStore:kcmlforms.chm::/tmp/Forms_UserColor.htm) in the developer documentation to see how this is implemented.
