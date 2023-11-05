@echo off
setlocal enabledelayedexpansion

REM Ouvrir le fichier texte en lecture
set "input_file=PingResults.txt"
set "output_file=votre_fichier.csv"

if not exist "%input_file%" (
    echo Le fichier texte %input_file% n'existe pas.
    exit /b
)

REM Créer le fichier CSV avec l'en-tête
(echo "All OK","Only 50 OK","Only 51 OK","Only 70 OK","Only 90 OK","Only 50,51 OK","Only 50,70 OK","Only 50,90 OK","Only 51,70 OK","Only 51,90 OK","Only 70,90 OK","None - KO") > "%output_file%"

@echo off
(
  echo "Colonne 1","Colonne 2","Colonne 3","Colonne 4","Colonne 5"
) > output.csv

setlocal enabledelayedexpansion
set count10_1_1_ok=0

for /f "tokens=2,4,5" %%a in (PingResults.txt) do (
  set "ip=%%a"
  set "status=%%b"
  
  if "!status!"=="reachable" (
    set /a count10_1_1_ok+=1
  )
  
  if "!count10_1_1_ok!"=="4" (
    set col=1
  ) else if "!count10_1_1_ok!"=="3" (
    set col=2
  ) else if "!count10_1_1_ok!"=="2" (
    set col=3
  ) else if "!count10_1_1_ok!"=="1" (
    set col=4
  ) else (
    set col=5
  )
  
  echo !col! >> output.csv
)
