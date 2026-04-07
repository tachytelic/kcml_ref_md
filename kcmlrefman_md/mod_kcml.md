# mod_kcml — Apache Module for KCML SOAP

> Apache 1.3+ module that connects Apache to KCML SOAP servers.

## Description

`mod_kcml` is an Apache extension module (`mod_kcml.c`) that provides KCML SOAP server integration with the Apache web server.

- **Status**: Extension
- **Compatibility**: Unix, Apache 1.3+; requires KCML 6.00.00.7173 or later.

## Features

- Routes HTTP requests to persistent KCML SOAP server processes.
- Apache dynamically adapts to load — creates KCML processes as needed.
- KCML SOAP servers can be on the same machine as Apache or on a remote machine.
- Converts browser HTTP `GET` and `POST` requests into SOAP requests for KCML; converts SOAP responses back to text for the browser.
- Maintains session variables for KCML using an extension to the SOAP envelope body.
- Allows access to KCML's SQL utility for executing SQL statements from browser `GET` requests (non-persistent processes).
- Supports various error reporting modes.

## Directives

### Server directives

| Directive | Description |
|-----------|-------------|
| `KcmlTraceFile` | Path for trace output file |
| `KcmlTraceLevel` | Trace verbosity level |
| `KcmlTraceMode` | Trace mode |
| `KcmlSessionCache` | Session cache configuration |
| `KcmlSessionTime` | Session timeout |

### Directory/Location directives

| Directive | Description |
|-----------|-------------|
| `SqlServer` | Address of the KCML SQL server |
| `SqlStatement` | SQL statement to execute |
| `KcmlSoapServer` | Address and configuration of the KCML SOAP server |
| `KcmlKeepServer` | Whether to keep KCML processes persistent |

## See Also

- `soapserver` — KCML as a SOAP server
- `ObjSoap` — SOAP client usage from KCML
- `cgi` — CGI scripting in KCML
