#!/opt/py36/bin/python3
"""
KCML Execution Server

A simple HTTP server that accepts KCML code via POST and returns execution results.
Designed to run on Ubuntu 8.04 with Python 3.6 and KCML.

Usage:
    /opt/py36/bin/python3 server.py [--port PORT] [--host HOST]

Endpoints:
    POST /execute - Execute KCML code
    GET /health   - Health check
    GET /version  - Get KCML version
"""

import os
import sys
import json
import subprocess
import tempfile
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import uuid

# Configuration
KCML_PATH = "/usr/lib/kcml/kcml"
DEFAULT_TIMEOUT = 30  # seconds
MAX_OUTPUT_SIZE = 1024 * 100  # 100KB max output
TEMP_DIR = "/tmp/kcml_exec"

class KCMLExecutor:
    """Handles KCML code execution"""
    
    def __init__(self, kcml_path=KCML_PATH, timeout=DEFAULT_TIMEOUT):
        self.kcml_path = kcml_path
        self.timeout = timeout
        
        # Ensure temp directory exists
        os.makedirs(TEMP_DIR, exist_ok=True)
    
    def execute(self, code, timeout=None):
        """
        Execute KCML code and return results.
        
        Args:
            code: KCML source code to execute
            timeout: Optional timeout override in seconds
            
        Returns:
            dict with keys: success, stdout, stderr, exit_code, error
        """
        if timeout is None:
            timeout = self.timeout
            
        # Generate unique temp file
        temp_file = os.path.join(TEMP_DIR, f"kcml_{uuid.uuid4().hex}.src")
        
        result = {
            "success": False,
            "stdout": "",
            "stderr": "",
            "exit_code": None,
            "error": None,
            "code": code
        }
        
        try:
            # Write code to temp file
            with open(temp_file, 'w') as f:
                f.write(code)
                # Ensure code ends with newline
                if not code.endswith('\n'):
                    f.write('\n')
            
            # Execute KCML with -p flag for non-interactive mode
            proc = subprocess.Popen(
                [self.kcml_path, "-p", temp_file],
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
                result["error"] = f"Execution timed out after {timeout} seconds"
                result["exit_code"] = -1
                
        except FileNotFoundError:
            result["error"] = f"KCML executable not found at {self.kcml_path}"
        except PermissionError:
            result["error"] = f"Permission denied executing {self.kcml_path}"
        except Exception as e:
            result["error"] = str(e)
        finally:
            # Clean up temp file
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except:
                pass
                
        return result
    
    def get_version(self):
        """Get KCML version info"""
        try:
            proc = subprocess.run(
                [self.kcml_path, "-v"],
                capture_output=True,
                timeout=5
            )
            return {
                "success": True,
                "version": proc.stdout.decode('utf-8', errors='replace').strip()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


class KCMLRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for KCML execution"""
    
    executor = KCMLExecutor()
    
    def _send_json(self, data, status=200):
        """Send JSON response"""
        response = json.dumps(data, indent=2)
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(response))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
    
    def _send_error(self, message, status=400):
        """Send error response"""
        self._send_json({"error": message, "success": False}, status)
    
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/health':
            self._send_json({"status": "ok", "success": True})
        elif self.path == '/version':
            result = self.executor.get_version()
            self._send_json(result)
        else:
            self._send_json({
                "success": True,
                "message": "KCML Execution Server",
                "endpoints": {
                    "POST /execute": "Execute KCML code (body: JSON with 'code' field)",
                    "GET /health": "Health check",
                    "GET /version": "Get KCML version"
                }
            })
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path != '/execute':
            self._send_error(f"Unknown endpoint: {self.path}", 404)
            return
        
        # Get content length
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            self._send_error("No content provided")
            return
        
        if content_length > 1024 * 1024:  # 1MB limit
            self._send_error("Content too large (max 1MB)")
            return
        
        # Read and parse body
        try:
            body = self.rfile.read(content_length).decode('utf-8')
            
            # Try JSON first
            content_type = self.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                data = json.loads(body)
                code = data.get('code', '')
                timeout = data.get('timeout', DEFAULT_TIMEOUT)
            else:
                # Plain text - treat entire body as code
                code = body
                timeout = DEFAULT_TIMEOUT
            
            if not code.strip():
                self._send_error("No KCML code provided")
                return
            
            # Execute the code
            result = self.executor.execute(code, timeout=min(timeout, 60))
            self._send_json(result)
            
        except json.JSONDecodeError as e:
            self._send_error(f"Invalid JSON: {e}")
        except Exception as e:
            self._send_error(f"Server error: {e}", 500)
    
    def log_message(self, format, *args):
        """Log requests"""
        print(f"[{self.log_date_time_string()}] {format % args}")


def main():
    parser = argparse.ArgumentParser(description='KCML Execution Server')
    parser.add_argument('--port', type=int, default=8765, help='Port to listen on')
    parser.add_argument('--host', default='127.0.0.1', help='Host to bind to')
    parser.add_argument('--kcml', default=KCML_PATH, help='Path to KCML executable')
    args = parser.parse_args()
    
    # Update executor with custom KCML path
    KCMLRequestHandler.executor = KCMLExecutor(kcml_path=args.kcml)
    
    server = HTTPServer((args.host, args.port), KCMLRequestHandler)
    print(f"KCML Execution Server starting on http://{args.host}:{args.port}")
    print(f"KCML executable: {args.kcml}")
    print("Press Ctrl+C to stop")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == '__main__':
    main()
