# CREATE (distributed object)

> Instantiates a distributed object (COM, CORBA, SOAP, or Dynamic) and returns an object reference.

## Syntax

```
OBJECT object_name = CREATE strexpr1 [, strexpr2 [, ...]]
```

| Parameter | Description |
|-----------|-------------|
| `object_name` | An `OBJECT` variable to hold the reference |
| `strexpr1` | Object type (case-insensitive string — see table below) |
| `strexpr2+` | Type-specific parameters (class name, URL, library name, etc.) |

## Object types

| `strexpr1` | Standard | Accessed by | Server OS |
|------------|----------|-------------|-----------|
| `serverCOM` | COM | Server | Windows only |
| `clientCOM` | COM | Client | Unix or Windows |
| `CORBA` | CORBA | Server | Unix or Windows |
| `SOAP` | SOAP/WSDL | Server | Unix or Windows |
| `Dynamic` | KIDL | Server | Unix or Windows |

## Description

`CREATE` connects KCML to an external object and returns a reference. KCML acts as a client — it can call methods exposed by the object. There is no event or callback mechanism.

### COM objects

`strexpr2` is the ProgId or ClassId string from the Windows registry:

```kcml
OBJECT Doc = CREATE "clientCOM", "Word.Basic"
OBJECT rsTable = CREATE "serverCOM", "ADODB.Recordset"
```

### CORBA objects

`strexpr2` is the object name in the naming service or an IOR string:

```kcml
OBJECT Add = CREATE "Corba", "Add", "-ORBNamingAddr", "inet:evb:9876"
```

### SOAP objects

`strexpr2` is the URL of the WSDL file. An optional `strexpr3` contains comma-separated options:

```kcml
OBJECT s = CREATE "SOAP", "http [colon] //services.xmethods.net/soap/urn.wsdl", "PROXY=user:pass@proxy:8080"
```

**SOAP options:**

| Option | Purpose |
|--------|---------|
| `AUTH=user:pass` | Basic HTTP authentication |
| `PROXY=user:pass@host:port` | HTTP proxy |
| `TUNNEL=old|new` | Redirect SOAP through SSL tunnel |
| `MPOST=1` | Use HTTP M-POST instead of POST |
| `RETRY=n` | Retry count on no response |
| `LIT=Y` | Literal document mode |

### Dynamic (KIDL) objects

`strexpr2` is the name of the shared library (no extension needed — `.so`, `.DLL`, or `.sl` is added automatically):

```kcml
OBJECT x = CREATE "Dynamic", "dyndom"
```

On Unix, set `USEMALLOC` environment variable or KCML will throw O30.18.

## Notes

- Only one CORBA ORB connection is allowed per KCML process.
- After `CREATE`, call object methods using `OBJECT.method(args)` syntax.
- On Unix with Dynamic objects, install dependent libraries into `/usr/local/lib` and add to `LD_LIBRARY_PATH`.

## See Also

- `OBJECT` — declare an object variable
- `$DECLARE` — declare external C functions (simpler alternative for non-object libraries)
- `CALL` — invoke UFN functions
