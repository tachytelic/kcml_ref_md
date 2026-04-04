# Changes to KCML 6.10 that are not also in KCML 6.00

Date

Build

Fix

2001-06-20

7171

REF5450: Changing the text of a button caused it to lose focus.

2001-06-21

7172

ENH: Allow editing of \<include\> files with kwebserv

 

 

REF5451: Was not sending the correct HALT and RESET keys to KClient when executed via the Connection Manager or inetd on Unix.

 

 

REF5440: Adding a description to a DBEdit that didn't already have one could lose any text that it previously contained.

 

 

ENH: SOAP and COM servers no longer use TERMFILE

 

 

REF5337: Tabbing into a grid that has TabThrough set was sometimes returning to the last cell that was edited rather than the first cell of the grid.

 

 

REF5403: Using the stock "Background" colour was not always choosing the right colour and sometimes came out black.

 

 

REF5438: Setting the grid NoSelection property did not always stop the highlight text colour was still being used resulting on white text on a white background with default Windows colours.

 

 

REF5446: On a grid cell that is the last cell of a grid and has the EditAlwaysValidate property set, it was possible to get into a state where trying to tab off always generated a validate and two EditRowNotify events, but the user was unable to leave the grid.

 

 

REF5449: When a grid cell is being edited, it is still sometimes possible to click on part of the cell that is not covered by the edit control (e.g. the grid lines). Such clicks were causing strange effects, but are now ignored.

 

 

REF5456: After continuing from a trap in a show event handler that terminates the form, the hourglass was being left up on the parent form.

 

 

REF5453: Increased the length of a pathname for \$SELECT from 63 to 256 characters.

2001-06-22

7173

REF5458: KCML, connected directly to the Unix inetd, failed to load environment variables from a **kcmlprofile**.

2001-06-25

7176

REF5459: The cached password could become corrupted when changing a KClient connection's properties.

 

 

REF5461: Save program information for the \$IMAGEF statement was sometimes being lost.

 

 

REF5447: Could gain access to ODBC after the licence file had been removed.

2001-06-26

7177

REF5462: The workbench ALT-Up and ALT-Down functions should not be available in debug mode.

2001-06-28

7179

REF5466: LOAD RUN will now use the value of the \$START environment variable.

2001-07-03

7184

REF5469: setting focus to a non-button control when focus was currently on a button could result in the default pushbutton state being incorrectly set.

2001-07-10

7191

REF5467: Shell commands with standard error redirected ie. 'command 2\> file' would display linefeeds incorrectly under Unix.

2001-07-11

7192

REF5477: Display accelerator text correctly on top level menu items.

 

 

REF5478: WKCML client installer kcmllan.exe was broken on Win9X and Win2000

 

 

REF5479: Select text when tabbing into a dbedit.

 

 

REF5480: When changing the contents of a tree or listbox control on a form other than the currently active one the control would not be redrawn until the current form terminated.

2001-07-17

7198

REF5400: Fixed display glitch on arrows with no outline and join-style ends.

 

 

REF5484: KServAdm will now terminate a KCML 5.02 process.

2001-07-19

7200

REF5485: Scrolling a grid using scroll bars or page-up / page-down keys could generate CursorMove events for cells that were not cursor enabled.

2001-07-20

7201

REF5492: Failing to display tree pictures if the picture was not already cached.

 

 

REF5486: Failed to put focus into a gridcell in a tab-through grid after a programmatic SetFocus if focus was initially on a button.

 

 

REF5415: Could generate an extra validate event when changing tab pages from within a valiate event.

 

 

REF5488: Tag lookup of an empty string will now work for a simple style dbedit drop list.

2001-07-23

7204

REF4842: Fixed display glitch when KClient overlaps the Windows task bar and the form text is changed. Only occurs with some graphics cards.

2001-07-24

7205

REF5501: Logging in to an NT server could appear to hang for one minute.

2001-07-26

7207

ENH: Changed the implementation of BYREF for strings and arrays. Now if you have a variable A\$ and pass it using BYREF to a subroutine where it is declared as B\$, a MAT REDIM on the original A\$ will immediately be reflected in B\$ and vice versa. Prior to KCML 6.01 such programming was not permitted.

2001-07-30

7211

REF5506: Grid ServerEdit event broken. Send grid Text\$ with event. Store tabthrough direction and move the cursor to the next or previous cell as appropriate after the event.

 

 

ENH: If a KI_REBUILD on a type 7 file finds duplicate keys all indices are rebuilt, but an error status of KE_DUPLICATE is returned.

2001-08-02

7214

REF5466: Fixed a problem where a dbedit with AlwaysValidate set could generate a spurious validate when dedugging.

2001-08-03

7215

ENH: The REDIM keyword in \$DECLARE and method calls is now available with scalar strings and will now redim each element of an array big enough to hold the biggest element of the returned array. Some problems with XML encoding in SOAP have also been fixed.

2001-08-24

7236

REF5541: An empty simple droplist style dbedit behaved incorrectly.

2001-09-12

7255

ENH: Added optional return status argument to KI_DIR, which no longer stops at directories with bad permissions, but continues having set the status to KE_FILENOTFOUND.

2001-09-21

7264

ENH: Constants are now enabled by default.

2001-09-25

7268

REF5568: The syslog warning message produced when unable to locate a Cache\$ picture now identifies the picture control.

2001-10-08

7281

ENH: Changed \$(UN)PACK UTF-8+ so that it does not XML encode characters \> 0x7F. This now produces strings suitable for XML text elements that can be parsed with CALL XML_PARSE_BUFFER.

 

 

REF5578: XML_NEXT would return both a value and a status of 2 if the XML document only contained one element

2001-10-10

7283

REF5590: \$COMPILE will now recover from file errors like D82 or D83 if an ERROR clause is used.

2001-10-15

7288

ENH: LIST DT also lists XML handles

2001-10-17

7290

ENH: Column names are now automatically qualified with an IPREFIX, if it was supplied in the CREATE TABLE statement. Any prefix supplied to KI_FLD is additional to any IPREFIX. Qualified names must be used in SQL DML statements, but unqualified names used in SQL DDL statements and in KI_BIND_COL.

2001-11-01

7305

ENH: If a prefix is passed to KI_FLD and the table already has an IPREFIX defined, strip off the IPREFIX from the column names and just use the IPREFIX.

2001-11-09

7313

ENH: Changed the way sym values are calculated so that they can be spotted by the workbench and other tools and displayed as SYM(var) rather than just numbers.

2001-11-12

7316

ENH: Changed KI_READ_RAW so that if an array is passed to hold the returned ROWIDs, then one ROWID is placed in each element of the array.

2001-11-30

7334

ENH: Now error attempts to call nested subroutines from outside. The forms browser now shows nested subroutines in the tree hierarchy.

2001-12-12

7346

ENH: Allow columns of greater than 256 bytes to be used in word search indices. This has required the KDB version to be changed to 7.1, all tables now created with a 6.01 KCML will create 7.1 tables. Before upgrading from 6.00 to 6.01 word searches need to be dropped, after the upgrade thay can then be re-created, tables without word search indices do not need any changes. Note also changes to KI_INFO output when reporting on word search indices.

2001-12-28

7362

REF5704: Handle embedded spaces in the -C command line when fetched with 'KCMLCommandLine(STR()).

2002-01-08

8008

REF5711: On a wizard style tab hitting next/prev will set focus to the correct control on the new page.

2002-02-06

8037

Support conditional loading in src files.

2002-02-11

8042

REF5744: Programatically changing a menu item's Help\$ did not work.

2002-02-13

8044

ENH: KI_EXECUTE now returns a zero rowcount for a SELECT statement. However, if the SELECT will return no result set the KI_EXECUTE call returns a KE_ENDOFFILE\_ status.

2002-02-15

8046

ENH: Changed the internal table schema format so that the numbers held as part of a RANGE column specifier are in SY8 format.

2002-02-22

8053

ENH: Added an SQL DROP DATABASE statement.

2002-02-25

8056

ENH: Added a FROM CATALOGUE clause to the DROP TABLE statement. Allows a table's catalog entry to be removed without removing the table's .kdb file.

2002-02-28

8059

REF5776: Handle keyboard acceleration in OCX controls.

 

 

ENH: Changed [KI_START_ON](mk:@MSITStore:kdb.chm::/tmp/KI_START_ON.htm) to treat any insignificant key segments as 0x00 or 0xFF depending on the direction of the search.

2002-03-01

8060

ENH: Default KClient cache size changed from 2MB to 1/5 of free disk space up to a maximum of 50MB.

2002-03-05

8064

REF5778: Fixed problems created by using magic numbers for syms when used with the Sym and SymNext form properties.

2002-03-06

8065

ENH: Allow tablespaces to be created locally to a service using a LOCAL clause to CREATE TABLESPACE.

 

 

REF5779: Data aware fields were not up to date inside a grid EditValidate event thrown by a ServerEdit event. A ServerEdit event would not be thrown when clicking the grid cell if focus was not already on the grid.

2002-03-07

8066

ENH: Added a [KI_START_FIRST](mk:@MSITStore:kdb.chm::/tmp/KI_START_FIRST.htm) call that restricts the size of the rowset returned when connected to an Oracle database to be controlled.

2002-03-11

8070

REF5733: Debug builds only. Check whether we have a suitable debugger installed before presenting an ASSERT Message Box.

2002-03-12

8071

ENH: Support \$PACK extended type TIMESTAMP and add a [\$TIMESTAMP](/$TIMESTAMP.htm) function.

2002-03-13

8072

REF5741: Fixed undo in workbench.

 

 

ENH: Honour the max_rows parameter to KI_START_FIRST when connected to a KDB database.

 

 

ENH: A new [SELECT MODULE](/SELECT_MODULE.htm) statement controls the module upon which subsequent @LIST statements will operate.

2002-03-14

8073

ENH: The [SOAPSTART](/EnvVars.htm#SOAPSTART) environment variable can be set for a service in kconf.xml to specify the program to be run when a SOAP server is started using that service. It takes precedence over the START variable which can also be specified in the service for interactive connections.

2002-03-15

8074

ENH: [KI_START_FIRST](mk:@MSITStore:kdb.chm::/tmp/KI_START_FIRST.htm) now takes a segment count which is used to control the number of significant segments in the key. Any insignificant segments are set to 0x00 or 0xFF as appropriate.

 

 

ENH: [DIM()](/DIM(.htm) and [LEN()](/LEN(.htm) can be used with fields when DIMing variable as in DIM a\$LEN(.f\$)

2002-03-18

8077

ENH: [BOOL()](/BOOL(.htm) can be used on strings and will interpret "T", "1" or "Y" as TRUE and "F", "0" or "N" as FALSE

2002-03-19

8078

ENH: The [CNUM()](/CNUM(.htm) function can be used to convert a string to a number.

 

 

ENH: The XML DOM constants are now defined by default and not just while the DOM object is loaded.

2002-03-20

8079

CHG: The BOOL pack specifier now packs TRUE as "1" and FALSE as "0"

2002-03-21

8080

ENH: KCML now supports a -S command line switch to load a service environment using kconf.xml without requiring the use of the connection manager.

2002-03-22

8081

REF5804: \$UNPACK("E=BASE64") on string arrays could crash.

 

 

ENH: KDB handles are now typed and the workbench will tooltip variables that contain handle values as handles displaying the name of the table, the last error and other table specific information.

2002-03-25

8084

CHG: The SY8 pack type has been renamed as FP.

 

 

ENH: [KI_START_BETWEEN](mk:@MSITStore:kdb.chm::/tmp/KI_START_BETWEEN.htm) can be used to specify a starting and an ending key and thus limit the size of the rowset that will be traversed. This is an important optimization that should be used where possible with Oracle tables.

2002-03-26

8085

ENH: Field arrays can be used as module variables.

2002-03-28

8087

ENH: Changes made to KDB tables to improve performance on reads mean that internal data structures have been altered. The new table format is version 7.2. Opening a KDB table in write mode will automatically reformat the table to the new format. It will not then be possible to open the table with any earlier version of KCML.

2002-04-02

8092

ENH: Set a grid's Index property in a validate event if the cell has a drop down list. The Index value is only valid within the Validate event.

2002-04-04

8094

REF5822: Unix [\$MACHINE](/$MACHINE.htm) did not include any daylight saving time bias in the timezone offset.

 

 

REF5821: Pass through legacy dbedit Type\$ to KClient without interpreting as a pack format.

 

 

[POS](/POS(.htm) and [VER](/VER(.htm) now support UTF-8 chacrter encoding.

 

 

New [kmake](/kmake.htm) and [kc6](/kmake.htm) utilities.

 

 

New context menu options to load module src component into foreground ( [Load into Foreground](mk:@MSITStore:workbench.chm::/wbcodecmenu.htm) ).

2002-04-11

8101

ENH: [\$SELECT](/$SELECT.htm) will no longer reset the device table and close all streams and tables.

2002-04-15

8105

REF5831: Display correct text colour when editing a grid cell.

 

 

REF5835: Protect against possible A04 when returning a string from a method.

2002-04-16

8106

Support sequences and optional BYREF parameters in KCML SOAP server. Fix bug whereby BYREF strings were being clipped.

2002-04-18

8108

ENH: More reliable and efficient multi channel KClient-KCML protocol for direct and connection manager connections.

 

 

KI_REBUILD utility calling fsort utility did not report an error if it failed to get enough memory. This would leave a KDB table's index in a corrupt state.

2002-04-26

8116

REF5858: SAVE \<G\> could crash on 32-bit Unixware versions.

2002-04-29

8119

ENH: EventPending can now distinguish between events and properties coming from the client on connections using the multi-channel protocol.

 

 

REF5834: a multifile LOAD\<\> where the first file was in new ascii format was not clearing out previous lines correctly.

2002-04-30

8120

REF5851: Rich text control's font color picker did not work under Windows XP.

2002-05-01

8121

REF5867: A memory overwrite was caused if you passed a long string to CNUM(

 

 

ENH: KClient cache directory is now set per user and defaults to a subdirectory of the user's 'My Documents' folder. This prevents bottlenecks caused by concurrent cache access from multiple users in a Citrix environment.

 

 

REF5869: MAT REDIM of global arrays in a global partition which executes a DEFFN @PART was reporting spurious P59 errors as a result of a secondary resolve by \$BREAK!.

 

 

REF5870: MAT REDIM of a scalar string using its SYM, e.g. MAT REDIM SYM(\*a)\$len, is now supported.

 

 

REF5873: FLD( operators could not be applied reliably to \$OPTIONS RUN, \$OPTIONS LIST or \$OPTIONS#.

 

 

REF5874: The Workbench record browser and LIST R generated bogus occurs for the field before a SKIP.

 

 

REF5875: Fix for COM problem in Excel where a method was invoked as a property put rather than the more sensible property get.

2002-05-02

8122

REF5882: A TEXT(s, r) fld format was only clearing out the first line in the \_Init function.

2002-05-03

8123

ENH: Can use interactive SHELL commands when connected via the connection manager.

2002-05-07

8127

ENH: Server side text storage in grids was not being updated when using the cell Clear() method.

 

 

ENH: Define [\$OPTIONS RUN](/$OPTIONS_RUN.htm) byte 62 for compatability error checking. Two bits are currently defined for checking grid cell references outside the grid and for attempting to retrieve properties not stored on the server. Prior to this no checking was performed and for compatibility with existing applications these error checks are disabled. Developers should be encouraged to enable them.

2002-05-09

8129

REF5883: Evaluate Window wrongly displayed line index as opposed to line numbers, on trap.

 

 

REF5887: Updates involving large number of blob deletions/writes could corrupt the table.

2002-05-10

8130

REF5889: Memory leak if a DEFSUB returns an OBJECT value but the result is ignored by the caller.

2002-05-13

8133

REF5890: Selecting a blank entry in a DBedit dropdown would select the first entry in the list in the validate.

 

 

REF5877: Pack images were not creating the correct Type\$ dbedit format.

2002-05-17

8137

REF5896: Record initialising function might report an error for wrong number of arguments or destination buffer too small but the error was not trappable.

 

 

REF5897: Handle NULL interface in a multi method sequence with a sensible serror message.

2002-05-20

8140

ENH: Added two properties to SOAP client objects. .Response\$, .Request\$. These return the Response and Request strings that are passed to and from server.

2002-05-22

8142

ENH: Added KI_CREATE_TMP, which is exactly the same as KI_CREATE except that KDB logging will not record the creation of the temporary file.

 

 

REF5898: KClient connection icons are no longer limited to 16 colours.

2002-05-23

8143

REF5900: Fixed a problem where a grid control could grab focus after an event.

 

 

REF5899: The form .SymNext property was incorrect for the last control on the form.

2002-05-27

8147

REF5901: Controls could get out of step if a word search deletion failed during a KI_DELETE.

2002-06-05

8156

ENH: Add SAX support to the Xerces XML parser allowing parsing of very large documents using a callback API.

2002-06-10

8161

REF5911: Forcing the ValidateText\$ property in a grid cell EditValidate() event, on a data aware row, was not updating the grid in the client the second time around due to a server optimisation thinking the cell was already up to date.

2002-06-12

8163

REF5913: Fix a problem in MAT REDIM of a zero sized 2-D numeric array to a new size where the second dimension was one. This was incorrectly converting the array to 1-D.

2002-06-17

8168

REF5920: String sent by server wasn't being converted to unicode, for display in browsers new form dlg.

 

 

REF5911: The SYM values returned by the method GetDataField() were not using the new magic number scheme, meaning that direct comparisons with taking the SYM of the data source or data field variable would always fail.

2002-06-19

8170

REF5925: Initialization of a DEFRECORD was confused by use of a FLD AT() to backup in the record.

 

 

ENH: Add [ULEN8()](mk:@MSITStore:kcmlrefman.chm::/ULEN8(.htm) to get the length in characters of a UTF-8 string, [UNEXT8()](mk:@MSITStore:kcmlrefman.chm::/UNEXT8(.htm) to get the byte index of the next UTF-8 encode character in a string and [UPREV8()](mk:@MSITStore:kcmlrefman.chm::/UPREV8(.htm) to get the index of the previous character.

2002-06-20

8171

REF5932: Extra '\n' being sent with kprint data caused problems.

2002-06-21

8172

REF5937: Dump in Excel COM sample program.

2002-06-24

8175

REF5942: Two minor workbench bugs. Unicode problem when looking up a folder using the file browser. A problem where the context menu option 'CLEAR P; load into foreground' could be called incorrectly, displaying odd data.

 

 

REF5941: LOADing and stepping through a program while traps are enabled in the workbench, could cause a crash.

 

 

REF5945: Passing a global array or string using BYREF did not work and would lead to a GPF on CLEAR.

2002-06-25

8176

ENH: XML panic files now use a W3C compliant stylesheet rather than the obsolete Microsoft IE5 one. You therefore need a standards compliant XML parser as shipped with XP, IE6 and Mozilla. IE5.x users should upgrade their XML parser component to MSXML3 or MSXML4. At this time this is avaiable from Microsoft at this [location](http://msdn.microsoft.com/downloads/default.asp?url=/downloads/sample.asp?url=/MSDN-FILES/027/001/772/msdncompositedoc.xml).

2002-06-26

8177

ENH: In the unicode version of KClient string arguments to \$DECLARE functions will be automatically translated to unicode only if the function has a unicode form. The Windows convention of decorating the unicode function name with 'W' is assumed.

2002-06-28

8179

REF5951: An error using the form.Import() was dumping the application into the console window rather than reporting the error properly.

2002-07-01

8182

ENH: Add TreeWalker and NodeFilter objects to Xerces DOM. Better callback support in the Workbench.

 

 

REF5954: Common variable chain was getting reordered after the LOAD of an overlay. As a consequence of this fix any modules will have to be rebuilt.

2002-07-02

8183

REF5955: Windows 2000 and XP hide the mouse cursor when text is entered into an edit control. KClient did not always show it again when the mouse was moved.

2002-07-03

8184

REF5958: Using the mouse to evalute a statement with a long return string, in the workbench, could cause a crash.

 

 

ENH5959: Tooltips containing large amounts of text will remain visible for up to 32 seconds.

 

 

REF5957: Stop DEFSUB labels being shown as undimmed even though they were in a loaded module.

 

 

REF5960: Fix corruption of symbol table after instantiation of module variables introduced in build 8182.

 

 

ENH: Changed the Xerces DOM MemBufOutput methods getLength() and getData\$() to be properties Length and Data\$ respectively.

2002-07-04

8185

REF5962: Workbench could be confused by a nested DEFFORM in a collapsed DEFEVENT.

 

 

ENH: Programs compiled on a UTF-8 encoding KCML are marked as such and will give a D88 error if loaded by a KCML using codepage encoding and vice versa. When compiling with UTF-8 enabled all string literals in a program are now checked for valid UTF-8. Print devices with LPD=Y will now send a command to kprint to enable UTF-8 if this encoding is used on the server.

2002-07-05

8186

ENH: \$UPPER and \$LOWER are no longer limited to LET statements and can be used anywhere as functions returning a string result. Code compiled on 6.10 using these functions will not execute on 6.0 but code compiled on 6.0 will execute on 6.10.

2002-07-08

8189

REF5653: BYREF in a \$DECLARE call changed a DIM argument into a STR argument.

 

 

REF5967: Problem with common chain getting corrupt after a compiled program is loaded.

2002-07-09

8190

REF5971: XML entities in the response were being incorrectly decoded by the SOAP client.

2002-07-10

8191

REF5973: Unicode problem cause bad string display in the workbench autosave dialog.

 

 

ENH: Add checks to stop the redefining of records as constants and vice versa. Changes to the symbol table means that any programs or modules should be recompiled.

2002-07-11

8192

REF5966: A grid cell validate event handler that returned FALSE could see the text being put back in the wrong cell.

2002-07-16

8197

REF5985: Fix for REF5901 was incomplete leading to table corruptions after a delete on a table with a word search.

 

 

REF5972: Improved performance of kservice.exe especially when authenticating KCML sessions. This means under NT more simultaneous logins can be accepted.

 

 

REF5987: Fixed problem with Workbench search dialog not displaying full string in edit box.

2002-07-17

8198

REF5989: When setting a dbedit's DropDownFilled property any text already in the edit is matched exactly against the items in the list ignoring partial matches eg. aa against aa1. This matches the operation of setting Text\$.

 

 

ENH: Add PUBLIC and PRIVATE keywords to be used with DEFSUB in a module.

2002-07-18

8199

ENH: \$LOWER and \$UPPER now use Unicode translation tables if USING_UTF8 is in effect.

 

 

ENH: KDB type 7 tables on Unix versions now have NT style lock semantics. You can no longer relock the same row without getting an error. In addition you can't rewrite or unlock a row that you didn't have locked on the same handle. When a table is open in write mode on two handles the write mode flag now accurately reflects the state.

2002-07-19

8200

ENH: On Unix systems *kcml* and *kc6* now use a shared library, *kserver.so*. (*kserver.sl* for HP-UX), to prevent mismatched versions when compiling modules.

2002-07-23

8204

REF5936: Workbench F1 help wasn't being displayed if a UNICODE client was used.

 

 

REF6000: Multiline text from the client will appear in the server using 0x0D carriage return line breaks. Setting a control's Text\$ with multiline text no longer inserts 0x0D 0x0A carriage return linefeed pairs. in the server. Plain 0x0D line breaks are sent between the client and server.

2002-07-24

8205

ENH: New option in the menu editor of KForm, labelled "First toolbar icon". Those menu items that have this option checked appear out of order on the toolbar menu as they always appear first. The intention here is for an Exit menu item which on a typical form will appear as the last item on the first (usually called "File") menu. Normally this leaves the Exit toolbar icon after other icons, but by checking this option the Exit toolbar icon can be made to consistently appear first (and hence always in the same place) across all forms.

 

 

ENH: Improved SOAP object browser. Better support for DOC=Y in the SOAP client when WSDL is complex. Better error messages particularly for bad WSDL URL.

 

 

REF6005: Setting the 'break on condition' in the workbench trap dialog to "" would cause a crash.

2002-07-25

8206

REF6006: setting \$OPTIONS LIST byte 4 to zero was still breaking lines that wrapped on the screen when copied to the clipboard.

 

 

ENH: The noise words file for a CREATE WORD INDEX statement is now expected to be an XML file.

 

 

REF5996: \$TRAN R will now cope with UTF-8 string if USING_UTF8 is in effect.

2002-07-26

8207

REF6909: A program that DIMs an @variable array in the foreground could potentially crash after a load.

 

 

ENH: Changed workbench F12 (insert chevrons) to only do the search afterwards if the current search is for literal strings.

 

 

REF6010: The SKIPnn keyword was not being accepted in \$FORMAT.

2002-07-29

8210

ENH: Added a new call, KI_WS_NOISE_INFO, to retrieve the list of noise words associated with a particular path on a particular handle. The words are returned in XML format.

2002-07-30

8211

REF6011: Workbench Module Browser could crash the workbench if the module contained \$DECLAREs where the subroutine name started " '\_ ".

2002-07-31

8212

ENH: A loophole that enabled SYM of a nested function to be taken from outside of the parent function will now produce a run-time error.

2002-08-01

8213

ENH: Added [SetObject()](mk:@MSITStore:kcmlforms.chm::/tmp/PROP_TREEITEM_SETOBJECT.htm) and [GetObject()](mk:@MSITStore:kcmlforms.chm::/tmp/PROP_TREEITEM_GETOBJECT.htm) methods to associate a KCML object with a tree item.

2002-08-02

8214

REF6023: No longer encoding chars above 0x7F as XML entities in \$PACK(E="XML").

2002-08-05

8217

REF6014: \$RELEASE LOAD RUN background processes could fail to start. Unix only problem.

 

 

\$UNPACK(E="TIMESTAMP") could error due to trailing space removal from source string.

2002-08-09

8221

Don't encode white space characters of CR, LF or TAB as XML entities in \$PACK(E="XML"). Just leave them as characters. Other characters below HEX(20) will be converted to general XML entities.

 

 

\$PRINTF can now handle %s minimum size and precision specifiers for UTF-8 strings

 

 

REF6021: Multiline data aware text was being clipped to the length of a single occurrence.

 

 

ENH: Added a read-only name\$ property to all form controls to make them easier to identify.

 

 

ENH: Added a DataField\$ property to data aware form controls.

2002-08-12

8224

REF6026: \$UNPACK(E="XML") could fail if the destination buffer was exactly filled.

 

 

REF5988: If the Type\$ property is deduced from the DataField property, then grid columns that were being sized by type were not being sized until the Type\$ was sent to the client, at the point when the first cell data that used it was sent. Thus grids that started off with no data did not have their columns sized correctly.

2002-08-13

8225

REF6019: Fixed a problem where tabbing into a grid and clicking a cell's ellipsis button would generate a spurious grid Left Click event.

 

 

REF6029: DIM a\$1 : \$PACK(E="XML") a\$ FROM "\>" did not report an error

2002-08-14

8226

REF6031: Not always updating properties of a toolbar button with the 'First Toolbar Icon' style set.

2002-08-21

8233

REF6039: Tooltips for help text and truncated edit text did not display ampersands.

2002-08-27

8239

REF6041: Editing Form controls via KForm could leave a trailing character when returning to the workbench. This would only happen if KCML was running in UTF8 mode.

 

 

REF6044: If a component program from a module is loaded into the foreground for debugging it should be allowed to call private functions in the overlaid program while executing in other components of that module.

2002-08-29

8241

REF6045: KClient could hang under windows 98 if the KCML process finished.

2002-08-30

8242

ENH: Allow REDIM on a string assignment for scalar strings. Also allow concatenated strings as arguments to functions and as the return value of a function.

2002-09-02

8245

REF6042: Setting up date aware field definitions in the create event had no effect when there was no explicit type\$ (as there should be today).

 

 

REF6048: \$PACK and \$UNPACK did nothing if the pack list variables were defined as SYM(\*)\$ strings.

2002-09-03

8246

REF6047: Fixed a problem pasting into a multiline dbedit with a simple length limiting TYPE\$ for instance S10.

 

 

REF6040: Setting a whole-grid default type\$ eg. .gridControl1.Cell(0, 0).Type\$ = "N-13.2" works correctly.

2002-09-04

8247

REF6054: Changing a tab control's appearance at run time does not move its child controls.

2002-09-05

8248

REF6056: Idle events could become queued while kclient was performing a modal task such as a menu selection.

2002-09-06

8249

ENH: Add LOG=Y to \$DEVICE options to request syslogging open open and close on the device. This permits support to see if spooled output has actually been sent to a spooler.

 

 

REF6058: Fix for problem retrieving an error message after a COM error.

 

 

REF6030: Fix for problem with KEY clause on FSORT introduced in 6.10
