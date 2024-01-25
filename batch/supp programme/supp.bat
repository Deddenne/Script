@echo off

wmic product get name > text.txt
wmic product where "Name like 'Adobe%'" call uninstall /nointeractive >> text.txt

REM wmic product where "Name like 'Adobe%'" call uninstall /nointeractive