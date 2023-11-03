@echo off

set "LogFile=PingResults.txt"
If exist %LogFile% Del %LogFile%

echo(
echo      ------- Ping status of targets hosts -------
echo(
(
echo ******************************************************
    echo   PingTest executed on %Date% @ Time %Time%
    echo ******************************************************
    echo(
) > %LogFile%

Setlocal EnableDelayedExpansion

for /l %%x in (1,1,2) do (
    for /l %%y in (1,1,4) do (
        for %%s in (50,51,70,90) do (
            ping -n 1 "10.%%x.%%y.%%s" | find "TTL=" >nul
            REM echo 10.%%x.%%y.%%s
            if errorlevel 1 (
                echo Host '10.%%x.%%y.%%s' not reachable KO & echo Host "10.%%x.%%y.%%s" not reachable KO >>%LogFile%
            ) else (
                echo Host '10.%%x.%%y.%%s' reachable OK & echo Host "10.%%x.%%y.%%s" reachable KO >>%LogFile%
            )
        )
    )
)


EndLocal
Start "" %LogFile%
pause>nul & exit


