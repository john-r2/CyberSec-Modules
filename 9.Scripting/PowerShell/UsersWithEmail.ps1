#For PowerShell Lab 4

#Grab the user file (FirstName, LastName, Domain)
cd D:\CyberSec-Modules\9.Scripting\PowerShell
$user = Import-Csv users.csv

#Create a new, empty, object
#It will have FirstName, LastName, Domain, Email when we're done
$usermail = @()

$user | ForEach-Object {
    #create the email address, example:  Luke.Skywalker@Starwars.edu
    $email = $_.firstname + “.” + $_.lastname + “@” + $_.domain + “.edu”

    #create a temporary object for our data
    $tempUserObj = New-Object System.Object

    #add our data to the correct properties of the temporary object
    $tempUserObj | Add-Member -Type NoteProperty -Name FirstName -Value $_.firstname
    $tempUserObj | Add-Member -Type NoteProperty -Name LastName -Value $_.Lastname
    $tempUserObj | Add-Member -Type NoteProperty -Name Domain -Value $_.Domain
    $tempUserObj | Add-Member -Type NoteProperty -Name Email -Value $email

    #append our temporary object to $usermail
    $usermail += $tempUserObj
}

$usermail