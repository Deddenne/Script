@echo off

REM Script pour définir un logiciel au démarrage, ici AirCall
REM PAR ©DEDDENNE 
REM 25/05/2023

REM ouvrir le dossier des logiciels par défaut pour voir si le programme y est bien (s'ouvre en fin de programme)
explorer c:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\

REM variables chemins du logiciel et chemin du raccourci 
set "targetPath=C:\Users\%USERNAME%\AppData\Local\Aircall\Aircall.exe"
set "shortcutPath=C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Aircall.lnk"

set "vbsScript=%temp%\CreateShortcut.vbs"

REM Créer un fichier VBScript temporaire pour créer le raccourci
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%vbsScript%"
echo sLinkFile = "%shortcutPath%" >> "%vbsScript%"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%vbsScript%"
echo oLink.TargetPath = "%targetPath%" >> "%vbsScript%"
echo oLink.Save >> "%vbsScript%"

REM Exécuter le fichier VBScript pour créer le raccourci
cscript /nologo "%vbsScript%"

REM Supprimer le fichier VBScript temporaire
del "%vbsScript%"

echo AirCall a ete ajouter au dossier demarrage et sera etre lancer a chaque demarage demarrage.

REM Remaque : %username% donne le nom de l'utilisateur , %userprofile% donne le chemin du dossier de l'utilisateur