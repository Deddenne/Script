# Paramètres de l'utilisateur
$prenom = Read-Host "Entrez le prénom du nouveau utilisateur"
$nom = Read-Host "Entrez le nom du nouveau utilisateur"
$ville = Read-Host "Entrez le nom de ville du nouveau utilisateur"
$nomouverture = $prenom.Substring(0,1) + "." + $nom
$mdp = Read-Host "Entrez le mot de passe du nouveau utilisateur"
$motdepasse = ConvertTo-SecureString -AsPlainText $mdp -Force

$fullname = $prenom + " " + $nom
$fullname = (Get-Culture).textinfo.totitlecase($fullname)

# Chemin de l'unité d'organisation et nom du groupe AD
do{
        write-host ""
        write-host "Quel est le type de l'utilisateur"
        write-host "1 - Direction"
        write-host "2 - Admin"
        write-host "3 - Compta"
        write-host "4 - Responsable"
        write-host "5 - Collaborateur"
        write-host ""
        write-host -nonewline "Entrez votre choix : "
        $choice = read-host
        $ok = $choice -match '^[12345]+$'
                
        if ( -not $ok) { write-host "Choix incorrecte" }
} until ( $ok )
    
switch -Regex ( $choice ) {
    "1"
    {
       $cheminou = "OU=Direction,OU=PROPHOT,DC=DOM-PROPHOT"
       $group = "New_Direction"
       write-host "L'utilisareur $user est affecté à l'OU Direction et au groupe Direction "
       Write-Host " "
    }
    "2"
    {
       $cheminou = "OU=Direction,OU=PROPHOT,DC=DOM-PROPHOT"
       $group = "Admin"
       write-host "L'utilisareur $user est affecté à l'OU Direction et au groupe Admin "
       Write-Host " "
    }
    "3"
    {
       $cheminou = "OU=Compta,OU=PROPHOT,DC=DOM-PROPHOT"
       $group = "Comptable"
       write-host "L'utilisareur $user est affecté à l'OU Compta et au groupe Comptable "
       Write-Host " "
    }
    "4"
    {
       $cheminou = "OU=Responsable,OU=PROPHOT,DC=DOM-PROPHOT"
       $group = "Responsable"
       write-host "L'utilisareur $user est affecté à l'OU Responsable et au groupe Responsable "
       Write-Host " "
    }
    "5"
    {
       $cheminou = "OU=Collaborateur,OU=PROPHOT,DC=DOM-PROPHOT"
       $group = "Collaborateur"
       write-host "L'utilisareur $user est affecté à l'OU Collaborateur et au groupe Collaborateur "
       Write-Host " "
    }
}


# Création de l'utilisateur
New-ADUser -Name "$fullname" -GivenName $prenom -Surname $nom -City $ville -SamAccountName $nomouverture -UserPrincipalName "$nomouverture@example.com" -AccountPassword $motdepasse -Enabled $true -Path $cheminou

# Ajout de l'utilisateur au groupe
Add-ADGroupMember -Identity $group -Members $nomouverture


Write-Host " "

Read-Host "Apppuyez sur Entrée pour quitter ... " 