$new_name = Read-Host "Entrez l'identifiant actuel de l'utilisateur "
Write-Host " "
$old_name = Read-Host "Entrez l'ancien identifiant de l'utilisateur dont vous voulez changer le nom de dossiers "
Write-Host " "

# Obtenez la liste des dossiers dans le chemin parent
$chemin_users = "C:\Users"

# Récupérer la liste de tous les dossiers des utilisateurs
$dossiersUtilisateurs = Get-ChildItem $chemin_users -Directory

# Liste pour stocker les dossiers similaires trouvés
$dossiersSimilairesTrouves = @()

# Variable pour sortir de la boucle while
$validfoledername = $false

# Vérifier l'ancien dossier utilisateur
while ( -not $validfoledername) {
	# Parcourez chaque dossier utilisateur et comparez le nom avec votre variables
	foreach ($dossier in $dossiersUtilisateurs) {
		if ($dossier.Name -eq $old_name) {
			$dossiersSimilairesTrouves = $null 
		}
		elseif ($dossier.Name -match $old_name) {
			# Stocker les dossiers similaires trouvés dans la liste
			$dossiersSimilairesTrouves += $dossier
		}
	}
	
	# Vérifier combien de comptes trouvé 
	if ($dossiersSimilairesTrouves.Count -eq 0){
		$dossierChoisi = $old_name
		$validfoledername = $true
	} 
	elseif ($dossiersSimilairesTrouves.Count -gt 0) {
		Write-Host "Le dossier que vous essayez de trouver n'existe pas. Cependant, voici les dossiers similaires :"
		# Afficher les dossiers similaires trouvés
		for ($i = 0; $i -lt $dossiersSimilairesTrouves.Count; $i++) {
			$choice = $i + 1
			Write-Host "$choice. $($dossiersSimilairesTrouves[$i])"
		}
		
		# Demander à l'admin de choisir un utilisateur parmi la liste
		$selectedFolder = Read-Host "Sélectionnez le numéro du dossier à utiliser : "
		$selectedFolder = $selectedFolder - 1  # Soustraire 1 pour correspondre à l'index dans la liste

		if (($selectedFolder -ge 0) -and ($selectedFolder -lt $dossiersSimilairesTrouves.Count)) {
			$dossierChoisi = $dossiersSimilairesTrouves[$selectedFolder]
			Write-Host "Vous avez selectionne le dossier utilisateur '$dossierChoisi'."	
			$validfoledername = $true
		} else {
			Write-Host "Choix invalide. Entrer un numéro correct."
		}
	}
}

# Sélectinner tous les noms d'utilisateurs
$verify_new_name = Get-WmiObject -Class Win32_UserAccount | Where-Object {$_.Name -match "$new_name"}  | Select-Object -ExpandProperty Name

# Liste pour stocker les dossiers similaires trouvés
$nameSimilairesTrouves = @()

# Variable pour sortir de la boucle while
$validname = $false

# Vérifier l'id utilisateur
while ( -not $validname) {
	# Parcourez chaque dossier utilisateur et comparez le nom avec votre variables
	foreach ($valid_name in $verify_new_name) {
		if ($verify_new_name -eq $new_name) {
			$nameSimilairesTrouves = $null 
		}
		elseif ($verify_new_name -match $new_name) {
			# Stocker les dossiers similaires trouvés dans la liste
			$nameSimilairesTrouves += $verify_new_name
		}
	}
	
	# Vérifier combien de comptes trouvé 
	if ($nameSimilairesTrouves.Count -eq 0){
		$nameChoisi = $new_name
		$validname = $true
	} 
	elseif ($nameSimilairesTrouves.Count -gt 0) {
		Write-Host "Le dossier que vous essayez de trouver n'existe pas. Cependant, voici les dossiers similaires :"
		# Afficher les dossiers similaires trouvés
		for ($i = 0; $i -lt $nameSimilairesTrouves.Count; $i++) {
			$choice = $i + 1
			Write-Host "$choice. $($nameSimilairesTrouves[$i])"
		}
		
		# Demander à l'admin de choisir un utilisateur parmi la liste
		$selectedUser = Read-Host "Sélectionnez le numéro du dossier à utiliser : "
		$selectedUser = $selectedUser - 1  # Soustraire 1 pour correspondre à l'index dans la liste

		if (($selectedUser -ge 0) -and ($selectedUser -lt $nameSimilairesTrouves.Count)) {
			$nameChoisi = $nameSimilairesTrouves[$selectedUser]
			Write-Host "Vous avez selectionne le dossier utilisateur '$nameChoisi'."	
			$validname = $true
		} else {
			Write-Host "Choix invalide. Entrer un numéro correct."
		}
	}
}

# Récupérer le SID de l'utilisateur
$utilisateur_SID = Get-WmiObject -Class Win32_UserAccount | Where-Object {$_.Name -eq "$nameChoisi"} | Select-Object SID
if ($utilisateur_SID -ne '') {
	$string = "$utilisateur_SID" #on obtient : "@{SID=S-1-5-21-677101690-4233763004-1632724977-2692}"
	$utilisateur_SID = $string.Substring(6, $string.Length - 7)
	Write-Host "SID de $dossierChoisi : $utilisateur_SID"
}
else {
	Write-Host "Aucun SID trouver, veuillez relancer le script et entrer un numéro correct."
}

# Création des paths 
$old_path= "C:\Users\" + $dossierChoisi
$new_path = "C:\Users\" + $nameChoisi

# construire le chemin d'accès complet à la clé de profil utilisateur
$profilekeypath = "hklm:\software\microsoft\windows nt\currentversion\profilelist\$utilisateur_SID"

# vérifier si la clé de profil utilisateur existe
if (test-path $profilekeypath) {
    # récupérer la valeur "profileimagepath" de la clé de profil utilisateur
    $profileimagepath = (get-itemproperty -path $profilekeypath).profileimagepath

    # afficher le chemin d'accès du profil utilisateur
    write-output "le chemin d'acces du profil utilisateur est : $profileimagepath"
	
    # modifier la valeur "profileimagepath" de la clé de profil utilisateur
	set-itemproperty -path $profilekeypath -name "profileimagepath" -value $new_path
}
else {
	write-output "la clé de profil utilisateur n'a pas été trouvée."
}

# renommer le dossier de l'utilisateur
rename-item -path "$old_path" -newname "$new_name"

# créer la liaison  
new-item -itemtype symboliclink -path "$old_path" -target "$new_path"

write-output  "L'utilisateur $nameChoisi peut utiliser sa session sans problème."


read-host "appuez pour quitter ..."$new_name = Read-Host "Entrez l'identifiant actuel de l'utilisateur "
Write-Host " "
$old_name = Read-Host "Entrez l'ancien identifiant de l'utilisateur dont vous voulez changer le nom de dossiers "
Write-Host " "

# Obtenez la liste des dossiers dans le chemin parent
$chemin_users = "C:\Users"

# Récupérer la liste de tous les dossiers des utilisateurs
$dossiersUtilisateurs = Get-ChildItem $chemin_users -Directory

# Liste pour stocker les dossiers similaires trouvés
$dossiersSimilairesTrouves = @()

# Variable pour sortir de la boucle while
$validfoledername = $false

# Vérifier l'ancien dossier utilisateur
while ( -not $validfoledername) {
	# Parcourez chaque dossier utilisateur et comparez le nom avec votre variables
	foreach ($dossier in $dossiersUtilisateurs) {
		if ($dossier.Name -eq $old_name) {
			$dossiersSimilairesTrouves = $null 
		}
		elseif ($dossier.Name -match $old_name) {
			# Stocker les dossiers similaires trouvés dans la liste
			$dossiersSimilairesTrouves += $dossier
		}
	}
	
	# Vérifier combien de comptes trouvé 
	if ($dossiersSimilairesTrouves.Count -eq 0){
		$dossierChoisi = $old_name
		$validfoledername = $true
	} 
	elseif ($dossiersSimilairesTrouves.Count -gt 0) {
		Write-Host "Le dossier que vous essayez de trouver n'existe pas. Cependant, voici les dossiers similaires :"
		# Afficher les dossiers similaires trouvés
		for ($i = 0; $i -lt $dossiersSimilairesTrouves.Count; $i++) {
			$choice = $i + 1
			Write-Host "$choice. $($dossiersSimilairesTrouves[$i])"
		}
		
		# Demander à l'admin de choisir un utilisateur parmi la liste
		$selectedFolder = Read-Host "Sélectionnez le numéro du dossier à utiliser : "
		$selectedFolder = $selectedFolder - 1  # Soustraire 1 pour correspondre à l'index dans la liste

		if (($selectedFolder -ge 0) -and ($selectedFolder -lt $dossiersSimilairesTrouves.Count)) {
			$dossierChoisi = $dossiersSimilairesTrouves[$selectedFolder]
			Write-Host "Vous avez selectionne le dossier utilisateur '$dossierChoisi'."	
			$validfoledername = $true
		} else {
			Write-Host "Choix invalide. Entrer un numéro correct."
		}
	}
}

# Sélectinner tous les noms d'utilisateurs
$verify_new_name = Get-WmiObject -Class Win32_UserAccount | Where-Object {$_.Name -match "$new_name"}  | Select-Object -ExpandProperty Name

# Liste pour stocker les dossiers similaires trouvés
$nameSimilairesTrouves = @()

# Variable pour sortir de la boucle while
$validname = $false

# Vérifier l'id utilisateur
while ( -not $validname) {
	# Parcourez chaque dossier utilisateur et comparez le nom avec votre variables
	foreach ($valid_name in $verify_new_name) {
		if ($verify_new_name -eq $new_name) {
			$nameSimilairesTrouves = $null 
		}
		elseif ($verify_new_name -match $new_name) {
			# Stocker les dossiers similaires trouvés dans la liste
			$nameSimilairesTrouves += $verify_new_name
		}
	}
	
	# Vérifier combien de comptes trouvé 
	if ($nameSimilairesTrouves.Count -eq 0){
		$nameChoisi = $new_name
		$validname = $true
	} 
	elseif ($nameSimilairesTrouves.Count -gt 0) {
		Write-Host "Le dossier que vous essayez de trouver n'existe pas. Cependant, voici les dossiers similaires :"
		# Afficher les dossiers similaires trouvés
		for ($i = 0; $i -lt $nameSimilairesTrouves.Count; $i++) {
			$choice = $i + 1
			Write-Host "$choice. $($nameSimilairesTrouves[$i])"
		}
		
		# Demander à l'admin de choisir un utilisateur parmi la liste
		$selectedUser = Read-Host "Sélectionnez le numéro du dossier à utiliser : "
		$selectedUser = $selectedUser - 1  # Soustraire 1 pour correspondre à l'index dans la liste

		if (($selectedUser -ge 0) -and ($selectedUser -lt $nameSimilairesTrouves.Count)) {
			$nameChoisi = $nameSimilairesTrouves[$selectedUser]
			Write-Host "Vous avez selectionne le dossier utilisateur '$nameChoisi'."	
			$validname = $true
		} else {
			Write-Host "Choix invalide. Entrer un numéro correct."
		}
	}
}

# Récupérer le SID de l'utilisateur
$utilisateur_SID = Get-WmiObject -Class Win32_UserAccount | Where-Object {$_.Name -eq "$nameChoisi"} | Select-Object SID
if ($utilisateur_SID -ne '') {
	$string = "$utilisateur_SID" #on obtient : "@{SID=S-1-5-21-677101690-4233763004-1632724977-2692}"
	$utilisateur_SID = $string.Substring(6, $string.Length - 7)
	Write-Host "SID de $dossierChoisi : $utilisateur_SID"
}
else {
	Write-Host "Aucun SID trouver, veuillez relancer le script et entrer un numéro correct."
}

# Création des paths 
$old_path= "C:\Users\" + $dossierChoisi
$new_path = "C:\Users\" + $nameChoisi

# construire le chemin d'accès complet à la clé de profil utilisateur
$profilekeypath = "hklm:\software\microsoft\windows nt\currentversion\profilelist\$utilisateur_SID"

# vérifier si la clé de profil utilisateur existe
if (test-path $profilekeypath) {
    # récupérer la valeur "profileimagepath" de la clé de profil utilisateur
    $profileimagepath = (get-itemproperty -path $profilekeypath).profileimagepath

    # afficher le chemin d'accès du profil utilisateur
    write-output "le chemin d'acces du profil utilisateur est : $profileimagepath"
	
    # modifier la valeur "profileimagepath" de la clé de profil utilisateur
	set-itemproperty -path $profilekeypath -name "profileimagepath" -value $new_path
}
else {
	write-output "la clé de profil utilisateur n'a pas été trouvée."
}

# renommer le dossier de l'utilisateur
rename-item -path "$old_path" -newname "$new_name"

# créer la liaison  
new-item -itemtype symboliclink -path "$old_path" -target "$new_path"

write-output  "L'utilisateur $nameChoisi peut utiliser sa session sans problème."


read-host "appuez pour quitter ..."