@echo off
    setlocal enableextensions enabledelayedexpansion

    rem the range of IP 
    set /p ip_range=Quel est la plage IP (XX.XX.XX) ? 

    :test_ip
        rem fist IP of the range
        set /p ip_first=Quel est la premiere IP de votre ranger ? 
        
        rem last IP of the range
        set /p ip_last=Quel est la derniere IP de votre ranger  ? 
    goto :done

    if (%ip_first% GTR %ip_last%) goto :test_ip  
    rem else FOR /L %%i IN (%ip_first%,1,%ip_last%) DO PING %ip_range%.%%i -n 1 


    

