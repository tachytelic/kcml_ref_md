<span id="overview"></span>

Machine Type and Overview

This page will display information about the host server, such as the operating system version and the machine's name. The Customer's name and address, from the KCML licence file, and the server's *Machine ID* will also be displayed.\
The licence file is usually *lic.txt*. However, if [SYSTEMID](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SYSTEMID) has been set then the WebServer will look for [lic.n.txt](asp.htm) first.\

Next will be a table of [System Logs](mk:@MSITStore:kcmlrefman.chm::/syslog.htm). The filename of each system log is a link which will display the log in a table, newest entry at the top. You can also [search a system log](websyslog.htm) with the **View with filter** links. Super-users, such as *root* on Unix or *Administrator* on Windows NT/2000/XP will also have links to configure the [system logs](mk:@MSITStore:kcmlrefman.chm::/syslog.htm).\
View an example [system log](examples/syslog.htm).

The **Free disk space** link will display a table of all filesystems with their size and free space. Under Unix operating sytems, the filesystem's inode usage will also be displayed. The column headings in this table are themselves links to change the order in which the table is displayed.\
View an example [filesystem table](examples/diskspace.htm).

The **Current process list** will show a table of all processes that are running on the server. The table will show the program's name, its process ID, memory usage and the amount of processor time it has used. Under some operating systems the amount of **System time** and **Average CPU usage** is also displayed. Like the **Free disk space** table, the column headings are links which will change the order in which the table is displayed. This can be useful in tracking down processes which are using lots of memory or are taking up a lot of processor time. The **Process ID** and **Parent PID** columns are also a links which will displayed more detailed information about that particular process. Unix versions also show the **User Name** column as a link to a page showing information about the owner's account.\
**Note:** Under some operating systems non-superusers may only see their own processes.\
View an example [process list](examples/proclist.htm).

<span id="unixAccess"></span>

##### Account Properties

On Unix versions of the WebServer, there are two links for displaying the properties of user's accounts on the system; **Look up user details** and **Look up every user's details**.\
The first link will show a form in which a list of usernames, seperated by a space, comma or semi-colon, can be entered. When the form is submitted the properties of the user's accounts will be displayed. The **Look up every user's details** link will show details of every account on the system.\
The properties shown by both links include the username, full-name (or comment), numeric user- and group-IDs and the account's home directory.\
The **Access** column of this table also shows which accounts are [authorized](auth.htm) to use the connection manager, ie those accounts whose home directory has a *.kcmlLogin* file. Selecting the link in this column adds or removes the *.kcmlLogin* file thus enabling or disabling access for the selected account. When a *.kcmlLogin* file is created by these pages it will have the contents


    # Kerridge Connection Manager access key

to indicate its purpose.

##### See Also:

[Remote Adminstration Functions](adminfns.htm)
