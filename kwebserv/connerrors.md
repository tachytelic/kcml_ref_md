Connection Manager Errors

Any errors that the [Connection Manager](connmgr.htm) produces are passed back to KClient and written to the [system log](mk:@MSITStore:kcmlrefman.chm::/syslog.htm).\
These will then be displayed by KClient in a message box.

<div id="ClickDiv">

<u>Click here to view an example</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example</u>

This example is caused by the system administrator creating a /etc/nologin file with the contents


    System locked for software upgrade.

<img src="bitmaps/kclienterror.png" data-border="1" alt="Connection Manager error displayed by KClient" />

</div>

Here are a list of errors that may occurr.

Example Error message

Platform

Cause

Remedy

Cannot find server program '/usr/local/kcml/kcml'

All

The kcml executable is not in the same directory as the Connection Manager, kwebserv

Make sure that the kcml and kserver.so files exist in the same directory as kwebserv

Access to '/usr/local/kcml/kcml' not allowed

Unix

The file permissions on the kcml executable do not allow you to run the program

Use *chmod* and *chown* to set the correct permissions on kcml and kserver.so

ERROR: Access denied.\
Problem finding service 'Sales'

All

The [KClient Connection](mk:@MSITStore:kclient.chm::/remoteconnection.htm) specified a service called *Sales* which does not exist in kconf.xml

Check spelling of the service name in the KClient connection, or add the service to kconf.xml

ERROR: Access denied.\
Problem setting service 'Sales'

All

The service's environment section tried to load an include file which doesn't exist

Check that the file exists or the pathname in kconf.xml is correct.

ERROR: Access denied for client '11.22.33.44'

All

A connection was made from a machine with an IP address of *11.22.33.44*, but this address was not allowed by the [valid clients](systemconf.htm#validip) access control list.

Add the 11.22.33.44 address to the valid clients section, or add the pattern 11.22.33.\* to allow the subnet.

ERROR: Access denied for user 'fred'

All

A user, called *fred*, attempted to login but was not allowed by the [valid users](systemconf.htm#validusr) access control list.

Add user *fred* to the valid users access control list.

ERROR: Access denied to service 'Sales' for user 'fred'

All

A user, called *fred*, attempted to login to the *Sales* service but was not allowed by the the services's private [valid users](systemconf.htm#services) access control list.

Add user *fred* to the valid users access control list for service *Sales*.

ERROR: Access to service 'Sales' denied for client '11.22.33.44'

All

A connection to service *Sales* was made from a machine with an IP address of *11.22.33.44*, but this address was not allowed by the the services's private [valid client](systemconf.htm#services) access control list.

Add the address *11.22.33.44* or pattern *11.22.33.\** to the valid clients access control list for service *Sales*.

ERROR: KClient access to service 'Sales' is not allowed

All

The [connection](systemconf.htm#services) property of service *Sales* has been set to false

Set the \<connection\> property to true

Cannot access home directory

Unix

The user's home directory does not exist or it has bad file permissions

Check home directory is spelt correctly in the account properties. Check the directory exists. Change the ownership or permissions of the home directory using *chown* or *chmod*.

Access Denied

Unix

The user's home directory doesn't contain a [.kcmlLogin](auth.htm) file

Use the [Look up user name](overview.htm) links or create a .kcmlLogin file manually

System locked by /etc/nologin

Unix

The root super-user as locked the system with an empty /etc/nologin file

Wait until the system has been unlocked

There have been too many unsuccessful login attempts

AIX

The user's account has been disabled because they have consecutively failed to login too many times.

Have the system administrator reset the account

Your account has been locked

AIX

The user's account have been disabled by the system administrator

Have the system administrator unlock the account

You are not allowed to login at this time

AIX

The account is only allowed to login at certain times

Only login when you are allowed to

Cannot open PAM configuration file '/etc/pam.d/kcc'. Users may not be able to login on port 790

Linux

Missing PAM configuration file

Need to create a set of authentication rules for [PAM](pam.htm)

Failed to initialise PAM for service 'kcc' ...

AIX 5.2, HPUX 11, Linux, Solaris

PAM failed to start up, probably due to a error in its configuration files.

Check the [syslog](mk:@MSITStore:kcmlrefman.chm::/syslog.htm) for errors from the PAM library. Check the OTHER rule in */etc/pam.conf*, or for Linux */etc/pam.d/other*

SOAP Error for URL 'Sales/stockInfo': Failed to change to user 'fred'

Unix

The *stockInfo* SOAP service has been setup to execute as user *fred*, however the Connection Manager was unable to assume this user's identity

Check that the user account is valid, for example use this account to login a KClient session.

SOAP Error for URL 'Sales/stockInfo': Access to service 'Sales' for user 'fred' is not allowed

Unix

The *Sales* service has a *stockInfo* SOAP interface whose is executed as user *fred*, but this user ID is not in the service's [valid users](systemconf.htm#services) access control list

Change the SOAP service's user ID to a user that exists in the service's access control list\
or, add user *fred* to the service's access control list

##### See Also:

[Connection Manager](connmgr.htm), [Connecting to a service](connserv.htm)
