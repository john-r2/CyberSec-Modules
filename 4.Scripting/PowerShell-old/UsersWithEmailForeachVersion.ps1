#For PowerShell Lab 4

#This version uses foreach instead of Foreach-Object

#Grab the user file (FirstName, LastName, Domain)
$user = Import-Csv users.csv

#Create a new, empty, object
#It will have FirstName, LastName, Domain, Email when we're done
$usermail = @()

foreach ($thisUser in $user) {
    #create the email address, example:  Luke.Skywalker@Starwars.edu
    $email = $thisUser.firstname + “.” + $thisUser.lastname + “@” + $thisUser.domain + “.edu”

    #create a temporary object for our data
    $tempUserObj = New-Object System.Object

    #add our data to the correct properties of the temporary object
    $tempUserObj | Add-Member -Type NoteProperty -Name FirstName -Value $thisUser.firstname
    $tempUserObj | Add-Member -Type NoteProperty -Name LastName -Value $thisUser.Lastname
    $tempUserObj | Add-Member -Type NoteProperty -Name Domain -Value $thisUser.Domain
    $tempUserObj | Add-Member -Type NoteProperty -Name Email -Value $email

    #append our temporary object to $usermail
    $usermail += $tempUserObj
}