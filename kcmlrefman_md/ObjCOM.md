# COM Support in KCML

> Reference for using COM (Component Object Model) objects from KCML on Windows.

## Description

COM is a Microsoft binary object standard. KCML supports COM through the `OBJECT` / `CREATE` grammar:

- **Client**: KCML programs can create and use COM objects (e.g. Excel, ADO, CDO).
- **Server**: KCML can expose its subroutines as a COM server that other COM clients (VB, Java, etc.) can call.

COM support is **Windows-only** (KClient or Windows KCML server). On Unix servers, COM objects must run on the Windows KClient PC — KCML server programs can still use them via the client-side `$DECLARE` / `OBJECT` mechanism.

### Requirements

- Objects must have a **Dual Interface** (IDispatch + type library) — i.e. support OLE Automation.
- KCML does not support pure vtable-only COM interfaces.

## Client example

```kcml
REM Automate Excel via COM
OBJECT xl
xl = CREATE "Excel.Application"
xl.Visible = 1
xl.Workbooks.Add()
xl.ActiveSheet.Cells(1,1).Value = "Hello from KCML"
xl.ActiveWorkbook.SaveAs("C:\temp\test.xlsx")
xl.Quit()
OBJECT xl = NULL
```

## Server setup

To expose KCML subroutines as a COM server:

```kcml
REM Initialize, then block awaiting COM calls
$DECLARE 'KCMLOBJECTExport(STR(), STR())="*"
'KCMLOBJECTExport("COM", "MyInterface")
$END

DEFSUB 'MyInterface_GetData$(arg$)
  LOCAL DIM result$100
  result$ = "Data for: " & arg$
  RETURN result$
END SUB
```

The subroutine name must be prefixed `InterfaceName_MethodName`. String-returning methods end with `$`.

## Notes

- DCOM (distributed COM) is not practically supported in KCML for Unix.
- Free COM objects explicitly with `OBJECT var = NULL` to release resources.
- COM calls from KCML run on the **client** machine (KClient) — the KCML server program drives them remotely.
- For cross-platform remote objects consider SOAP instead.

## See Also

- `CREATE` — create an object instance
- `OBJECT` — object variable declaration and null release
- `ObjSoap` — SOAP web service client/server
- `ObjServer` — KCML as object server
