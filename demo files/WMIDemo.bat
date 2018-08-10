REM This only makes sense in the demo VM. Path should be adjusted
cd C:\Users\vks\Desktop
REM Sets the WMIFilter and WMIConsumer objects and binds them together
powershell -c .\setWMI.ps1
timeout 5
REM Triggers the WMIFilter by crating the process taskmgr.exe
start taskmgr.exe
timeout 30
REM Cleans up the VM by killing the opened process and removing the WMI objects created
taskkill /F /IM Notepad.exe
taskkill /F /IM taskmgr.exe
powershell -c .\delWMI.ps1

timeout 30  