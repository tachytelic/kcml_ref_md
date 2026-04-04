Serving Web Pages

The Connection Manager can be used to serve your own web pages, in a similar manner to the [Remote Administration pages](adminfns.htm). This is done by defining an **\<alias\>** in kconf.xml. The list of aliases can be viewed and edited by selecting the **Display/Update <u>web aliases</u>** link on the [Kerridge System Configuration](systemconf.htm) page.

An alias maps the URL that a browser will use to request the web page to a file or directory on the host's filesystem. An alias has the follow properties:

| Property | Purpose |
|----|----|
| Alias Name | The alias name is used in the URL to request the page |
| Real Name | The location of a file or directory on the host's filesystem |
| Type | Controls how the requested URL is processed |
| Authentication required | If set yo **Yes**, the a valid username and password will be required to view the page. |

\

Let's take an example of an alias called *TestAlias*. The Connection Manager will then use this alias when processing requests for a URL of the form **http://hostname:790/TestAlias**.

### <u>Alias Types</u>

The behaviour of the web server, when processing a requested URL, depends on the **Type** of the alias.

#### Directory

The **Real Name** property points to a directory, for example */user1/myapp/docs*. Characters after the **Alias Name**, in the requested URL, are treated as components of a pathname. So the URL **http://hostname:790/TestAlias/index.htm** would map to a file with the pathname */user1/myapp/docs/index.htm*. Sub-directories are also allowed, for example the URL **http://hostname:790/TestAlias/misc/appendix.htm** would map to a file with the pathname */user1/myapp/docs/misc/appendix.htm*. For regular files, like the previous examples, the contents of the file will be downloaded to the browser. If the URL is a request for a directory, then the contents of the directory will be listed. The filenames in this table, will be links to files or subdirectories. The headings of the table are links which can be used to sort the listing by modification date and size.

#### UrlAlias

This is very similar to the **Directory** type. The difference is that the URL must point to a regular file. Requests for directory listings are not allowed.

#### FileHTML

This type is used to display a specific file. Characters after the **Alias Name** are not allowed. For example, if the **Real Name** has the value */user1/myapp/readme.htm*, then the page can be downloaded using the URL **http://hostname:790/TestAlias**.

#### CGIScript

The Connection Manager also supports the generation of web pages from a CGI script. The **CGIScript** type is used to map a URL to such a script. The **Real Name** must point to a regular file, which can be a command script (such a Unix shell script, or a DOS batch file) or a KCML program. If the **Real Name** value does not contain a dot extension, eg .bat, .sh or .src, then the Connection Manager will attempt to look for files in the following order.

| Extension | Description | Supported platform |
|----|----|----|
|   | No extension, try to open the specified file first | All |
| .cmd | DOS command script | NT only |
| .bat | DOS batch file | NT only |
| .ksh | Unix Korn Shell script | All |
| .sh | Unix Shell script | All |

\
If the **Real Name** is the pathname to a KCML program, then the program is executed as a [KCML script](mk:@MSITStore:kcmlrefman.chm::/script.htm). The CGI script will inherit environment variables from the [General section](systemconf.htm#genenv) of kconf.xml, plus a set of [CGI environment variables](webenvvar.htm).

| Variable | Typical Value or example | Purpose |
|----|----|----|
| SERVER_NAME | Hostname or IP address | Derived the hostname in a HTTP URL. |
| SERVER_PORT | integer, typically 790 | Network port number that the Connection Manager is listening on. |
| SERVER_SOFTWARE | kwebserv/06.90.00.*nnnn* | Program identifier and version |
| PATH_INFO | myalias/cgi.ksh | HTTP URI, without query string |
| PATH_TRANSLATED | /user1/app/htdocs/info/cgi.ksh | URI which has been translated to a file or directory on the host's filesystem |
| QUERY_STRING |  | HTTP query string, ie the part of a URL after a **?** character |

\
These environment variables can then be used by a CGI script to construct URLs for subsequent web pages.

#### CGIDirectory

This alias type allows any command script or KCML program in the directory specified by the **Real Name** value to be executed as a CGI script. The execution of the script follows the same rules as the **CGIScript** alias.

#### UserDirectory

The **Real Name** value specifies a directory, the pathname is based on a valid user account on the host system. For example, if there is a user account of **fred**, then a suitable pathname would be */user1/myapp/fred*. Access to files within this directory always require authentication and are restricted to the owner of the account, in this case **fred**.

### <u>Per-Service aliases</u>

The Connection Manager also allows a [service](systemconf.htm#services) to define its own aliases. When requesting pages that are defined in a per-service alias, the service name is used in the URL.\
For Example:\
**http://hostname:790/serviceName/TestAlias**\
\
The Connection Manager will expand any environment variables that are used in the **Real Name** value. Scripts that are executed using a **CGIScript** and **CGIDirectory** alias type will also inherit the service's environment variables.

### <u>Include files</u>

It may be more convenient to define a list of aliases outside of kconf.xml. This can be achvied, in KCML 6.20 onwards, by storing the aliases in an included XML file. This include file is then referenced by adding an alias, in kconf.xml, with a **Alias Name** of 'include' and a **Real Name** which is the location of the the XML file.

### <u>Caching</u>

From KCML 6.20 onwards, the Connection Manager supports HTTP Caching. When a web page is downloaded to a browser, the datestamp of the file is also sent. The web browser now 'knows' how old the file is. If the browser then requests the web page again, it sends this datestamp to the Connection Manager. The Connection Manager then compares this datestamp to the modification time of the file on host's filesystem. If the file has not changed, a tiny HTTP packet is sent back to the browser. This instructs the browser that its cached copy is up to date. If the file has been modified since, then the Connection Manager will resend the new page to the browser. The use of caching can greatly reduce the amount of network traffic for frequently requested web pages.

### <u>File Types</u>

When a file is downloaded to a browser, the browser is told what type of data it is receiving. The browser can then decide how to process the data. This file type information called the MIME type and is deduced from the dot extension of the file's pathname. If the file has no dot extension, the contents of the file are scanned. However, this can be ineffecient on large files. The list of MIME types and filename extensions that the Connection Manager recognized are

MIME type

File extensions

Desciption

application/msword

doc

Microsoft Word document

application/octet-stream

bin dms lha lzh exe class dll ocx drv com so sl

Binary files, eg executable programs, shared libraries

application/pdf

pdf

Adobe Acrobat document

application/vnd.ms-excel

xls

Micorsoft Excel spreadsheet

application/vnd.ms-powerpoint

ppt

Microsoft Point Point presentation

application/x-cpio

cpio

Unix CPIO archive

application/x-gtar

gtar

Gnu TAR archive

application/x-gzip

gz gzip

GZIP archive

application/x-javascript

js

Java script

application/x-tar

tar

Unix TAR archive

application/zip

zip

ZIP archive

image/bmp

bmp

Windows BitMap image

image/gif

gif

Graphics Interchange Format (GIF) image

image/jpeg

jpeg jpg jpe

Joint Photographics Expert Group (JPEG) image

image/png

png

Portable Network Graphics (PNG) image

image/tiff

tiff tif

Tagged Image File Format (TIFF) image

text/css

css

Cascading Style Sheet

text/html

html htm

HyperText Markup Language (web page) document

text/plain

asc txt ksh sh cmd bat

Text files, command scripts etc

text/richtext

rtx

Text with formatting data

text/rtf

rtf

Microsoft Rich Text Format

text/sgml

sgml sgm

Standard Generalized Markup Language document

text/tab-separated-values

tsv

Tab Separated Values data

text/xml

xml dtd

eXtened Mark Langauage (XML) document

application/xml

xsl

eXtensible Stylesheet Language transform script

encoding/x-compress

Z

File compressed with the Unix *compress* command
