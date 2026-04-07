# CGI Scripts in KCML

> How to write CGI (Common Gateway Interface) web scripts in KCML.

## Description

KCML can be used to write CGI scripts that run on a web server. When the web server receives an HTTP request for a `.kcml` URL, it invokes the KCML interpreter to execute the script and return an HTML response.

## How it works

A CGI script is invoked for a URL like:

```
http://www.example.com/cgi-bin/echo.kcml?param1=Hello&param2=World
```

The web server separates the server name, script path, and query string, then runs the KCML script. The script must write HTTP headers followed by HTML to standard output.

## Script structure

Every CGI script must output a `Content-type` header and a blank line before any HTML:

```kcml
10 PRINT "Content-type: text/html"
   PRINT
   PRINT "<HTML><BODY>"
   PRINT "<P>Hello world, my parameters were: ";ENV("QUERY_STRING");"</P>"
   PRINT "</BODY></HTML>"
   $END
```

- The `Content-type` line and blank line are **mandatory** — without them nothing will be displayed.
- The browser does not see any output until `$END`.
- `ENV("QUERY_STRING")` returns the parameter string following `?` in the URL.

## CGI environment variables

The web server sets standard CGI environment variables. The most useful is:

| Variable | Description |
|----------|-------------|
| `QUERY_STRING` | Parameters from the URL (after `?`) |
| `REQUEST_METHOD` | `GET` or `POST` |
| `CONTENT_LENGTH` | Length of POST data |
| `PATH_INFO` | Extra path after the script name |
| `DOCUMENT_ROOT` | Web server document root |

Use `ENV(` to read these within a KCML script.

## URL encoding

Query string parameters use `%xx` hex encoding for special characters (space, `?`, `%`, `/`, etc.). Use the extended `$PACK` specifier to encode/decode such strings.

## Configuring IIS (Windows)

On Windows with IIS 4/5 or Personal Web Server, KCML registers its `.kcml` extension automatically during installation. If manual configuration is needed, add the extension in the Script Map (Web Site Properties → Home Directory → Configuration → App Mapping):

```
.kcml    c:\kerridge\kcml\kcml.exe -p "%s" "%s"
```

Mark the script directory as executable but not readable.

## Configuring Apache (Unix/Linux)

Add to `httpd.conf`:

```
AddType application/x-httpd-kcml    .kcml
Action application/x-httpd-kcml    "/cgi-bin/kcmlrun"
```

Create the wrapper script `cgi-bin/kcmlrun`:

```sh
#!/bin/sh
/usr/lib/kcml/kcml -p $DOCUMENT_ROOT$PATH_INFO
```

Make it executable: `chmod +x kcmlrun`, then restart Apache.

## Configuring Apache (Windows)

Create `cgi-bin/kcmlrun.bat`:

```batch
@echo off
c:/kerridge/kcml/kcml -p %DOCUMENT_ROOT%%PATH_INFO%
```

## Notes

- CGI scripts run non-interactively (same as `-p` mode) — do not use `INPUT` or `KEYIN`.
- All output goes to stdout; errors to stderr.
- POST data is available via stdin; read `CONTENT_LENGTH` bytes.

## See Also

- `ENV(` — read environment variables
- `$PACK` — string packing/encoding
- `PRINT` — output to stdout
