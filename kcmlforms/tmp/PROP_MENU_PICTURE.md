Picture (menuitem control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Indexed property

**Specifies the toolbar picture for the menu item**

The picture property is used to add an image to a menu item. These images appear as a toolbar when the form is displayed. The toolbar buttons generate the same events as the corresponding menu items. Menu items that are disabled are displayed as disabled toolbar buttons, and menu items that are not visible have invisible toolbar buttons as well. The toolbar buttons have separators placed between items on separate pull-down menus. A large number of stock pictures are available including many for standard operations such as Open, Save, Cut, Copy and Paste. The pictures should ideally be 16x16 images, as they are scaled to this size anyway. The mask color is gray meaning that any part of the picture that is grey will be drawn in the default button face color. On a standard windows setup this is also gray, but many users have their own preferences.

Note that the picture properties must be set either at design time with the Forms Designer or dynamically during the Enter() event. The toolbar is created after the Enter() event but prior to the Show() event and does not change after that. The picture must be specified before the toolbar can be created.

In KCML 6.10 an option was added to the menu editor of KForm, labelled "First toolbar icon". Those menu items that have this option checked appear out of order on the toolbar menu as they always appear first. The intention here is for an Exit menu item which on a typcial form will appear as the last item on the first (usually called "File") menu. Normally this leaves the Exit toolbar icon after other icons, but by checking this option the Exit toolbar icon can be made to consistently appear first (and hence always in the same place) across all forms.

An example demonstrating a menu with a toolbar is available.

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    00010 - DEFFORM Form1()=\
              {.form,.form$,.Style=0x50c000c4,.Width=216,.Height=92,.Text$="Form",.Id=1024,.Menu=.menu1},\
              {.ok,.button$,.Style=0x50010001,.Left=160,.Top=6,.Width=50,.Height=14,.Text$="OK",.__Anchor=5,.Id=1},\
              {.cancel,.button$,.Style=0x50010000,.Left=160,.Top=23,.Width=50,.Height=14,.Text$="Cancel",.__Anchor=5,.Id=2},\
              {.help,.button$,.Style=0x50010000,.Left=160,.Top=44,.Width=50,.Height=14,.Text$="&Help",.__Anchor=5,.Id=9},\
              {.menu1,.Menu$,.Id=1000,.file=\
              {.Flag=16,.Text$="&File"},.filenew=\
              {.Text$="&New",.Key=19970,.Picture=.filenew},.fileopen=\
              {.Text$="&Open",.Key=20226,.Picture=.fileopen},.filesave=\
              {.Flag=128,.Text$="&Save",.Key=21250,.Picture=.filesave},.edit=\
              {.Flag=144,.Text$="&Edit"},.editcut=\
              {.Text$="&Cut",.Key=22530,.Picture=.Cut},.editcopy=\
              {.Text$="C&opy",.Key=17154,.Picture=.Copy},.editpaste=\
              {.Flag=128,.Text$="&Paste",.Key=22018,.Picture=.Paste}},\
              {.txtControl1,.static$,.Style=0x50000000,.Left=10,.Top=67,.Width=50,.Height=9,.Text$="Last command:",.Id=1001},\
              {.Last,.static$,.Style=0x50000000,.Left=71,.Top=67,.Width=50,.Height=9,.Text$="<None>",.Id=1002},\
              {.PasteEnabled,.checkbox$,.Style=0x50010002,.Left=10,.Top=22,.Width=59,.Height=10,.Text$="Paste enabled",.Id=1003},\
              {.PasteVisible,.checkbox$,.Style=0x50010002,.Left=10,.Top=38,.Width=53,.Height=10,.Text$="Paste Visible",.Id=1004}
        :     + DEFEVENT Form1.Enter()
        :         REM Insert your code here
        :         .menu1.editpaste.Visible = .PasteEnabled.State
        :         .menu1.editpaste.Enabled = .PasteVisible.State
        :     END EVENT
        :     + DEFEVENT Form1.menu1.filenew.Select()
        :         .Last.Text$ = "New"
        :     END EVENT
        :     + DEFEVENT Form1.menu1.fileopen.Select()
        :         .Last.Text$ = "Open"
        :     END EVENT
        :     + DEFEVENT Form1.menu1.filesave.Select()
        :         .Last.Text$ = "Save"
        :     END EVENT
        :     + DEFEVENT Form1.menu1.editcut.Select()
        :         .Last.Text$ = "Cut"
        :     END EVENT
        :     + DEFEVENT Form1.menu1.editcopy.Select()
        :         .Last.Text$ = "Copy"
        :     END EVENT
        :     + DEFEVENT Form1.menu1.editpaste.Select()
        :         .Last.Text$ = "Paste"
        :     END EVENT
        :     + DEFEVENT Form1.PasteEnabled.Click()
        :         .menu1.editpaste.Enabled = ..State
        :     END EVENT
        :     + DEFEVENT Form1.PasteVisible.Click()
        :         .menu1.editpaste.Visible = ..State
        :     END EVENT
        : FORM END Form1
        : Form1.Open()

##### Example:


     .menuitem.Picture

##### See also:

Other [menuitem](menuitem.htm) properties, methods and events, [menu](menu.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
