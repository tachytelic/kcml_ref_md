# KCML CGI Configuration Guide

This guide documents how to configure Apache to execute KCML scripts via CGI, enabling HTTP-based access to KCML programs and the creation of REST APIs.

## Overview

KCML CGI allows you to:
- Execute KCML scripts via HTTP requests
- Build REST APIs returning JSON
- Create web dashboards and reports
- Integrate KCML applications with modern systems
- Access system information via HTTP endpoints

## Prerequisites

- Apache 2.x web server
- KCML interpreter installed (typically at `/usr/lib/kcml/kcml`)
- Root/sudo access for Apache configuration

## Apache Configuration

### 1. Create the CGI Wrapper Script

KCML binary files cannot be executed directly by Apache. A shell wrapper script is required:

```bash
sudo tee /usr/lib/cgi-bin/runkcml << 'EOF'
#!/bin/sh
/usr/lib/kcml/kcml -p $PATH_TRANSLATED
EOF
sudo chmod +x /usr/lib/cgi-bin/runkcml
```

The `$PATH_TRANSLATED` environment variable contains the full filesystem path to the requested `.kcml` file.

### 2. Configure Apache Modules

Ensure the required modules are enabled:

```bash
# Check if modules are loaded
ls /etc/apache2/mods-enabled/ | grep -E 'actions|cgi'

# Enable if not present
sudo a2enmod actions
sudo a2enmod cgid
```

### 3. Add KCML Handler Configuration

Add the following to `/etc/apache2/httpd.conf` (or create it):

```apache
# Associate .kcml files with a custom MIME type
AddType application/x-httpd-kcml .kcml

# Route requests for this type through the wrapper script
Action application/x-httpd-kcml /cgi-bin/runkcml
```

**Important:** Do NOT use `AddHandler cgi-script .kcml` as this conflicts with the Action directive and causes Apache to try executing KCML files directly.

### 4. Enable CGI Execution in Document Root

Edit your site configuration (e.g., `/etc/apache2/sites-enabled/000-default`):

```apache
<Directory /var/www/>
    Options Indexes FollowSymLinks MultiViews ExecCGI
    AllowOverride None
    Order allow,deny
    allow from all
</Directory>
```

The key addition is `ExecCGI` to the Options directive.

### 5. Restart Apache

```bash
sudo apache2ctl configtest   # Verify configuration
sudo apache2ctl graceful     # Reload without dropping connections
```

## Writing KCML CGI Scripts

### Required Output Format

CGI scripts **must** output:
1. HTTP headers (at minimum `Content-type:`)
2. A blank line
3. The response body

```kcml
PRINT "Content-type: text/html"
: PRINT
: PRINT "<html><body>Hello World</body></html>"
: $END
```

### Common Content Types

| Type | Header |
|------|--------|
| HTML | `Content-type: text/html` |
| JSON | `Content-type: application/json` |
| Plain text | `Content-type: text/plain` |
| XML | `Content-type: text/xml` |

### Accessing CGI Environment Variables

Use the `ENV()` function to read CGI variables:

```kcml
DIM query$200, ip$20, method$10
: query$ = ENV("QUERY_STRING")      : REM URL parameters after ?
: ip$ = ENV("REMOTE_ADDR")          : REM Client IP address
: method$ = ENV("REQUEST_METHOD")   : REM GET, POST, etc.
: PRINT "Content-type: text/plain"
: PRINT
: PRINT "Query: "; query$
: PRINT "Your IP: "; ip$
: $END
```

### Common CGI Environment Variables

| Variable | Description |
|----------|-------------|
| `QUERY_STRING` | URL parameters (after `?`) |
| `REQUEST_METHOD` | HTTP method (GET, POST, etc.) |
| `REMOTE_ADDR` | Client IP address |
| `SERVER_NAME` | Server hostname |
| `CONTENT_TYPE` | Content type of POST data |
| `CONTENT_LENGTH` | Length of POST data |
| `HTTP_USER_AGENT` | Client browser/agent string |
| `PATH_INFO` | Extra path after script name |
| `PATH_TRANSLATED` | Filesystem path to script |

## Example: JSON API Endpoint

Create `/var/www/api.kcml`:

```kcml
DIM q$20, qt$1
: qt$ = HEX(22)
: PRINT "Content-type: application/json"
: PRINT
: q$ = ENV("QUERY_STRING")
: IF q$ = "time" THEN PRINT "{"; qt$; "time"; qt$; ": "; qt$; $TIME; qt$; ", "; qt$; "date"; qt$; ": "; qt$; $TODAY; qt$; "}"
: IF q$ = "env" THEN PRINT "{"; qt$; "ip"; qt$; ": "; qt$; ENV("REMOTE_ADDR"); qt$; ", "; qt$; "server"; qt$; ": "; qt$; ENV("SERVER_NAME"); qt$; "}"
: IF q$ <> "time" AND q$ <> "env" THEN PRINT "{"; qt$; "endpoints"; qt$; ": ["; qt$; "time"; qt$; ", "; qt$; "env"; qt$; "]}"
: $END
```

**Note:** Use `HEX(22)` for the quote character in JSON output. Do NOT use `CHR$(34)` as it causes a runtime panic.

### Testing the API

```bash
# List endpoints
curl http://server/api.kcml
# {"endpoints": ["time", "env"]}

# Get time
curl http://server/api.kcml?time
# {"time": "164532", "date": "20260404"}

# Get environment info
curl http://server/api.kcml?env
# {"ip": "192.168.1.100", "server": "myserver.local"}
```

## Example: HTML Page

Create `/var/www/hello.kcml`:

```kcml
PRINT "Content-type: text/html"
: PRINT
: PRINT "<html><body>"
: PRINT "<h1>KCML CGI Works!</h1>"
: PRINT "<p>Query string: "; ENV("QUERY_STRING"); "</p>"
: PRINT "<p>Date: "; $TODAY; "</p>"
: PRINT "</body></html>"
: $END
```

## Troubleshooting

### 403 Forbidden

**Cause:** ExecCGI not enabled for the directory.

**Fix:** Add `ExecCGI` to the Options directive in your site configuration.

### 500 Internal Server Error

Check Apache error log:
```bash
tail -20 /var/log/apache2/error.log
```

**Common causes:**
- "Exec format error" - Apache trying to execute KCML directly instead of through wrapper
- "Premature end of script headers" - KCML script crashed or didn't output headers
- Syntax errors in KCML code

### Script Not Executing (Shows Source)

**Cause:** `AddHandler cgi-script .kcml` is overriding the Action directive.

**Fix:** Remove or comment out the AddHandler line. Use only AddType + Action.

### Debugging CGI Scripts

Add temporary debug logging to the wrapper:

```bash
#!/bin/sh
echo "PATH_TRANSLATED=$PATH_TRANSLATED" >> /tmp/cgi_debug.log
/usr/lib/kcml/kcml -p $PATH_TRANSLATED 2>> /tmp/cgi_debug.log
```

Test scripts directly from command line:
```bash
export QUERY_STRING="time"
/usr/lib/kcml/kcml -p /var/www/api.kcml
```

## KCML CGI Limitations

1. **No early exit with $END in IF blocks** - Restructure logic to avoid `$END` inside conditionals
2. **Use HEX(22) for quotes** - `CHR$(34)` causes runtime panics
3. **No interactive input** - `INPUT`, `KEYIN` etc. cannot be used
4. **Stdout only** - All output must go through PRINT statements

## File Permissions

For scripts uploaded via SCP:
```bash
# Make web directory writable by your user
sudo chown youruser:youruser /var/www

# Scripts don't need execute permission (wrapper handles execution)
chmod 644 /var/www/*.kcml
```

## Security Considerations

1. **Sanitize input** - Always validate `ENV("QUERY_STRING")` before using
2. **Limit file access** - CGI scripts run as the Apache user (www-data)
3. **Error handling** - Don't expose internal errors to clients
4. **Rate limiting** - Consider adding rate limiting at the Apache level

## Server Details (Reference Installation)

| Setting | Value |
|---------|-------|
| Server | 10.1.1.213 (Ubuntu 8.04) |
| Apache | 2.2.8 |
| KCML Path | `/usr/lib/kcml/kcml` |
| CGI Wrapper | `/usr/lib/cgi-bin/runkcml` |
| Document Root | `/var/www/` |
| Config File | `/etc/apache2/httpd.conf` |

## Quick Reference

```bash
# Test connectivity
curl http://server/hello.kcml

# Check Apache config
sudo apache2ctl configtest

# Reload Apache
sudo apache2ctl graceful

# View error log
tail -f /var/log/apache2/error.log

# Test KCML script directly
export QUERY_STRING="param=value"
/usr/lib/kcml/kcml -p /var/www/script.kcml
```
