AutoEdit (gridcell control property)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Write<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, AutoEditOff, AutoEditOn, NoEditFixed, ServerEdit)*

**Put cell into edit mode when it gets focus**

\

|  |  |
|----|----|
| Default | The same as AutoEditOff |
| AutoEditOff | Not in AutoEdit mode |
| AutoEditOn | Enables AutoEdit mode for all the cells of the grid |
| NoEditFixed | Enables AutoEdit mode for those cells of the grid that are not fixed |
| ServerEdit | Enables Autoedit mode for the cell and allows the [ServerEdit()](PROP_GRID_SERVEREDIT.htm) event to be triggered |

This property allows a much simpler and more efficient editing mode than the older [EditCell()](PROP_GRID_EDITCELL.htm), [EditRow()](PROP_GRID_EDITROW.htm) and [EditGrid()](PROP_GRID_EDITGRID.htm) methods. It is particularly well suited to data aware grids where the rows represent rows in a database table. If enabled then clicking on a cell will put the row into edit mode allowing the clicked cell to be edited directly. When combined with the [TabThrough](PROP_GRID_TABTHROUGH.htm) and [HideSelection](PROP_GRID_HIDESELECTION.htm) styles, the grid can be made to behave as if it were a collection of edit boxes, as in the example:

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    00010 - DEFFORM Form1()=\
              {.form,.form$,.Style=0x50c000c4,.Width=418,.Height=211,.Text$="Form",.Id=1024},\
              {.ok,.button$,.Style=0x50010001,.Left=363,.Top=6,.Width=50,.Height=14,.Text$="OK",.__Anchor=5,.Id=1},\
              {.cancel,.button$,.Style=0x50010000,.Left=363,.Top=23,.Width=50,.Height=14,.Text$="Cancel",.__Anchor=5,.Id=2},\
              {.Help,.button$,.Style=0x50010000,.Left=363,.Top=44,.Width=50,.Height=14,.Text$="&Help",.__Anchor=5,.Id=9},\
              {.gridControl1,.KCMLgrid$,.Style=0x50013030,.Left=11,.Top=30,.Width=333,.Height=150,.Id=1000,.Rows=8,.Cols=4,.FixedRows=1,.LeftAction=2,.CursorEnable=3,.EditCursor=1},\
              {.editControl1,.kcmldbedit$,.Style=0x50810083,.Left=15,.Top=186,.Width=129,.Height=13,.Id=1001},\
              {.editControl2,.kcmldbedit$,.Style=0x50810080,.Left=157,.Top=187,.Width=50,.Height=13,.Id=1002},\
              {.txtControl1,.static$,.Style=0x50000000,.Left=11,.Top=9,.Width=283,.Height=8,.Text$="This form demonstrates the use of the TabThrough, AutoEdit and HideSelection properties",.Id=1003}
        :     + DEFEVENT Form1.Enter()
        :         FOR c = 1 TO .gridControl1.Cols
        :             IF (c==2)
        :                 .gridControl1.Cell(0,c).CursorEnable = &.Disable
        :             ELSE 
        :                 .gridControl1.Cell(0,c).ColWidth = 72
        :                 a$ = $FMT("(## and ##)",1,c)
        :                 b$ = $FMT("#",c)
        :                 .editControl1.Add(a$,b$)
        :                 IF (c<.gridControl1.Cols)
        :                     REM Cannot go oustide of grid, so do not do int last col.            
        :                     .gridControl1.Cell(0,c).DropAdjust = 50
        :                 END IF
        :                 .gridControl1.Cell(0,c).AutoEdit = &.AutoEditOn
        :             END IF
        :         NEXT c
        :         .editControl1.DropDownFilled = TRUE
        :         REM Insert your code here
        :         c = 3
        :         FOR r = 1 TO .gridControl1.Rows
        :             a$ = $FMT("(## and ##)",r,c)
        :             b$ = $FMT("#",r)
        :             .gridControl1.Cell(0,c).Add(a$,b$)
        :         NEXT r
        :         .gridControl1.Cell(0,c).DropDownFilled = TRUE
        :     END EVENT
        :     + DEFEVENT Form1.gridControl1.LeftClick()
        :         REM Called when the user left clicks on a cell
        :         ..EditGrid(..CursorRow,..CursorCol)
        :     END EVENT
        : FORM END Form1
        : Form1.Open()

The server will be alerted with an [EditRowNotify()](PROP_GRID_EDITROWNOTIFY.htm) event when the user clicks on a new row. This event handler has access to both the previous row, if any, in [CursorRow](PROP_GRID_CROW.htm) and the new row in the [NewRow](PROP_GRID_NEWROW.htm) property so the program can update the old row in the database and take a lock on the new row. The EditRowNotify() event will also trigger when the focus leaves the grid entirely. In this case the **NewRow** property will then be zero so the program can update the database for the row that has been left.

The grid should normally be put into AutoEdit mode using the **NoEditFixed** value as this protects any fixed row or column heading. The **AutoEditOn** value will allow these cells to be edited which may not be desirable.

The **ServerEdit** enumeration allows a finer control over how AutoEdit mode works. Typically an entire grid might be put into Autoedit by applying the NoEditFixed enumeration to the whole control. Individual cells might then have their AutoEdit property set to ServerEdit to allow them to generate a [ServerEdit()](PROP_GRID_SERVEREDIT.htm) event as it becomes the current cell. This event can be used to allow complex processing to take place at that point, typically bringing up a child dialog.

|  |  |
|----|----|
| **Note:** | If a grid is in AutoEdit mode then you must not use the EditCell(), EditRow() and EditGrid() direct editing modes on it. These techniques are mutually exclusive. |

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

The **Default** behaviour of an enumerated gridcell property is to check for an overriding setting using the [prededence rules](../GridCellPrecedence.htm) and if not set elsewhere to use the next setting from the enumeration, in this case **AutoEditOff**.

##### Example:


     .gridcell.AutoEdit = &.Default

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
