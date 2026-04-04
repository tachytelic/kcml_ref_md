## Multiple window user interface

The editor debugger is now implemented using an MDI user interface with a number of tiled windows being displayed simultaneously. They can be independently minimized, resized and moved. A new Window menu lists the windows that are active and allows them to be brought to the front, cascaded, tiled or restored to their default.

The **[console window](console_wnd.htm)** is still available but is normally hidden. It can be brought to the front or sent to the back with the TAB key.

The [application window](output_wnd.htm) is an 25x80 or 25x132 screen image used by text mode applications as the /005 device. It is only visible while the program is executing and takes the name of the kclient connection as its title. If you break into the brogram with CTRL-BREAK, or the program stops with an error, then the debugger MDI window will become visible and the application window will be sent to the back though it can be displayed with F4. When in the debugger to indicate that the window is not active its title is changed to DEBUG WINDOW in red. Use F4 again or ESC to dismiss the window.

When you break into a **Form** the form is sent to the back but can be revealed with F4. It will be greyed out and have a DEBUG WINDOW title to indicate that it is inactive but if you click on a control thebrowser window will display the name and details of the control.

There are 3 standard window layouts called [scenes](scene.htm) which can be switched using the toolbar buttons marked A, B and C. These layouts are configurable and persistent.

The available MDI windows are listed in this table. They can also be located in the Workbench using the [View Menu](view_menu.htm).

|  |  |
|----|----|
| [Editor](WinEditor.htm) | This is modal with the [debugger](Debug_mode.htm) window. Only one can be visible depending on the mode of KCML. |
| [Browser](wbbrowser.htm) | This currently has 5 modes, selectable from its own toolbar, for browsing forms, objects, functions, files and options |
| [Current variables](WinCurrentVars.htm) | This is active in the debugger to display the values of the variables on the current line as you step through the program. |
| [Variables](LargeVars.htm) | This can display a string variable or expression in both hex and ascii. It replaces the old Large Variables display |
| [Return Stack](WinReturnStack.htm) | This is active in the debugger to display the RETURN stack dynamically as you step though a program |
| [Evaluate](WinEvaluate.htm) | This displays expressions evaluated with F5, right context menu Evaluate or by entering an expression into the expressions combo box on the toolbar. |
| [Events](WinEvents.htm) | This displays a history of events triggered by a form |
| [List Add](WinListAdd.htm) | This displays the programs currently in memory |
| [Traps](WinTrap.htm) | The currently defined traps are listed in this window. |

You can restore the default layout for the scene, with the child MDI windows tiled to use all the available space in the parent window, by selecting the Revert To Default option from the [Window menu](Window_Menu.htm).
