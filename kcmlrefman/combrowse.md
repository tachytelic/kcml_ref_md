### <span id="Browsing">Browsing objects</span>

In this initial implementation only **clientCOM** objects can be browsed by the [Object Browser](mk:@MSITStore:workbench.chm::/wbbrowseobjects.htm) in the KCML Workbench. Furthermore the objects must have been [instantiated](cominst.htm) which generally means that program must have been RUN or at least executed as far as the CREATE statment for the object to be browsed. The methods, properties, enumerations and any collections or other internal objects may be viewed in a tree control. If any help text is associated with such an element it may be viewed with a right click.

The [LIST OBJECT](LIST_OBJECT.htm) statement lists all the objects in the current program in the console window showing their internal handle number, the object type (clientCOM, serverCOM etc), the symbol name, the object description from its type library.
