Appearance (tabbed control property)

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
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, Invisible, LikeGroup, Wizard)*

**Controls tab appearance**

The **Appearance** property can be used to alter the appearance of tab control to be used for wizards or as a convenient method of grouping controls on a form.

|  |  |
|----|----|
| Default | This is the classic tab control appearance. |
| Invisible | The tab control container itself is invisible but the embedded controls for the curent page remain visible. There is no user navigation and pages have to be switched under program control. This is convenient in the case where, depending on the state of a form, certain sets of controls may appear in the same place. This is particularly convenient at form design time. |
| LikeGroup | This is similar to invisible, except that a group box is drawn around the border of the tab control with the title taken from the title of the currently displayed tab page. |
| Wizard | This uses the pages of the tab control to form a wizard display. Two buttons appear at the bottom of the screen for "Back" and "Next" (the actual text will depend on the current locale). On the last page "Next" is replaced by "Finish" and the [Finish()](PROP_TABBED_FINISH.htm) event will be triggered if this button is clicked. On the first page the "Back" button is disabled. On any page, the "Next" / "Finish" button can be disabled or re-enabled by using the [DisableNext](PROP_TABBED_DISABLENEXT.htm) property. |

An example demonstrating the various tab appearances is available.

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    00010 REM Tab test
        : - DEFFORM Form1()=\
              {.form,.form$,.Style=0x50c000c4,.Width=316,.Height=124,.Text$="Form",.Id=1024},\
              {.ok,.button$,.Style=0x50010001,.Left=260,.Top=6,.Width=50,.Height=14,.Text$="OK",.__Anchor=5,.Id=1},\
              {.cancel,.button$,.Style=0x50010000,.Left=260,.Top=23,.Width=50,.Height=14,.Text$="Cancel",.__Anchor=5,.Id=2},\
              {.tabControl1,.tabbed$,.Style=0x500100c0,.Left=15,.Top=11,.Width=210,.Height=94,.Id=1000,.Tab1=\
              {.Text$="Groupbox"},.Tab2=\
              {.Text$="Tab"},.tab3=\
              {.Text$="Tab"},.tab4=\
              {.Text$="Tab"}},\
              {.Default,.radio$,.Style=0x50010004,.Left=243,.Top=58,.Width=57,.Height=13,.Text$="DefaultTabs",.Id=1001,.State=1,.ButtonGroup=.tabstyle},\
              {.Invisible,.radio$,.Style=0x50010004,.Left=243,.Top=72,.Width=50,.Height=13,.Text$="Invisible",.Id=1006,.ButtonGroup=.tabstyle},\
              {.LikeGroup,.radio$,.Style=0x50010004,.Left=243,.Top=86,.Width=50,.Height=13,.Text$="LikeGroup",.Id=1007,.ButtonGroup=.tabstyle},\
              {.Wizard,.radio$,.Style=0x50010004,.Left=243,.Top=100,.Width=50,.Height=13,.Text$="Wizard",.Id=1017,.ButtonGroup=.tabstyle},\
              {.grpControl1,.groupbox$,.Style=0x50000007,.Left=233,.Top=49,.Width=75,.Height=71,.Text$="Groupbox",.Id=1008},\
              {.editControl1,.kcmldbedit$,.Style=0x50810080,.Left=13,.Top=22,.Width=50,.Height=13,.Parent=.tabControl1,.Page=.Tab1,.Id=1002},\
              {.rbControl1,.radio$,.Style=0x50010004,.Left=7,.Top=17,.Width=50,.Height=13,.Text$="Radio",.Parent=.tabControl1,.Page=.Tab2,.Id=1003},\
              {.gridControl1,.KCMLgrid$,.Style=0x50010030,.Left=13,.Top=18,.Width=91,.Height=50,.Parent=.tabControl1,.Page=.tab3,.Id=1004,.Rows=2,.Cols=2,.FixedRows=1},\
              {.cbControl1,.checkbox$,.Style=0x50010002,.Left=20,.Top=70,.Width=133,.Height=10,.Text$="CHECK TO ENABLE NEXT BUTTON",.Parent=.tabControl1,.Page=.tab3,.Id=1009},\
              {.rtfControl1,.richedit$,.Style=0x50a11044,.Left=9,.Top=18,.Width=193,.Height=69,.Parent=.tabControl1,.Page=.tab4,.Id=1005}
        :     + DEFEVENT Form1.Enter()
        :     END EVENT
        :     + DEFEVENT Form1.Default.Click()
        :         REM Called when a radio button is selected
        :         .tabControl1.Appearance = &.Default
        :     END EVENT
        :     + DEFEVENT Form1.Invisible.Click()
        :         REM Called when a radio button is selected
        :         .tabControl1.Appearance = &.Invisible
        :     END EVENT
        :     + DEFEVENT Form1.LikeGroup.Click()
        :         REM Called when a radio button is selected
        :         .tabControl1.Appearance = &.LikeGroup
        :     END EVENT
        :     + DEFEVENT Form1.Wizard.Click()
        :         REM Called when a radio button is selected
        :         .tabControl1.Appearance = &.Wizard
        :     END EVENT
        :     + DEFEVENT Form1.tabControl1.Finish()
        :         REM Called when Finish button on Wizard style tabs is clicked
        :         + DEFFORM FinishForm()=\
              {.form,.form$,.Style=0x50c000c4,.Width=134,.Height=67,.Text$="Form",.Id=1024},\
              {.ok,.button$,.Style=0x50010001,.Left=42,.Top=38,.Width=50,.Height=14,.Text$="OK",.__Anchor=5,.Id=1},\
              {.txtControl1,.static$,.Style=0x50000000,.Left=39,.Top=14,.Width=55,.Height=15,.Text$="Finished",.Id=1000,.Font=.BigBold}
        :         FORM END FinishForm
        :         FinishForm.Open()
        :     END EVENT
        :     + DEFEVENT Form1.tabControl1.Tab1.Enter()
        :         REM Insert your code here
        :         .tabControl1.DisableNext = FALSE
        :     END EVENT
        :     + DEFEVENT Form1.tabControl1.Tab2.Enter()
        :         REM Insert your code here
        :         .tabControl1.DisableNext = FALSE
        :     END EVENT
        :     + DEFEVENT Form1.tabControl1.tab3.Enter()
        :         REM Insert your code here
        :         .tabControl1.DisableNext = 1-.cbControl1.State
        :     END EVENT
        :     + DEFEVENT Form1.tabControl1.tab4.Enter()
        :         REM Insert your code here
        :         .tabControl1.DisableNext = FALSE
        :     END EVENT
        :     + DEFEVENT Form1.cbControl1.Click()
        :         REM Called when the used clicks on the checkbox
        :         .tabControl1.DisableNext = 1-..State
        :     END EVENT
        : FORM END Form1
        : Form1.Open()
        : REM Character test "Hello", 'Hello', < >

##### Example:


     .tabControl.Appearance = &.Default

##### See also:

Other [tabbed](tabbed.htm) properties, methods and events, [tabbeditem](tabbeditem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
