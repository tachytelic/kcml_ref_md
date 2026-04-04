## Inspecting variables

To inspect the value of a variable point the simplest way is just to hold the mouse cursor over it to invoke a [tooltip](wbtooltips.htm). You can also put the mouse cursor on it in the debug window and click the right mouse button to bring up a [context menu](wbcontext.htm). This has an Evaluation option and a [Display Variable](LargeVars.htm) option for strings only. If you chose Evaluate, by just clicking again or by pressing RETURN, the variable name will be copied to the [Evaluate Window](WinEvaluate.htm) and a [LIST DIM](mk:@MSITStore:kcmlrefman.chm::/LIST_DIM.htm) operation executed upon it.

In this window A 'C' or 'D' is printed before the variable name to indicate whether the variable is common (i.e. declared in a [COM](mk:@MSITStore:kcmlrefman.chm::/COM.htm) statement) or non-common (declared in a [DIM](mk:@MSITStore:kcmlrefman.chm::/DIM.htm) statement). Local variables are prefixed by an 'L'. For arrays and strings the dimensional details are given e.g.


    D MAJOR(8)    1.5,2,0,4,5,19,3.5,0

For numeric scalar variables only the decimal value will be printed. For numeric arrays KCML will print in comma separated decimal as many elements as will fit on the one line in the window. A trailing comma indicates that the list of elements had to be truncated.

For strings and string array elements the strings will be displayed as quoted strings if printable or in HEX() otherwise. Characters above HEX(80) are not considered printable unless byte 50 of [\$OPTIONS RUN](mk:@MSITStore:kcmlrefman.chm::/$OPTIONS_RUN.htm) is set to indicate a non-English locale.


    D MTH_NAME$(12)10   "January","February","March","April","May",

Some string variables may be too large to fit in the single line of the evaluate window. By pressing CTRL-F2 with the cursor under the variable, or by right clicking the variable to get a [context menu](wbcontext.htm) and picking the display variable option, then a popup window showing the variable will appear. See [Large variable dialog](LargeVars.htm).
