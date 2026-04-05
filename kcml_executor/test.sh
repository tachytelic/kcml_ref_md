#!/bin/bash
# Quick test script for KCML execution server

SERVER="${1:-http://localhost:8765}"

echo "Testing KCML Execution Server at $SERVER"
echo "========================================="

# Test 1: Health check
echo -e "\n[1] Health check..."
curl -s "$SERVER/health" | python3 -m json.tool 2>/dev/null || curl -s "$SERVER/health"

# Test 2: Version
echo -e "\n\n[2] KCML version..."
curl -s "$SERVER/version" | python3 -m json.tool 2>/dev/null || curl -s "$SERVER/version"

# Test 3: Simple PRINT
echo -e "\n\n[3] Simple PRINT test..."
curl -s -X POST "$SERVER/execute" \
  -H "Content-Type: application/json" \
  -d '{"code": "PRINT \"Hello from KCML!\"\n$END"}' | python3 -m json.tool 2>/dev/null

# Test 4: Math operations
echo -e "\n\n[4] Math operations..."
curl -s -X POST "$SERVER/execute" \
  -H "Content-Type: application/json" \
  -d '{"code": "DIM result\nresult = 2 + 2 * 10\nPRINT \"2 + 2 * 10 = \"; result\n$END"}' | python3 -m json.tool 2>/dev/null

# Test 5: FOR loop
echo -e "\n\n[5] FOR loop..."
curl -s -X POST "$SERVER/execute" \
  -H "Content-Type: application/json" \
  -d '{"code": "FOR i = 1 TO 5\nPRINT \"Count: \"; i\nNEXT i\n$END"}' | python3 -m json.tool 2>/dev/null

# Test 6: String operations
echo -e "\n\n[6] String operations..."
curl -s -X POST "$SERVER/execute" \
  -H "Content-Type: application/json" \
  -d '{"code": "DIM name$30\nname$ = \"KCML Programming\"\nPRINT \"Length: \"; LEN(name$)\nPRINT \"Upper: \"; $UPPER(name$)\n$END"}' | python3 -m json.tool 2>/dev/null

echo -e "\n\n========================================="
echo "Tests complete!"
