Delete (listitem control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Delete() Method

**Used to delete this item**

This method can be used to delete the listbox item object to which it is applied e.g. this program populates a listbox then deletes all the selected items.

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    00010 - DEFFORM Form1()=\
              {.form,.form$,.Style=0x50c000c4,.Width=216,.Height=94,.text$="Listboxes as objects",.Id=1024},\
              {.ok,.button$,.Style=0x50010001,.Left=160,.Top=6,.Width=50,.Height=14,.text$="OK",.__Anchor=5,.Id=1},\
              {.cancel,.button$,.Style=0x50010000,.Left=160,.Top=23,.Width=50,.Height=14,.text$="&Populate",.__Anchor=5,.Id=1004,.Type=9},\
              {.Help,.button$,.Style=0x50012000,.Left=160,.Top=44,.Width=50,.Height=23,.text$="&Delete selected",.__Anchor=5,.Id=1003,.Type=9},\
              {.listControl1,.ListBox$,.Style=0x50a1018b,.Left=18,.Top=12,.Width=97,.Height=70,.Id=1000,.Selection=1},\
              {.textControl1,.static$,.Style=0x5000000c,.Left=127,.Top=71,.Width=85,.Height=20,.Id=1001}
        :     LOCAL DIM _MAXSEL = 10
        :     + DEFEVENT Form1.cancel.Click()
        :         REM populate
        :         LOCAL DIM i
        :         .listControl1.Delete()
        :         FOR i = 1 TO _maxsel
        :             .listControl1.Add($FMT("##",i))
        :         NEXT i
        :         .textControl1.text$ = .listControl1.ListCount
        :     END EVENT
        :     + DEFEVENT Form1.Help.Click()
        :         REM drop selected items from listbox
        :         LOCAL DIM OBJECT c,OBJECT n
        :         OBJECT c = .listControl1.SelectedFirst
        :         WHILE OBJECT c <> NULL DO
        :             OBJECT n = c.SelectedNext
        :             c.Delete()
        :             OBJECT c = n
        :         WEND
        :         .textControl1.text$ = .listControl1.ListCount & "/" & .listControl1.SelCount
        :     END EVENT
        :     + DEFEVENT Form1.listControl1.Click()
        :         LOCAL DIM a$(_MAXSEL)2,b$100,i,x
        :         REM show selected indices
        :         a$() = .listControl1.multiindex$
        :         i = 1
        :         WHILE i<=.listControl1.SelCount DO
        :             $UNPACK(F=HEX(E002)) a$(i) TO x
        :             IF (i==1)
        :                 b$ = $PRINTF("%d",x)
        :             ELSE
        :                 b$ = b$ & $PRINTF(",%d",x)
        :             END IF
        :             i++ 
        :         WEND
        :         REM show total/selected counts
        :         .textControl1.text$ = .listControl1.ListCount & "/" & .listControl1.SelCount & HEX(0D0A) & "(" & b$ & ")"
        :     END EVENT
        : FORM END
        : Form1.Open()

##### Example:


     .listitem.Delete()

##### See also:

Other [listitem](listitem.htm) properties, methods and events, [listbox](listbox.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
