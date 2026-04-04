Command line flags.

The Connection Manager has command line flags to enable it to be used from an command shell or script. These command line flags are mainly to used to testing and conversion purposes.

| Flags | Purpose |
|----|----|
| -c *envfile* | Convert a [text-format environment file](#textenv) to an XML document |
| -e *configFile* | [Examine](#examine) a configuration file |
| -i | [Initialize](#initsrv) services |
| -p *script* | [Execute](#execscript) a shell script using a service's environment. |
| -s *service* | [Test](#convapp) a **S**ervice from a telnet session (Unix only) |
| -x *SSLcert* | Use SSL certificate **SSLcert** to enable [Secure Connection](secureconn.htm) mode |

<span id="textenv"></span>

### Converting Environment files.

Applications may define their environment in a plain text file. This has the following format:


    [UNB]"VAR","value"

The first character of a line in this file determines what platform the variable applies to.\
It can take the following values.

| Character | Meaning                                 |
|-----------|-----------------------------------------|
| U         | Set variable on Unix platforms only     |
| N         | Set variable on NT platforms only       |
| B         | Set variable on both types of platforms |

These files can be loaded by the Connection Manager by using the [get_include](systemconf.htm#services) or [try_include](systemconf.htm#services) directives. Alternatively, this text format file can be converted to an XML document by using the **-c** flag, and the loaded using the [include](systemconf.htm#services) directive.

<span id="convapp"></span>

### Converting Applications to run under the Connection Manager.

Applications which use telnet connections and define their environment in shell scripts can be adapted for the the Connection Manager. The current environment can be dumped into a text file using the **set** command:


    set >myenv.txt

This can then be conveted into the above text file format by using commands such as **sed**, although some editing with **vi** will be necessary to recreate variables which are based on other variables, ie.


    B"BASE","/user1/myapp"
    B"HOME","/user1/myapp/home"

Should be changed to


    B"BASE","/user1/myapp"
    B"HOME","$BASE/home"

As mentioned above the resulting file can either be loaded by the [get_include](systemconf.htm#services) or [try_include](systemconf.htm#services) directives, or it can be converted to XML and loaded using the [include](systemconf.htm#services) directive. Prior to using the Connection Manager directly, ie via network port 790, the application can be tested, from a telnet session, by using the **-s** flag, Eg:


    $ export PATH=$PATH:/usr/local/kcml:.
    $ export KCML_SOURCES=/usr/local/kcml/kconf.xml
    $ kwebserv -s MyApp

The Connection Manager will load the environment variables, from *kconf.xml* and any included files, and then execute kcml. If the environment has been setup correctly, including the [START](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#START) variable, the the application should function correctly. Once this has been confirmed, client PC's should connected directly to the Connection Manager by adding the service name to the **Connect to Service** field in the properties of a [KClient connection](mk:@MSITStore:kclient.chm::/connectionpage.htm).

<span id="execscript"></span>

### Executing scripts under a service's environment.

A shell script can be executed under the Connection Manager by using the **-p** flag. When used in conjunction with the **-s *servicename*** flag, the script will inherit the service's environment settings.

<span id="initsrv"></span>

### Initializing a service.

When the host server is started, it may be desirable for any background processes that application requires, to be started automatically. These processes will require the same environment as the application. Attempting to write shell scripts to parse *kconf.xml* and any other evnironment files would not be trivial. To simplify this process, the Connection Manager can automate this by using the **-i** flag. For more details see [ASP support](webasp.htm).

<span id="examine"></span>

### Checking the kconf.xml Configuration file

If the Connection Manager fails to start one cause can be a corrupt kconf.xml configuration file. The configuration file can be **examined** with the -e flag


    kwebserv -e kconf.xml

Kwebserv will parse the file and, if it is valid XML, will list the top level access control lists, eg:


    kwebserv: kconf.xml is valid XML
    validclients: localhost 11.22.33.* 44.55.66.*
    validusers: root kcc* fred alf bert
    adminusers: root sysadmin kcc*

If the file contains a syntax error, then the line number and reason on which the error occurred will be reported, eg:


    Corrupt configuration file kconf.bad: XML parser failed with "mismatched tag" on line 15

When the -e flag is used in conjunction with the *-s serviceName* flag, the service's access control lists, database catalogue, alias and table space lists will be displayed.\
For example, the command:


    kwebserv -s SalesSystem -e kconf.xml

may display something of the form:


    kwebserv.exe: kconf.xml is valid XML
    validclients: 11.22.33.* localhost
    validusers: fred joe kcc*
    adminusers: kcc*
    KDB catalogue /user1/myapp/data/catalogue.kdb OK

    Tablespace       status           location
    GLOBAL           OK               /user1/myapp/data/GLOBAL
    MISC             OK               /user1/myapp/data/MISC
    ACCOUNTS         OK               /user1/myapp/data/ACCOUNTS
    STOCK            OK               /user1/myapp/data/STOCK
    WORKSPACE        OK               /user1/myapp/work

    Alias            status           location
    Forms            OK               /user1/myapp/sw/Docs/Forms
    Docs             OK               /user1/myapp/sw/Docs
    Reports          OK               /user1/myapp/misc/Reports
    UserReports      Does not exist   /user1/myapp/misc/UserReports
    Help             OK               /user1/myapp/sw/Docs/Help
    CGI              OK               /user1/myapp/sw/Docs/CGI

| Value | Description |
|----|----|
| 0 | Success. kconf.xml is valid XML. If *-s service* is also used then the DB catalogue, table spaces and aliases exist. |
| 1 | Failed to open or parse kconf.xml, or an environment \<include\> file. |
| 2 | Database catalogue does not exist |
| 3 | One or more table spaces does not exist |
| 4 | One or more aliases does not exist |

**Return values for kwebserv -e**

\
When making manual changes to kconf.xml in an existing system it is recommended that a copy is made. The new copy can then be edited and then checked with the -e flag before it is copied back. Eg:


    cd /usr/local/kcml
    cp kconf.xml kconf.new
    vi kconf.new
    kwebserv -e kconf.new

##### See Also:

[Connection Manager](connmgr.htm) [Remote Adminstration Functions](adminfns.htm)
