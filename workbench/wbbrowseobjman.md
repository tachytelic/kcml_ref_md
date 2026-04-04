## Workbench object management dialog

This dialog is used to added and remove object definitions from the Object Browser References section.

<img src="bitmaps/ObjBrowseTreeDia.png" data-border="0" usemap="#DiaMap" width="606" height="352" alt="Object Management Dialog" />

The dialog allows both local and remote definition to be added. The procedure of adding these objects is very different.

- **COM Type Library** - To add an Type Library simple scroll down the list until you find the one you are looking for, check it and then click OK. You can check and uncheck more than one Type Library before clicking OK.
  \
   
- **SOAP Objects** - To add a SOAP object you first need to know the location of the WSDL file. If this is a remote URL then you may also need to know your proxy details. If the file is local (i.e on your machine) you will need to specify the URL using *file://c:/mywork/mywsdl.wsdl* notation.\
  \
  The description information is used to identify the object in the browser window, if this is left blank a description will be automatically created.\
  \
  The proxy details should be specified in the following format *user:password@proxyaddress:port*. You can leave out user:password if these aren't required by your proxy server.
