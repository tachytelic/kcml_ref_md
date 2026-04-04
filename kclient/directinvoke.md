# <span id="directlyinvokingthekclientprogram"></span> Directly invoking the kclient program

Kclient is also available as an executable program, which can be started on Windows 98 and NT4 via the Universal Resource Indicator (URI) **kclient**, which is similar to the telnet URI. This can be used to make up a Universal Resource Locator string (URL) which can be referenced on a web page or used in a shortcut with the version of Explorer that comes with Windows 98 and NT4. Note that you may not be able to use this form of URI or URL in other browsers.

For example in HTML intended for IE3/4/5 you can use

\<A HREF="kclient:-A?V8profile"\>Run V8\</A\> \<A HREF="kclient:pjc@someserver"\>Connect to someserver\</A\> \<A HREF="kclient:pjc@someserver?-C?MODULE=SO"\>Use of a bookmark\</A\>

The usual kclient command line options are available following the URI with the convention that ? characters stand in for spaces. See the appendix on [command line switches](commandlineswitches.htm) for more information on switches. There is also a simple shorthand of userid@server to replace the -u and -h switches.

Strictly speaking in HTML all non alphanumeric characters in the HREF URL should be replaced with their URL encoded value e.g. an = sign would be encoded as %2D and space by %20. In practice IE5 does not require this other than for the quote character. Kclient has its own convention for spaces and will replace all '?' characters in the string with spaces so any genuine '?' characters in the string must be encoded as %2F.

If you have KClient installed on your PC you can try this by clicking this [link](kclient:-d?-C?some?bookmark).
