Cache\$ (picture control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Cached object property

**Specifies the cached server file name of the picture file**

Specifies the full server name of the [picture object](/PicObjects.htm) used by a KCML picture control. This property is the same as the [*Filename\$* property except that filename used with *cache\$* should point to a picture file on the server rather than on the client. In general *.cache\$* should be used in preference to *.filename\$* to centralize the pictures in one place on the server.](PROP_PICTURE_NAME.htm)

On first reference the client will automatically download the picture from the server and cache it locally so that future executions of the program need not copy the file over the network to the client. The picture is identified in the cache with a signature which depends on its last modification time and a hash of its contents so that if the picture is updated on the server a fresh copy will be sent to the client when the picture is next referenced. Note that this signature is computed only once per picture per form instance and so if the picture is updated on the fly while a form is presented, it is not sufficient to set the .cache\$ property reduntantly a second time in some form event handler; you must either close and reopen the form or use a different filename as the value of the .cache\$ property.

Picture controls can be assigned to the form background, picture button controls, tree nodes and grid cells.

From KCML version 5.03 onwards it is possible to put environment variables in the cache filename. These are expanded at the server end to determine where the picture is located. e.g. "\$PICTURE/menu/menu1.bmp". All sequences of a \$ followed by alphanumeric characters up the the next '/' or the end of the filename are replaced by the value of the environment variable or an empty string if the variable is not defined. .Picture1.Cache\$ = "../PictureFiles/BackGround.WMF" .Picture2.Cache\$ = "\$PICTURE/logo.jpg"

Here is an example program demonstrating the use of server pictures which can be pasted from the clipboard into a Workbench session. Don't be confused by the fact that the names are PC filenames as it is intended to be run against a Windows server. If you have some pictures on a Unix server then run against that and specify a Unix filename.

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    00010 - DEFFORM Form1()=\
              {.form,.form$,.Style=0x50c000c4,.Width=275,.Height=154,.Text$="Server picture demo",.Id=1024},\
              {.picButton1,.picbutton$,.Style=0x5001000b,.Left=44,.Top=62,.Width=138,.Height=81,.Text$="Click me to set the filename ",.Id=1000,.Picture=.picUserPic},\
              {.editControl1,.kcmldbedit$,.Style=0x50810892,.Left=80,.Top=14,.Width=188,.Height=14,.Id=1001,.DropDownFilled=1},\
              {.cancel,.button$,.Style=0x50010000,.Left=217,.Top=122,.Width=50,.Height=14,.Text$="Close",.__Anchor=5,.Id=2},\
              {.txtControl1,.static$,.Style=0x50000000,.Left=4,.Top=15,.Width=62,.Height=11,.Text$="Server &Filename:",.Id=1002},\
              {.picUserPic,.Picture$,.Cache$="dummy"}
        :     + DEFEVENT Form1.Enter()
        :         REM default filename if Windows server
        :         IF (STR($MACHINE,,1)=="N")
        :             LOCAL DIM buf$(1)32,count,path$100
        :             path$ = ENV("WINDIR") & "/*.BMP"
        :             CALL KI_DIR path$,1,"N",32,-SYM(buf$()) TO count
        :             count = ABS(count)
        :             i = 1
        :             WHILE i<=count DO
        :                 .editControl1.Add(buf$(i++))
        :             WEND
        :             .editControl1.DropDownFilled = TRUE
        :             .editControl1.Text$ = buf$(1)
        :         END IF
        :     END EVENT
        :     + DEFEVENT Form1.picButton1.Click()
        :         REM set pic object to use the server filename     
        :         .picUserPic.Cache$ = ENV("WINDIR") & "/" & .editControl1.Text$
        :         .picButton1.Picture = &.picUserPic
        :     END EVENT
        : FORM END Form1
        : Form1.Open()
        : $DECLARE 'FindFirst()

##### See also:

Other [picture](picture.htm) properties, methods and events and [generic](generic.htm) properties and methods.
