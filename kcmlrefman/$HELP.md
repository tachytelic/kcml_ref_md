\$HELP

------------------------------------------------------------------------

General Forms :

1.  \$HELP = alpha_expression
2.  alpha_receiver = \$HELP
3.  \$HELP(strexpr)

------------------------------------------------------------------------

The \$HELP statement is used to provide access to information screens relevant to the operation of the application currently being executed. The screens are stored in files which are written in HTML (HyperText Markup Language) format. Microsoft Windows help files can also be displayed if running under Windows using either Windows KCML or UNIX KCML connected using KCLient. For compatibility reasons, help files can also be stored in ASCII format though this method is rather antiquated and its use is not recommended. For existing users of the ASCII method a program is available to convert the old style help files into HTML format.

HTML Help files can be referenced in any of two ways:

- The [\$HELPINDEX]($HELPINDEX.htm) statement is used to specify the name of the directory containing the HTML files and \$HELP is used to specify the name of the file to be displayed. These files should have a .htm or .html extension.
- The [\$HELPINDEX]($HELPINDEX.htm) statement is used to specify the name of an HTML file and \$HELP is used to specify the name of an HTML anchor within that file.

Help screens are accessed by executing the function form of \$HELP passing a filename or by setting the \$HELP function and then pressing the help key as defined in the [TERMINFO](TextTermIntro.htm) description for that terminal, normally CTRL-L when running KClient or WDW or ESC-ESC on a VT100. The help key is enabled in immediate mode or whenever a program is executing one of the following statements:

|                      |                                |
|----------------------|--------------------------------|
| [LINPUT](LINPUT.htm) | [LINPUT LINE](LINPUT_LINE.htm) |
| [KEYIN](KEYIN.htm)   | [LINPUT LIST](LINPUT_LIST.htm) |

\
The second form of \$HELP is used to return the name of the \$HELP file currently being used.

When the help key is pressed or if the \$HELP function is executed, execution of the application program is suspended, the contents of the screen are saved, and the help screen is displayed. If the current value of \$HELP is blank or the help file does not exist, the message "No help information" is displayed in the middle of the screen. Once the help screen has been read, pressing the RETURN key switches back to immediate mode or the application restoring the original screen.

The filename contained in \$HELP remains set across successive program loads, therefore to prevent any possible confusion \$HELP should be set to blanks, or to a new Help file before new programs that do not contain \$HELP statements are loaded.

Windows KCML and the Windows DW terminal emulator can also be instructed to call a Windows Internet Browser to display HTML format help files. This is done by setting byte 41 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE41) to HEX(0C) and setting the HELPSERVER environment variable to point to the DOS/Windows directory containing the help files. For example:

ENV("HELPSERVER") = "C:\HelpFiles"\
STR(\$OPTIONS RUN,41,1) = HEX(0C)\
\$HELP("Main.html")

The HELPSERVER environment variable can also be used to point to a Web Server. In this case [\$HELPPARAMS]($HELPPARAMS.htm) is added to the URL passed to the browser, for example:

ENV("HELPSERVER") = "http://www.kerridge.com"\
STR(\$OPTIONS RUN,41,1) = HEX(0C)\
\$HELPPARAMS = "?priority=7&lang=en&detail=full"\
\$HELP("Index.htm")

To display Windows Help files, the HEX(10) bit of byte 41 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE41) must be set to instruct Windows KCML or Windows DW to spawn the Windows Help system to view a .HLP file. Also the HELPSERVER environment variable must be set to the name of the local Windows Help file and \$HELP is set to a context within the help file. For example, the following could be used to display the [\$DECLARE]($DECLARE.htm) page from the KCML Language Reference Help file:

ENV("HELPSERVER") = "C:\HelpFiles\KCMLMAN.HLP"\
\$HELP("\$DECLARE’")

Examples:

\$HELPINDEX = "/user1/HelpFiles"\
\$HELP = "Index.html"

In the example above the help file Index.html would be displayed if the help key is pressed. The help file could also be displayed automatically with the following:

\$HELP("Index.html")

The following example uses [\$HELPINDEX]($HELPINDEX.htm) to point to the help file and \$HELP to start displaying from the specified tag:

\$HELPINDEX = "Info.html"\
\$HELP("Profile")

Syntax examples:

\$HELP = "help1"\
\$HELP = STR(file\$,80,8)\
current\$ = \$HELP & ".html"

See also:

[\$HELPINDEX]($HELPINDEX.htm) [\$HELPPARAMS]($HELPPARAMS.htm)
