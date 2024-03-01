Stop-Process -Force -Name 'teamviewer'
winget uninstall --disable-interactivity TeamViewer
start-process -FilePath "C:\distrib\TeamViewer_Host_Setup.exe"