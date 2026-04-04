### Object servers

KCML can act as a server for methods exposed through the [COM](ObjCOM.htm), [Corba](ObjCORBA.htm) and [SOAP](ObjSoap.htm) protocols. The methods can be invoked by either another KCML acting as a client or an application written in some other programming language that conforms to the appropriate protocol.

COM servers are special in that they are started by the COM subsystem in Windows and the name of the program to load is specified in the registry. SOAP and CORBA servers run as daemons with the program to run passed on the command line with a -p switch. In all cases the specified program is loaded and execution continues until a 'KCMLOBJECTExport() \$DECLARE function is reached whereupon the instance of KCML blocks awaiting the first method call. The methods available for the interface must be visible in the foreground of the program that has blocked.

##### Exporting an interface

The exported methods are grouped together under an interface name. The 'KCMLOBJECTExport() function is used to define the interface as well as to suspend the KCML program to await the initial method request. The first argument is always the type of the object, "COM", "Corba" or "SOAP", the second argument is the interface name and any subsequent arguments depend on the type of server. These two arguments are not case sensitive.

##### Exposing methods

The only methods that can be called in the server program must be prefixed with the interface name and an underscore. Thus in the following example the interface is *time* and the method is *.getTime()*. The name of the function is not case sensitive. Methods returning strings must have their [DEFSUB](DEFSUB.htm) name ending in \$ but the \$ is not used in the method name.

REM do any necessary initialization here 'KCMLOBJECTExport("SOAP", "time") REM do any tidy up code here \$END DEFSUB 'time_getTime\$() REM return time as string "CCCC-MM-DD HH:MM:SS" LOCAL DIM t\$24 CONVERT \#DATE TO t\$ CONVERT \#TIME TO STR(t\$,LEN(t\$)+2) RETURN t\$ \$DECLARE 'KCMLOBJECTExport(STR(), STR())
