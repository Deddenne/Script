@echo off
setlocal

rem Liste des ordinateurs cibles
set "ordinateurs=LAP-IT-023"

rem Nom d'utilisateur à interroger
set "nom_utilisateur=slin"

rem Boucle à travers la liste des ordinateurs
for %%i in (%ordinateurs%) do (
    echo Résultats pour %%i :
    net use \\%%i
)

endlocal