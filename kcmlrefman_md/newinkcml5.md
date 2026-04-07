# What's New in KCML 5

> Summary of major new features introduced in KCML 5.

## Client-server architecture

KCML 5 on Windows runs with the same client-server model as Unix: the KCML execution engine is separate from the presentation layer. Presentation is handled by **KClient**, a TCP/IP-based client that connects to the KCML process. Client and server can be on the same machine or different machines.

A **KCML Service Manager** on Windows NT manages incoming KClient connections, starts KCML sessions, manages ODBC server sessions, and can auto-start global library partitions at boot.

## GUI Forms

Forms provide a graphical front end for KClient users. A form is a KCML `DEFFORM` object containing controls (buttons, list boxes, grids, edit boxes, OCX controls).

- Forms are defined with `DEFFORM` statements; edited with the `KFORM32` graphical editor.
- Controls have **properties** (inspected/set with dot notation, e.g. `.AccountCode.Text$`).
- Controls generate **events** (`.Click()`, `.Enter()`, `.Exit()`), handled by `DEFEVENT` subroutines.
- The Object Browser (`Ctrl-F` in the editor) shows all form objects, properties, events, and methods.
- Generic OCX controls from third-party vendors are supported.

## Database (KISAM)

- **Type 6 KISAM files**: up to 4 billion records (vs. 16 million for type 5); 18 key paths (vs. 9); 8 key segments per path (vs. 4).
- Optional SQL database backend (Oracle initially); standard ISAM operations are mapped to SQL.
- `KI_ALLOC_CONNECT` — new call to allocate a SQL connection number.
- `KI_ALLOC_HANDLE` / `KI_FREE_HANDLE` — explicit handle management.
- `KI_OPEN` now requires a full filename (stream table no longer used).
- `KI_CREATE` uses a connection number; stream parameter dropped.

## Other changes

- Case-sensitive symbol names (KCML 4 forced uppercase).
- `BYREF`, `RTRIM()`, `LTRIM()` are reserved words.
- Hex literal prefix: `0xNN`.
- `ENV()` assignments are exported to child processes by default.
- `LIST DT` shows current KISAM connections and handles.

## See Also

- `compatver` — compatibility flags
- `new610` — what's new in KCML 6.10
- `new620` — what's new in KCML 6.20
