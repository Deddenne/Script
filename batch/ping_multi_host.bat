@echo off
Title Multi-Ping hosts Tester with colors by Hackoo 2016
call :init
set "nomPC=listePC.txt"
If Not exist %nomPC% goto error
mode con cols=70 lines=35
set "LogFile=PingResults.txt"
If exist %LogFile% Del %LogFile%
echo(
call :color 0E "      ------- Ping status of targets hosts -------" 1
echo(
(
    echo ******************************************************
    echo   PingTest executed on %Date% @ Time %Time%
    echo ******************************************************
    echo(
) > %LogFile%
Setlocal EnableDelayedExpansion
for /f "usebackq delims=" %%a in ("%nomPC%") do (
    ping -n 1 %%a | find "TTL=" >nul
    if errorlevel 1 (
        call :color 0C " Host %%a not reachable KO" 1 & echo Host %%a not reachable KO >>%LogFile%
    ) else (
        call :color 0A " Host %%a reachable OK" 1 & echo Host %%a reachable OK >>%LogFile%
    )
)
EndLocal
Start "" %LogFile%
pause>nul & exit
::************************************************************************************* 
:init
prompt $g
for /F "delims=." %%a in ('"prompt $H. & for %%b in (1) do rem"') do set "BS=%%a"
exit /b
::*************************************************************************************
:color
set nL=%3
if not defined nL echo requires third argument & pause > nul & goto :eof
if %3 == 0 (
    <nul set /p ".=%bs%">%2 & findstr /v /a:%1 /r "^$" %2 nul & del %2 2>&1 & goto :eof
) else if %3 == 1 (
    echo %bs%>%2 & findstr /v /a:%1 /r "^$" %2 nul & del %2 2>&1 & goto :eof
)
exit /b
::*************************************************************************************
:error
mode con cols=70 lines=3
color 0C
cls
echo(
 echo   ATTENTION !!!  Verifier bien si le fichier "%nomPC%" existe !
pause>nul & exit
::*************************************************************************************





















You can try this solution :

@echo off
Title Ping Test
set "URLS=URLS.txt"
set "LogFile=PingResults.txt"
If exist %LogFile% Del %LogFile%
(
    echo ******************************************************
    echo   PingTest executed on %Date% @ Time %Time% 
    echo ******************************************************
    echo(
) > %LogFile%

Setlocal EnableDelayedExpansion
for /f "usebackq delims=" %%a in ("%URLS%") do (
    for /f "tokens=2 delims=[]" %%b in ('ping -n 1 %%a') do set "ip=%%b"
        ping -n 1 %%a>nul && set "msg=%%a : !ip! ALive ok" || set "msg=%%a : !ip! Dead failed to respond"
        echo !msg!
        echo !msg! >> %LogFile%
    ) 
)
EndLocal
Start "" %LogFile%
pause>nul & exit
EDIT : on 29/07/2016 @ 12:48

Another version with multi-colors : Special thanks goes to ICARUS for the color function (-_°)

enter image description here

@echo off
Rem Special thanks goes to Iracus for the color function (-_°)
mode con cols=60 lines=20
Title Multi-Ping hosts Tester with Multi-colors by Hackoo
set "URLS=URLS.txt"
set "LogFile=PingResults.txt"
If exist %LogFile% Del %LogFile%
call :init
echo(
call :color 0E "------- Ping Status of Computers hosts -------" 1
echo(
(
    echo ******************************************************
    echo   PingTest executed on %Date% @ Time %Time% 
    echo ******************************************************
    echo(
) > %LogFile%
Setlocal EnableDelayedExpansion
for /f "usebackq delims=" %%a in ("%URLS%") do (
    for /f "tokens=2 delims=[]" %%b in ('ping -n 1 %%a') do set "ip=%%b"
        ping -n 1 %%a>nul && set "msg=%%a - !ip! ALive ok" && Call :Color 0A "!msg!" 1 || set "msg=%%a - !ip! Dead failed to respond" && Call :Color 0C "!msg!" 1
        echo !msg! >> %LogFile%
    ) 
)
EndLocal
Start "" %LogFile%
pause>nul & exit

:init
prompt $g
for /F "delims=." %%a in ('"prompt $H. & for %%b in (1) do rem"') do set "BS=%%a"
exit /b

:color
set nL=%3
if not defined nL echo requires third argument & pause > nul & goto :eof
if %3 == 0 (
    <nul set /p ".=%bs%">%2 & findstr /v /a:%1 /r "^$" %2 nul & del %2 2>&1 & goto :eof
) else if %3 == 1 (
    echo %bs%>%2 & findstr /v /a:%1 /r "^$" %2 nul & del %2 2>&1 & goto :eof
)
exit /b
