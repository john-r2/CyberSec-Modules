# Grab the user file (FirstName, LastName, Domain)
$user = Import-Csv D:\SVGS\4.Scripting\PowerShell\users.csv

# Create a new empty array object
# It will have FirstName, LastName, Domain, Email when we are done
$usermail = @()

$user | ForEach-Object {
    # Create the email address, ex Luke.Skywalker@Starwars.edu
    $email = $_.FirstName + '.' + $_.LastName + '@' + $_.Domain + '.edu'

    # Create a temporary object that holds data for one user
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