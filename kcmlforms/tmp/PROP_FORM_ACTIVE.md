ActiveControl (form control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Advanced</td>
<td>KCML<br />
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Object property

**Control active at last event**

This object property refers to the control that was active (i.e. had focus) at the time the current event was triggered. You can use it within an event handler and in particular it is very useful within a menu [Select()](PROP_MENU_SELECT.htm) event especially when that selection is linked to a toolbar button. Toolbar buttons and menu selections do not switch focus away from the control that was active when the button was clicked.

Consider the case of a paste feature that updates a controls [.text\$](PROPSTR_TITLE.htm) property. The form might contain lots of grid cells and edit controls. By clicking the toolbar button some text can be pasted into the control. This can be done with a single event handler for the button as in the example which simulates the Cut and Paste features of the Windows clipboard by using a local variable.

To execute the program in KCML simply click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard, switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program. - DEFFORM Form1()={.form,.form\$,.Style=0x50c000c\\ 4,.Width=216,.Height=94,.text\$="Cut and paste wi\\ t\\ hout using clipboard",.Id=1024,.Menu=.mnuControl\\ 1},{.editControl1,.kcmldbedit\$,.Style=0x50810080\\ ,\\ .Left=13,.Top=12,.Width=49,.Height=14,.Id=1000},\\ {.editControl4,.kcmldbedit\$,.Style=0x50810080,.L\\ e\\ ft=90,.Top=12,.Width=49,.Height=14,.Id=1003},{.e\\ ditControl2,.kcmldbedit\$,.Style=0x50810080,.Left\\ =\\ 13,.Top=39,.Width=49,.Height=14,.Id=1001},{.edit\\ Control3,.kcmldbedit\$,.Style=0x50810080,.Left=13\\ ,\\ .Top=66,.Width=49,.Height=14,.Id=1002},{.ok,.but\\ ton\$,.Style=0x50010001,.Left=160,.Top=6,.Width=5\\ 0\\ ,.Height=14,.text\$="OK",.\_\_Anchor=5,.Id=1},{.can\\ cel,.button\$,.Style=0x50010000,.Left=160,.Top=23\\ ,\\ .Width=50,.Height=14,.text\$="Cancel",.\_\_Anchor=5\\ ,.Id=2},{.mnuControl1,.Menu\$,.Id=1004,.file={.te\\ x\\ t\$="File"},.edit={.Flag=144,.text\$="Edit"},.edit\\ cut={.text\$="Cut",.Picture=.Cut,.Select()},.edit\\ p\\ aste={.Flag=128,.text\$="Paste",.Picture=.Paste,.\\ Select()}} LOCAL DIM MyClipboard\$100 - DEFEVENT Form1.mnuControl1.editcut.Select() LOCAL DIM OBJECT a OBJECT a = .form.ActiveControl IF (a.Id \> 10) REM don't clobber buttons MyClipboard\$ = a.text\$ a.text\$ = "" END IF END EVENT - DEFEVENT Form1.mnuControl1.editpaste.Select() LOCAL DIM OBJECT a OBJECT a = .form.ActiveControl IF (a.Id \> 10) REM don't clobber buttons a.text\$ = MyClipboard\$ END IF END EVENT FORM END Form1 Form1.Open()

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
