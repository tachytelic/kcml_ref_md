## Debugger features

The workbench debugger functions much the same as the KCML5 debugger though there are some useful new features that improve useability.

- When debugging the workbench displays multiple windows showing the code as before, the current [return stack](WinReturnStack.htm), an [event log](WinEvents.htm) and a [current variable window](WinCurrentVars.htm) which shows changed variables are you step through the code.
- [Tool tipping](wbtooltips.htm) can be used to see the value of a variable or expression by hovering the mouse cursor.
- The [browser](wbbrowser.htm) window, displayed when editing, is also available while debugging and can be used for navigation and inspection.
- An [evaluate window](WinEvaluate.htm) shows variables that get evaluated by left double clicking. It also acts as a log showing traps as they fire.
- There is now a [trap window](WinTrap.htm) to view and edit traps without having to use [LIST TRAP](mk:@MSITStore:kcmlrefman.chm::/LIST_TRAP.htm). Breaking may now be conditional on an expression being met (the expression may be any expression that can be used in an IF statement). The trap editor also includes a display expression evaluator. This takes anything that may be used in a print statement, including print separators such as ',' and ';'. Each time the trap is reached these expressions are evaluated. If desired execution can continue always, break always, or break only when the specified condition is met.
- Traps set in the workbench are implemented differently to traps set by the [TRAP](mk:@MSITStore:kcmlrefman.chm::/TRAP.htm) statement. In the workbench the actual code is modified temporarily when a trap is set. This permits faster, more reliable execution, especially in expanded/collapsed code. However traps set this way do not persist across a [LOAD](mk:@MSITStore:kcmlrefman.chm::/LOAD.htm). If you need to set a trap that will always break on a particular line whatever the program then you need to use the TRAP statement set in the console window.
- Events are logged in a new [Events window](WinEvents.htm).
- Events with handlers can be trapped using the [context menu](wbcontext.htm) for the event in the forms browser.
- There is a [toolbar](toolbar.htm#debug) with common debugging operations attached to buttons.
- Debugger colors are now the same as the editor colors except that the debugger has a different background color (a light pink by default). Lines with breakpoint are marked with a red spot in the margin rather than the whole line being colored as in the previous debugger.
- A new [spy mode](FormSpy.htm) for forms allows the properties of any control on the form to be inspected. Only those properties which have been altered are listed.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/debugger.png" data-border="0" alt="A typical debugger window (scene A)" />

</div>
