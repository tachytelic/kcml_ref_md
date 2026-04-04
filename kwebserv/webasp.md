Connection Manager ASP Support

The Connection Manager has support for [ASP/VSP](mk:@MSITStore:kcmlrefman.chm::/asp.htm) systems. This is done by defining each ASP system in a [service](systemconf.htm#services) within kconf.xml. The service would define its own value of [SYSTEMID](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SYSTEMID) so that it has its own private [\$PSTAT](mk:@MSITStore:kcmlrefman.chm::/$PSTAT.htm) area and licence file.

To ensure security, each service should define its own private [valid user](systemconf.htm#validusr), [valid client](systemconf.htm#validip) and [admin user](systemconf.htm#adminusr) access control lists. This will prevent users from one ASP service from accessing data from other ASP services.

Startup and shutdown scripts, as run by */etc/inittab*, */sbin/init.d* or */etc/rc\*.d*, on ASP systems can be quite complex. Scripts of this type are usually used to

- increase the size the \$PSTAT area using [bkstat -x, -y](mk:@MSITStore:kcmlrefman.chm::/bkstat.htm)
- start [global library processes](mk:@MSITStore:kcmlrefman.chm::/TutorialGlobal.htm)
- start the [Remote Licence deamon](mk:@MSITStore:kcmlrefman.chm::/kplicserver.htm)

These scripts may also which to use environment variables that are set in a [service's](systemconf.htm#services) environment, which would be hard to implement using script commands.\
To simplify the management of the environment the Connection Manager can be used to **initialize** a service.\
The service needs to specify an [Startup script](systemconf.htm#services) in kconf.xml. This is the location of a shell script which contains the necessary commands for starting service-specific programs, ect. The ASP server's boot script can then call kwebserv using the **-s** and **-i** command line flags. When executed in this mode, kwebserv will load the environment from the [general](systemconf.htm#genenv) and [service](systemconf.htm#services) sections of kconf.xml. The [Startup script](systemconf.htm#services) is then executed with the remaining command line arguments that were passed to kwebserv.

For example, if we have a service called **Accounts**, which defines an [Startup script](systemconf.htm#services) of **/user1/accounts/scripts/start.ksh**\
The server's boot script could contain a command of the form


    kwebserv -s Accounts -i start

After loading the environment for the *Accounts* service, kwebserv would execute the command


    ksh /user1/accounts/scripts/start.ksh start

The shell interpreter that is used, in this case *ksh*, to execute the script is determined by the value of \$SHELL or \$SH. If neither of these environment variables are set, then a default of /bin/sh is used. If the script produces any output, then this is displayed.\
After the script has been executed, kwebserv will print a message containing the command and its return code.


    kwebserv: Info: /user1/accounts/scripts/start.ksh start returned 0

These messages, along with any script output, can be redirected to a log file, ie


    kwebserv -s Accounts -i start >/user1/boot.log 2>&1

Alternatively, if no *-s Service* flag is used, then kwebserv will enumerate over all services. In this mode kwebserv will execute a command of the form


    kwebserv -s servicename argmuents

for each service in *kconf.xml*. This eliminates any need to write shell script code to enumerate all available ASP systems.

##### See Also:

[ASP](mk:@MSITStore:kcmlrefman.chm::/asp.htm) support, [Connection Manager](connmgr.htm), [Remote Adminstration Functions](adminfns.htm)
