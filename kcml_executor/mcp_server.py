#!/opt/py36/bin/python3
"""
KCML MCP Server

Model Context Protocol server that provides KCML code execution capability.
This can be used directly by Claude to execute KCML code snippets.

Usage via stdio (for MCP clients like Claude):
    /opt/py36/bin/python3 mcp_server.py

Or connect to a remote HTTP server:
    /opt/py36/bin/python3 mcp_server.py --remote http://localhost:8765
"""

import os
import sys
import json
import subprocess
import tempfile
import uuid

# For MCP stdio mode
def read_message():
    """Read a JSON-RPC message from stdin"""
    line = sys.stdin.readline()
    if not line:
        return None
    return json.loads(line)

def write_message(msg):
    """Write a JSON-RPC message to stdout"""
    sys.stdout.write(json.dumps(msg) + '\n')
    sys.stdout.flush()

# KCML Executor (same as HTTP server)
KCML_PATH = "/usr/lib/kcml/kcml"
TEMP_DIR = "/tmp/kcml_exec"
DEFAULT_TIMEOUT = 30
MAX_OUTPUT_SIZE = 1024 * 100

class KCMLExecutor:
    def __init__(self):
        os.makedirs(TEMP_DIR, exist_ok=True)
    
    def execute(self, code, timeout=DEFAULT_TIMEOUT):
        temp_file = os.path.join(TEMP_DIR, f"kcml_{uuid.uuid4().hex}.src")
        result = {
            "success": False,
            "stdout": "",
            "stderr": "",
            "exit_code": None,
            "error": None
        }
        
        try:
            with open(temp_file, 'w') as f:
                f.write(code)
                if not code.endswith('\n'):
                    f.write('\n')
            
            proc = subprocess.Popen(
                [KCML_PATH, "-p", temp_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=TEMP_DIR
            )
            
            try:
                stdout, stderr = proc.communicate(timeout=timeout)
                result["stdout"] = stdout.decode('utf-8', errors='replace')[:MAX_OUTPUT_SIZE]
                result["stderr"] = stderr.decode('utf-8', errors='replace')[:MAX_OUTPUT_SIZE]
                result["exit_code"] = proc.returncode
                result["success"] = proc.returncode == 0
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.communicate()
                result["error"] = f"Timeout after {timeout}s"
                result["exit_code"] = -1
                
        except Exception as e:
            result["error"] = str(e)
        finally:
            try:
                os.remove(temp_file)
            except:
                pass
        
        return result

# MCP Server Implementation
class MCPServer:
    def __init__(self):
        self.executor = KCMLExecutor()
        self.tools = {
            "kcml_execute": {
                "name": "kcml_execute",
                "description": "Execute KCML code and return the output. KCML is a BASIC-derived programming language. The code runs non-interactively.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "KCML source code to execute. Should end with $END for clean termination."
                        },
                        "timeout": {
                            "type": "integer",
                            "description": "Execution timeout in seconds (default 30, max 60)",
                            "default": 30
                        }
                    },
                    "required": ["code"]
                }
            },
            "kcml_version": {
                "name": "kcml_version",
                "description": "Get the KCML interpreter version",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
    
    def handle_initialize(self, params):
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "kcml-executor",
                "version": "1.0.0"
            }
        }
    
    def handle_tools_list(self, params):
        return {"tools": list(self.tools.values())}
    
    def handle_tools_call(self, params):
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        if tool_name == "kcml_execute":
            code = arguments.get("code", "")
            timeout = min(arguments.get("timeout", 30), 60)
            result = self.executor.execute(code, timeout)
            
            # Format output for Claude
            output_parts = []
            if result["stdout"]:
                output_parts.append(f"=== STDOUT ===\n{result['stdout']}")
            if result["stderr"]:
                output_parts.append(f"=== STDERR ===\n{result['stderr']}")
            if result["error"]:
                output_parts.append(f"=== ERROR ===\n{result['error']}")
            output_parts.append(f"=== EXIT CODE: {result['exit_code']} ===")
            
            return {
                "content": [{
                    "type": "text",
                    "text": "\n\n".join(output_parts) if output_parts else "No output"
                }]
            }
        
        elif tool_name == "kcml_version":
            try:
                proc = subprocess.run([KCML_PATH, "-v"], capture_output=True, timeout=5)
                version = proc.stdout.decode('utf-8', errors='replace').strip()
                return {
                    "content": [{
                        "type": "text",
                        "text": f"KCML Version: {version}"
                    }]
                }
            except Exception as e:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"Error getting version: {e}"
                    }],
                    "isError": True
                }
        
        return {
            "content": [{
                "type": "text",
                "text": f"Unknown tool: {tool_name}"
            }],
            "isError": True
        }
    
    def handle_request(self, request):
        method = request.get("method")
        params = request.get("params", {})
        req_id = request.get("id")
        
        handlers = {
            "initialize": self.handle_initialize,
            "tools/list": self.handle_tools_list,
            "tools/call": self.handle_tools_call,
        }
        
        if method in handlers:
            result = handlers[method](params)
            return {"jsonrpc": "2.0", "id": req_id, "result": result}
        elif method == "notifications/initialized":
            return None  # No response for notifications
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"}
            }
    
    def run(self):
        """Run the MCP server in stdio mode"""
        while True:
            try:
                request = read_message()
                if request is None:
                    break
                
                response = self.handle_request(request)
                if response:
                    write_message(response)
                    
            except json.JSONDecodeError:
                continue
            except KeyboardInterrupt:
                break
            except Exception as e:
                sys.stderr.write(f"Error: {e}\n")


if __name__ == '__main__':
    server = MCPServer()
    server.run()
