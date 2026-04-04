Connection Manager Environment variables

These environment variables, set in kconf.xml, control the behaviour of the Connection Manager.

| Variable | Values | Purpose |
|----|----|----|
| SERVICE | Name of a service | Load the environment for the specified service when using [administration](adminfns.htm) pages |
| BASE or SYSADDR | A directory name | Application's base directory |
| UMASK | Octal integer, eg 003 | File creation mask to emulate the **umask** command |
| WEBADMIN | "true" or "false" | Enable/disable access to the [administration](adminfns.htm) pages |
| WEBSERVER | "true" or "false" | Enable/disable HTTP access to the webserver pages |

These environment variables, although not used by kwebserv itself, are used by KCML or the Unix command shell, when invoked by the Connection Manager.

| Variable | Values | Purpose |
|----|----|----|
| [CWD](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#CWD) | A directory name | Current working directory, especially useful for applications which rely on relative pathnames |
| [PSEUDOTTY](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#PSEUDOTTY) | "true" or "false" | Enable/disable pseudo-tty support for interactive ! shell prompts |
| [TERM](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#TERM) | vt220 | Useful terminal type when using the **vi** editor from a ! shell prompt. |
| [EDITOR](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#EDITOR) | vi | Useful command history when using the ! shell prompt from the console window. |

The Connection Manager will automatically set these variables.

| Variable | Typical Value or example | Purpose |
|----|----|----|
| KCMLDIR | /usr/local/kcml or C:/Kerridge/KCML | Installation directory of KCML |
| SERVER_NAME | Hostname or IP address | Derived from the hostname used by KClient, after build 9296, or from the hostname in a HTTP URL. |
| SERVER_PORT | integer, typically 790 | Network port number that the Connection Manager is listening on. |
| SERVER_SOFTWARE | kwebserv/06.90.00.*nnnn* | Program identifier and version |
| SERVER_TYPE |  | Description of host platform |
| SERVER_HTTP_URI | http: or https: | URI to construct HTTP URLs. If the Connection Manager is using a [Secure Connection](secureconn.htm), the the value will be *https:* |
| PATH_INFO | myalias/cgi.ksh | HTTP URI, without query string |
| PATH_TRANSLATED | /user1/app/htdocs/info/cgi.ksh | URI which has been translated to a file or directory on the host's filesystem |
| QUERY_STRING |  | HTTP query string, ie the part of a URL after a **?** character |

The value of *SERVER_TYPE* depends on what type of operating system the host machine is running. Currently, this can be one of the following.

| Value of SERVER_TYPE | Description                                |
|----------------------|--------------------------------------------|
| AIX                  | IBM AIX 4.3 or later, RS6000               |
| HPUX11               | HP-UX 11.00 or later                       |
| Linux                | Linux, typically with GLIBC 2.2.4 or later |
| Solaris              | Sun Solaris 8                              |
| Windows              | Microsoft Windows NT                       |

\
The *PATH\_*, *QUERY_STRING* and *SERVER\_* variables are provided to support a simple [CGI-script](aliases.htm) interface.\
A typical example:

**http://server.domain.com:790/myalias/cgi.ksh?param1+param2+param3**

When the Connection Manager receives this request, the resulting environment variables will be

| Variable        | Value                          |
|-----------------|--------------------------------|
| PATH_INFO       | myalias/cgi.ksh                |
| PATH_TRANSLATED | /user1/app/htdocs/info/cgi.ksh |
| QUERY_STRING    | param1+param2+param3           |
| SERVER_NAME     | server.domain.com              |
| SERVER_PORT     | 790                            |

\
In addition the QUERY_STRING will also be passed as a set of command-line arguments to the CGI-script. The resulting command being:


    /user1/app/htdocs/info/cgi.ksh param1 param2 param3

##### See Also:

[Connection Manager](connmgr.htm) [Remote Adminstration Functions](adminfns.htm)
