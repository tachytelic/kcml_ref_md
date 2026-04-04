DisplayScreen method

<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> DisplayScreen(Data\$)

This interface allows the display of a form dumped to disk by the [\$ALERT SCREEN](mk:@MSITStore:kcmlrefman.chm::/$ALERT_SCREEN.htm) signal. A program should load the screen definition into a variable and pass it to this method as its argument. The client will then display the form with a special red title bar. DEFSUB 'DumpForm(partno) LOCAL DIM a\$(1), a, h, dir\$256, OBJECT client, z\$1 \$ALERT SCREEN partno \$BREAK -1 dir\$ = ENV("SCREENDIR") IF (dir\$ == " ") THEN dir\$ = "." h = OPEN \$PRINTF("%s/form%d", dir\$, partno) ERROR DO RETURN END DO a = SEEK \#h, END MAT REDIM a\$(1)a a = SEEK \#h, BEG a = READ \#h, a\$() CLOSE \#h OBJECT client = CREATE "ClientCOM", "KClient" client.DisplayScreen(a\$()) KEYIN z\$ OBJECT client = NULL RETURN
