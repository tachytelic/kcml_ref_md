# Keyboard and mouse shortcuts for forms

Forms can be navigated with the TAB (to move to the next control) and SHIFT-TAB (to move to the previous control). It is also possible to jump directly to a control that has an accelerator key. These are combinations of ALT and a letter with the letter to be used being indicated by an underscore in the controls caption. Other keys are summarized in the table

| Key | Purpose |
|----|----|
| RETURN | If there is an default button on the form (usually called OK) then presing RETURN in any control will be the same as clicking that button.  With some text boxes, especially multiline ones, RETURN may be processed locally by the control to move to the next line. |
| Esc | If there is a button with the CANCEL attribute on the form then pressing Esc from within any control will be the same as pressing that key. |
| Enter | The Enter key on the numeric keypad is generally identical to the RETURN key except in text edit boxes and editable grid cells where it will act like TAB |
| CTRL-RETURN | This will allow a newline character to be entered in a text box. |
| ALT-DOWN | In a combo box or a grid cell with an ellipsis this will cause the dropdown list to drop down. |
| SPACE | If focus is on a button then SPACE will action it.  In a listbox or a dropdown list it will select the current entry. |

The CTRL key can be used with a mouse click to copy the contents of a grid thus

| Key | Purpose |
|----|----|
| CTRL right click | A CTRL right mouse click on the fixed row or column of a grid (i.e. a row or column heading) will copy the contents of the grid to the clipboard in a tab separated form |
