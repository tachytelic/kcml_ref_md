<#
.SYNOPSIS
    Run KCML code on remote server via SSH/SCP or CGI

.DESCRIPTION
    Creates a temp file with KCML code and executes it.
    Supports SSH/SCP method or Apache CGI method.

.PARAMETER Code
    KCML code to execute (single string)

.PARAMETER File
    Path to a local .kcml file to execute

.PARAMETER Method
    Execution method: 'ssh' (default) or 'cgi'

.EXAMPLE
    .\run_kcml.ps1 -Code 'PRINT "Hello" : $END'

.EXAMPLE
    .\run_kcml.ps1 -File .\myprogram.kcml -Method cgi
#>
param(
    [Parameter(Mandatory=$false)]
    [string]$Code,
    
    [Parameter(Mandatory=$false)]
    [string]$File,
    
    [Parameter(Mandatory=$false)]
    [ValidateSet('ssh', 'cgi')]
    [string]$Method = 'ssh'
)

$SSH = "C:\Windows\System32\OpenSSH\ssh.exe"
$SCP = "C:\Windows\System32\OpenSSH\scp.exe"
$SSHOpts = @("-o", "HostKeyAlgorithms=+ssh-rsa", "-o", "PubkeyAcceptedKeyTypes=+ssh-rsa")
$Server = "interpartuk@10.1.1.213"
$KCMLPath = "/usr/lib/kcml/kcml"
$WebRoot = "/var/www"
$BaseUrl = "http://10.1.1.213"

if ($File) {
    if (!(Test-Path $File)) {
        Write-Error "File not found: $File"
        exit 1
    }
    $LocalFile = $File
} elseif ($Code) {
    $LocalFile = "$env:TEMP\kcml_exec.kcml"
    # For CGI, wrap code with Content-type header
    if ($Method -eq 'cgi') {
        $CgiCode = "PRINT `"Content-type: text/plain`"`n: PRINT`n: " + ($Code -replace "`n", "`n: ")
        [System.IO.File]::WriteAllText($LocalFile, $CgiCode)
    } else {
        [System.IO.File]::WriteAllText($LocalFile, $Code)
    }
} else {
    Write-Error "Either -Code or -File must be specified"
    exit 1
}

if ($Method -eq 'cgi') {
    $RemotePath = "$WebRoot/kcml_exec_temp.kcml"
    # SCP file to web root
    & $SCP @SSHOpts -q $LocalFile "${Server}:${RemotePath}"
    if ($LASTEXITCODE -ne 0) {
        Write-Error "SCP failed"
        exit 1
    }
    # Execute via HTTP GET
    try {
        $response = Invoke-WebRequest -Uri "$BaseUrl/kcml_exec_temp.kcml" -TimeoutSec 30
        Write-Output $response.Content
    } catch {
        Write-Error "HTTP request failed: $_"
        exit 1
    }
} else {
    # SSH method
    $RemotePath = "/tmp/kcml_exec.kcml"
    # SCP file to server
    & $SCP @SSHOpts -q $LocalFile "${Server}:${RemotePath}"
    if ($LASTEXITCODE -ne 0) {
        Write-Error "SCP failed"
        exit 1
    }
    # Execute on server (capture both stdout and stderr)
    & $SSH @SSHOpts $Server "$KCMLPath -p $RemotePath 2>&1"
}
