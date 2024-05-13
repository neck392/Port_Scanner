$ip = Read-Host "Enter the IP address to scan"
$ports = @(21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389)
$results = @()

foreach ($port in $ports) {
    $tcpClient = New-Object System.Net.Sockets.TcpClient
    try {
        $connect = $tcpClient.BeginConnect($ip, $port, $null, $null)
        $wait = $connect.AsyncWaitHandle.WaitOne(5000, $true)
        if ($tcpClient.Connected) {
            $tcpClient.EndConnect($connect)
            $results += "[+] $port port is opened."
        } else {
            $results += "[-] $port port is closed."
        }
    } catch {
        $results += "[!] Error occurred while scanning $port port: $_"
    } finally {
        $tcpClient.Close()
    }
}

Write-Host "------------- Result -------------"
$results | ForEach-Object { Write-Host $_ }
