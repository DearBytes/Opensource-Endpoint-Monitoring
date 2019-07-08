# Open Source Endpoint monitoring

This repository contains all the config files and scripts used for our Open Source Endpoint monitoring project. We will be submitting pull request to all the different projects. This is just there as an archive of what we spoke about.

![Architecture](images/arch.png)

## Def Con 27 Blue Team Village video is available
[![Watch the talk](https://img.youtube.com/vi/qs6sTVffx8Q/maxresdefault.jpg)](https://www.youtube.com/watch?v=qs6sTVffx8Q)

## Contents

### Sigma rules
* sysmon_wmi_persistance.yml 
    - Detect the creation of EventConsumers containing suspicisous binaries.  
* sysmon_wmi_spawn_susp.yml 
    - Detect wmiprvse.exe spawning suspicious binaries.
* Correlation_squiblyfoo.yml
    - Ghetto correlation of the two rules we use to detect squiblyfoo.
* sysmon_squiblyfoo.yml
    - looks at specific commandline arguments and strings in the path.
* sysmon_squiblyfoo_fileCreation.yml
    - looks for the creation of WsmPty.xsl or WsmTxt.xsl.
* sysmon_rogue_powershell.yml
    - detect loading of the powershell.dll's by powershell.exe less powershell hosts.
* sysmon_unicorn.yml
    - detect unicorn.py based on commandline arguments (version specific approach, look at powershell_mem_inject_keywords for a more thorough approach)
* powershell_mem_inject_keywords.yml
    - detects memory injection based on PowerShell script block logging. (Such as unicorn.py)
* sysmon_shell_spawn_susp_program.yml
    - Detects a suspicious child process of a Windows shell
* sysmon_office_spawn_susp.yml
    - Detects a Windows command line executable started from Microsoft Word, Excel, Powerpoint, Publisher and Visio.
* sysmon_susp_system_create_proc.yml
    - Detects system utilities being executed by 'NT AUTHORITY\SYSTEM'. (e.g. whoami, nslookup and ipconfig)
* sysmon_potential_miners.yml
    - Detects XMRIG command line parameters

### Sysmon config
It's a modified version of the [SwiftOnSecurity Sysmon config](https://github.com/SwiftOnSecurity/sysmon-config). We added the following things:
* Log the loading of specific powershell dll's, if loaded outside of powershell.exe might be an indication of a powershell.exe less powershell host. Such as p0wnedShell.
    - System.Management.Automation.Dll
    - System.Management.Automation.ni.Dll
    - System.Reflection.Dll
* Log the creation of .xsl files, in this case for squiblyfoo detection. However xsl files can be used to execute VBScript/Jscript when [wscript.exe is blocked](http://subt0x11.blogspot.com/2018/04/wmicexe-whitelisting-bypass-hacking.html).
* Log the creation of [.SettingContent-ms files](https://posts.specterops.io/the-tale-of-settingcontent-ms-files-f1ea253e4d39). 
* Log the creation of WmiEventFilter, WmiEventConsumer, WmiEventConsumerToFilter. Can be used to detect persistence trough [WMI EvenConsumers](https://d.uijn.nl/2016/05/09/wmi-some-persistence-ideas/). 

### Demo files 
* squiblyfoo.py 
    - an RTA script that emulates SquiblyFoo. It drops WsmPty.xsl and WsmTxt.xsl and executes cscript with all the different argument options.
* WMIdemo.bat
    - Emulates the entire WMI persistence mechanism and cleans up afterwards. 
* SetWMI.ps1
    - Creats an EventConsumer/Filter to check if taskmgr.exe spawns, then starts notepad.exe.
* DelWMI.ps1
    - Removes the EventConsumer/Filter
* Emotet word document containing [Daniel Bohannon's Invoke-DOSFuscation](https://github.com/danielbohannon/Invoke-DOSfuscation) can be downloaded here: https://app.any.run/tasks/df25be59-0a0a-4ea3-a449-12437d9bff5c
* unicorn stager can be generated using the [project](https://github.com/trustedsec/unicorn).


### Paper
For those of you who want to read some more we added our paper called Fileless Threats - Analysis and Detection.
