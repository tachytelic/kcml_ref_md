## Code Menu

<img src="bitmaps/VarContext.png" data-border="0" data-align="MIDDLE" alt="Context menu for variable" />\
\

The default in this case is **Evaluate** so you can click again or press RETURN to get the same effect as the old right double click.

The options on the menu are

|  |  |
|----|----|
| Evaluate | This will display the value of the variable or expression in the Evaluate Window (in [LIST DIM](mk:@MSITStore:kcmlrefman.chm::/LIST_DIM.htm) format for variable). This is usually the default so you can click again or press RETURN to get the same effect as the old right double click. |
| Select expression | This will just select the expression displaying it in reverse. It has the same effect as F5. KCML will attempt to match the whole expression by looking for the closing bracket for functions like STR( |
| Modify | This is only available for variables or expressions that are legal on the left hand side of LET statements. It displays a modify dialog box showing the current value and allowing a new value to be entered. If you OK this dialog the variable is modified and a line is written to the output window confirming it. |
| Trap variable | This will set a breakpoint on the variable. Execution will stop if the variable is modified. |
| Display variable | For string variables only this will bring up the [Display Variable](LargeVars.htm) window showing the contents of the string. This is particularly useful for large string variables. |
| Select line | This will select the whole statement (one line on the screen) containing the item you clicked. |
| Suggest | This brings up a [suggestions](wbsuggestion.htm) popup menu containing variables that have the same stem as the selected variable, allowing auto-completion. You can also trigger this with ALT-DOWN |
| Help | This will display an appropriate help page if used with a KCML keyword. It can also display application help for DEFSUB functions if a suitable file has been registered. See the page on [documentation](Documentation.htm) for more information on how this works. |
| Revisit | If you have jumped to this part of the program as a result of [actioning](Objects_and_actions.htm) then this will return you to the previous location just like the F6 [revisit](Revisting.htm) key. |
| Evaluate sym | This Evaluates the sym value. |
| Run From | This will attempt to run the program from the mouse position. This will perform some checks to see if the program is in a safe state to run from here. |
| Load into Foreground | This will determine the src file component for the current line in a module, load the src file into the foreground and place the cursor at the same code point as in the module. This option does not clear out the current foreground first and so the programs are merged. This is suitable for development where components of modules are routinely loaded into the foreground. This option only works for modules built using the [kc6](mk:@MSITStore:kcmlrefman.chm::/kmake.htm) utility and not those built with SAVE . |
| CLEAR P; Load into Foreground | As above, except that a [CLEAR P](mk:@MSITStore:kcmlrefman.chm::/clear.htm) is executed before the src file component is loaded into the foreground. |

[Context Menus](wbcontext.htm)
