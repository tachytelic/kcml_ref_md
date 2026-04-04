Description (kcmledit control property)

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
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**The control text can be given a tab-separated description**

If set to *TRUE* the edit control will treat a tab in its text as a flag that subsequent text should be displayed as a description. If the user edits the text the description is removed and only the body text is returned in the [ValidateText\$](PROP_KCMLEDIT_VALIDATETEXT.htm) property. It is the responsibility of the application to then reset the [Text\$](PROPSTR_TITLE.htm) property with the new text and description as required. For example: .form1.editControl1.Text\$ = "Some Text" & HEX(09) & "A description"

An example demonstrating an edit control with a description is available.

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    00010 DIM a$100
        : - DEFFORM Form1()=\
              {.form,.form$,.Style=0x50c000c4,.Width=270,.Height=49,.Text$="Form",.Id=1024},\
              {.ok,.button$,.Style=0x50010001,.Left=215,.Top=6,.Width=50,.Height=14,.Text$="OK",.__Anchor=5,.Id=1},\
              {.cancel,.button$,.Style=0x50010000,.Left=215,.Top=23,.Width=50,.Height=14,.Text$="Cancel",.__Anchor=5,.Id=2},\
              {.editControl1,.kcmldbedit$,.Style=0x50812080,.Left=9,.Top=14,.Width=179,.Height=13,.Id=1000,.Type$="S15",.Validate()}
        :     + DEFEVENT Form1.Show()
        :         REM Initialise text    
        :         Form1.editControl1.Text$ = "Some Text" & HEX(09) & "A description"
        :     END EVENT
        :     + DEFEVENT Form1.editControl1.Validate()
        :         REM Build a string with a description appropriate to what the user entered
        :         a$ = Form1.editControl1.ValidateText$ & HEX(09) & "You typed " & """" & Form1.editControl1.ValidateText$ & """"
        :         Form1.editControl1.Text$ = a$
        :     END EVENT
        : FORM END Form1
        : Form1.Open()
        : $END 

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
