@echo off
echo Deleting Chrome Cache and Browsing History...
echo.
del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\History"
del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Cache"
del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Cookies"
echo.
echo Deletion Complete!
pause


:: del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\History" # supprimer l'historique
:: del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache\*.*" # supprimer le cache 
:: del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Cookies" # supprimer les cookies
:: del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Default" # NOPE , efface tout 