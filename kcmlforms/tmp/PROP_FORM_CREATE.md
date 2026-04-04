Create (form control server-side event)

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
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool52.png" data-border="0" width="16" height="15" alt="server-side event icon" /> Server-side Event

**Called before form is created**

This event handler is the only place the various [Duplicate()](PROP_GENERIC_DUPLICATE_2.htm) methods can be called. The [Duplicate()](PROP_GENERIC_DUPLICATE_2.htm) method is the basic method used to duplicate controls onto the form so that forms can be dynamically constructed under program control. See [Dynamic Forms](/DynamicForms.htm) for more details of control duplication.

The Create() event handler is also the only place the [Import()](PROP_FORM_IMPORT.htm) and [EditForm()](PROP_FORM_EDIT.htm) events can be called. These methods can be used to generate a sub form definition as a string which can be stored in a database and then used to add the controls to a form during its Create() event. This technique is described in [User Editable Forms](/UserEditForms.htm).

[Style properties](/tmp/styleprops.htm) which control the look of a control or dialog may be set during this event handler as the controls have yet to be created. Normally these properties are only set at design time. Once the form has been created at the end of this event the style properties are ignored at runtime.

If the form size is set in this event it becomes the design-time size. This means that the user cannot resize the window smaller than this size. If the size is set in the [Enter](PROP_FORM_ENTER.htm) event or later the user may still shrink the form down to its design-time size.

This event handler is called before any other event handlers within the form, i.e. before the forms [Enter()](PROP_FORM_ENTER.htm) event, if it exists.

##### Example:


     DEFEVENT Form1.Create()

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
