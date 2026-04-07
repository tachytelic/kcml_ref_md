# Example: SOAP web service client

> Shows how to call SOAP web services from KCML using `CREATE "SOAP"`.

## Description

KCML can consume SOAP web services by creating a `SOAP` object with `CREATE`. Pass the WSDL URL (and optionally a proxy server) to `CREATE`, then call methods on the returned object as if they were native KCML subroutines.

## Syntax

```kcml
OBJECT s = CREATE "SOAP", "http://example.com/service.wsdl" [, options$]
result = s.MethodName(arg1, arg2, ...)
OBJECT s = NULL
```

Optional `options$` string:
- `"PROXY=proxyhost:port"` — route requests through an HTTP proxy.

## Examples

### Simple call: numeric return value

```kcml
DIM rate, opt$="PROXY=proxy:8080"
OBJECT s = CREATE "SOAP", "http://services.xmethods.net/soap/urn:xmethods-CurrencyExchange.wsdl", opt$
rate = s.getRate("England", "Japan")
PRINT "Exchange rate: "; rate
OBJECT s = NULL
```

### Method returning a sequence (multiple BYREF return values)

A SOAP sequence (structure) is "unrolled" into individual arguments. Pass them `BYREF` to receive the values:

```kcml
DIM opt$="PROXY=proxy:8080"
DIM OBJECT s
DIM location$40, sky$40, wind$40, temp$40, humidity$40, visibility$40, pressure$40

OBJECT s = CREATE "SOAP", "http://live.capescience.com/wsdl/AirportWeather.wsdl", opt$
s.getSummary("EGLL", BYREF location$, BYREF sky$, BYREF wind$, BYREF temp$, BYREF humidity$, BYREF visibility$, BYREF pressure$)
PRINT "Location: "; location$
PRINT "Sky: "; sky$
PRINT "Wind: "; wind$
PRINT "Temp: "; temp$
OBJECT s = NULL
```

The WSDL defines how many elements the sequence has — all must be passed as `BYREF` arguments in the call.

## Notes

- The `CREATE "SOAP"` object requires the WSDL URL at creation time. KCML uses it to resolve method signatures.
- SOAP sequences are unrolled into their component elements; nested sequences are **not** supported.
- The `HTTP_PROXY` environment variable can also set a global proxy (the `PROXY=` option in `CREATE` overrides it).
- Set the `SOAP` object to `NULL` when done to release resources.
- The SOAP client works with both Windows and Unix KCML.

## See Also

- `CREATE` — create a SOAP or other object
- `OBJECT` — object reference declaration
- `BYREF` — pass argument by reference
- `ENV(` — read environment variables (e.g. HTTP_PROXY)
