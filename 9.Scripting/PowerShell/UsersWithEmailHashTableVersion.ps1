# To add the email property to our $user object, we
#  need to create a new object

# Grab the user file (FirstName, LastName, Domain)
cd D:\CyberSec-Modules\9.Scripting\PowerShell
$user = Import-Csv users.csv

# Create a new empty array object
# It will have FirstName, LastName, Domain, Email when we are done
# @() with parenthesis is an array
$usermail = @()

$user | ForEach-Object {
    # Create the email address, ex Luke.Skywalker@Starwars.edu
    $email = $_.FirstName + '.' + $_.LastName + '@' + $_.Domain + '.edu'

    # Create a temporary object that holds data for one user
    # @{} with curly braces is a hashtable
    $tempUserObj = New-Object psobject -Property @{
        FirstName = $_.FirstName
        LastName = $_.LastName
        Domain = $_.Domain
        Email = $email
    } 

    # Append our temporary object to $usermail
    $usermail += $tempUserObj
}

$usermail