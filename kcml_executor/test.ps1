# Quick test script for KCML execution server (PowerShell)

param(
    [string]$Server = "http://localhost:8765"
)

Write-Host "Testing KCML Execution Server at $Server" -ForegroundColor Cyan
Write-Host "========================================="

# Test 1: Health check
Write-Host "`n[1] Health check..." -ForegroundColor Yellow
try {
    Invoke-RestMethod -Uri "$Server/health" | ConvertTo-Json
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
}

# Test 2: Version
Write-Host "`n[2] KCML version..." -ForegroundColor Yellow
try {
    Invoke-RestMethod -Uri "$Server/version" | ConvertTo-Json
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
}

# Test 3: Simple PRINT
Write-Host "`n[3] Simple PRINT test..." -ForegroundColor Yellow
$body = @{ code = "PRINT `"Hello from KCML!`"`n`$END" } | ConvertTo-Json
try {
    Invoke-RestMethod -Uri "$Server/execute" -Method POST -Body $body -ContentType "application/json" | ConvertTo-Json -Depth 5
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
}

# Test 4: Math operations  
Write-Host "`n[4] Math operations..." -ForegroundColor Yellow
$body = @{ code = "DIM result`nresult = 2 + 2 * 10`nPRINT `"2 + 2 * 10 = `"; result`n`$END" } | ConvertTo-Json
try {
    Invoke-RestMethod -Uri "$Server/execute" -Method POST -Body $body -ContentType "application/json" | ConvertTo-Json -Depth 5
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
}

# Test 5: FOR loop
Write-Host "`n[5] FOR loop..." -ForegroundColor Yellow
$body = @{ code = "FOR i = 1 TO 5`nPRINT `"Count: `"; i`nNEXT i`n`$END" } | ConvertTo-Json
try {
    Invoke-RestMethod -Uri "$Server/execute" -Method POST -Body $body -ContentType "application/json" | ConvertTo-Json -Depth 5
} catch {
    Write-Host "Error: $_" -ForegroundColor Red
}

Write-Host "`n========================================="
Write-Host "Tests complete!" -ForegroundColor Green
