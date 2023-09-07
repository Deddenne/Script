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



@echo off
echo Deleting Chrome Cache and Browsing History...
echo.
del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\History"

del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache\*.*"
del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Guest Profile\Cache\*.*"

SET count=0
FOR /d %%G IN ("%LOCALAPPDATA%\Google\Chrome\User Data\Profile*") DO (
	:: echo %%G
	set /a count+=1 
)


FOR /L %%F IN (1,1,10) DO (
	echo variable F : %%F
	set name_folder=%LOCALAPPDATA%\Google\Chrome\User Data\Profile %%F
	set name_folder=%name_folder%\Cache\*.*
	echo %name_folder%
	del /f/q/s "%name_folder%"
)



del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Cookies"
echo.
echo Deletion Complete!
pause


:: del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\History" # supprimer l'historique
:: del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache\*.*" # supprimer le cache 
:: del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Cookies" # supprimer les cookies
:: del /f/s/q "%LOCALAPPDATA%\Google\Chrome\User Data\Default" # NOPE , efface tout 