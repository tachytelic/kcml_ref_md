Writing CGI scripts in KCML

KCML can be used to write CGI or Common Gateway Interface scripts to run on a web server. This is not intended to be a tutorial on CGI scripts as there are many texts available on this topic. Fundamentally a CGI script is invoked when a HTTP request is sent to a server and the server recognizes the extension at the end of the URL as corresponding to a known scripting language. Thus the url

http://www.kcml.com/cgi-bin/echo.kcml?param1=Hello&param2=World

would be parsed by the web server to separate the server *www.kcml.com*, identify the script file *cgi-bin/echo.kcml*, and separate out any parameters that follow a ?. Such parameters obey an escaping convention which protects ?, %, /, space etc by sending them as % and the character as two hex digits. There is a [Extended \$PACK specifier](tmp/xp.htm#extended) to encode such strings. See CGI texts for more on this encoding.

These URLs can be used in either GET or POST requests. The former just returns a page and the latter is sent by a button on a form or by JavaScript and can pass parameters taken from the form to the program.

The example echo.kcml program might look like

10 PRINT "Content-type: text/html" PRINT PRINT "\<HTML\>\<BODY\>" PRINT "\<P\>Hello world, my parameters were: ";ENV("QUERY_STRING");"\</P\>" PRINT "\</BODY\>\</HTML\>" \$END

The first two lines, the content type declaration and the blank line, are mandatory and without them you will not see any result. The rest of the program should just print a standard HTML document. The browser will not see the resulting page until the \$END. The program can make use of various [CGI environment variables](httpenv.htm) setup by the web server and the most useful is the QUERY_STRING which returns the string following the ? in the URL.

Configuring IIS and Personal Web Server

On NT with IIS4/IIS5 or the Personal Web Server KCML will automatically register on installation its .kcml [extension](FileExt.htm) in the registry as the scripting language to be run to satisfy such requests. This may not work for IIS4 where you may have to manually put the .kcml extension in the script map (web site properties\|Home Directory\|Configuration\|App mapping) with something like

.kcml c:\kerridge\kcml\kcml.exe -p "%s" "%s"

using the IIS management console (Properties\|Home Directory\|Configuration). IIS4 is supposed to check the registry key on bootup and copy it to the ScriptMap but it appears to be unreliable. The directory containing the .kcml scripts should be marked executable and not readable.

Configuring Apache

Put the following in the Apache configuration file *hppd.conf*

AddType application/x-httpd-kcml .kcml Action application/x-httpd-kcml "/cgi-bin/runkcml"

and, on a Unix system, create the following script file *runkcml* in the cgi-bin directory

\$ cd cgi-bin \$ cat \<\<EOT \>kcmlrun \#!/bin/sh /usr/lib/kcml/kcml -p \$DOCUMENT_ROOT\$PATH_INFO EOT \$ chmod +x kcmlrun

Then restart the server. This script is necessary on Linux or other BSD based platforms where you cannot directly invoke a kcml [script](script.htm) with the \#! script trick.

On an NT Apache system you need a batch file called runkcml.bat in the cgi-bin directory containing the following

@echo off c:/kerridge/kcml/kcml -p %DOCUMENT_ROOT%%PATH_INFO%
