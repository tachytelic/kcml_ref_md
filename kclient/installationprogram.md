# <span id="installationprogram"></span> Installation program

Kclient is installed by running an installation program SETUP.EXE This is an interactive program that will display dialogs and ask for confirmation of the suggested destination directory (this will go into the usual Kerridge default of C*:\kerridge\KCML* or the value of the registry key string value

HKEY_LOCAL_MACHINE\SOFTWARE\Kerridge\KCML\InstallPath

if defined already.

For an unattended installation run SETUP.EXE /S. The default values for each dialog will be chosen automatically.

See the [**KCML Reference Manual**](mk:@MSITStore:kcmlrefman.chm::/installers.htm) for a full overview of the Windows install programs.

For a network installation a system administrator can put the setup program in a shared directory and have the users install via a batch file from there. Other alternatives are using a web page and deploying as an ActiveX A network install can be tailored by creating a SETUP.INI file in the same directory and setting some keys. This is what the WINNT installation program will do.
