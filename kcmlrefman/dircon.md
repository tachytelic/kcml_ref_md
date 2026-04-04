Direct Login mode for UNIX

The Direct Login mode enables KCML to be a service availabe through the Unix **inetd** TCP/IP super server. This should only be used if the end user runs KClient. It is not available for Windows. The [Connection Manager](mk:@MSITStore:kwebserv.chm::/connmgr.htm) may be a more general and appropriate solution.

Instead of being invoked indirectly by the Unix telnet daemon, in this configuration KCML is executed directly. This avoids the performance overhead associated with telnet on many systems. KCML is launched by the inetd daemon when a KClient connects and the presence of the -l [command line switch](kcml.htm) tells KCML to assume a direct connection.

KCML will handle prompting for a login and password and will authenticate the user in */etc/passswd*, set the security context to that of the user and will set the working directory to that specified for the user.

As there is no shell and no *.profile* script executed, KCML will not have access to many environment variables. These can be loaded from the \<general\> and \<service\> sections of the **kconf.xml** file by adding the [-S service_name](kcml.htm) flag to the KCML command line.

A typical line in */etc/inetd.conf* would be:

kcml stream tcp nowait root /usr/lib/kcml/kcml /usr/lib/kcml/kcml -l -S my_application In this case the *my_application* service should define a [START](EnvVars.htm#START) environment variable which is the filename of the KCML program to be executed on startup.

**NOTE**: The original *kcmlprofile* method has been withdrawn. Environment variables from the .ini format kcmlprofile should be added to the \<general\> and \<service\> sections of kconf.xml

The important thing to note is that the first argument to KCML *must* be the full path of KCML, and that one of the arguments *must* be "-l"

A typical line in /etc/services might be:

    kcml 777/tcp

Where 777 is the port number. Be careful when you choose your port number. Have a look at port-numbers in use on your system (/etc/services and the *netstat -a* command) or [RFC793](http://www.isi.edu/in-notes/iana/assignments/port-numbers) before choosing a port number
