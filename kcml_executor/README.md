# KCML Execution Server

A Python-based server that enables Claude to execute KCML code snippets and verify they work.

## Architecture

```
┌─────────────┐     SSH Tunnel      ┌──────────────────┐     subprocess     ┌──────────┐
│   Claude    │ ──────────────────► │  HTTP Server     │ ─────────────────► │   KCML   │
│  (VS Code)  │ ◄────────────────── │  (Ubuntu 8.04)   │ ◄───────────────── │  -p flag │
└─────────────┘     JSON response   └──────────────────┘     stdout/stderr  └──────────┘
```

## Files

| File | Purpose |
|------|---------|
| `server.py` | HTTP server for remote execution |
| `mcp_server.py` | MCP protocol server for direct Claude integration |

## Server Deployment (Ubuntu 8.04)

### 1. Copy files to the server

```bash
scp server.py mcp_server.py user@your-server:/home/user/kcml_executor/
```

### 2. Make executable

```bash
ssh user@your-server
cd /home/user/kcml_executor
chmod +x server.py mcp_server.py
```

### 3. Test KCML is working

```bash
echo 'PRINT "Hello World"' | /usr/lib/kcml/kcml
# Or
/usr/lib/kcml/kcml -v
```

### 4. Start the HTTP server

```bash
# Start on localhost only (recommended for security)
/opt/py36/bin/python3 server.py --host 127.0.0.1 --port 8765

# Or allow remote connections (use with firewall/SSH tunnel)
/opt/py36/bin/python3 server.py --host 0.0.0.0 --port 8765
```

### 5. Run as a service (optional)

Create `/etc/systemd/system/kcml-executor.service`:

```ini
[Unit]
Description=KCML Execution Server
After=network.target

[Service]
Type=simple
User=kcml
WorkingDirectory=/home/user/kcml_executor
ExecStart=/opt/py36/bin/python3 /home/user/kcml_executor/server.py --host 127.0.0.1 --port 8765
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable kcml-executor
sudo systemctl start kcml-executor
```

## Connecting from Windows (SSH Tunnel)

Create an SSH tunnel to forward local port to the server:

```powershell
ssh -L 8765:127.0.0.1:8765 user@your-server -N
```

Keep this terminal open. Now `http://localhost:8765` on Windows routes to the Ubuntu server.

## Testing the Server

### Health check
```bash
curl http://localhost:8765/health
```

### Execute KCML
```bash
curl -X POST http://localhost:8765/execute \
  -H "Content-Type: application/json" \
  -d '{"code": "PRINT \"Hello from KCML\"\n$END"}'
```

### Using PowerShell
```powershell
$body = @{ code = "PRINT `"Hello World`"`n`$END" } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8765/execute -Method POST -Body $body -ContentType "application/json"
```

## VS Code MCP Configuration

To use the MCP server directly with Claude in VS Code, add to your VS Code settings or `~/.vscode/mcp.json`:

### Option A: Via SSH (recommended)

```json
{
  "mcpServers": {
    "kcml-executor": {
      "command": "ssh",
      "args": [
        "user@your-server",
        "/opt/py36/bin/python3",
        "/home/user/kcml_executor/mcp_server.py"
      ]
    }
  }
}
```

### Option B: Local with port forwarding

First start the SSH tunnel, then configure Claude to use HTTP calls via the skill.

## API Reference

### POST /execute

Execute KCML code.

**Request:**
```json
{
  "code": "PRINT \"Hello\"\n$END",
  "timeout": 30
}
```

**Response:**
```json
{
  "success": true,
  "stdout": "Hello\n",
  "stderr": "",
  "exit_code": 0,
  "error": null,
  "code": "PRINT \"Hello\"\n$END"
}
```

### GET /health

Health check endpoint.

### GET /version

Returns KCML interpreter version.

## Security Considerations

⚠️ **This server executes arbitrary code. Use only in trusted environments.**

Recommendations:
1. Bind to `127.0.0.1` only
2. Use SSH tunnels for remote access
3. Run as unprivileged user
4. Set execution timeouts (max 60s enforced)
5. Consider containerization for isolation

## Troubleshooting

### "KCML executable not found"
Check the path: `/usr/lib/kcml/kcml` - update `KCML_PATH` in the scripts if different.

### "Permission denied"
Ensure the kcml executable is accessible: `chmod +x /usr/lib/kcml/kcml`

### Timeout errors
Increase timeout in request, or check if KCML program has infinite loop.

### Python version issues
This requires Python 3.6+. Verify: `/opt/py36/bin/python3 --version`
