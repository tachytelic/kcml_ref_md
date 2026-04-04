Duplicate (generic control method)

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
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Duplicate(int, int) Method

**Duplicate control**

|      |                                            |
|------|--------------------------------------------|
| Int1 | The horizontal position of the new control |
| Int2 | The vertical position of the new control   |

This method is used within the [*Create()* event handler to duplicate a control to a new location on the current form. The parameters specify the new location of the control relative to the top left hand corner of the form. The optional string parameter allows the controls label to be changed, this is only relevant to controls that have text labels such as buttons and static text controls.](PROP_FORM_CREATE.htm)

The method returns a [sym](PROPNUM_SYM.htm) pointer to the newly created control to allow the program to later reference the controls properties and methods.

For example, the following duplicates the control *editControl1* and then modifies the controls properties: newsym = .editControl1.Duplicate(10, 25) .\*newsym.Type\$ = "N-8.3" .\*newsym.Text\$ = Total

If the new control has a [.Text\$](PROPSTR_TITLE.htm) property this can be set using a third argument as in [Duplicate(int, int, str).](PROP_GENERIC_DUPLICATE_3.htm)

The Duplicate() method can also be used to create new tab pages and add controls to those pages; see the tab control [Duplicate(str)](PROP_TABBED_DUPLICATE.htm) method and the generic [Duplicate(int, int, str, int)](PROP_GENERIC_DUPLICATE_4.htm) method

The Duplicate() method can also be used to duplicate menu options including child menus and separators. For details on how to do this see the menu methods [Duplicate(str)](PROP_MENU_DUPLICATE.htm), [Duplicate()](PROP_MENU_DUPLICATE_SEP.htm) and [Duplicate(str, int)](PROP_MENU_DUPLICATE_CHILD.htm).

The method can also be used to create a picture object on the fly. Because picture objects are an abstraction and not actually part of the form, in this one case it is possible to use the Duplicate() method at run time after the Create() event. To see an example program demonstrating creating a picture, simply click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard. Then switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program. This example uses a specific filename that may not work on your system. - DEFFORM Form1()={.form,.form\$,.Style=0x50c000c\\ 4,.Width=330,.Height=228,.Text\$="Form",.Id=\\ 1024},{.ok,.button\$,.Style=0x50010001,.Left=275,\\ .Top=6,.Width=50,.Height=14,.Text\$="OK",.\_\_\\ Anchor=5,.Id=1},{.cancel,.button\$,.Style=0x50010\\ 000,.Left=275,.Top=23,.Width=50,.Height=14,\\ .Text\$="Cancel",.\_\_Anchor=5,.Id=2},{.help,.butto\\ n\$,.Style=0x50010000,.Left=275,.Top=44,.Wid\\ th=50,.Height=14,.Text\$="&Help",.\_\_Anchor=5,.Id=\\ 9},{.gridControl1,.kcmlgrid\$,.Style=0x50010\\ 030,.Left=18,.Top=22,.Width=230,.Height=178,.Id=\\ 1000,.Rows=2,.Cols=2,.FixedRows=1,.Row1={.R\\ ow=1,.Col=0,.RowHeight=82},.Row2={.Row=2,.Col=0,\\ .RowHeight=66},.Col1={.Row=0,.Col=1,.ColWid\\ th=80},.Col2={.Row=0,.Col=2,.ColWidth=84}},{.pic\\ Control1,.Picture\$,.Template=1} + DEFEVENT Form1.Create() END EVENT - DEFEVENT Form1.help.Click() a = .picControl1.Duplicate(0, 0) .\*a.Filename\$ = "d:/winnt/winnt.bmp" .gridControl1.Cell(2, 1).Picture = SYM(\*a) END EVENT FORM END Form1 Form1.Open()

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
