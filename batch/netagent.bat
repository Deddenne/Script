@echo off
echo Installing Kaspersky administration agent...
msiexec /i "\\10.10.27.106\commun\z instal Logiciels\Kaspersky\NetAgent_11.0.0.1131\exec\Kaspersky Network Agent.msi" /qn DONT_USE_ANSWER_FILE=1 SERVERADDRESS=kscserver.mycompany.com EULA=1
echo Installation completed.
exit

