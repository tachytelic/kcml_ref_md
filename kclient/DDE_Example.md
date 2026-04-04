DDE client example

This example shows the use of DDE to drive MS Word and MS Excel via their (orioginal) macro languages. This is an historic example as the preferred way to drive these applications today in Office 97 or Office 2000 would be to use Automation and VBA scripts.

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    00010 REM Requires at least MS Word 6 & Excel 5
        : REM Copyright Kerridge Computer Company Ltd., 1995-1999
        : REM EMail kcml@kerridge.com
        : DIM MB_OK=1,MB_ICONEXCLAMATION=48,MB_ICONQUESTION=32
        : DIM MB_YESNO=4,IDYES=6,IDNO=7
        : DIM title$256,edit$256,command$256,x$(1)1
        : DIM text$256
        : REM Create initial dialog
        : - DEFFORM Form1()=\
              {.form,.form$,.Style=0x50c000c4,.Width=342,.Height=159,.Text$="DDE demo",.Id=1024},\
              {.cancel,.button$,.Style=0x50010000,.Left=271,.Top=7,.Width=68,.Height=28,.Text$="Cancel",.__Anchor=5,.Id=2},\
              {.btnExcel,.button$,.Style=0x50010000,.Left=19,.Top=12,.Width=93,.Height=29,.Text$="&Excel",.Id=1000,.Click()},\
              {.btnWord,.button$,.Style=0x50010000,.Left=23,.Top=118,.Width=93,.Height=29,.Text$="&Word",.Id=1001,.Click()},\
              {.txtControl1,.static$,.Style=0x50000000,.Left=20,.Top=69,.Width=109,.Height=15,.Text$="Enter some text for Word:",.Id=1002},\
              {.editWordText,.kcmldbedit$,.Style=0x50810080,.Left=21,.Top=93,.Width=303,.Height=13,.Id=1003}
        :     + DEFEVENT Form1.btnExcel.Click()
        :         'exceldemo()
        :     END EVENT
        :     + DEFEVENT Form1.btnWord.Click()
        :         'worddemo(.editWordText.Text$)
        :     END EVENT
        : FORM END Form1
        : Form1.Open()
        : END
        : DEFSUB 'ExcelDemo()
        : REM First attempt to load Excel. If DDELoad fails, then Quit
        : ret = 'kcmlddeload("excel","excel.exe")
        : IF (ret)
        :     'messagebox(0,"An error occurred attempting to load Excel.","Error",mb_ok+mb_iconexclamation)
        :     RETURN
        : END IF
        : REM Now attempt to open a DDE conversation with Excel
        : xldde = 'kcmlddeopen("excel","sheet1")
        : IF (xldde==0) THEN DO
        :     'messagebox(0,"Unable to start a DDE conversation with Excel!","Error",mb_ok+mb_iconexclamation)
        :     RETURN
        : END DO
        : REM Maximise Excel
        : 'kcmlddeexec(xldde,"[APP.MAXIMIZE]")
        : FOR row = 1 TO 3
        :     FOR col = 1 TO 9
        :         STR(a$,,2) = HEX(0000)
        :         STR(b$,,2) = HEX(0000)
        :         PRINTUSING TO a$, "R#C#",row,col
        :         PRINTUSING TO b$, "###",RND(1)*100
        :         'kcmlddepoke(xldde,STR(a$,3,4),STR(b$,3,3))
        :     NEXT col,row
        : REM Close DDE conversation with Excel worksheet
        : 'kcmlddeclose(xldde)
        : xldde = 'kcmlddeopen("excel","system")
        : IF (xldde==0) THEN DO
        :     'messagebox(0,"Error starting DDE conversation with Excel System","Error",mb_ok+mb_iconexclamation)
        :     RETURN
        : END DO
        : REM Excel Macro Commands START
        : REM Select the figures we downloaded
        : 'kcmlddeexec(xldde,"[SELECT(""R1C1:R3C9"")]")
        : REM The $BREAKs are here so that you can see whats happening
        : $BREAK -1
        : REM Open a new chart window showing the selected figures           
        : 'kcmlddeexec(xldde,"[NEW(2,1)]")
        : $BREAK -1
        : REM Format the chart to be a 3D bar chart
        : 'kcmlddeexec(xldde,"[FORMAT.MAIN(8,4,,50,0,0,0,,50,100,0,0,1)]")
        : $BREAK -1
        : REM Copy the 3D chart into the Clipboard
        : 'kcmlddeexec(xldde,"[COPY()]")
        : $BREAK -1
        : REM Bring Excel to the foreground
        : 'kcmlddeexec(xldde,"[APP.ACTIVATE]")
        : $BREAK -1
        : REM Maximise the chart window within Excel
        : 'kcmlddeexec(xldde,"[WINDOW.MAXIMIZE]")
        : $BREAK -1
        : REM Close all open windows without saving data and Quit Excel
        : 'kcmlddeexec(xldde,"[FILE.CLOSE(0)]")
        : 'kcmlddeexec(xldde,"[FILE.CLOSE(0)]")
        : $BREAK -1
        : REM Shut Excel down
        : 'kcmlddeexec(xldde,"[QUIT]")
        : REM Excel Macro Commands END
        : REM Close conversation with Excel
        : 'kcmlddeclose(xldde)
        : REM Now load the Windows Clipboard viewer to confirm the chart has been copied across
        : 'winexec("clipbrd",1)
        : RETURN
        : DEFFN 'WordDemo(edit$)
        : REM Now we need to load Word and paste in the chart
        : ret = 'kcmlddeload("winword","winword.exe")
        : IF (ret)
        :     'messagebox(0,"Error attempting to load Word","Error",mb_ok+mb_iconexclamation)
        :     RETURN
        : END IF
        : worddde = 'kcmlddeopen("winword","document1")
        : IF (worddde==0) THEN DO
        :     'messagebox(0,"Unable to start DDE conversation with Word!","Error",mb_ok+mb_iconexclamation)
        :     RETURN
        : END DO
        : REM Word for Windows Macro Commands - START
        : REM Insert text on first line and para marker
        : 'kcmlddeexec(worddde,"[Insert ""Here are the February sales figures for the new Widget...""]")
        : 'kcmlddeexec(worddde,"[InsertPara]")
        : REM Insert next line
        : 'kcmlddeexec(worddde,"[Insert ""This graph was imported from Excel via the Clipboard""]")
        : 'kcmlddeexec(worddde,"[InsertPara]")
        : REM Insert text from edit control
        : command$ = "[Insert " & HEX(22) & edit$ & HEX(22) & "]"
        : 'kcmlddeexec(worddde,command$)
        : 'kcmlddeexec(worddde,"[InsertPara]")
        : REM Text in Arial, bold, italic, 24pts
        : 'kcmlddeexec(worddde,"[Font ""Arial"", 24]")
        : 'kcmlddeexec(worddde,"[Bold 1]")
        : 'kcmlddeexec(worddde,"[Italic 1]")
        : 'kcmlddeexec(worddde,"[Insert ""This text in Arial, bold, italic at 24pts""]")
        : 'kcmlddeexec(worddde,"[ResetChar]")
        : 'kcmlddeexec(worddde,"[InsertPara]")
        : REM Copy Clipboard contents into document and resize
        : 'kcmlddeexec(worddde,"[EditPaste]")
        : 'kcmlddeexec(worddde,"[CharLeft 1,1]")
        : 'kcmlddeexec(worddde,"[FormatPicture .SetSize = 0, .CropLeft = ""0 cm"", .CropRight = ""0 cm"", .CropTop = ""0 cm"", .CropBottom = ""0 cm"", .ScaleX = ""50%"", .ScaleY = ""50%"", .SizeX = ""10.94 cm"", .SizeY = ""4.68 cm""]")
        : REM Add border around frame
        : 'kcmlddeexec(worddde,"[FormatBordersAndShading .FromText = """", .ApplyTo = 1, .Shadow = 1, .TopBorder = 4, .LeftBorder = 4, .BottomBorder = 4, .RightBorder = 4, .HorizBorder = - 1, .VertBorder= - 1]")
        : REM Centre picture on page
        : 'kcmlddeexec(worddde,"[CenterPara]")
        : REM Print the document (Remove the following REM if required)
        : REM   'KCMLDdeexec(worddde, "[FilePrintDefault]")
        : REM Save the document
        : 'kcmlddeexec(worddde,"[FileSaveAs .Name = ""c:\test.doc"", .Format = 0, .LockAnnot = 0, .Password = """"]")
        : REM Word for Windows Macro Commands - END
        : REM Close DDE conversation with Word
        : 'kcmlddeclose(worddde)
        : RETURN
        : REM The following are the $DECLARE statements required  for this demo
        : $DECLARE 'KCMLDdeInit()
        : $DECLARE 'KCMLDdeLoad(STR(),STR())
        : $DECLARE 'KCMLDdeOpen(STR(),STR()) TO INT(4)
        : $DECLARE 'KCMLDdeClose(INT(4))
        : $DECLARE 'KCMLDdeDestroy()
        : $DECLARE 'KCMLDdeExec(INT(4),STR())
        : $DECLARE 'KCMLDdePoke(INT(4),STR(),STR())
        : $DECLARE 'WinExec(STR(),INT())
        : $DECLARE 'MessageBox(INT(),STR(),STR(),INT())
