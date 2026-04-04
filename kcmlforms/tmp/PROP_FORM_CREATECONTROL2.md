CreateControl (form control method)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Advanced</td>
<td>KCML<br />
6.20+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> CreateControl(int, int, OBJECT, OBJECT) Method

**Create control in the Create event, placing it after the specified control in the tab order**

The CreateControl() method allows controls to be created dynamically during the [Create()](/tmp/PROP_FORM_CREATE.htm) event. The result is an object reference to the new control.

### Parameters

##### Control type

This is the type of control to create. Any of the standard controls can be created using the prefefined constants. Refer to [Constants](mk:@MSITStore:kcmlrefman.chm::/tmp/ControlHelp.htm) for a list of constants.

##### Style

This is used to modify the style of the control. The style is dependent on the type of control. For most controls, either \_STYLE_NORMAL or \_STYLE_NOTABSTOP should be used, but see the comments below. For the style contants, refer to [Constants](mk:@MSITStore:kcmlrefman.chm::/tmp/StyleHelp.htm).

##### Group

To allow events to be handled, all create controls must belong to a group defined in the DEF FORM itself. These groups can be created in the Forms Designer using the "Make Peristent Group ..." menu option. (The group must be persistent as the Forms Designer will remove redundant groups, and if all controls in the group are to be dynamic, then the group may appear to be redundant). The argument here should be an OBJECT representation of the control. If no events are required then you can pass OBJECT NULL here.

##### After

This parameter is optional and may be omitted completely - it was not available in the original implementation of CreateControl. It is used to specify the control on the form after which the new control will appear in the tab order. If NULL or omitted then the new control will appear at the end.

### Specific Controls

#### DBEdit

Create using \_CREATE_DBEDIT

Use styles of \_STYLE_DBEDIT, \_STYLE_DBEDIT_DROPDOWN and \_STYLE_DBEDIT_ELLIPSIS to create the three most common forms of dbedit.

#### Tab control

Create using \_CREATE_TABBED

The style of \_STYLE_NORMAL should be used. Each page of the tab control is created using [CreateTabPage()](/tmp/PROP_TABBED_CREATE.htm). Controls can be added to the created tab pages using the [AddControl()](/tmp/PROP_TABBED_ADDCONTROL.htm) method.


    OBJECT TabControl = .form.CreateControl(_CONTROL_TABBED, _STYLE_NORMAL, OBJECT Group)
    OBJECT FrontPage = TabControl.CreateTabPage("&Main Details");
    OBJECT EditName = .form.CreateControl(_CONTROL_DBEDIT, _STYLE_DBEDIT, OBJECT EditGroup)
    REM Fill in EditName.Left, EditName.Top etc.
    FrontPage.AddControl(EditName);
    OBJECT ContactPage = TabControl.CreateTabPage("&Contacts")

#### Menu control

Create using \_CREATE_MENU

To create a menu for the whole form, use \_STYLE_MAIN_MENU, and set the Menu property of the form to the created menu. Add top-level menu items to the created menu using [CreateMenuItem()](/tmp/PROP_MENU_CREATE.htm) and add sub menu items to these using [CreateMenuItem()](/tmp/PROP_MENUITEM_CREATE.htm).


    OBJECT MainMenu = .form.CreateControl(_CONTROL_MENU, _STYLE_MAIN_MENU, OBJECT MenuGroup)
    OBJECT .form.Menu = MainMenu
    OBJECT FileMenu = MainMenu.CreateMenuItem("&File")
    OBJECT NewFile = FileMenu.CreateMenuItem("&New")
    OBJECT EditMenu = MainMenu.CreateMenuItem("&Edit")

To create a popup menu use \_STYLE_POPUP_MENU instead.

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
