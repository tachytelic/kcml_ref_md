# <span id="examplewebpage"></span> Example HTML for a Web page

This is an HTML object tag containing. The \<OBJECT\> tag is a Microsoft HTML tag that defines an ActiveX object.

\<OBJECT ID="KClient1" BGCOLOR="#c0c0c0" CLASSID="CLSID:494b8c10-bdb5-11d1-8373-00a0c901b28c" WIDTH="50" HEIGHT="50" CODEBASE="ftp://ftp.yourco.com/pub/kclient.cab#Version=5,0,2,4245" \> \<PARAM NAME="Connect" VALUE="-A V8profile"\> \<PARAM NAME="OwnBackground" VALUE="1"\> \</OBJECT\>

The important subtags are the mandatory CLASSID which defines the GUID under which the control is registered and the optional CODEBASE which defines a URL from which the control can be downloaded. See the section on [Downloading from the Internet](download.htm). The ID subtag defines the name with which the object can be referenced in any JavaScript.

The properties Connect and OwnBackground are set with the \<PARAM\> clauses. See [ActiveX properties](properties.htm) for more information about the available properties.

You may wish to invoke the activeX by placing it in a secondary window so as to disable the back and forward buttons of the browser. With IE you can add a TARGET tag e.g.

\<A HREF="Apptest.htm" TARGET="\_blank"\>Click me \</A\>

or you could use a Javascript window.open() method.

onclick='window.open("the url", "Prima", "height=600, width=800, toobar=no, menubar=no, location=no, status=no, resizable=no, scrollbars=no, menubar=no, directories=no")'

Here is an example embedded into this page. Click <a href="apptest.htm" target="_blank">here</a> to connect. Alas this will only actually work inside the Kerridge firewall.
