Simple XML parsing in KCML

KCML has a built in XML 1.0 non-validating parser based on version 1.0 of James Clark's [Expat](http://www.jclark.com/xml/expat.html) which can build a tree from XML supplied either in a file ([XML_OPEN](tmp/XML_OPEN.htm)) or in a string buffer ([XML_PARSE_BUFFER](tmp/XML_PARSE_BUFFER.htm)). A program can then traverse the tree from top to bottom by calling [XML_NEXT](tmp/XML_NEXT.htm) repeatedly to get the next element together with its value and any attributes.

Advantages

- It is simple to use as it flattens the XML document into a simple table that can be tranversed.
- It was supported in KCML 5.02 and 6.00.

Disadvantages

- This built in parser will read the entire document into an internal memory based data structure on the first XML_NEXT call. This can take some time and may use a lot of memory if the document is large. Very big documents may be better processed with SAX2 using [Xerces](mk:@MSITStore:kcmlrefman.chm::/xerces.htm).
- It can't be used to construct or modify a document. This requires a DOM based parser like [Xerces](mk:@MSITStore:kcmlrefman.chm::/xerces.htm).
- It does not handle non-Unicode encodings properly. Only the certain [encodings](#encodings) are recognized.
- It will load a DTD if requested allowing it to access external definitions but it does not validate against it.

Encodings

<span id="encodings"></span>

Data returned by the parser in XML_NEXT is always [Unicode](mk:@MSITStore:kcmlrefman.chm::/TutorialUnicode.htm) expressed as UTF-8 and it can reformat other encodings or subsets of Unicode into UTF-8. The parser recognizes the following encoding in the initial \<? xml ?\> tag.

<div class="indent">

|            |
|------------|
| ISO-8859-1 |
| US-ASCII   |
| UTF-8      |
| UTF-16     |
| UTF-16BE   |
| UTF-16LE   |

</div>

If no encoding attribute is given then the parser will try to autodetect UTF-16 and if not detected it will assume the document is in UTF-8. An error will be thrown if the data is not compatible with the declared or presumed encoding.

Note that ISO-8859-1 is the same as Latin-1 and almost identical to Windows 1252 however the Euro symbol € is at 0x0080 rather than 0x20AC. Latin-1 is default encoding for KCML 5.x and 6.00. UTF-8 is the default encoding for KCML 6.10 and above.

Example:

This example shows parsing XML and building a tree control displaying the values. You can either parse a file or parse the contents of the clipboard. An example XML fragment is included below to test this feature.

To execute the program in KCML simply click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program.



    XMLform.Open()
    END
    - DEFFORM XMLform()={.form,.form$,.Style=0x50c000c4,.Width=316,.Height=255,.Text$="XML tree example",.Id=1024},       {.editControl1,.kcmldbedit$,.Style=0x50810080,.Left=48,.Top=7,.Width=196,.Height=13,.Id=1001,.EditGroup=.editgroup1,.Label$="&File:"}, {.cmdButton1,.button$,.Style=0x50010001,.Left=263,.Top=2,.Width=50,.Height=23,.Text$="&Open",.Id=1003,.Type=9,.Click()}, {.cmdButton2,.button$,.Style=0x50012000,.Left=263,.Top=40,.Width=50,.Height=23,.Text$="&Parse from clipboard",.Id=1004,.Click()}, {.cancel,.button$,.Style=0x50010000,.Left=263,.Top=78,.Width=50,.Height=23,.Text$="Close",.__Anchor=5,.Id=2}, {.treeControl1,.tree$,.Style=0x50810007,.Left=9,.Top=32,.Width=235,.Height=203,.Id=1000},          {.editgroup1,.EditGroup$,.Left=9,.Top=2,.Width=253,.Height=26,.Id=1002},{.textControl1,.static$,.Style=0x50000000,.Left=9,.Top=241,.Width=297,.Height=9,.Id=1005,.Font=.Bold}
        + DEFEVENT XMLform.cmdButton1.Click()
            REM parse from file
            LOCAL DIM s,h
            CALL XML_OPEN .editControl1.Text$ TO s,h
            IF (s==0) THEN 'parsetree(h)
        END EVENT
        + DEFEVENT XMLform.cmdButton2.Click()
            REM parse from clipboard
            LOCAL DIM s,h,clipsize,a$1
            clipsize = 'kcmlgetclipboardlength()
            MAT REDIM a$clipsize+1
            'kcmlreadclipboard(a$,clipsize)
            CALL XML_PARSE_BUFFER SYM(a$) TO s,h
            IF (s==0) THEN 'parsetree(h)
        END EVENT
    FORM END

    DEFSUB 'ParseTree(h)
    LOCAL DIM s,level,last,parent,s1,root
    LOCAL DIM a$(1),v$(1),name$,value$,buf$128,x(20),x,i
    .treeControl1.Delete()
    REM get the root
    CALL XML_NEXT h,SYM(name$),SYM(value$),SYM(a$()),SYM(v$()) TO s,x
    IF (s==0)
        parent = .treeControl1.Add(name$,1)
        root = parent
        last = 0
        x = 1
        REM now the tree
        WHILE s==0 DO
            CALL XML_NEXT h,SYM(name$),SYM(value$),SYM(a$()),SYM(v$()) TO s,level
            IF (s==0)
                REM build string with value and any attributes
                buf$ = name$
                IF (value$<>" ")
                    buf$ = buf$ & " (" & value$ & ")"
                END IF
                IF (DIM(a$(),1)>0)
                    FOR i = 1 TO DIM(a$(),1)
                        buf$ = & " " & a$(i)
                        IF (DIM(v$(),1)>=i) THEN buf$ = & "=""" & v$(i) & """"
                    NEXT i
                END IF
                SELECT CASE TRUE
                CASE level==x
                    REM sibling
                CASE level>x
                    REM child
                    parent = last
                CASE ELSE
                    REM back up the stack
                    REPEAT
                        parent = .treeControl1.Item(parent).Parent
                    UNTIL  --x==level
                END SELECT
                last = .treeControl1.Item(parent).Add(buf$,0)
                x = level
            END IF
        WEND
    ELSE IF (s==40)
        LOCAL DIM errcode,errtext$100,row,col,offset
        REM parsing error
        CALL XML_ERROR h TO s,errcode,errtext$,row,col,offset
        .textControl1.Text$ = $PRINTF("ERROR: %s at row %d, column %d",errtext$,row,col)
    END IF
    REM display top level
    IF (root) THEN .treeControl1.Item(root).Expand()
    CALL XML_CLOSE h TO s1
    END SUB

    $DECLARE 'KCMLGetClipboardLength()
    $DECLARE 'KCMLReadClipboard(RETURN STR(),INT())



    To put some example XML into the clipboard click here.  You can use the clipboard option in the program to parse this.



    <?xml version='1.0'?>
    <!-- This file represents a fragment of a book store inventory database -->
    <bookstore>
      <book genre="autobiography">
        <title>The Autobiography of Benjamin Franklin</title>
        <author>
          <first-name>Benjamin</first-name>
          <last-name>Franklin</last-name>
        </author>
        <price>8.99</price>
      </book>
      <book genre="novel">
        <title>The Confidence Man</title>
        <author>
          <first-name>Herman</first-name>
          <last-name>Melville</last-name>
        </author>
        <price>11.99</price>
      </book>
      <book genre="philosophy">
        <title>The Gorgias</title>
        <author>
          <name>Plato</name>
        </author>
        <price>9.99</price>
      </book>
    </bookstore>
