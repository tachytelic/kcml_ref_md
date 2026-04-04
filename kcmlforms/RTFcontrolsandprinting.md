RTF controls and printing

------------------------------------------------------------------------

To allow the user to print the contents of the RTF control you need to make use of several of the controls methods and event handler. Firstly you need to open a connection with the printer and allow the user to select the required printer. This is done with the [*PrintOpen()* method and would most likely get called from within the](tmp/PROP_RICHEDIT_PRINTOPEN.htm)

*Click()* event handler of a push button or drop down menu option, for example:

\- DEFEVENT Form1.btnPrint.Click() .rtfControl1.PrintOpen("RTF Control Print", FALSE) END EVENT

This example would display the Windows printer selection dialog box after the button was selected, allowing the user to select a Windows printer. The first parameter passed to the

*PrintOpen()* method allows a document name to be specified. The text is only used as a reference name for queuing purposes, it will not normally appear on the document(s) that are to be printed. The second parameter determines if the default Windows printer is to be used. If ***TRUE*** is specified then the default Windows printer will be used otherwise the user will be given the chance to select a printer as is the case in the above example.

The [*PrintOpen()* method does not actually send anything to the printer, it is used only to create a connection. Once complete the](tmp/PROP_RICHEDIT_PRINTOPEN.htm) [*PrintStatus()* event handler is called to allow the program to act on the return from](tmp/PROP_RICHEDIT_PRINTEVENT.htm) [*PrintOpen()*. Within this event handler the](tmp/PROP_RICHEDIT_PRINTOPEN.htm) [*PrintStatus* property can be used to determine the result from the](tmp/PROP_RICHEDIT_PRINTSTATUS.htm) [*PrintOpen().* A value of zero is returned if the](tmp/PROP_RICHEDIT_PRINTOPEN.htm)

*PrintOpen()* was successful and a value of one is returned if it failed.

If [*PrintOpen()* was successful then the](tmp/PROP_RICHEDIT_PRINTOPEN.htm) [*Print()* method can be called. A good place to do this is from within the](tmp/PROP_RICHEDIT_PRINT.htm) [*PrintStatus()* event handler as part of the test for the return of the](tmp/PROP_RICHEDIT_PRINTEVENT.htm) [*PrintStatus* property. Once the](tmp/PROP_RICHEDIT_PRINTSTATUS.htm) [*Print()* method has completed the](tmp/PROP_RICHEDIT_PRINT.htm) [*PrintStatus()* event handler is then called again to allow the program to determine the result of the](tmp/PROP_RICHEDIT_PRINTEVENT.htm) [*Print()* method. If successful the](tmp/PROP_RICHEDIT_PRINT.htm) [*PrintStatus* property is set to 2 and if unsuccessful it is set to 3. The following is an example of a](tmp/PROP_RICHEDIT_PRINTSTATUS.htm)

*PrintStatus()* event handler:

\- DEFEVENT Template.rtfControl1.PrintStatus() SELECT CASE (..PrintStatus) CASE 0 REM Print open successful ..Print() ..PrintClose() CASE 1 REM Print Open fail . . . CASE 2 REM print doc successful . . . CASE 3 REM Print doc fail . . . CASE 4 REM user cancelled page setup or printer select dialog . . . END SELECT END EVENT

Note that the documents are not physically printed until the

*PrintClose()* method is called. This is to allow multiple documents to be prepared before they are actually sent to the printer as is the case with certain tasks for example a mail merge.

 

 
