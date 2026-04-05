# KCML CGI Snippets — XML Output

Verified working patterns for KCML CGI scripts served via Apache on KOPEN3 (KCML 06.00.88).

---

## Apache Setup (One-Time)

### `/etc/apache2/conf.d/kcml-cgi.conf`
```apache
Action kcml-cgi /cgi-bin/runkcml
AddHandler kcml-cgi .kcml
```

### `/usr/lib/cgi-bin/runkcml`
```sh
#!/bin/sh
/usr/lib/kcml/kcml -p $DOCUMENT_ROOT$PATH_INFO
```

Key points:
- Use `$DOCUMENT_ROOT$PATH_INFO` — **not** `$PATH_TRANSLATED` (Apache Action directive doesn't set it correctly)
- Scripts live in `/var/www/` (the document root), not in `/cgi-bin/`
- Deploy: `scp -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa file.kcml interpartuk@10.1.1.213:/var/www/`

---

## Minimal XML CGI Script

```kcml
: PRINT "Content-type: text/xml"
: PRINT
: PRINT "<?xml version="; HEX(22); "1.0"; HEX(22); "?>"
: PRINT "<result>Hello</result>"
: $END
```

Rules:
- `PRINT "Content-type: text/xml"` — HTTP header
- `PRINT` (bare, no argument) — required blank line separating headers from body
- `PRINT ""` is a **no-op** — does NOT produce the blank line separator
- Use `HEX(22)` for embedded quotes in strings (not `CHR$(34)`)

---

## Reading QUERY_STRING Parameters

```kcml
: DIM qs$256, param$64, eq_pos, amp_pos
: qs$ = ENV("QUERY_STRING")
: eq_pos = POS(qs$ = "=")
: IF eq_pos == 0 THEN PRINT "<error>Missing parameter</error>"
: IF eq_pos == 0 THEN $END
: param$ = STR(qs$, eq_pos + 1, 64)
: amp_pos = POS(param$ = "&")
: IF amp_pos > 0 THEN STR(param$, amp_pos, 65 - amp_pos) = " "
```

- `ENV("QUERY_STRING")` returns the raw query string, e.g. `order=016519`
- `POS(str$ = "=")` finds position of `=`
- Strip any second parameter by blanking from `&` onward

---

## KISAM Lookup by Key + XML Output

Full pattern: accept key from URL, look up KISAM file, return XML.

```kcml
: REM KCML CGI - KISAM record lookup returning XML
: DIM ki_status, handle, ki_sym, ki_dataptr$6, ki_key$64, rec$2048
: DIM qs$256, key_val$20, eq_pos, amp_pos, read_ok
: PRINT "Content-type: text/xml"
: PRINT
: qs$ = ENV("QUERY_STRING")
: eq_pos = POS(qs$ = "=")
: IF eq_pos == 0 THEN PRINT "<error>Missing parameter</error>"
: IF eq_pos == 0 THEN $END
: key_val$ = STR(qs$, eq_pos + 1, 20)
: amp_pos = POS(key_val$ = "&")
: IF amp_pos > 0 THEN STR(key_val$, amp_pos, 21 - amp_pos) = " "
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: IF ki_status <> 0 THEN PRINT "<error>KI_ALLOC_HANDLE failed</error>"
: IF ki_status <> 0 THEN $END
: CALL KI_OPEN handle, "/full/path/to/FILE", "R" TO ki_status
: IF ki_status <> 0 THEN PRINT "<error>KI_OPEN failed</error>"
: IF ki_status <> 0 THEN $END
: CALL KI_START handle, key_val$, 1 TO ki_status
: ki_sym = SYM(rec$)
: CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
: IF ki_status == 0 THEN read_ok = 1
: IF read_ok == 0 THEN PRINT "<error>Record not found</error>"
: IF read_ok == 0 THEN CALL KI_CLOSE handle TO ki_status
: IF read_ok == 0 THEN $END
: IF STR(ki_key$, 1, 20) <> key_val$ THEN read_ok = 0
: IF read_ok == 0 THEN PRINT "<error>Record not found</error>"
: IF read_ok == 0 THEN CALL KI_CLOSE handle TO ki_status
: IF read_ok == 0 THEN $END
: CALL KI_CLOSE handle TO ki_status
: PRINT "<?xml version="; HEX(22); "1.0"; HEX(22); "?>"
: PRINT "<record>"
: PRINT "  <field1>"; RTRIM(STR(rec$, 1, 10)); "</field1>"
: PRINT "</record>"
: $END
```

Key rules:
- **`read_ok` flag** — `KI_CLOSE` resets `ki_status` to 0, so use a flag rather than checking `ki_status` after the close call
- **`KI_START` order** — `handle, key$, path` (key before path — reversed from libKI)
- **Two IF lines** — `IF cond THEN $END` doesn't work reliably; always use two separate lines
- **`ki_dataptr$` must be 6 bytes**
- **Pre-assign `ki_sym = SYM(rec$)`** before passing to `KI_READ_NEXT` — do not pass `SYM()` inline

---

## Field Extraction Patterns

### Character field (type C/A)
```kcml
: PRINT "  <name>"; RTRIM(STR(rec$, offset, length)); "</name>"
```

### Packed date field (type D, 4 bytes — stores YYYYMMDD as BCD)
```kcml
: DIM hex$12, date$10
: HEXUNPACK STR(rec$, offset, 4) TO hex$
: date$ = STR(hex$, 7, 2) & "/" & STR(hex$, 5, 2) & "/" & STR(hex$, 1, 4)
: PRINT "  <date>"; date$; "</date>"
```

`HEXUNPACK` on 4 bytes gives 8 hex chars = YYYYMMDD directly. Rearrange to DD/MM/YYYY by taking chars 7-8, 5-6, 1-4.

### PRINT rules for mixed content
```kcml
: PRINT "  <tag>"; RTRIM(STR(rec$, 1, 10)); "</tag>"
```
- Always use `;` as separator in PRINT — **never** `&` when arguments include `STR(var, n, len)` (commas inside confuse the parser)
- Never `PRINT "literal" & variable` in a THEN clause — KCML ends the THEN at the closing `"`, the `&` becomes an invalid statement

---

## JSON Output

Use `application/json` content type. Store `HEX(22)` in a variable to avoid repeating it on every PRINT line.

```kcml
: DIM q$1
: q$ = HEX(22)
: PRINT "Content-type: application/json"
: PRINT
: PRINT "{"
: PRINT "  "; q$; "order_number"; q$; ": "; q$; RTRIM(STR(rec$, 18, 6)); q$; ","
: PRINT "  "; q$; "last_field"; q$; ": "; q$; RTRIM(STR(rec$, 557, 4)); q$
: PRINT "}"
: $END
```

Note: the last field has no trailing `,`. Error objects follow the same pattern:
```kcml
: PRINT "{"; q$; "error"; q$; ": "; q$; "Order not found"; q$; "}"
```

Live example: `kcml_executor/order_lookup_json.kcml` deployed at `/var/www/order_lookup_json.kcml`

---

## Deploying Without CRLF Issues

The Write tool / Windows editors produce CRLF line endings. KCML `-p` treats the entire file as one concatenated line if CRLFs are present.

Write directly on the server to avoid this:
```powershell
& ssh interpartuk@10.1.1.213 @"
cat > /var/www/script.kcml << 'KCMLEOF'
: PRINT "Content-type: text/xml"
: PRINT
: PRINT "<result>ok</result>"
: $END
KCMLEOF
"@
```

Or convert after SCP:
```powershell
& ssh interpartuk@10.1.1.213 "sed -i 's/\r//' /tmp/script.kcml && cp /tmp/script.kcml /var/www/"
```

---

## Live Example

`/var/www/order_lookup.kcml` — Order header lookup from OEHDR01.
URL: `http://10.1.1.213/order_lookup.kcml?order=016519`
Source: `kcml_executor/order_lookup.kcml`
