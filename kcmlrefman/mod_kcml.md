<span id="top"></span>

# Apache module mod_kcml

This module provides for KCML SOAP server connection.

<a href="module-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="module-dict.html#SourceFile" rel="Help"><strong>Source File:</strong></a> mod_kcml.c\
<a href="module-dict.html#ModuleIdentifier" rel="Help"><strong>Module Identifier:</strong></a> mod_kcml\
<a href="module-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> Available for Unix in Apache 1.3 and later. Requires KCML 6.00.00.7173 or later.\
<a href="#examples" rel="Help"><strong>Installation and Examples:</strong></a> Installation and syntax examples are included below.

## Summary

Allow access to a KCML SOAP server. Uses Apache Server to dynamically adapt to the current load. Persistent KCML processes are created for each SOAP server connected to each Apache Server daemon. The KCML SOAP servers may either be on the Web Server machine or on another machine. See [KcmlSoapServer](#kcmlsoapserver). Can convert browser HTTP GET and POST requests into SOAP requests for KCML, and can convert the SOAP responses back into text output for a browser. Mod_kcml can maintain session variable for KCML using an extension to the SOAP envelope body. Also allows access to KCML's sql utility for executing SQL statements from browser GET requests. In this case the sql processes are not persistent. Various error reporting modes are supported. See [KcmlErrorMode](#kcmlerrormode).

More information on the [Apache HTTP Server](http://httpd.apache.org/) is available.

## Directives

Server directives;

- [KcmlTraceFile](#kcmltracefile)
- [KcmlTraceLevel](#kcmltracelevel)
- [KcmlTraceMode](#kcmltracemode)
- [KcmlSessionCache](#kcmlsessioncache)
- [KcmlSessionTime](#kcmlsessiontime)

Directory/Location directives;

- [SqlServer](#sqlserver)
- [SqlStatement](#sqlstatement)
- [KcmlSoapServer](#kcmlsoapserver)
- [KcmlKeepServer](#kcmlkeepserver)
- [KcmlSources](#kcmlsources)
- [KcmlDatabase](#kcmldatabase)
- [KcmlUser](#kcmluser)
- [KcmlPassword](#kcmlpassword)
- [KcmlXSLT](#kcmlxslt)
- [KcmlXSLTdebug](#kcmlxsltdebug)
- [KcmlXSL](#kcmlxsl)
- [KcmlEnv](#kcmlenv)
- [KcmlProfile](#kcmlprofile)
- [KcmlAction](#kcmlaction)
- [KcmlArguments](#kcmlarguments)
- [KcmlErrorMode](#kcmlerrormode)
- [KcmlAuthenticate](#kcmlauthenticate)
- [KcmlRetryConnect](#kcmlretryconnect)
- [KcmlRetryWrite](#kcmlretrywrite)
- [KcmlRetryRead](#kcmlretryread)

------------------------------------------------------------------------

## <span id="kcmltracefile">KcmlTraceFile</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlTraceFile *filename*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlTraceFile /disk4/tmp/mod_kcml.log`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> server config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlTraceFile is only available for Unix in Apache 1.3 and later.

The trace file used for logging SOAP and browser GET and POST requests. Can also contain very verbose output for debugging.

------------------------------------------------------------------------

## <span id="kcmltracelevel">KcmlTraceLevel</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlTraceLevel *trace_level*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlTraceLevel 1`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> server config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlTraceLevel is only available for Unix in Apache 1.3 and later.

Trace output verbosity. 0 - off, 1 - low, 9 - high. KcmlTraceLevel could be set high while a site is being developed and then changed to 1 or 0 when the site is finished.

------------------------------------------------------------------------

## <span id="kcmltracemode">KcmlTraceMode</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlTraceMode *mode*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlTraceMode a+`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> server config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlTraceMode is only available for Unix in Apache 1.3 and later.

Trace file open mode. Defaults to "a+" for create/append. See fopen() for possible modes.

------------------------------------------------------------------------

## <span id="kcmlsessioncache">KcmlSessionCache</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlSessionCache *dirname*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlSessionCache /tmp/kcmlCache`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> server config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlSessionCache is only available for Unix in Apache 1.3 and later.

KCML session variables are currently implemented using plain files. KcmlSessionCache is the directory in which these files are created.

------------------------------------------------------------------------

## <span id="kcmlsessiontime">KcmlSessionTime</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlSessionTime *seconds*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlSessionTime 300`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> server config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlSessionTime is only available for Unix in Apache 1.3 and later.

Time in seconds that a session can remain inactive before it is automatically deleted. Both accessing and changing any of the session variables restarts this time.

------------------------------------------------------------------------

## <span id="sqlserver">SqlServer</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> SqlServer *filename*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> SqlServer is only available for Unix in Apache 1.3 and later.

Location of KCML's sql utility on the Web Server machine.

------------------------------------------------------------------------

## <span id="sqlstatement">SqlStatement</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> SqlStatement *statement*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> SqlStatement is only available for Unix in Apache 1.3 and later.

SQL statement to be executed. This could also be supplied as the `sql` parameter in the URL.

------------------------------------------------------------------------

## <span id="kcmlsoapserver">KcmlSoapServer</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlSoapServer *filename*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlSoapServer is only available for Unix in Apache 1.3 and later.

Location of the KCML executable. This could be on the Web Server machine, as in `/usr/lib/kcml/kcml`. If it is on another machine then the port number used by the SOAP server must be specified, as in `some.machine.com:8081` The machine name can be specified as a numeric IP address. The port number can be specified as a service name.

------------------------------------------------------------------------

## <span id="kcmlkeepserver">KcmlKeepServer</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlKeepServer *filename*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlKeepServer is only available for Unix in Apache 1.3 and later.

The machine name can be specified as a numeric IP address. The port number can be specified as a service name. Location of the KCML service. This could be on the Web Server machine, as in `/usr/lib/kcml/kcml`. If it is on another machine then the port number used by the KCML server must be specified, as in `some.machine.com:8081` If it is not on another machine then KCML will require it's `-k` argument in the [KcmlArguments](#kcmlarguments) directive. The machine name can be specified as a numeric IP address. The port number can be specified as a service name.

------------------------------------------------------------------------

## <span id="kcmlsources">KcmlSources</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlSources *filename*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlSources is only available for Unix in Apache 1.3 and later.

Location of the kconf.xml or sources.txt file. This only makes sense for servers running on the Web Server machine. This could also be supplied as the `sources` parameter in the URL.

------------------------------------------------------------------------

## <span id="kcmldatabase">KcmlDatabase</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlDatabase *database*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlDatabase is only available for Unix in Apache 1.3 and later.

Database or service in the kconf.xml file that the service should connect to. This only makes sense for servers running on the Web Server machine. This could also be supplied as the `database` parameter in the URL.

------------------------------------------------------------------------

## <span id="kcmluser">KcmlUser</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlUser *user_name*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlUser is only available for Unix in Apache 1.3 and later.

User that the server should impersonate. This only makes sense for servers running on the Web Server machine. This could also be supplied as the `user` parameter in the URL.

------------------------------------------------------------------------

## <span id="kcmlpassword">KcmlPassword</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlPassword *password*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlPassword is only available for Unix in Apache 1.3 and later.

Password for the user that the server should impersonate. This only makes sense for servers running on the Web Server machine. This could also be supplied as the `password` parameter in the URL.

------------------------------------------------------------------------

## <span id="kcmlxslt">KcmlXSLT</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlXSLT *On/Off*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlXSLT Off`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlXSLT is only available in mod_kcml 1.1 for Unix and Apache 1.3 and later.

SOAP response bodies that are themselves XML documents referencing XSL translation stylesheets can be translated by mod_kcml using Sablot 0.51 when mod_kcml is compiled to include Sablot support and this feature is enabled. TRUE/FALSE and 1/0 are understood as synonyms for On/Off.

------------------------------------------------------------------------

## <span id="kcmlxsltdebug">KcmlXSLTdebug</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlXSLTdebug *On/Off*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlXSLTdebug Off`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlXSLTdebug is only available in mod_kcml 1.1 for Unix and Apache 1.3 and later.

Sablot 0.51 XSL translation can produce verbose XSLT logging and debugging information, which is copied to the [KcmlTraceFile](#kcmltracefile) and can also be returned to a browser with [KcmlErrorMode](#kcmlerrormode). This is only supported when mod_kcml is compiled to include Sablot support and this feature is enabled. TRUE/FALSE and 1/0 are understood as synonyms for On/Off.

------------------------------------------------------------------------

## <span id="kcmlxsl">KcmlXSL</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlXSL *filename*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlXSL is only available for Unix in Apache 1.3 and later.

XSL file to include in any XML document produced by the server, if that document does not already contain a reference to an XSL stylesheet. This only makes sense for servers running on the Web Server machine. This could also be supplied as the `xsl` parameter in the URL.

------------------------------------------------------------------------

## <span id="kcmlenv">KcmlEnv</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlEnv *filename*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlEnv is only available for Unix in Apache 1.3 and later.

Environment parameters to set up before starting the server. This only makes sense for servers running on the Web Server machine. This could also be supplied as the `env` parameter in the URL.

------------------------------------------------------------------------

## <span id="kcmlprofile">KcmlProfile</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlProfile *filename*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlProfile is only available for Unix in Apache 1.3 and later.

The filename is expected to be a simple Korn shell .profile style of file. Environment parameters are set up before starting the server. This only makes sense for servers running on the Web Server machine. The filename may be of the form ~fred/.profile which may, for example be expanded to /home/fred/.profile.

------------------------------------------------------------------------

## <span id="kcmlaction">KcmlAction</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlAction *SOAPAction*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlAction is only available for Unix in Apache 1.3 and later.

The KcmlAction value is used to build the HTTP header line for SOAPAction. This is built from "urn:kcml-" the value of KcmlAction, "#" and the method name. If no value is specified for KcmlAction then the value is taken from the requested URL.

------------------------------------------------------------------------

## <span id="kcmlarguments">KcmlArguments</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlArguments *environment_parameter=value*\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlArguments is only available for Unix in Apache 1.3 and later.

Arguments to the server. This only makes sense for servers running on the Web Server machine. This could also be supplied as the `arguments` parameter in the URL.

------------------------------------------------------------------------

## <span id="kcmlerrormode">KcmlErrorMode</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlErrorMode *mode or filename*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlErrorMode 0`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlErrorMode is only available for Unix in Apache 1.3 and later.

Set the mode in which mod_kcml should report errors. If set to 0 or unset mod_kcml will leave Apache to return an HTTP 404 File not found. If set to 1 a special debug page is produced with specific information as to what happened. If set to a filename then the file is returned, allowing the use of a generic error page. KcmlErrorMode could be set to 1 while a site is being developed and then changed to a filename or 0 when the site is finished.

------------------------------------------------------------------------

## <span id="kcmlauthenticate">KcmlAuthenticate</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlAuthenticate *type*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlAuthenticate basic`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlAuthenticate is only available for Unix in Apache 1.3 and later.

Should the connection to the SOAP server require authentication then the authentication type can be declared to mod_kcml with this directive. If authentication is not supplied, or the wrong authentication is supplied then mod_kcml will reject the request. If the correct authentication is supplied then it is passed on in the HTTP headers to KCML. Only basic authentication is supported at this time.

------------------------------------------------------------------------

## <span id="kcmlretryconnect">KcmlRetryConnect</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlRetryConnect *retry_attempts*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlRetryConnect 2`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlRetryConnect is only available in mod_kcml 1.1 for Unix and Apache 1.3 and later.

Should connection to the SOAP server fail of any reason mod_kcml will retry, a default of twice, to connect to the server. NOTE Retry can have unexpected side effects at the server. For example if the request increments a data value at the server before it fails, the mod_kcml retry logic could cause the data value to be incremented more that once.

------------------------------------------------------------------------

## <span id="kcmlretrywrite">KcmlRetryWrite</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlRetryWrite *retry_attempts*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlRetryWrite 2`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlRetryWrite is only available in mod_kcml 1.1 for Unix and Apache 1.3 and later.

Should writing a SOAP request to the server fail of any reason mod_kcml will retry, a default of twice, to write to the server. NOTE Retry can have unexpected side effects at the server. For example if the request increments a data value at the server before it fails, the mod_kcml retry logic could cause the data value to be incremented more that once.

------------------------------------------------------------------------

## <span id="kcmlretryread">KcmlRetryRead</span> directive

<a href="directive-dict.html#Syntax" rel="Help"><strong>Syntax:</strong></a> KcmlRetryRead *retry_attempts*\
<a href="directive-dict.html#Default" rel="Help"><strong>Default:</strong></a> `KcmlRetryRead 2`\
<a href="directive-dict.html#Context" rel="Help"><strong>Context:</strong></a> per-directory config\
<a href="directive-dict.html#Status" rel="Help"><strong>Status:</strong></a> Extension\
<a href="directive-dict.html#Module" rel="Help"><strong>Module:</strong></a> mod_kcml\
<a href="directive-dict.html#Compatibility" rel="Help"><strong>Compatibility:</strong></a> KcmlRetryRead is only available in mod_kcml 1.1 for Unix and Apache 1.3 and later.

Should reading a SOAP response from a server fail of any reason mod_kcml will retry, a default of twice, to read from the server. NOTE Retry can have unexpected side effects at the server. For example if the request increments a data value at the server before it fails, the mod_kcml retry logic could cause the data value to be incremented more that once.

------------------------------------------------------------------------

## <span id="examples">Installation instructions and syntax examples</span>

In order to use mod_kcml the shared library mod_kcml.so must be copied to Apache's libexec directory and the following must be added to the appropriate sections in httpd.conf to load the module.\
\
`LoadModule mod_kcml libexec/mod_kcml.so`\
\
`AddModule mod_kcml.c`\
\
In addition consider the following httpd.conf syntax examples. A discussion follows.\
\
`KcmlTraceFile /disk4/tmp/mod_kcml.log`\
`KcmlTraceLevel 6`\
`KcmlSessionCache /tmp/kcmlCache`\
`KcmlSessionTime 300`\
\
`<Location /kcmltest>`\
`SetHandler mod_kcml`\
`KcmlServer douglas:8021`\
`KcmlErrorMode 0`\
`</Location>`\
\
`<Location /sqltest>`\
`SetHandler mod_kcml`\
`SqlServer /usr/lib/kcml/sql`\
`SqlStatement "SELECT * FROM DATA1"`\
`KcmlDatabase BENCH`\
`KcmlUser fred`\
`KcmlPassword 987xyz`\
`KcmlArguments "-t 0 -h"`\
`KcmlErrorMode 1`\
`</Location>`\
\
`<Location /session>`\
`SetHandler mod_kcml`\
`KcmlServer /usr/lib/kcml/kcml`\
`KcmlProfile ~fred/.profile`\
`KcmlEnv "PANICDIR=/tmp FRED=bert MEME=test"`\
`KcmlArguments "-b -p /disk2/SESSIONTEST.kcml"`\
`KcmlErrorMode /sqltest/error.html`\
`</Location>`\
\
Mod_kcml will append level `6` trace output to `/disk4/tmp/mod_kcml.log`. KCML session variables will be implemented by creating files in `/tmp/kcmlCache`. Any sessions that are inactive for more that 5 minutes will be automatically deleted.\
\
SOAP requests within `/kcmltest` will be sent to the machine `douglas` on port `8021`, where persistent KCML SOAP server processes will service requests. Any errors will result in Apache returning `HTTP 404 File not found`.\
\
Browsers pointed to `/sqltest` will get the result of `SELECT * FROM DATA1` in the `BENCH` database executed as user `fred`. Any errors will result in a special page with specific information about the error.\
\
SOAP requests within `/session` will be sent to persistent KCML SOAP servers `/usr/lib/kcml/kcml` started on the Web Server machine with environment parameters `PANICDIR=/tmp FRED=bert MEME=test` and arguments `-b -p /disk2/SESSIONTEST.kcml`. Any errors will result in the generic error page `/sqltest/error.html` being sent.\
\
Requests can also be made of the SOAP servers by simply using a browser. For example;\
\
`http://douglas/session/reverse?string=Hello&mode=6`\
\
would make a SOAP request of the KCML SOAP server on the Web Server machine. It would call the `reverse` method with two request parameters; `string` set to `Hello` and `mode` set to `6`. The response from the method would be sent back to the browser as text.\

Return to [top](#top).\

------------------------------------------------------------------------

### Apache module mod_kcml
