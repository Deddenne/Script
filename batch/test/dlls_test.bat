set mydate=%date:~6,4%%date:~3,2%%date:~0,2%

>output-%mydate%.txt (
    echo Poste : 10.3.6.46
    IF EXIST not "\\10.3.6.46\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting" md "\\10.3.6.46\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"
    echo.
    echo --------- copy DLL
    xcopy /y "\\srv-data\Louis Pion\Informatique\13-Distrib\Nepting" "\\10.3.6.46\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting"   
    timeout 5 > NUL
    echo.
    echo --------- Cegid.CPOS.Nepting.dll
    "\\10.3.6.46\c$\Program Files (x86)\Cegid\Cegid Retail\Cegid Retail Y2 23.0\Front Office\CPOS_DLLManager.exe" -reg "\\10.3.6.46\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting\Cegid.CPOS.Nepting.dll"
    echo.
    echo --------- NepPosDLL32.dll
    "\\10.3.6.46\c$\Program Files (x86)\Cegid\Cegid Retail\Cegid Retail Y2 23.0\Front Office\CPOS_DLLManager.exe" -reg "\\10.3.6.46\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting\NepPosDLL32.dll"
    echo.
    echo.
    echo ---------------------------------------
)

@REM ----------- Résultat -----------
@REM Poste : 10.3.6.46

@REM --------- copy DLL
@REM \\srv-data\Louis Pion\Informatique\13-Distrib\Nepting\Cegid.CPOS.Nepting.dll
@REM \\srv-data\Louis Pion\Informatique\13-Distrib\Nepting\install_register_nepting.bat
@REM \\srv-data\Louis Pion\Informatique\13-Distrib\Nepting\NepPosDLL32.dll
@REM 3 fichier(s) copié(s)

@REM --------- Cegid.CPOS.Nepting.dll
@REM CPOS_DLLManager
@REM Ver. 1.3 (Managing register files on version 1.0.100)
@REM Cegid Point Of Sale (CPOS) driver manager
@REM (c) CEGID 2010
@REM Checking Cegid.CPOS.Nepting.dll ...
@REM Registering Cegid.CPOS.Nepting.dll ...
@REM Cegid.CPOS.Nepting.dll has been successfully registered
@REM WARNING : Registered data has been updated.

@REM --------- NepPosDLL32.dll
@REM CPOS_DLLManager
@REM Ver. 1.3 (Managing register files on version 1.0.100)
@REM Cegid Point Of Sale (CPOS) driver manager
@REM (c) CEGID 2010
@REM Checking NepPosDLL32.dll ...
@REM WDF00004 : Le point d'entrée getPluginLoader n'est pas exporté par la DLL \\10.3.6.46\c$\Program Files (x86)\Cegid\Cegid Retail\CPOS Drivers\Nepting\NepPosDLL32.dll (MC_WrapperDefault.TMC_WrapperWin32Default.getLibrary)
@REM TODO : Vérifiez la construction de la DLL
@REM Syntax : CPOS_DLLManager -[reg [path]DllName.dll [local]|unreg DllReference [local]|list|deprecate DllReference] 

@REM ---------------------------------------
