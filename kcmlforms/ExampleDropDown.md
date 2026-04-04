Example Program - Using a dropdown with an Edit Control

------------------------------------------------------------------------

This example shows the use of tagging in the dropdown listbox of a KCML edit control. The edit box is set up to 3 letter edit country codes but when populating the listbox with the [.Add()](tmp/PROP_ECOMBO_ADDTAG.htm) method the descriptive name of the country is supplied as a tag. This allows the control to display the description next to the code to make its meaning more obvious. As the code is changed the client will consult the contents of the lisbox to get the corresponding descriptive text. As a side effect of using listbox tags, the user is limited to only entering codes from the list.

When the form was created in the Forms Designer the following design time attributes were set on the edit controls to allow a list box.

|                                              |             |
|----------------------------------------------|-------------|
| [.DropDown](tmp/PROP_EDIT_DROPDOWN.htm)      | DropEnabled |
| [.DropStyle](tmp/PROP_EDIT_DROPSTYLE.htm)    | DropDown    |
| [.SortedListBox](tmp/PROP_EDIT_SORTLIST.htm) | TRUE        |

There are two controls on this form to illustrate the issues associated with prefilling the listbox when the form is created versus filling it on demand. The first is filled in the [Enter()](tmp/PROP_FORM_ENTER.htm) event and the second is filled by the controls [DropDown()](tmp/PROP_KCMLEDIT_DROPEVENT.htm) event being triggered by the user clicking the down arrow or pressing ALT-DOWN. In general it is better to fill only on demand, particularly with large lists, as this makes the initial display of the form more snappy. Often a user will not need to see the listbox and filling in advance would be a waste of bandwidth.

However if you do fill on demand this means that the descriptive text is unavailable when the form is first drawn and the second edit box looks incomplete compared to the first. If you press OK to move to the second example you will see that this time the initial value for the control was prefilled at the Enter() event but the rest of the list was deferred. To make sure the default was not added twice the 'Fill() routine clears out the list with a [.Delete()](tmp/PROP_ECOMBO_RESET.htm) method.

This example fills the listbox from text in the program but a real world example would probably load this from a database table.

Note that this example uses [labels](tmp/PROP_EDIT_EDITLABEL.htm) and [edit groups](IntroEditGroup.htm).

To execute the program in KCML simply click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program.

\- DEFFORM Form1()={.form,.form\$,.Style=0x50c000c\\ 4,.Width=264,.Height=118,.Id=1024},{.ok,.button\$\\ ,\\ .Style=0x50010001,.Left=209,.Top=6,.Width=50,.He\\ ight=14,.text\$="OK",.\_\_Anchor=5,.Id=1},{.editCon\\ t\\ rol1,.kcmldbedit\$,.Style=0x50810882,.Left=87,.To\\ p=31,.Width=100,.Height=12,.Id=1000,.EditGroup=.\\ e\\ ditgroup1,.label\$="Prefilled:"},{.editControl2,.\\ kcmldbedit\$,.Style=0x50810882,.Left=89,.Top=66,.\\ W\\ idth=100,.Height=12,.Id=1001,.EditGroup=.editgro\\ up1,.label\$="Filled on drop:"},{.editgroup1,.Edi\\ t\\ Group\$,.Left=11,.Top=9,.Width=186,.Height=98} LOCAL DIM OBJECT a + DEFEVENT Form1.Enter() REM first box, prefilled OBJECT a = .editControl1 'Fill(OBJECT a) .editControl1.text\$ = "E" REM 2nd box, filled only if listbox dropdown req\\ uested IF (fix) .editControl2.Add("Spain", "E") END IF .editControl2.text\$ = "E" REM set the title .form.text\$ = "KCML edit dropdown example - " & \\ (fix == 0 ? "1st" : "2nd") & " attempt" END EVENT + DEFEVENT Form1.editControl2.DropDown() OBJECT a = .editControl2 'Fill(OBJECT a) END EVENT + DEFEVENT Form1.cmdbutton1.Click() END EVENT FORM END fix = FALSE Form1.Open() fix = TRUE Form1.Open() END DEFSUB 'Fill(OBJECT a) REM populate the edit box a.Delete() a.Add("Belgium", "B") a.Add("United States", "US") a.Add("Spain", "E") a.Add("France", "F") a.Add("United Kingdom", "UK") a.DropDownFilled = TRUE END SUB
