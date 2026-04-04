# <span id="selfid"></span>The use of selfid

The [selfid](mk:@MSITStore:kcmlrefman.chm::/selfid.htm) application is a Kerridge UNIX utility to determine the type of the terminal connected to it. However, having successfully recognised KClient it can provide many additional advantages to the UNIX .profile script.

##### Force text mode

selfid -f

Used in the .profile this will force the text window to appear. If the .profile contains a menu or otheruser input then KClient will appear to hang unless the user has selected the text window option in KClient.The alternative is to use this command which will direct KClient to show the text window anyway.

##### KClient command-line arguments

selfid -c

This selfid command will retrieve any kclient command-line arguments. These were arguments passed using the -C switch to kclient. They can also be set using the Application Command Line field in the KCML client properties. KCML will parse this field up into a number of arguments separated by whitespace. This is an easy way to automate .profile menu selections, allowing you to have a separate KClient icon for each menu option to take you straight into the application. Thus for forms based applications you need never see a text window.

This command replaces the usual selfid command by setting KTERM, WDWVERSION, arg1, arg2, .., argn and argc environment variables. There are *argc* arguments (which may be 0) and these are *arg1*, *arg2* etc. To apply this the eval shell command can be used as the output of selfid -c is already in the correct format. eval \`selfid -c\`

##### A typical .profile

eval \`selfid -c\` export KTERM if \[ "\$arg1" = "" \] then \# no preset arguments, do normal menu request, start by forcing text window selfid -f \# lots of echos to display menu options \# echo ... \# read in the menu command read arg1 fi \# Now arg1 contains either preset choice or response from menu case \$arg1 in \# menu choices in the usual way esac
