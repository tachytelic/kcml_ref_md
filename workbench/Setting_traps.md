## Setting breakpoints

A breakpoint or [TRAP](mk:@MSITStore:kcmlrefman.chm::/TRAP.htm) may be set on any statement or variable within the foreground or currently selected global program. A breakpoint on a statement can be set by double clicking with the mouse in the left hand margin by the statement to be trapped. The presence of a breakpoint is signified by a red circle in the left margin of the source line. Clicking this way acts as a toggle so you can remove an existing breakpoint by clicking again. Alternatively the *Toggle breakpoint* key ('B', available only in debug mode) can be used if a mouse is not available. Traps can also be set using the [Trap menu](Trap_menu.htm).

A trap on a variable is set by selecting the variable and either bringing up a right click [context menu](wbcontext.htm) or selecting the *Select Trap on Variable* option from within the [<u>Trap menu.</u>](Trap_menu.htm) Like normal traps this option works as a toggle, therefore attempting to trap a variable a second time removes the trap.

All traps can be removed with the *Clear All Traps* option from within the [<u>Trap menu</u>](Trap_menu.htm).

Currently defined traps are displayed in the [trap window](WinTrap.htm). This allows editing and deleting of these traps. In particular you can add conditions to a trap using the [trap dialog](trap.htm) which can be invoked from this window.

Traps can also be set and deleted with the [TRAP](mk:@MSITStore:kcmlrefman.chm::/TRAP.htm) immediate mode statement in the [console window](console_wnd.htm). Only traps set this way will remain in position through successive program loads. Breakpoints set in the workbench are inserted into a copy of the code and will be lost if the program line is dropped or replaced following a LOAD.
