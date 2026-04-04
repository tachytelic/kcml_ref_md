Introduction to menus

------------------------------------------------------------------------

Menu bars and popup menus are created at design time by the [Menu Editor](FormsDesignerMenubars.htm) within the [Forms Designer](TheKCMLFormsDesigner.htm). As menus and menu options are created new objects for each menu and option are also created. For example, lets say a menu called *Menu1* is created that has a "File" menu containing the options "Open", "Save", and "Close". Once the menu is created KCML will automatically create the control *Menu1* which is then visible in the [Object Browser](TheKCMLObjectBrowser.htm), [Control List](ObjectBrowserformcontrolslist.htm). KCML will also create objects for each menu option, in this case the objects *File*, *FileOpen, FileSave* and *FileClose* are created. These objects names can then be used with the various menu properties and event handlers. If a menu has a sub-menu, for example, if the "File" menu has a sub menu called "Save As" that has two options called "Data" and "ASCII" then the object names *FileSaveAs*, *FileSaveAsData,* and *FileSaveAsASCII* would be created.

 
