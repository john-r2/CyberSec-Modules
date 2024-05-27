#Note: this could be a one-liner
#
$x = Import-Csv D:\CyberSec-Modules\9.Scripting\PowerShell\users.csv
$x | Sort-Object -Property LastName | Format-Table LastName
$x