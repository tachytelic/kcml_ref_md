KCML Constants

Flags for MessageBox()

These constants are flag for the [MessageBox()](../MessageBox.htm) Windows API. This is commonly used in conjunction with [\$DECLARE](../$DECLARE.htm) To check which button was pressed, compare the return value of the **MessageBox()** call with the [Button ID](ButtonIdHelp.htm) constants.

| Constant name         | Value | Description                     |
|-----------------------|-------|---------------------------------|
| \_MB_OK               | 0x000 | OK button                       |
| \_MB_ABORTRETRYIGNORE | 0x002 | Abort, Retry and Ignore buttons |
| \_MB_OKCANCEL         | 0x001 | OK and Cancel buttons           |
| \_MB_RETRYCANCEL      | 0x005 | Retry and Cancel buttons        |
| \_MB_YESNO            | 0x004 | Yes and No buttons              |
| \_MB_YESNOCANCEL      | 0x003 | Yes, No and Cancel buttons      |
| \_MB_ICONEXCLAMATION  | 0x030 | Exclamation icon                |
| \_MB_ICONINFORMATION  | 0x040 | Info icon                       |
| \_MB_ICONQUESTION     | 0x020 | Question mark icon              |
| \_MB_ICONSTOP         | 0x010 | Stop! icon                      |
| \_MB_DEFBUTTON1       | 0x000 | First button is default         |
| \_MB_DEFBUTTON2       | 0x100 | Second button is default        |
| \_MB_DEFBUTTON3       | 0x200 | Third button is default         |

Back to list of [Constants](constindex.htm)
