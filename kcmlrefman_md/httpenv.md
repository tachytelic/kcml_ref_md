# CGI Environment Variables

> Standard CGI environment variables available to KCML CGI scripts.

## Description

When a KCML program is invoked as a CGI script by a web server, the server sets standard CGI environment variables. Use `ENV(` to read them from within a KCML program.

## Variables

| Variable | Description |
|----------|-------------|
| `AUTH_TYPE` | Authentication method used to validate the browser (e.g. Basic, Digest) |
| `CONTENT_LENGTH` | Byte length of user-provided POST data |
| `CONTENT_TYPE` | MIME type of the POST data (e.g. `text/html`, `image/jpeg`) |
| `DOCUMENT_ROOT` | Directory from which web documents are served |
| `GATEWAY_INTERFACE` | CGI specification version (e.g. `CGI/1.1`) |
| `PATH_INFO` | Additional virtual path appended to the script URL |
| `PATH_TRANSLATED` | Server-side translation of `PATH_INFO` to a filesystem path |
| `QUERY_STRING` | URL parameters after `?` (GET requests or URL-encoded data) |
| `REMOTE_ADDR` | IP address of the client browser |
| `REMOTE_HOST` | Hostname of the client browser (if DNS resolution available) |
| `REMOTE_IDENT` | Login name of the user (only if server supports identification) |
| `REMOTE_USER` | Username supplied by the browser for authentication |
| `REQUEST_METHOD` | HTTP method: `GET` or `POST` |
| `SCRIPT_NAME` | Virtual path to the script |
| `SERVER_NAME` | Hostname of the web server |
| `SERVER_PORT` | Port number on which the request was received |
| `SERVER_PROTOCOL` | HTTP protocol version (e.g. `HTTP/1.1`) |
| `SERVER_SOFTWARE` | Name and version of the web server software |

## Example

```kcml
DIM qs$256
qs$ = ENV("QUERY_STRING")
PRINT "Content-type: text/html"
PRINT
PRINT "<HTML><BODY><P>Query: "; qs$; "</P></BODY></HTML>"
$END
```

## See Also

- `cgi` — writing CGI scripts in KCML
- `ENV(` — read an environment variable
- `$PACK` — URL encoding/decoding
