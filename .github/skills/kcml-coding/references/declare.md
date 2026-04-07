# KCML $DECLARE — Windows DLL Calls

`$DECLARE` binds a KCML function name to a Windows DLL entry point, allowing direct calls
into Win32 APIs and other DLLs from KCML programs and form event handlers.

---

## Syntax

```kcml
$DECLARE 'FunctionName(param_types) = "DLLEntryPoint"
$DECLARE 'FunctionName(param_types) = ".DLLEntryPoint"    : REM client-side
$DECLARE 'FunctionName(param_types) = "*module.EntryPoint" : REM explicit server/module
```

After declaration, call the function like any KCML subroutine:

```kcml
result = 'FunctionName(arg1, arg2, ...)
'FunctionName(arg1, arg2)    : REM discard return value
```

---

## Prefix Conventions

| Prefix | Meaning |
|--------|---------|
| (none) | Standard DLL — looks in preloaded DLLs |
| `.` | Client-side execution (runs on Windows client, not server) |
| `*module` | Force specific module/server-side execution |

**Important:** Most Windows API calls require `.` prefix to run on the client where the UI is.
Shell operations, file dialogs, clipboard, and environment variables all need `.`.

```kcml
$DECLARE 'sv_shell(INT(),STR(),STR(),STR(),STR(),INT())=".ShellExecute"
$DECLARE 'sv_getenv(STR(),RETURN STR(),INT())=".GetEnvironmentVariableA"
```

---

## Parameter Types

| Type | Description | Use for |
|------|-------------|---------|
| `INT()` | Integer passed by value | Numeric arguments, handles, flags |
| `STR()` | Null-terminated string (trailing spaces stripped) | String arguments, file paths |
| `DIM()` | Raw buffer passed by address | Binary buffers, output byte arrays |
| `RETURN INT()` | Output integer (written by the DLL) | Handle return values |
| `RETURN STR()` | Output string buffer (filled by DLL) | GetWindowText-style output params |

### RETURN STR() — the critical distinction

`RETURN STR()` is for parameters where the DLL **writes into** the buffer (output parameters).
The DLL fills the buffer up to a null terminator; KCML reads the result back automatically.
`RTRIM()` works directly on the result:

```kcml
$DECLARE 'sv_getenv(STR(),RETURN STR(),INT())=".GetEnvironmentVariableA"
DIM sv_tmpdir$260
'sv_getenv("TEMP",sv_tmpdir$,260)
sv_tmpdir$ = RTRIM(sv_tmpdir$)    : REM "C:\Users\Paul\AppData\Local\Temp"
```

**Never use `DIM()` for output string buffers** — `DIM()` passes the raw address but does not
handle the null terminator, resulting in an empty or garbage string.

---

## Preloaded DLLs (no prefix needed)

These DLLs are available without a module prefix:

| DLL | Common functions |
|-----|----------------|
| `USER32` | `MessageBoxA`, `GetFocus`, `GetParent`, `SendDlgItemMessage`, `GetWindowText` |
| `KERNEL32` | `GetEnvironmentVariableA`, `GetTempPathA`, `CopyFileA` |
| `GDI32` | Graphics functions |
| `SHELL32` | `ShellExecuteA` (use `.ShellExecute` for client-side) |
| `ADVAPI32` | Registry functions |
| `GSWDLL32` | Kerridge-specific extensions, `KCMLWriteClipboard` |

---

## Common Declarations (Verified Working)

### ShellExecute — open a file with its default application

```kcml
$DECLARE 'sv_shell(INT(),STR(),STR(),STR(),STR(),INT())=".ShellExecute"
'sv_shell(0,"open",sv_tmp_path$,HEX(00),HEX(00),1)
: REM hwnd=0, verb="open", file=path, params=null, dir=null, show=SW_SHOWNORMAL(1)
```

### GetEnvironmentVariableA — get user's temp folder

```kcml
$DECLARE 'sv_getenv(STR(),RETURN STR(),INT())=".GetEnvironmentVariableA"
DIM sv_tmpdir$260
'sv_getenv("TEMP",sv_tmpdir$,260)
IF sv_tmpdir$ == " " THEN sv_tmpdir$ = "C:\Windows\Temp"
```

Always fall back to a default — the call fails silently if the variable is not set.

### Win16 File I/O — write a temp file

```kcml
$DECLARE 'sv_creat(STR(),INT())="._lcreat"
$DECLARE 'sv_write(INT(),DIM(),INT())="_lwrite"
$DECLARE 'sv_close(INT())="_lclose"

sv_file = 'sv_creat(sv_tmp_path$,0)    : REM returns handle, or -1 on failure
IF sv_file <> -1 THEN DO
    'sv_write(sv_file,buf$,sv_flen)
    'sv_close(sv_file)
END DO
IF sv_file == -1 THEN sv_tmp_path$ = " "   : REM signal failure
```

Note `_lcreat` uses `._lcreat` (dot prefix for client-side) but `_lwrite` and `_lclose` do not.

### KCMLWriteClipboard — copy text to Windows clipboard

```kcml
$DECLARE 'KCMLWriteClipboard(STR())
'KCMLWriteClipboard(STR(buf$,,buf_pos-1))
```

The `STR(buf$,,buf_pos-1)` form passes only the populated portion of the buffer.

### SendDlgItemMessage — select a listbox item by index

```kcml
$DECLARE 'sv_getfocus()="GetFocus"
$DECLARE 'sv_getparent(INT())="GetParent"
$DECLARE 'sv_senddlg(INT(),INT(),INT(),INT(),INT())="SendDlgItemMessage"

sv_hwnd = 'sv_getparent('sv_getfocus())
'sv_senddlg(sv_hwnd,1000,0x0186,sv_found-1,0)
: REM 1000=listbox control ID, 0x0186=LB_SETCURSEL, sv_found-1=0-based index
```

---

## Inline Parameter Expressions

`$DECLARE` function calls do **not** accept complex expressions inline — pre-assign to a LOCAL DIM variable first:

```kcml
REM WRONG — syntax error:
'sv_shell(0,"open",RTRIM(sel_file$) & ".txt",HEX(00),HEX(00),1)

REM CORRECT:
LOCAL DIM sv_fpath$280
sv_fpath$ = RTRIM(sel_file$) & ".txt"
'sv_shell(0,"open",sv_fpath$,HEX(00),HEX(00),1)
```

---

## Where to Declare

`$DECLARE` can appear anywhere before first use — inside a DEFEVENT, inside a DEFSUB,
or at program level. Declaring inside the DEFEVENT or DEFSUB that uses it is cleanest:

```kcml
+ DEFEVENT MyForm.btnOpen.Click()
    $DECLARE 'sv_shell(INT(),STR(),STR(),STR(),STR(),INT())=".ShellExecute"
    'sv_shell(0,"open",sv_tmp_path$,HEX(00),HEX(00),1)
END EVENT
```
