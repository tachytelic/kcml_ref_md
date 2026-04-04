# DHTML Access to the container

A KCML program running in an ActiveX can get access to the IE4 Browser container, in particular the IHTMLDocument2 Dynamic HTML interface though a standard OBJECT reference. To do this use a pseudo ProgId of ActiveXContainer as in OBJECT a = CREATE "ClientCom", "ActiveXContainer"

This will give you access to the DHTML functions for the current document allowing you to control the text and media on the browser.
