The tab control Enter() and Exit() event handlers

------------------------------------------------------------------------

To make sure that forms containing tab controls are displayed as quickly as possible it is recommended that all tabs apart from the default tab are not filled until they are selected, this is done by creating an

*Enter()* event handler for each tab.

The [*Exit()* event handler, if it exists, is called when a user selects another tab in the control. This can be used to prevent other tabs being selected until the information in the current tab has been entered correctly. To prevent other tabs from being selected the](PROP_TABBED_EXIT.htm)

*Exit()* event for the current tab should execute a *RETURN FALSE* statement, for example:

-DEFEVENT Form1.tabControl1.tab3.Exit()\
   IF ('VerifyTab() \<\> 0)\
      RETURN FALSE\
   END IF\
   ...\
 END EVENT
