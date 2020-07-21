#Note: this could be a one-liner
#
$x = Import-Csv D:\SVGS\4.Scripting\PowerShell\users.csv
$x | Sort-Object -Property LastName | Format-Table LastName
