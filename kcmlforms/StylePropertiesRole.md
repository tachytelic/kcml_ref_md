The role of style properties

Certain properties, called **style properties**, which describe the look and behaviour of a control are handled specially by Microsoft Windows. With certain exceptions they must be set before the control is created and are ineffective after that point. For instance the look of an edit control is very dependent on the value of the [DropDown](tmp/PROP_EDIT_DROPDOWN.htm) and [DropStyle](tmp/PROP_EDIT_DROPSTYLE.htm) properties. A menu is radically different if the [popup](tmp/PROP_MENU_POPUP.htm) style is set. These cannot be changed on the fly once the control exists.

As a consequence of this, these properties will generally be set for a form at design time in the Forms Designer. It is also possible to defer setting styles until the [Create()](tmp/PROP_FORM_CREATE.htm) event as this server side event is triggered before the form is instantiated in the client.

However some few style properties can be changed at runtime. This should be considered a feature of the current client on the current versions of Windows and may not be available in the future. The documentation will say in the summary at the top of the page if the property is design time only (including the Create() event) or available at runtime also. Examples are the generic properties [Enabled](tmp/PROPNUM_ENABLED.htm), [Visible](tmp/PROPNUM_VISIBLE.htm) and [TabStop](tmp/PROPNUM_TABSTOP.htm).

For a comprehensive list of style properties see the [appendix](tmp/styleprops.htm).
