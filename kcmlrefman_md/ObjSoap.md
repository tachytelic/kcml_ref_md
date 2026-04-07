# SOAP Support in KCML

> Reference for using SOAP web services from KCML (client and server).

## Description

SOAP (Simple Object Access Protocol) uses XML over HTTP for remote procedure calls. KCML 6.0 implements SOAP 1.1 and is interoperable with Apache SOAP, Microsoft SOAP SDK 2, and Microsoft .NET.

KCML can act as both a **SOAP client** (calling remote services) and a **SOAP server** (exposing KCML subroutines).

### Requirements

- The SOAP server must provide WSDL — KCML uses WSDL to discover the service interface.
- A KCML SOAP server auto-generates WSDL at `endpoint?WSDL`.

## Client

```kcml
DIM wsdl$200
wsdl$ = "http://www.example.com/stockquote?WSDL"
OBJECT s
s = CREATE "SOAP", wsdl$
DIM quote$50
quote$ = s.GetQuote$("MSFT")
PRINT quote$
OBJECT s = NULL     : REM must free to release WSDL memory
```

### Through a proxy

```kcml
s = CREATE "SOAP", wsdl$, "PROXY=proxy.example.com:8080"
```

### Document-style service

```kcml
s = CREATE "SOAP", wsdl$, "DOC=Y"
DIM req$500, resp$500
req$ = "<type1><arg0>1</arg0><arg1>2</arg1></type1>"
resp$ = s.GetSomething$(req$)
OBJECT s = NULL
```

## HTTP Cookies

```kcml
s._AddCookie("sessionid", "abc123")    : REM add cookie to all requests
s._AddCookie("sessionid", "")          : REM remove cookie
```

## Error handling

```kcml
$DECLARE 'KCMLObjectGetLastError(STR(), RETURN INT())="*"
$DECLARE 'KCMLObjectGetLastErrorString(STR(), RETURN STR())="*"
DIM soap_err, soap_msg$200
'KCMLObjectGetLastError("SOAP", soap_err)
'KCMLObjectGetLastErrorString("SOAP", soap_msg$)
PRINT soap_err; " "; TRIM(soap_msg$)
```

## Server

See `ObjServer` for the full server setup. Summary:

```kcml
$DECLARE 'KCMLOBJECTExport(STR(), STR())="*"
'KCMLOBJECTExport("SOAP", "MyService")
$END

DEFSUB 'MyService_Echo$(input$)
  RETURN input$
END SUB
```

Browse `http://server/endpoint` to get the auto-generated service description. Use `?WSDL` suffix for the WSDL document.

## Notes

- `OBJECT s = NULL` is mandatory after use — KCML holds WSDL in memory until the object is released.
- HTTP cookies persist for the lifetime of the SOAP object.
- SOAP 1.1 only (not 1.2).

## See Also

- `CREATE` — create object instance
- `ObjServer` — KCML as SOAP/COM/CORBA server
- `ExSOAPclient` — worked example of SOAP client call
- `ObjCOM` — COM support
