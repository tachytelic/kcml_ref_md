## Return stack dialog

This dialog displays the current position in the subroutine return stack. This is a visual form of the [LIST RETURN](mk:@MSITStore:kcmlrefman.chm::/LIST_RETURN.htm) statement. Note that the return stack is also shown as a permanent MDI window in the debugger scene A. This [return stack window](WinReturnStack.htm) is continuously refreshed as the program executes and may be easier to use than the dialog.

You can see where the current statement is in the program directly from the program text shown in the debug window. However it is often important to know how the program came to be at that point. KCML tracks nested subroutine calls on the return stack and this can be inspected to see which subroutines are active. The List Return option from within the [<u>Window menu</u>](Window_Menu.htm) can be used to display the current return stack contents. The shortcut key CTRL T has the same effect. Each time a subroutine is entered its position is pushed down on this stack. At the bottom of the list is the main program and above it are the first lines of each of the subroutines currently active with the current subroutine at the top. If the main program is the only line in the list then the program was not executing within a subroutine when it was stopped.

The main list box shows the subroutines in the stack with the current routine at the top. A subroutine can be selected by moving the cursor to that line in the list box and pressing RETURN or by double clicking using the mouse. This will cause the main program display to jump to the line within the selected subroutine that calls the next subroutine in the stack.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/TRACEDLG.png" data-align="BASELINE" data-border="0" alt="LIST RETURN dialog" />

In the example above the program is currently executing inside the global routine 'DB_SEARCH_LINPUT_LIST() which was called from 'DB_CSEARCH(), which was called from 'GB_FILE_SEARCH() etc. Routines in a global are prefixed with an '@' sign. To see exactly where the program is in that routine either double click this line in the list box or select it and click the List button. Similarly to see how 'DB_SEARCH_LINPUT_LIST() was called double click the second line and the IDE will display the part of the routine 'DB_CSEARCH() that calls 'DB_SEARCH_LINPUT_LIST().

</div>

If any of the routines have local variables then they can be displayed in LIST DIM format in a child dialog by selecting the routine and clicking the Variables button. If there are no local variables in the selected routine a warning message box will be presented.
