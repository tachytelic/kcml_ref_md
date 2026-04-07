# $DECLARE 'MessageBox (Windows API)

> Example of using `$DECLARE` to call the Windows `MessageBox` API to display a dialog.

## Description

`MessageBox` is a common Win32 API function that displays a dialog with a message and buttons (OK, Cancel, Yes/No, etc.). In KCML 6.0 KClient, the call is intercepted and the parent window handle is always replaced by the top-most form — so passing `0` for the parent is safe.

KClient also recognises `Ctrl+BREAK` during a MessageBox call (though the Workbench does not appear until the box is dismissed).

## Declaration and use

```kcml
$DECLARE 'MessageBox(INT(), STR(), STR(), INT())
DIM _MB_OK = 16
'MessageBox(0, "This message box appears properly", "Application", _MB_OK)
```

## Common MB_ constants

| Constant | Value | Buttons |
|----------|-------|---------|
| `MB_OK` | 0 | OK |
| `MB_OKCANCEL` | 1 | OK, Cancel |
| `MB_YESNO` | 4 | Yes, No |
| `MB_YESNOCANCEL` | 3 | Yes, No, Cancel |
| `MB_ICONERROR` | 16 | (adds error icon) |
| `MB_ICONQUESTION` | 32 | (adds question icon) |
| `MB_ICONWARNING` | 48 | (adds warning icon) |

Add icon flags to button flags: `DIM _QUERY = 4 + 32` = Yes/No with question icon.

## Return values

| Value | Meaning |
|-------|---------|
| 1 | OK |
| 2 | Cancel |
| 6 | Yes |
| 7 | No |

## Notes

- Windows client only (`$DECLARE` calls are executed on the client).
- In KCML 6.0+ KClient, the `hwnd` (first) parameter is always replaced by the top-most form — pass `0`.
- For cross-platform dialog, consider using KCML forms with `DEFFORM` instead.

## See Also

- `$DECLARE` — declare an external (Win32 / DLL) function
- `DEFFORM` — KCML GUI forms
