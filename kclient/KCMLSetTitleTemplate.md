KCMLSetTitleTemplate(text\$)

This function sets a title template to be used on all subsequent top level forms taking precedence over the normal [.form.text\$](mk:@MSITStore:kcmlforms.chm::/tmp/PROPSTR_TITLE.htm) title. The template can contain tokens which will be replaced by strings.

| Token | Replacement string |
|----|----|
| %T | The forms proper title |
| %H | The server hostname, blank if a local connection |
| %S | The connection manager service, blank if not connected through the CM |
| %U | The userid used to connect to the server, blank if a local connection |

Setting a blank or empty string will disable the template and subsequent titles will be shown unmodified. If the template is changed with this function, it will take effect with the opening of the next top level form or on the next change of the title of the current top level form by setting its .text\$ property.

Syntax

\$DECLARE 'KCMLSetTitleTemplate(STR())

Returns

This function returns TRUE on success, or FALSE on failure due to lack of client memory.

Example

The title of all forms will be modified to append the current company selected in a multicompany accounting system. Note the %% to protect the % in [\$PRINTF](mk:@MSITStore:kcmlrefman.chm::/$PRINTF.htm).

\$DECLARE 'KCMLSetTitleTemplate(STR()) t\$ = \$PRINTF("%%T - Company %d", company_no) 'KCMLSetTitleTemplate(t\$)

Sample program

To see a complete program illustrating this function, click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard, then switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program.

\$DECLARE 'KCMLSetTitleTemplate(STR()) DIM rc - DEFFORM Form1()={.form,.form\$,.Style=0x50c000c\\ 4,.Width=276,.Height=130,.Text\$="Original title"\\ ,.Id=1024},{.ok,.button\$,.Style=0x50010\\ 001,.Left=220,.Top=6,.Width=50,.Height=14,.Text\$\\ ="OK",.\_\_Anchor=5,.Id=1},{.Cancel,.button\$,.Styl\\ e=0x50010000,.Left=220,.Top=23,.Width=5\\ 0,.Height=14,.Text\$="Cancel",.\_\_Anchor=5,.Id=2},\\ {.Help,.button\$,.Style=0x50010000,.Left=206,.Top\\ =82,.Width=63,.Height=14,.Text\$="&Reset\\ title",.\_\_Anchor=4,.Id=9},{.cmdButton1,.button\$\\ ,.Style=0x50010000,.Left=206,.Top=106,.Width=63,\\ .Height=14,.Text\$="&Set template",.\_\_An\\ chor=4,.Id=1000,.Click()},{.editControl1,.kcmldb\\ edit\$,.Style=0x50810080,.Left=20,.Top=83,.Width=\\ 153,.Height=13,.\_\_Anchor=2,.Id=1001},{.\\ editControl2,.kcmldbedit\$,.Style=0x50810080,.Lef\\ t=20,.Top=106,.Width=153,.Height=13,.\_\_Anchor=2,\\ .Id=1002},{.textControl1,.static\$,.Styl\\ e=0x50000000,.Left=15,.Top=12,.Width=189,.Height\\ =67,.Text\$="Click Reset Title to change the titl\\ e programmatically.....Click SetTemplat\\ e to use a template. Use %T to insert title tex\\ t. A blank template will revert.....When you cl\\ ick OK a second form will appear and th\\ e template should persist into it.",.Id=1003},{.\\ frameControl1,.groupbox\$,.Style=0x50000007,.Left\\ =8,.Top=3,.Width=203,.Height=71,.Id=100\\ 4} + DEFEVENT Form1.Enter() REM fill in the defaults .editControl1.Text\$ = .form.Text\$ .editControl2.Text\$ = "%T - template active" END EVENT + DEFEVENT Form1.Help.Click() REM set title programmatically .form.Text\$ = .editControl1.Text\$ END EVENT + DEFEVENT Form1.cmdButton1.Click() REM set template 'KCMLSetTitleTemplate(.editControl2.Text\$) END EVENT FORM END Form1 rc = Form1.Open() REM prove it persists + DEFFORM Form2()={.form,.form\$,.Style=0x50c000c\\ 4,.Width=216,.Height=94,.Text\$="Second form",.Id\\ =1024},{.ok,.button\$,.Style=0x50010001,\\ .Left=160,.Top=6,.Width=50,.Height=14,.Text\$="OK\\ ",.\_\_Anchor=5,.Id=1},{.Cancel,.button\$,.Style=0x\\ 50010000,.Left=160,.Top=23,.Width=50,.H\\ eight=14,.Text\$="Cancel",.\_\_Anchor=5,.Id=2},{.He\\ lp,.button\$,.Style=0x50010000,.Left=160,.Top=44,\\ .Width=50,.Height=14,.Text\$="&Reopen th\\ is",.\_\_Anchor=5,.Id=9,.Click()},{.textControl1,.\\ static\$,.Style=0x50000000,.Left=21,.Top=15,.Widt\\ h=123,.Height=63,.Text\$="Any template s\\ hould have persisted into this form.....You can \\ use the Reopen button to open this form again as \\ a child of this one. The template sho\\ uld NOT persist into this form...",.Id=1000} + DEFEVENT Form2.Help.Click() REM open a child form Form2.Open() END EVENT FORM END IF (rc) Form2.Open() END IF
