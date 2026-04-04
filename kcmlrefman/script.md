Scripting in KCML

KCML can be used inside Unix shell scripts, NT batch files or [CGI scripts](cgi.htm). When used this way it will generally not invoke the client to interact with the user but will read from standard input and write to standard output. Any runtime errors will terminate the kcml with a panic dump.

In a script you should either redirect standard input or use the -p command line switch e.g. kcml \< myscript.src kcml -p someprog

The second case is useful if you need to process standard input in the script and maybe write a reply to standard output, as in a CGI script. Standard input is available on the /001 device and standard output on /005 so the script can use INPUT, KEYIN or READ \# to get input and can output with PRINT.

Unix scripts

A KCML program can be run directly from with the Bourne or Korn shells by using \#! followed by the full kcml program name on the first line of the script. Thus a utility to print the KCML license number might be written

\$ cat \<\<EOT \>test.ks \#!/usr/lib/kcml/kcml -p PRINT \$SER EOT \$ chmod +x test.ks \$ test.ks 123456 \$

The -p switch is necessary to stop KCML interacting with any client and to force it to read and write through standard input and output. This trick does not work on some versions of Unix (e.g. Linux) unless the kcml directory is on the [PATH](EnvVars.htm#PATH) or set in the special [KCMLPATH](EnvVars.htm#KCMLPATH) environment variable as Linux does not pass the full kcml filename to kcml thus preventing it discovering its original directory.

NT batch scripts

NT (and Win9x) batch files support simple redirection of standard input and output so you can do things like

kcml \< myprog.asc

assuming kcml to be on the path. However the .ks [file extension](FileExt.htm) is registered in the shell.
