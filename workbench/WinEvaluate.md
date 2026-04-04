## Evaluate Window

This window hold a lists of variables or expressions which have been selected for evaluation using a right click [context menu](wbcontext.htm).

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/WinEvaluate.png" data-border="0" alt="Evaluate Window" />

</div>

The variables are displayed in [LIST DIM](mk:@MSITStore:kcmlrefman.chm::/LIST_DIM.htm) format. A 'C' or 'D' is printed before the variable name to indicate whether the variable is common (i.e. declared in a [COM](mk:@MSITStore:kcmlrefman.chm::/COM.htm) statement) or non-common (declared in a [DIM](mk:@MSITStore:kcmlrefman.chm::/DIM.htm) statement). Local variables are prefixed by an 'L'. For arrays and strings the dimensional details are given e.g.


    D MAJOR(8)    1.5,2,0,4,5,19,3.5,0

For numeric scalar variables only the decimal value will be printed. For numeric arrays KCML will print in comma separated decimal as many elements as will fit on the one line status bar. A trailing comma indicates that the list of elements had to be truncated.

For strings and string array elements the strings will be displayed as quoted strings if printable or in HEX() otherwise.


    D MTH_NAME$(12)10   "January","February","March","April","May",
