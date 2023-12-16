@echo off

set mydate=%date:~6,4%%date:~3,2%%date:~0,2%

>output-%mydate%.txt (
    for /f "usebackq tokens=1-4 delims=," %%a in ("ouiiiiiii.csv") do (
        echo Poste %%a : %%b
        IF EXIST not "\\%%b\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting" md "\\%%b\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
        echo.
        echo --------- copy DLL
        xcopy /y "\\srv-data\Louis Pion\Informatique\13-Distrib\Nepting" "\\%%b\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"   
        timeout 5 > NUL
        echo.
        echo --------- Cegid.CPOS.Nepting.dll
        "\\%%b\c$\Program Files (x86)\Cegid\Cegid Retail\Cegid Retail Y2 23.0\Front Office\CPOS_DLLManager.exe" -reg "\\%%b\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting\Cegid.CPOS.Nepting.dll"
        echo.
        echo --------- NepPosDLL32.dll
        "\\%%b\c$\Program Files (x86)\Cegid\Cegid Retail\Cegid Retail Y2 23.0\Front Office\CPOS_DLLManager.exe" -reg "\\%%b\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting\NepPosDLL32.dll"
        echo.
        echo.
        echo ---------------------------------------
        )
)