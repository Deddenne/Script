@echo off
    setlocal enableextensions enabledelayedexpansion

    rem fist IP of the range
    set /p ip_first=Quel plage d'ip voulez-vous scanner ?

    rem last IP of the range
    set /p ip_last=Quel plage d'ip voulez-vous scanner ?

    rem try some ip addresses 
    for %%i in (%ip_first% %ip_last% ) do (

        echo --------------------------------------------

        rem call with a variable to get return value
        call :validateIP %%~i ret 
        echo %%~i : return value : !ret! 

        rem call with or without variable to get errorlevel
        call :validateIP %%~i  && echo %%i is valid || echo %%i is invalid
	echo.
    )   
    exit /b 

:validateIP ipAddress [returnVariable]
    rem prepare environment
    setlocal 

    rem test if address conforms to ip address structure
    echo %~1^| findstr /b /e /r "[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*" >nul

    rem if it conforms to structure, test each octet for rage values
    if not errorlevel 1 for /f "tokens=1-4 delims=." %%a in ("%~1") do (
        if %%a gtr 0 if %%a lss 255 if %%b leq 255 if %%c leq 255 if %%d gtr 0 if %%d leq 254 set "_return=0"
    )

