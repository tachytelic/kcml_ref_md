Data Binding in Forms

In KCML6.10, the binding of controls to data was enhanced to provide extra functionality but the original data aware mechanisms continue to work. The changes are to the way the data source is referenced by the form and are to allow for more control at run-time than was previously possible.

Under the old scheme the table browser in the forms editor lists the tables used by the form and it allows the user to expand the tables to see the columns. Column entries may be dragged from the table window onto a form where a dbedit with a label is created. The original list of tables is determined by the [DEFOBJ](mk:@MSITStore:kcmlrefman.chm::/DEFOBJ.htm) statements in the program and the list of columns for each table are determined by reference to the dictionary schemas specified in these DEFOBJ statments.

In the new scheme any [DEFRECORD](mk:@MSITStore:kcmlrefman.chm::/DEFRECORD.htm) can be used to define data awareness, which removes the restriction that data awareness could only be done against database tables and opens it up to allow data aware structures. Each [DEFFORM](mk:@MSITStore:kcmlrefman.chm::/DEFFORM.htm) contains the data sources used for the form as data binding pseudo-controls (this is similar to how colors, fonts and pictures are managed), rather than using separate DEFOBJ statements. Extra bindings for a form can easily be added in the workbench, by dragging a record from the browser window directly onto a DEFFORM statement in the editor window. The forms editor will list the available tables for the form, and controls can be dragged onto the form in the usual manner. The .DataField\$ property of the control is updated by the forms editor to be the names of the field as a string. The label for the control is taken from the comment for the [FLD](mk:@MSITStore:kcmlrefman.chm::/FLD.htm) (this is a REM statement immediately following the FLD statement. The variable to be bound is exposed through the [Bind](tmp/PROP_DATASOURCE_BIND.htm) property of the [DataBind](tmp/DataBind.htm) object and is defaulted to be the same as the name of the record

Programmatically there are several advantages to the new scheme, as the data binding can be now be done dynamically using new variants of the [SetDataField()](tmp/PROP_SETDATAFIELD_CELL.htm) method. Firstly, SetDataField now applies to all data aware controls and not just grid cells. Secondly, instead of passing start and pack formats, SetDataField can also take a single string argument specifying the name of the record and the values are deduced from the DEF RECORD statement. Finally, the data source for a control can now also be defined programmatically, by associating it with a particular data bind control in the same manner as picture items.

##### Examples


    .myControl1.DataBind = &.data_sl_ac_accts
    .myControl1.SetDataField(10, "DATE")
    .myControl1.SetDataField("ACCOUNT_NAME")
    .myGrid1.cell(10,10).SetDataField(10, "DATE")
    .myGrid1.cell(10,10).SetDataField("ACCOUNT_NAME")

##### Working example

This example shows a program with two records used to instantiate two buffers. Both records were dropped onto the form in the forms editor whose table view dialog will display two tables. One table was used to populate an edit group with four dbedits by dragging off the table view and dropping into the edit group. Note how the REM comments assocaited with the FLDs have been used as the label text for the dbedits. The second table is not used and is left as an example to the reader.

To execute this example program in KCML simply click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program.


    REM the main record, note the REMs so we get labels on the form
    DEFRECORD one
    FLD numval = "NUM(7,2)"                     : REM Value
    FLD desc$16                                 : REM Description
    FLD now = "DATE"                            : REM Purchase date
    FLD actual$ = "TS6"                         : REM Transactional timestamp
    END RECORD
    REM the bound buffer for the record
    DIM one$_one
    REM initial values
    FLD(one$.now) = #DATE
    FLD(one$.actual$) = $TIMESTAMP
    FLD(one$.desc$) = "Hello"
    FLD(one$.numval) = 1.345


    REM another record, so we can have a choice
    DEFRECORD two
    FLD price                                   : REM Price
    FLD partno$12                               : REM Part number
    END RECORD
    DIM two$_two

    - DEFFORM BoundForm()={.form,.form$,.Style=0x50c000c4,.Width=405,.Height=251,.Text$="Form",.Id=1024},\
    {.ok,.button$,.Style=0x50010001,.Left=349,.Top=6,.Width=50,.Height=14,.Text$="OK",.__Anchor=5,.Id=1},\
    {.cancel,.button$,.Style=0x50010000,.Left=349,.Top=23,.Width=50,.Height=14,.Text$="Cancel",.__Anchor=5,.Id=2},\
    {.help,.button$,.Style=0x50010000,.Left=349,.Top=44,.Width=50,.Height=14,.Text$="&Help",.__Anchor=5,.Id=9},\
    {.editgroup1,.editgroup$,.Left=37,.Top=28,.Width=280,.Height=134,.Id=1000},\
    {.actual,.kcmldbedit$,.Style=0x50810080,.Left=163,.Top=45,.Width=134,.Height=13,.Id=1001,.EditGroup=.editgroup1,.Label$="Transactional timestamp:",.DataBind=.data_one,.DataField$="actual$"},\
    {.desc,.kcmldbedit$,.Style=0x50810080,.Left=163,.Top=69,.Width=134,.Height=13,.Id=1002,.EditGroup=.editgroup1,.Label$="Description:",.DataBind=.data_one,.DataField$="desc$"},\
    {.now,.kcmldbedit$,.Style=0x50810080,.Left=163,.Top=101,.Width=134,.Height=13,.Id=1003,.EditGroup=.editgroup1,.Label$="Purchase date:",.DataBind=.data_one,.DataField$="now"},\
    {.numval,.kcmldbedit$,.Style=0x50810080,.Left=163,.Top=133,.Width=134,.Height=13,.Id=1004,.EditGroup=.editgroup1,.Label$="Value:",.DataBind=.data_one,.DataField$="numval"},\
    {.data_one,.DataBind$,.Bind=one$,.Record=_one},\
    {.data_two,.DataBind$,.Bind=two$,.Record=_two}
    FORM END BoundForm
    BoundForm.Open()

##### See also:

[Data Aware Forms](DataAwareForms.htm), [DataBind object](tmp/DataBind.htm), [SetDataField()](tmp/PROP_SETDATAFIELD_CELL.htm), [GetDataField()](tmp/PROP_GETDATAFIELD.htm)
