@echo off

@REM # // -------------------------------------------------- \\ 
@REM # // ----------    Fichier batch :           ---------- \\ 
@REM # // ----------  - installer python          ---------- \\ 
@REM # // ----------  - lancer ficheir de ping    ---------- \\ 
@REM # // -------------------------------------------------- \\ 
@REM # // ----------      BY © LIN SANDRINE       ---------- \\ 
@REM # // ----------          07/11/2023          ---------- \\ 
@REM # // -------------------------------------------------- \\ 


REM Vérifier si Python est installé sinon l'installé  
python --version > nul 2>&1
if %errorlevel% == 0 (
    echo pyhton n'est ps installé sur votre système
) else (
    echo pyhton n'est ps installé sur votre système
    start /wait python-3.12.0-amd64.exe
)

start /wait python final_test_ping.py

exit 