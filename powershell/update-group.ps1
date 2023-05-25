                ##########################################################################
                #########                                                        #########
                #########      Ajouter les utilsateurs d'un OU à un groupe       #########
                #########                    [ automatisé ]                      #########
                #########                                                        #########
                #########               Réalisée le 20/04/2023                   #########
                #########                  Par Lin Sandrine                      #########
                #########                                                        #########
                ##########################################################################


# Le fichier n'est pas appliqué sur l'OU "Direction", car il peut y avoir des admins dans ce groupe.

######################################################### Ajouts des utilisateurs de l'OU "Collaborateur" au groupe "Collaborateur" #########################################################
Write-Host " "
    # Récupère les noms des utilisateurs présents dans le groupe actuel avant ajout
$groupName1 = "Collaborateur"
$members1 = Get-ADGroupMember -Identity $groupName1 | Select-Object SamAccountName

    # Récupère les noms des utilisateurs présents dans l'OU
$users_collab = Get-ADUser -Filter * -SearchBase "OU=Collaborateur,OU=PROPHOT,DC=DOM-PROPHOT" 
foreach ($user in $users_collab) {
    Add-ADGroupMember -Identity "Collaborateur" -Members $user
}
$groupName2 = "Collaborateur"
$members2 = Get-ADGroupMember -Identity $groupName2 | Select-Object SamAccountName
$diff2 = $members2 | Where-Object { $_.SamAccountName -notin $members1.SamAccountName }
if (-not $diff2_bis.SamAccountName) {  Write-Host "Aucun utilisateurs n'a été ajouté pour le groupe $groupName2" }
else {
    Write-Host "Les utilisateurs ajoutés dans le groupe $groupName2 : "
    $diff2.SamAccountName
}
Write-Host " "

######################################################### Ajouts des utilisateurs de l'OU "Compta" au groupe "Comptable" #########################################################

    # Récupère les noms des utilisateurs présents dans le groupe actuel avant ajout
$groupName1 = "Comptable"
$members1 = Get-ADGroupMember -Identity $groupName1 | Select-Object SamAccountName

    # Récupère les noms des utilisateurs présents dans l'OU
$users_compta = Get-ADUser -Filter * -SearchBase "OU=Compta,OU=PROPHOT,DC=DOM-PROPHOT" 
foreach ($user in $users_compta) {
    Add-ADGroupMember -Identity "Comptable" -Members $user
}

$groupName2 = "Comptable"
$members2 = Get-ADGroupMember -Identity $groupName2 | Select-Object SamAccountName
$diff2 = $members2 | Where-Object { $_.SamAccountName -notin $members1.SamAccountName }
if (-not $diff2_bis.SamAccountName) {  Write-Host "Aucun utilisateurs n'a été ajouté pour le groupe $groupName2" }
else {
    Write-Host "Les utilisateurs ajoutés dans le groupe $groupName2 : "
    $diff2.SamAccountName
}
Write-Host " "

######################################################### Ajouts des utilisateurs de l'OU "Responsable" au groupe "Responsable" #########################################################

# Récupère les noms des utilisateurs présents dans le groupe actuel avant ajout
$groupName1 = "Responsable"
$members1 = Get-ADGroupMember -Identity $groupName1 | Select-Object SamAccountName

    # Récupère les noms des utilisateurs présents dans l'OU
$users_resp = Get-ADUser -Filter * -SearchBase "OU=Responsable,OU=PROPHOT,DC=DOM-PROPHOT"
foreach ($user in $users_resp) {
    Add-ADGroupMember -Identity "Responsable" -Members $user
}

$groupName2 = "Responsable"
$members2 = Get-ADGroupMember -Identity $groupName2 | Select-Object SamAccountName
$diff2 = $members2 | Where-Object { $_.SamAccountName -notin $members1.SamAccountName }
if (-not $diff2_bis.SamAccountName) {  Write-Host "Aucun utilisateurs n'a été ajouté pour le groupe $groupName2" }
else {
    Write-Host "Les utilisateurs ajoutés dans le groupe $groupName2 : "
    $diff2.SamAccountName
}
Write-Host " "


######################################################### Ajouts des utilisateurs de l'OU "Responsable" au groupe "Responsable" #########################################################

# Récupère les noms des utilisateurs présents dans le groupe actuel avant ajout
$groupName1 = "Responsable"
$members1 = Get-ADGroupMember -Identity $groupName1 | Select-Object SamAccountName

    # Récupère les noms des utilisateurs présents dans l'OU
$users_resp = Get-ADUser -Filter * -SearchBase "OU=Responsable,OU=PROPHOT,DC=DOM-PROPHOT"
foreach ($user in $users_resp) {
    Add-ADGroupMember -Identity "Responsable" -Members $user
}

$groupName2 = "Responsable"
$members2 = Get-ADGroupMember -Identity $groupName2 | Select-Object SamAccountName
$diff2 = $members2 | Where-Object { $_.SamAccountName -notin $members1.SamAccountName }
if (-not $diff2_bis.SamAccountName) {  Write-Host "Aucun utilisateurs n'a été ajouté pour le groupe $groupName2" }
else {
    Write-Host "Les utilisateurs ajoutés dans le groupe $groupName2 : "
    $diff2.SamAccountName
}
Write-Host " "

######################################################### Ajouts des utilisateurs de l'OU "Direction" au groupe "New_Direction" ou "Admin" #########################################################

# Récupère les noms des utilisateurs présents dans le groupe actuel avant ajout
$groupName1 = "New_Direction"
$members1 = Get-ADGroupMember -Identity $groupName1 | Select-Object SamAccountName

$groupName1_bis = "Admin"
$members1_bis = Get-ADGroupMember -Identity $groupName1_bis | Select-Object SamAccountName


    # Récupère les noms des utilisateurs présents dans l'OU
$users_resp = Get-ADUser -Filter * -SearchBase "OU=Direction,OU=PROPHOT,DC=DOM-PROPHOT"
foreach ($user in $users_resp) {
    $result = (Get-ADPrincipalGroupMembership $user).Name
    if ($result -match "Direction" -or $result -match "Admin") { continue }
    else {
        do{
        write-host ""
        write-host "Dans quel groupe voulez-vous affecter l'utilisarteur $user"
        write-host "1 - Direction"
        write-host "2 - Admin"
        write-host ""
        write-host -nonewline "Entrez votre choix : "
        $choice = read-host
        $ok = $choice -match '^[12]+$'
                
        if ( -not $ok) { write-host "Choix incorrecte" }
        } until ( $ok )
    
        switch -Regex ( $choice ) {
            "1"
            {
                Add-ADGroupMember -Identity "New_Direction" -Members $user
                write-host "L'utilisareur $user est affecté au gorupe Direction "
                Write-Host " "
            }
            "2"
            {
                Add-ADGroupMember -Identity "Admin" -Members $user
                write-host "L'utilisareur $user est affecté au gorupe Admin'"
                Write-Host " "
            }
        }
    }
}

$groupName2 = "New_Direction"
$members2 = Get-ADGroupMember -Identity $groupName2 | Select-Object SamAccountName
$diff2 = $members2 | Where-Object { $_.SamAccountName -notin $members1.SamAccountName }
if (-not $diff2_bis.SamAccountName) {  Write-Host "Aucun utilisateurs n'a été ajouté pour le groupe $groupName2" }
else {
    Write-Host "Les utilisateurs ajoutés dans le groupe $groupName2 : "
    $diff2.SamAccountName
}

Write-Host " "

$groupName2_bis = "Admin"
$members2_bis = Get-ADGroupMember -Identity $groupName2_bis | Select-Object SamAccountName
$diff2_bis = $members2_bis | Where-Object { $_.SamAccountName -notin $members1_bis.SamAccountName }
if (-not $diff2_bis.SamAccountName) {  Write-Host "Aucun utilisateurs n'a été ajouté pour le groupe $groupName2_bis" }
else {
    Write-Host "Les utilisateurs ajoutés dans le groupe $groupName2_bis : "
    $diff2_bis.SamAccountName
}


Write-Host " "

Read-Host "Apppuyez sur Entrée pour quitter ... " 