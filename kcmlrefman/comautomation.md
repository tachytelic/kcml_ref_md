### COM Automation issues

Automation, once called OLE automation, is the name Microsoft gives to the Visual Basic support in Windows which has been documented and included as a COM technology. In general KCML should be able to use Automation to control any object that follows these standards and exposes the VB style IDispatch interface.

##### Properties and methods

KCML supports only the current COM specification in which properties are read or written using methods. We do try to expose some of the old VB property based syntax where it fits in to the KCML syntax thus it is legal to say app.Visible = TRUE name\$ = worksheet.name\$ For grammatical reasons you will need to add a \$ to VB properties that have string values. However when getting or setting properties you can also use the underlying method call e.g. app.Visible(TRUE) name\$ = worksheet.name\$() This becomes important with the strange VB specific grammar where functions can be lvalues e.g. in VBA for Word to set a default template you use an expression like app.Options.DefaultFilePath(wdUserTemplatesPath) = "\mytemplates" To do this in KCML, where functions cannot appear on the left of a LET expression, you need to use a function as in app.Options.DefaultFilePath(ENUM wdUserTemplatesPath, "\mytemplates") The new value for the property must be the last argument to the method.

There is no support for the VB concept of a default property value for an object, e.g .value\$ for a cell in Excel, so all properties must be explicitly specified.

##### Word and Excel issues

These objects are implemented as .EXE executables rather than .DLL libraries. They are initially created hidden and you will have to make them visible if you wish the user to be able to interact with them. The objects will not terminate automatically when the last KCML object is set to NULL and you will have to explicitly close them before releasing the application object e.g. for Word OBJECT app = CREATE "clientCOM", "Word.Application" app.visible=TRUE ... app.Quit() OBJECT app = NULL Word will not shutdown while any of its objects are still referenced by KCML. Any objects you instantiate must be set to NULL when you are done with them.
