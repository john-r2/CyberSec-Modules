#For PowerShell Lab 4

#This version uses foreach instead of Foreach-Object

#Grab the user file (FirstName, LastName, Domain)
cd D:\CyberSec-Modules\9.Scripting\PowerShell
$user = Import-Csv users.csv

#Create a new, empty, object
#It will have FirstName, LastName, Domain, Email when we're done
$usermail = @()

foreach ($thisUser in $user) {
    #create the email address, example:  Luke.Skywalker@Starwars.edu
    $email = $thisUser.firstname + “.” + $thisUser.lastname + “@” + $thisUser.domain + “.edu”
    $tempUserObj = @{
        FirstName = $thisuser.FirstName
        LastName = $thisuser.LastName
        Domain = $thisuser.Domain
        Email = $email
    } 
    #append our temporary object to $usermail
    $usermail += $tempUserObj
}

$usermail