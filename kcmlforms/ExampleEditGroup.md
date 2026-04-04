Example Program - Using label\$ and edit groups

The following program contains three edit controls placed in a container. It is the same form that was created in the [Working with Edit Groups page](FormsDesignerWorkingWithEditGroups.htm). The text of the third control is set in the Enter() event and can be changed at runtime by clicking the 'click me' button. Here is the form at design time:

<img src="bitmaps/EditGroupFD.png" data-border="0" alt="An edit group container containing 3 edit controls in the forms designer" />

And here it is at run time. Notice how the size of the largest KCML edit control had to be clipped to accommodate the long label text and still stay within the edit group container.

<img src="bitmaps/EditGroupRun.png" data-border="0" alt="An edit group container containing 3 edit controls at runtime" />

To execute the program in KCML simply click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program.


    - DEFFORM Form1()={.form,.form$,.Style=0x50c000c\
    4,.Width=295,.Height=129,.Text$="Edit group exam\
    ple",.Id=1024},{.ok,.button$,.Style=0x50010001,.\
    Left=239,.Top=6,.Width=50,.Height=14,.Text$="OK"\
    ,.__Anchor=5,.Id=1},{.cancel,.button$,.Style=0x5\
    0010000,.Left=239,.Top=23,.Width=50,.Height=14,.\
    Text$="Cancel",.__Anchor=5,.Id=2},{.help,.button\
    $,.Style=0x50010000,.Left=239,.Top=44,.Width=50,\
    .Height=14,.Text$="Click me",.__Anchor=5,.Id=9,.\
    Click()},{.editgroup1,.EditGroup$,.Left=18,.Top=\
    12,.Width=195,.Height=97,.Style=0x50010000},{.ed\
    itControl1,.kcmldbedit$,.Style=0x50810080,.Left=\
    66,.Top=22,.Width=109,.Height=15,.Id=1000,.EditG\
    roup=.editgroup1,.Label$="A very much longer lab\
    el:"},{.editControl2,.kcmldbedit$,.Style=0x50810\
    080,.Left=66,.Top=49,.Width=138,.Height=15,.Id=1\
    001,.EditGroup=.editgroup1,.Label$="Short label:\
    "},{.editControl3,.kcmldbedit$,.Style=0x50810080\
    ,.Left=66,.Top=82,.Width=31,.Height=15,.Id=1002,\
    .EditGroup=.editgroup1,.Label$="Testiing:"}
    - DEFEVENT Form1.Enter()
    .editControl3.Label$ = "This was set at Enter() \
    time:"
    END EVENT
    - DEFEVENT Form1.help.Click()
    .editControl3.Label$ = "This was set at run time\
    :"
    END EVENT
    FORM END Form1
    Form1.Open()
