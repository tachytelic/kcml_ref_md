DescText\$ (kcmledit control property)

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
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Text that will appears in edit's description field**

Text in this proprty is displayed as a description after the main body of text in the control. The description text is hidden when the user edits the text and reshown after the [*validate event*](PROP_KCMLEDIT_VALIDATE.HTM). If the description should change as a result of the user's edits DescText\$ should be updated in the validate event. For example: .form1.editControl1.DescText\$ = "A description"

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
        :         Form1.editControl1.Text$ = "Some Text"
        :         Form1.editControl1.DescText$ = "A description"
        :     END EVENT
        :     + DEFEVENT Form1.editControl1.Validate()
        :         REM Build a string with a description appropriate to what the user entered
        :         Form1.editControl1.DescText$ = "You typed " & """" & Form1.editControl1.ValidateText$ & """"
        :     END EVENT
        : FORM END Form1
        : Form1.Open()
        : $END 

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
