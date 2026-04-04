# Changes to KCML 6.20 that are not also in KCML 6.10

<table data-border="1" width="100%">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th width="12%">Date</th>
<th width="6%">Build</th>
<th>Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>2002-09-10</td>
<td>8253</td>
<td>ENH: Added LOCAL DEFRECORD to define records with local variable scope. That is, when executed, local variables for all the fields and the constant size are created. Also a local '_init_recname() function is defined. For all record types, a function '_enum_recname() is also defined to allow a programmer to retrieve all the fieldnames from a field, and their pack values.</td>
</tr>
<tr>
<td>2002-09-11</td>
<td>8254</td>
<td>REF6067: Help(F1) lookup on statement did not work in workbench if the token began with a $</td>
</tr>
<tr>
<td>2002-09-12</td>
<td>8255</td>
<td>ENH: Setting STR($OPTIONS RUN, 61, 1) to 0xFF sets the current language to UTF-8 for the $PACK( and $UNPACK( UTF-nn conversions.</td>
</tr>
<tr>
<td>2002-09-12</td>
<td>8256</td>
<td>REF6075: Not correctly parsing the command line in a .kcc connection file.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6072: Fixed a workbench crash when deleting a line number, while you have selected text.</td>
</tr>
<tr>
<td>2002-09-16</td>
<td>8259</td>
<td>REF6074: Fixed a workbench crash when pasting multiple lines of code in, immediatly after a CLEAR P command has been executed.</td>
</tr>
<tr>
<td>2002-09-19</td>
<td>8262</td>
<td>REF6076: Fixed crash using the continue command in workbench, when it directly followed a syntax error entered into the console.</td>
</tr>
<tr>
<td>2002-09-20</td>
<td>8263</td>
<td>REF6089: Fixed workbench pasting, inserted lines may not be correctly saved with the rest of the program.</td>
</tr>
<tr>
<td>2002-09-23</td>
<td>8266</td>
<td>REF6091: Fixed a bug caused by the fix for REF6076. The workbench could crash if a syntax error occued in a DEFEVENT.</td>
</tr>
<tr>
<td>2002-09-30</td>
<td>8273</td>
<td>REF6102: If opening the catalog file failed for a database being viewed via the workbench. An ASSERT would be generated. This has now been fixed.</td>
</tr>
<tr>
<td>2002-10-08</td>
<td>8281</td>
<td>ENH: Added a %S format to $PRINTF which will not strip trailing spaces from inserted strings.</td>
</tr>
<tr>
<td>2002-10-14</td>
<td>8287</td>
<td>ENH: Support Xerces 2.1, specifically its multiple inheritance for the Document object.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Allow comparison of objects in IF (OBJECT a = b) even if the objects came from different sources.</td>
</tr>
<tr>
<td>2002-10-15</td>
<td>8288</td>
<td>REF6129: Could get a spurious error status of 52 when reading the last row of a table using KI_READ_RAW.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6115: Require BYREF for record initializer functions sources.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6119: HEX fields now initialized to ALL(00) rather than ALL(20) sources.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6128: ERR$(30) was returning a spurious value taken from the last result of the function. sources.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6130: Could get spurious text in workbench save dialog.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6131: Workbench could crash if trying to evaluate a number greater than 120 characters.</td>
</tr>
<tr>
<td>2002-10-16</td>
<td>8289</td>
<td>REF6133: Using XLA=Y with more than one $DEVICE to invoke $PRINTER could crash</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6132: BREAK could error when use din a FOR OBJECT iteration immediately after a method call that returned a string value.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6118: Setting the picture property of a duplicated menu item had no effect.</td>
</tr>
<tr>
<td>2002-10-18</td>
<td>8291</td>
<td>REF6137: Problems reading the catalogue when multiple KCMLs where creating temporary tables simultaneously.</td>
</tr>
<tr>
<td>2002-10-21</td>
<td>8294</td>
<td>ENH: KI_START_BETWEEN and KI_START_FIRST return a status of KE_ENDOFRANGE iff the max_rows condition has been met.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6136: Fix problems with looking up in libraries BYREF callback functions and fields used in FLD AT(POS()) expressions</td>
</tr>
<tr>
<td>2002-10-22</td>
<td>8295</td>
<td>ENH: Support DOM3 serialization with Xerces 2.1</td>
</tr>
<tr>
<td>2002-10-24</td>
<td>8297</td>
<td>ENH: The environment variables $LOGNAME, $LOGIN, $KCMLDIR, $SYSTEMID and $TERMFILE are now read only. Any attempt to reset these variables with the ENV() function will be ignored.</td>
</tr>
<tr>
<td>2002-10-25</td>
<td>8298</td>
<td>ENH: Maximum KDB handles increased to 1024 ENH: Requirement for -y (use malloc) flag with dynamic objects (eg Xerces) has been relaxed on some platforms, viz. Linux and AIX.</td>
</tr>
<tr>
<td>2002-10-30</td>
<td>8303</td>
<td>REF6147: Grid cursor key navigation could hang moving through a cursor disabled cell with joins across multiple lines.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Allow the minimum word length in a word search index to be 2.</td>
</tr>
<tr>
<td>2002-10-31</td>
<td>8304</td>
<td>REF6150: A KEYIN in a program with SELECT PRINT set to a file could send a HEX(02012B0F) sequence to the file and possibly hang.</td>
</tr>
<tr>
<td>2002-11-05</td>
<td>8309</td>
<td>REF6149: Copying from the workbench to the clipboard could sometimes linebreak to leave a space at the beginning of the line that could be lost during a subsequent paste.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6146: Persistant toolbar menuitems not firing events in Unicode version of kclient</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6154: Attempting to set an edit group's visible property to false could hang the form. Although the form no longer hangs the programmer should not assume that because setting this property has no effect that this will always be the case.</td>
</tr>
<tr>
<td>2002-11-06</td>
<td>8310</td>
<td>REF6158: Error an attempt to pass a numeric field to a string argument and vice versa in a DEFSUB call.</td>
</tr>
<tr>
<td>2002-11-07</td>
<td>8311</td>
<td>REF6162: Workbench crashed occasionally single-stepping through code whilst attempting to display current variables.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Now defer allocation of memory for scalar strings in LOCAL DIM until they are first used. Permit zero size dimensions for LOCAL DIM scalar strings. Allow REDIM SYM(*x)$ in REDIM LET.</td>
</tr>
<tr>
<td>2002-11-08</td>
<td>8312</td>
<td>REF6165: The daylight saving time bias component of the GMT offset field in $MACHINE bytes 43 and 44 was not reliable for some Unix versions and has been replaced by a better algorithm.</td>
</tr>
<tr>
<td>2002-11-11</td>
<td>8315</td>
<td>REF6164: Don't generate a validate event if a read-only dbedit is set to AlwaysValidate.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6167: CONVERT TIME was confused and might give an X71 error if string to be converted was followed by numeric characters.</td>
</tr>
<tr>
<td>2002-11-13</td>
<td>8317</td>
<td>ENH: KDB 7.3 tables can have 16 segments per key</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Better memory compacting on $SPACE.</td>
</tr>
<tr>
<td>2002-11-14</td>
<td>8318</td>
<td>REF6172: New conatenation operator for REDIM and DEFSUB now treats blank strings as having a length of one to be compatible with previous behaviour in LET.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6173: KI_READ_NEXT with a path of zero could get confused by a KI_READ or KI_READ_HOLD on a different path or even the same path but in a different direction.</td>
</tr>
<tr>
<td>2002-11-19</td>
<td>8323</td>
<td>REF6163: Expanding Modules in workbench Module browser could cause server crash.</td>
</tr>
<tr>
<td>2002-11-21</td>
<td>8325</td>
<td>REF6183: We now ckeck that KLOGKEY is 4 characters. Introduced kwho utility which lists all the foreground users running KCML. This is useful where the connection manager is used as users don't appear in the operating system's who display. Default install directory is now /usr/local/kcml.</td>
</tr>
<tr>
<td>2002-11-27</td>
<td>8331</td>
<td>REF6201: Fixed a prolem when using the Duplicate() method on a grid, where the WholeDataAware property was not being duplicated.</td>
</tr>
<tr>
<td>2002-11-29</td>
<td>8333</td>
<td>ENH: Dropped DUMP environment variable. Added new DUMPCORE environment variable.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Better handling of large numeric SOAP arguments.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6207: Workbench record browser has been fixed to display records correctly.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6205: Possible to lose focus from a dbedit whose validate handler returns false by using the Ctrl-PgUp/Down hotkey to change tab pages.</td>
</tr>
<tr>
<td>2002-12-03</td>
<td>8338</td>
<td>REF6160: The workbench could crash during resizing, when using dual monitors.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6211: KI_ERROR_TEXT could crash when displaying a connection's error status.</td>
</tr>
<tr>
<td>2002-12-09</td>
<td>8343</td>
<td>REF6212: When enabling a menu all the toolbar buttons relating to it would be enabled, even if their corresponding menu items were disabled.</td>
</tr>
<tr>
<td>2002-12-12</td>
<td>8346</td>
<td>REF6214: Some disabled items were being displayed with the wrong color labels.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>After a LOAD RUN, a crash could occur in a program using DEF RECORD and modules.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Allow FLD(a$.b$.c) instead of FLD(FLD(a$.b$.c))</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6215: Fixed copy in workbench. Copy was inserting to many newlines, in wrapped, collapsed statements.</td>
</tr>
<tr>
<td>2002-12-13</td>
<td>8347</td>
<td>REF6161: Fixed workbench crashes while browsing records. This was cause by unresolve code, be more verbose with the user, prompting a resolve if necessary.</td>
</tr>
<tr>
<td>2002-12-16</td>
<td>8350</td>
<td>REF6218: Allow Citrix WTS clients to be properly identified so that multiple logins do not take separate user licences.</td>
</tr>
<tr>
<td>2002-12-18</td>
<td>8352</td>
<td>REF6043,5910: Fixed a bug when entering an invalid or duplicate control name into the kform32 popup edit window, which could cause a crash or a looped message box.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF5933: Partially fixed. When editing tab pages in kform32, the "Close" button now reads "OK" and the "Cancel" button is disabled.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6178: Top-level dialog controls (e.g. dbedits) can now have the same name as menu items.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a new "Data Bindings" page to the kform32 object browser (Tools|Object Browser) that will display a list of all DataBind controls, allowing them to be edited and their usage displayed.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When dragging and dropping a numeric column onto a form, kform32 will now automatically set the alignment property to "Right". Note that this option can be disabled via "Edit|Options|Miscellaneous".</td>
</tr>
<tr>
<td>2003-01-06</td>
<td>9006</td>
<td>ENH: Dropped DBCS support in favour of UTF8 in type 7 word search routines.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6219: Fixed Autosave in workbench. The timeout wasn't been recorded correctly.</td>
</tr>
<tr>
<td>2003-01-07</td>
<td>9007</td>
<td>ENH: Fixed problem with SOAP server arguments of zero length.</td>
</tr>
<tr>
<td>2003-01-08</td>
<td>9008</td>
<td>ENH: Tooltip truncated text on static text controls, dbedit labels and groupbox titles.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6233: Pasting a single new line into a blank program would crash the workbench.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6232: Trap Variables menu option in workbench could cause crash if in module.</td>
</tr>
<tr>
<td>2003-01-09</td>
<td>9009</td>
<td>REF6242: Fixed a redraw problem when changing images on a transparent button.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6243: DIM a$="test" would leave undimmed flag set on a$.</td>
</tr>
<tr>
<td>2003-01-10</td>
<td>9010</td>
<td>ENH6111: If a grid column's colsize property is set to largest and it is joined to cells on its right the text will flow into the joined cells before increasing the column width.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: If you take the SYM() of a DEFSUB label which is defined in a library then that label will be added to the common chain thus preserving the validity of the SYM value across a LOAD.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: It is no longer necessary to use the GOSUB keyword if invoking a subroutine through 'SYM(*). Existing statements will be recreated without the GOSUB which may cause backward compatibility issues with source taken back to previous version of KCML. However there is no change to the binary code generated and this will still be compatible.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: If a program was compiled with COMPAT32 set such that we use the old rules for passing strings back from functions, then an error will be signalled if the program is executed in an environment without COMPAT32 set.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6196: Fix for a tooltipping problem where the tooltip could not evaluate the function and the workbench cursor happened to be on a DEFSUB ant the time. The debugger then failed to allow stepping onto the next line.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6235: Taking the SYM of a LOCAL DEFRECORD enumerating function would fail if the parent function was in a library.</td>
</tr>
<tr>
<td>2003-01-14</td>
<td>9014</td>
<td>ENH: Added a CreateDataBind() method.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6247: Fixed a problem with occurs in data-aware controls using the _x7$ type extension where only a single line rather than the entire entity was being used in data-awareness.</td>
</tr>
<tr>
<td>2003-01-15</td>
<td>9015</td>
<td>REF6254: Fixed a problem where tabbing into a grid from a dbedit that fired a validate would require two presses of the tab key to work.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH6241: Generate a right-click event for a gridcell if Shift+F10 is pressed.</td>
</tr>
<tr>
<td>2003-01-16</td>
<td>9016</td>
<td>REF6259: Fixed a problem stopping library functions calling back into the foreground with 'SYM(*) introduced by the new ability to drop the GOSUB in these calls.</td>
</tr>
<tr>
<td>2003-01-17</td>
<td>9017</td>
<td>ENH: CTRL-G in the workbench now shows the function the cursor is in, including any function nesting.</td>
</tr>
<tr>
<td>2003-01-21</td>
<td>9021</td>
<td>REF6265: Selecting text in an integer edit works correctly when the text is right or centre aligned.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6264: FLD(a$.b$.c$) was not recreating properly in the IDE.</td>
</tr>
<tr>
<td>2003-01-22</td>
<td>9022</td>
<td>ENH: Support immediate mode RENAME OBJECT command to allow renaming forms and handle objects in a program.</td>
</tr>
<tr>
<td>2003-01-23</td>
<td>9023</td>
<td>ENH: Support $OPEN as a function taking a timeout value and returning a status so that it does not require a line number to poll a device to see if it is locked.</td>
</tr>
<tr>
<td>2003-01-28</td>
<td>9028</td>
<td>ENH: New structured error handling using TRY and CATCH As a result TRY, CATCH and THROW should now be considered as now reserved words though when possible KCML will attempt to spot their legitimate use as a variable.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: New option added to kform32 allowing the form definition to be edited by hand (<strong>File|Edit</strong>). NOTE: You should only use this option if you know what you are doing as it will cause the form to be re-created based on your changes.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: New option added to kform32 allowing a list of screen sizes to be maintained (<strong>View|Screen Sizes</strong>). These screen sizes are drawn as part of the main editor window background (640x480, 800x600, etc.).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: New option added to kform32 allowing form properties to be displayed (<strong>File|Properties</strong>), including the number of controls, the form size, etc.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When using the kform32 <strong>Align|Space Evenly|Down</strong> option and dbedit controls on an editgroup are selected, they will now be spaced 16 DLUs apart, starting from the top of the first control. Any single-line dbedit controls that are not the correct height (13 DLUs) will be updated.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: In kform32, when creating new dbedits on an editgroup or dragging columns from the table list onto an edit group, the new control will be aligned and spaced automatically.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a new kform32 option that will resize certain controls to ensure consistency (<strong>Size|Reset Control Sizes To Default</strong>).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a new option to kform32 displaying the various accelerator keys used by the program (<strong>Help|Keyboard Map</strong>).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: The kform32 <strong>Display Control Extents</strong> option now works for controls on nested tabs.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: When creating a new control in kform32 by selecting one from the palette and then clicking on the form, the correct default size will now be used, fixing a problem where a tiny control could end up being created.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: You can now drag multiple-columns onto a form from the table list in kform32. Controls will be created in the order they were selected and will be aligned/spaced automatically if dropped on an editgroup.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: You can add new columns to a form by double-clicking the column in the table list in kform32. The new column will be added below the last column added and will be aligned/spaced correctly.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Dropping a dbedit control on top of another dbedit in kform32 will no longer get the parentage wrong.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: A new kform32 option (<strong>Edit|Options|Misc|Include editgroup contents when setting tab order</strong>) will suppress the display of tab positions for dbedits on editgroups when using the Edit|Set Tab Order option. This is to support an upcoming kclient feature that will automatically set the control order.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When setting the tab order in kform32, you can now use <strong>Shift+Click</strong> to set the starting tab position.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: When displaying the tab order in kform32, menu controls and the status bar will no longer be included in the tab position count.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When displaying the tab order in kform32, if a tab page only has one control, the control no longer has its tab position displayed.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When displaying the tab order in kform32, clicking on the form background will now toggle tab ordering off.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a new kform32 option, <strong>Tools|Check Tab Order</strong>, which will display the current tab position of controls on the form, with incorrect tab ordering displayed in red.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a new kform32 option, <strong>Tools|Auto Tab Order</strong>, which will automatically set the tab order on a form.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: It is now easier to click on an editgroup when setting the tab order for controls in kform32.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When using the kform32 property list, you can now hit <strong>TAB</strong> to select the next control after you have changed a property.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When selecting a dbedit control in kform32, the Label$ property will now be selected automatically (if the previously selected property doesn't appear in the list).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: When setting the Label$ property of a dbedit control on an editgroup in kform32, the dialog is now redrawn to fix a paint bug.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The kform32 About dialog has been replaced.</td>
</tr>
<tr>
<td>2003-01-29</td>
<td>9029</td>
<td>REF6273: Using CreateDataBind() passing the SYM of a function defined in a library could crash.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Increased size of buffer for CTRL-G cursor info workbench function to stop truncated messages.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6270: Extra security layer on Unix versions of the Connection Manager.
<ul>
<li>Access will only be granted if a <strong>.kcmlLogin</strong> file exists in the user's home directory.</li>
<li>Added support in the <em>/admin</em> Web pages to list user accounts and create or remove <strong>.kcmlLogin</strong>.</li>
<li>The install process will create <strong>.kcmlLogin</strong> files for accounts which match the list of &lt;adminusers&gt; in <em>kconf.xml.example</em></li>
</ul></td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6279: Fixed a crash on NT4 if an application mistakenly puts separators on a top level menu bar.</td>
</tr>
<tr>
<td>2003-01-29</td>
<td>9029</td>
<td>ENH: Renumber of P57 errors issued by $PACK/UNPACK and some UTF-8 translation functions. Now errors where the output buffer is too small will be reported as X76 and where the input was badly encoded will be reported as X73. Some errors about bad extended field specifiers that were previously P57 are now reported as P58. P57 will now only be used for problems with extracting a substring because of bad arguments to STR and FLD operators.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Add Turkish (<a href="mk:@MSITStore:kcmlrefman.chm::/LanguageCodes.htm">language code</a>=15) to the list of languages supported for translation between the native codepage (Windows 1254 or ISO-8859-9) and UTF-8 on the server with $(UN)PACK extended format E="UTF-8".</td>
</tr>
<tr>
<td>2003-01-30</td>
<td>9030</td>
<td>ENH: Added <a href="mk:@MSITStore:kcmlforms.chm::/tmp/PROP_EDIT_LISTFIRST.htm">First</a> property to dbedits to provide the same functionality as for listboxes - to enable enumeration of the items in the list.</td>
</tr>
<tr>
<td>2003-01-31</td>
<td>9031</td>
<td>ENH: The structure returned by the '_Enum_ record <a href="mk:@MSITStore:kcmlrefman.chm::/DEFRECORD.htm#enum">pseudofunction</a> has been extended by 64 bytes to hold the text of any REM on the same line as the FLD. This REM conventionally holds the field title for databound database columns.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The '_Find_ record <a href="mk:@MSITStore:kcmlrefman.chm::/DEFRECORD.htm#find">pseudofunction</a> now takes two arguments. The first is the name of the field to be found in the record and is unchanged but the second is now expected to be an instance of the same structure used for the result of a 'Enum_ function. It must be the right size and must be passed BYREF.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The structure of the program code generated for DEFSECTION, DEFRECORD and FLD has been changed to reduce slightly the memory used. This means that programs and libraries compiled before build 9031 will not be compatible and will error.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: There are now built in constants for the <a href="mk:@MSITStore:kcmlrefman.chm::/LanguageCodes.htm">language codes</a> used for chevron and codepage operations.</td>
</tr>
<tr>
<td>2003-02-03</td>
<td>9034</td>
<td>REF6275: The client did not support input of negative numbers into an edit control bound to a INT(4) datafield or which had a type$ of "I-4".</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Anchor code in kform32 changed to fix a problem selecting some controls (such as a frame on a tab for example). Anchored controls on tab pages will now be repositioned correctly when the tabs are sized.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a new kform32 option, <strong>Tools|Control Events</strong>, that allows you to choose which events are set when creating new controls.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When adding a tab control or frame to a new form, you can now simply click to create a control that will fill the form client area.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: When creating a new editgroup in kform32, simply clicking on the form will no longer create a 0x0 sized control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The new kform32 <strong>Edit|Form</strong> option now has a replace facility, a custom font option and will now display child elements of controls on separate lines.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The new kform32 <strong>Form|Properties</strong> dialog box now displays the estimated download time for the form over a 64Kbps line.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When creating a <strong>new form</strong> in kform32, a dialog box is now displayed that allows you to set some form properties, allowing template style forms to be created. You can choose the form size, frame options (menu, toolbar, status bar), which buttons to include, as well as creating some standard frame/tab controls.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: In kform32, when dropping a data control on a grid, the selected cell will now have the new data properties applied, instead of the selected column. Note that if no cell is selected, then the column under the cursor will be used as before.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: DBEdit controls on editgroups will now have their tab order set automatically by kform32. Controls will be sorted left to right and down.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The screen size guide lines displayed by kform32 will now take the size of the menubar and toolbar into account.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: The Send to Back/Bring to Front kform32 options were the wrong way round, causing much confusion.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: If you hold down the <strong>SHIFT</strong> key when selecting controls in kform32, each click will cycle through any controls under the cursor, making easier to select overlapping controls.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When setting the tab stop position of controls in kform32, only controls with the TabStop property or accelerators will be included.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When right-clicking on a tab control in kform32, the list of tab pages is now displayed on the menu, allowing easy access to hidden pages.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Editgroups support edits arranged in multiple columns.</td>
</tr>
<tr>
<td>2003-02-04</td>
<td>9035</td>
<td>ENH: The kat utility is no longer supplied.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6284 Pasting single statement that begain with line number would crash workbench.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: The kform32 anchoring code has been fixed to allow anchored controls on tabs and frames to be psoitioned correctly when the controls parent is sized.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a new kform32 option, <strong>Tools|Control Events</strong>, that allows you to select which events will be automatically set when creating new controls. Note that these settings are also honoured when <strong>creating a new form</strong>.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When creating a new tab or frame control, you can simply click on the form background to have the control fill the available form client area. The control will be positioned 2 DLUs form the top-left corner of the form.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added <strong>search/replace</strong> (<strong>Ctrl+R</strong>) and a <strong>custom font</strong> option to the <strong>Edit|Form</strong> dialog box. Controls that have <strong>child objects</strong> (menu, tab, grids, etc.) now have their children displayed on separate lines.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Fixed a bug where clicking on a form when creating an <strong>editgroup</strong> control will no longer create a 0x0 sized control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The <strong>File|Properties</strong> dialog box now displays the estimated time to download the form at <strong>64Kbps</strong>.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When <strong>creating a new form</strong> a new dialog box is displayed allowing you to set various form properties. You can set the <strong>screen size</strong>, frame options such as the <strong>manu</strong>, <strong>toolbar</strong>, <strong>status bar</strong>, which buttons are created, and an assortment of options allowing various standard controls to be added to the form.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When <strong>dragging and dropping</strong> an entry from the table list onto a <strong>grid</strong>, the current cell will now have its properties changed (instead of the entire column). If no cell is selected, then the column under the cursor will be used as before.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The menu and toolbar is no longer displayed when editing a form. Instead, if the form has a menu/toolbar, a special icon will be displayed in the forms <strong>title bar</strong>. Simply click this icon to display the <strong>menu editor</strong>.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When displaying the <strong>screen size guidelines</strong> in kform32, the size of the <strong>menu</strong> and <strong>toolbar</strong> will now be taken into account. For example, if you size a form that has a menu/toolbar to 800x600 based on the screen guides, the form height will actually be slighlty smaller. When you then actually run the form via kclient, the size will be correct.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: The kform32 <strong>Send To Back</strong> and <strong>Bring To Front</strong> options were the wrong way round.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Fixed a kform32 bug that could break the auto-capitalisation code (resulting in <strong>Fileexit</strong> instead of <strong>FileExit</strong> for example).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: In kform32, when a dbedit is placed in the top left corner of an editgroup, it was very difficult to select - this has now been made easier.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: In kform32, if you hold down <strong>Shift</strong> when selecting a control, each click will cycle through all controls under the cursor. This is very useful when trying to select controls that are positioned beneath others.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: In kform32, when dragging a control that isn't a dbedit over an editgroup, there is no reason to invert the editgroup control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The kform32 <strong>Edit|Duplicate</strong> option now uses a 16 DLU vertical spacing.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Fixed a bug in kform32 where <strong>Edit|Cut</strong> would delete any colours, fonts or picture objects used by the control being cut, without then restoring these when the control is pasted back on the form. This could also have caused a crash with some forms.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When setting the tab order in kform32, controls that do not have the <strong>TabStop</strong> property enabled will no longer be included. The exception is controls that have <strong>accelerator keys</strong> (such as some labels) are always included.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The kform32 <strong>Tools|Check Tab Order</strong> option now makes controls with a bad tab order more obvious.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The <strong>context menu</strong> displayed when you <strong>right-click on a tab control</strong> in kform32 now lists each tab page, allowing easy access to the ears on large tabs. This is particularly useful for tab controls that have the <strong>Invisible</strong> Appearance property set.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF5551. In kform32, when moving a dbedit that has a label and is on an editgroup, the old label now longer stays visible.</td>
</tr>
<tr>
<td>2003-02-05</td>
<td>9036</td>
<td>REF5905: The install programs no longer set the install directory key if the <strong>Make Default ...</strong> checkbox has been cleared.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6286: Fixed a recently introduced problem where a run-time error could occur whilst trying to expand tables in the kform table list from a DEFOBJ table definition.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6285: Old type 7.0 KDB tables were no longer supported.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6289: Workbench, Repeated empty message boxes could appear after a long error messsage was displayed.</td>
</tr>
<tr>
<td>2003-02-06</td>
<td>9037</td>
<td>FIX: Fixed a bug in kform32 that could cause a GPF when cutting/copying a control that has DataField or DataSource properties set.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6291: When right-clicking on a tab control, kform now checks if the tab page has changed, and if so removes the current selection and selects the tab control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: <a href="mk:@MSITStore:kcmlrefman.chm::/DIM.htm">PRIVATE DIM</a> and <a href="mk:@MSITStore:kcmlrefman.chm::/DEFRECORD.htm">PRIVATE DEFRECORD</a> now supported.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: New form of the <a href="mk:@MSITStore:kcmlforms.chm::/tmp/PROP_FORM_CREATECONTROL2.htm">CreateControl()</a> method which allows tab order to be specified.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6292: Allow disabled grid cells to be selected in kform. The cell is still displayed in the disabled state.</td>
</tr>
<tr>
<td>2003-02-07</td>
<td>9038</td>
<td>REF6282: Fixed a problem reading large amounts of binary data from KClient.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6179: Cursor position issue in workbench after a delete caused lines to be merged.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: When loading a form in kform32, the Z-order of controls is tweaked to fix a dbedit painting problem on some forms.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Tree control created via the <strong>New Form</strong> dialog has been changed.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When creating a new dbedit control on an editgroup, the other controls in the column will no longer be automatically aligned vertically.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Remove the old <strong>Tools|Grouping</strong> option form kform32.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a new option to kform32 that allows the events for any form button groups to be set (<strong>Edit|Grouping|Set Group Events</strong>).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: You can <strong>quickly copy a control</strong> in kform32 by holding down the Control key whilst dragging an existing control. When the mouse button is released, the selected control will be copied and pasted to the new location.</td>
</tr>
<tr>
<td>2003-02-11</td>
<td>9042</td>
<td>ENH: Various fixes to the Connection Manager when checking attributes of a user's account on Unix systems.
<ul>
<li>Fixed the checking of password and account expiry dates for <em>/etc/shadow</em> accounts.</li>
<li>Check the account attributes in <em>/etc/security/user</em> on AIX.</li>
<li>If a user's home directory has no <strong>.kcmlLogin</strong> file, then error with <strong>Access Denied</strong> instead <strong>Incorrect Password</strong>, which could have been misleading.</li>
</ul></td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6297: The 'Reset Hourglass' feature is only enabled if network core files are enabled. This is to enforce logging of obscure hangs.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6298: SOAP requests failed due to client not being able to cope with zero length chunks.</td>
</tr>
<tr>
<td>2003-02-11</td>
<td>9042</td>
<td>REF6299: Fixed a spurious error P50, 14 that could arise in a statement such as LOCAL DIM x$ = 'Function$().</td>
</tr>
<tr>
<td>2003-02-13</td>
<td>9044</td>
<td>FIX: Fixed a subtle kform32 bug that could stop a single-click on a tree items button in the table list from working correctly.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Backslash characters are now encoded correctly by kform32, fixing a potential bug running on a Chinese MBCS system.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6301: Unicode problem when using kform32 with a 6.00 KCML - the table list would be corrupted.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: An error message will now be displayed by kform32 if KCML fails to pass table data across.</td>
</tr>
<tr>
<td>2003-02-14</td>
<td>9045</td>
<td>FIX: Fixed problems with stack overflow when TRY blocks were embedded in WHILE loops and BREAK or CONTINUE was used. Fixed problems with THROW across libraries. THROW ERR can now throw user error numbers between 1000 and 9999. An unhandled THROW will always be errored at the THROW and not in some outermost TRY/CATCH block. These changes will require rebuilding libraries and compiling any programs that include TRY/CATCH blocks. There is a new minimum library build number of 9045.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The use of line numbers as labels in statements is now forbidden in programs with $COMPLIANCE 3</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6306: Problem inserting line numbers in workbench, when you already have a very large amount.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6303: KCML6 could write to a KCML5 KDB log, which disabled logging.</td>
</tr>
<tr>
<td>2003-02-19</td>
<td>9050</td>
<td>ENH: KCML now has a number of built in DEFRECORDs describing $PSTAT, $MACHINE, $OPTIONS etc. There are also some built in $DECLARE definitions. These can be viewed with the function browser in the workbench.</td>
</tr>
<tr>
<td>2003-02-20</td>
<td>9051</td>
<td>ENH: When displaying the menu editor in kform32, the form menu is now selected by default.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The display of dbedit labels in kform32 has been improved.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Fixed a potential crash in kform32 when changing the style of a dbedit control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: KForm32 now longer adds the TabStop style to existing editgroups, which stops unnecessary CVS deltas.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a new option to kform32 (<strong>Size|Size to Fit</strong>) that allows a tab, frame or editgroup to be sized to fit the available parent client area. The control will be sized so it is 4 DLUs away from the nearest controls.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The kform32 <strong>Edit|Grouping|Set Group Events</strong> option has been enhanced to display the events for all controls in the group. For example, if you create a group containing dbedits and buttons, this option will now display button and dbedit events for the group.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When exiting kform32, menu items will now be checked for accelerators. If any menu items are missing accelerators, then the user will have the chance to display the menu editor.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The kform32 table list is now refreshed each time kform is started by KCML.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6315: DEFSECTIONS, caused crashes in KCML.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6313: Mouse click positions in workbench could be calculated wrong, if the display of line numbers was suppressed.</td>
</tr>
<tr>
<td>2003-02-21</td>
<td>9052</td>
<td>REF6321: Fixed a potential memory overwrite after breaking into a form that takes object references into non-local variables. May lead to crash or other unexpected behaviour.</td>
</tr>
<tr>
<td>2003-02-24</td>
<td>9055</td>
<td>REF6308: Dbedit labels are drawn using the form font not the edit's font.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6326: Support OBJECT a='SYM(*b)() notation for indirect calling of functions that return an object.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6327: Fix for ASSERT using Duplicate() to add child menu options to previous children.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Runtime lookup of fields in libraries is now the default. Byte 49 of <a href="mk:@MSITStore:kcmlrefman.chm::/$OPTIONS_RUN.htm#BYTE49">$OPTIONS RUN</a> is now defaulted to HEX(03).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Rename the 'ModuleConstructor() function generated in libraries by <a href="/kc6.htm">kc6</a> compiler to the new convention of 'LibraryConstructor(). Only generate this function if at least one component has a <a href="mk:@MSITStore:kcmlrefman.chm::/TutorialModules.htm#constructor">'Constructor() function</a>. The minimum library build number is now 9055 as this changes the library internals.</td>
</tr>
<tr>
<td>2003-02-28</td>
<td>9059</td>
<td>REF6332: Libraries were being loaded in the wrong order by LIBRARY ADD as a consequence of the introduction of internal structures in 9050.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Fix for memory leaks with OCX events. More agressive recovery of memory on LOAD and $SPACE.</td>
</tr>
<tr>
<td>2003-03-04</td>
<td>9063</td>
<td>REF6333: Allow BREAK and CONTINUE inside a TRY inside a REPEAT UNTIL.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Add a <a href="mk:@MSITStore:kcmlrefman.chm::/tmp/kintfld.htm#KCMLStringMD5">'KCMLStringMD5(doc$, digest$)</a> internal $DECLARE to compute an MD5 message digest from a document.</td>
</tr>
<tr>
<td>2003-03-06</td>
<td>9065</td>
<td>ENH: Added a new <strong>Group</strong> option the the kform32 menu editor, allowing menus to be assigned to persistent groups.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: The kform32 <strong>Edit|Grouping|Set Group Events</strong> option now hides depracated events.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The form <strong>Name</strong> property is no longer displayed by kform32.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The kform32 <strong>New Form</strong> dialog settings are now saved between sessions.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When adding new dbedit controls to editgroups in kform32, the <strong>tab order</strong> is now re-calculated.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Fixed a potential kform32 hang when creating a new frame control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When dragging and dropping controls from the kform32 table list, the <strong>Label$</strong> now has an automatic accelerator set.</td>
</tr>
<tr>
<td>2003-03-07</td>
<td>9066</td>
<td>REF6338: Was sometimes failing to update the word search index correctly on a KI_REWRITE because an internal buffer was incorrectly sized.</td>
</tr>
<tr>
<td>2003-03-10</td>
<td>9069</td>
<td>REF6331: Fixed small memory leak when using the CreateDataBind() method.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH6334: Added ListCount property to dbedit lists to be more like ListBox controls. Also Add() method for both now returns the index of the item added.</td>
</tr>
<tr>
<td>2003-03-12</td>
<td>9071</td>
<td>REF6344: Unicode KClient did not display its stock text correctly in a locale using a multibyte character set. For example Japanese.</td>
</tr>
<tr>
<td>2003-03-14</td>
<td>9073</td>
<td>REF6345: Title of a WINDOW OPEN style text window was truncated by a character.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6341: Shift F10 in a tree will perform a right click.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Save memory in KDB by various means including not loading the table schema until it's needed.</td>
</tr>
<tr>
<td>2003-03-17</td>
<td>9076</td>
<td>REF6346: Incorrect Indenting could prevent text from being inserted correctly.</td>
</tr>
<tr>
<td>2003-03-18</td>
<td>9077</td>
<td>REF6350: F2 buffers handling of non-existant line number's was broken.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6336: Fixed a problem where KClient could crash when passed very large strings (&gt;300Kb) in $DECLARE or COM situations.</td>
</tr>
<tr>
<td>2003-03-19</td>
<td>9078</td>
<td>REF6351: Using an expression such as LEN(.fred$) in a DIM statement could cause the field name to become lower case as only defining statements are saved in correct casing when saving ascii programs.</td>
</tr>
<tr>
<td>2003-03-20</td>
<td>9079</td>
<td>FIX: Fixed a kform32 crash when adding a new tab page.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added new kform32 <strong>Size to Fit</strong> option to the main context menu.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: The kform32 <strong>New Form</strong> dialog box was displaying the wrong form name.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>FIX: Forms created using the kform32 <strong>New Form</strong> dialog box now use the correct main menu prefix.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added pictures, fonts and colour objects to the kform32 <strong>Control Name Prefix</strong> option.</td>
</tr>
<tr>
<td>2003-03-24</td>
<td>9083</td>
<td>REF6356: ON x GOSUB 'a, 'b was broken.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6359: Fix for memory leak in FOR OBJECT i IN collection if OBJECT i was not NULL.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6357: Using SetFocus(FALSE) to change tab pages always generated an exit event for the first page regardless of which page was actually being hidden.</td>
</tr>
<tr>
<td>2003-03-25</td>
<td>9084</td>
<td>REF6361: Fixed a buffer overrun when returning a error message from Excel.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6360: #TERM would not be consistent when using the range syntax of BCDPART.</td>
</tr>
<tr>
<td>2003-03-26</td>
<td>9085</td>
<td>ENH: KForm32 now includes dbedit labels when checking for missing or duplicate accelerator keys.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: When developing in the workbench if a runtime error occurs in a TRY block which could be caught by an outer CATCH outside the subroutine, then the error will be actioned and execution will stop. If execution is resumed in the debugger, it will be resumed at the point of the CATCH. Errors invoked by THROW are treated as before and will not enter the debugger.</td>
</tr>
<tr>
<td>2003-03-27</td>
<td>9086</td>
<td>REF6363: The Connection Manager will now error if it could not &lt;get_include&gt; an environment file.</td>
</tr>
<tr>
<td>2003-03-28</td>
<td>9087</td>
<td>REF6364: A PRIVATE DIM followed by a COM statement could leave the COM variables as private.</td>
</tr>
<tr>
<td>2003-04-01</td>
<td>9091</td>
<td>REF6365: Fix for duplicate label problem in 4D.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6116: 'a(BYREF 'b) would error if the target DEFSUB 'a(BYREF 'b) argument had the same name</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: 'KCMLGetWindow() can now return the active form window.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6114: LOCAL DIM BYREF a=1 is now a syntax error. Previously the redundant BYREF was allowed but was harmless.</td>
</tr>
<tr>
<td>2003-04-02</td>
<td>9092</td>
<td>REF6352: Data binding now supported against PRIVATE records provided the form is executing in the same library.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6368: Fixed a problem where opening a form could crash when complicated load overlays are used.</td>
</tr>
<tr>
<td>2003-04-03</td>
<td>9093</td>
<td>REF6362: Table browsing in the forms editor had been broken for a couple of weeks.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6369: Some KI_READ_RAWs did not return all of the rows in a table.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6176: Using the workbench Spy feature of forms in libraries could produce garbled property names.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: SOAP server now generates WSDL endpoint from HTTP Host: line and URL.</td>
</tr>
<tr>
<td>2003-04-04</td>
<td>9094</td>
<td>REF6372: Passing OBJECT NULL to a method with a variable number of parameters could dump on AIX.</td>
</tr>
<tr>
<td>2003-04-07</td>
<td>9097</td>
<td>REF6373: Character box graphics were not appearing in text mode.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6377: DEFEVENT handlers in a program without a corresponding form definition should have been reported as an error.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6378: The position of an error that occurred resolving a program in a LOAD was not being reported correctly by the workbench.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6374: SELECT PASSWORD was broken, causing erratic behavour.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6375: Developers were unable to PANIC in immediate mode.</td>
</tr>
<tr>
<td>2003-04-08</td>
<td>9098</td>
<td>REF6380: In a form with an idle event, the simultaneous occurrence of the idle event with a user different event on the form could occasionally lead to an erroneous A00, 3 error when the form is terminated.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6352: Further fixes. Data binding against a locally scoped record in a library was not working.</td>
</tr>
<tr>
<td>2003-04-09</td>
<td>9099</td>
<td>REF6387: More intelligent step over in the debugger skipping more declarative statements and fixing a bug where REMs were not being skipped if a TRAP had been set on the line.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6381: Support CreateDataBind() with fixes done for 6352.</td>
</tr>
<tr>
<td>2003-04-10</td>
<td>9100</td>
<td>REF6389: Platter corrupted by resaving a program into a space that is too small.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6383: Fixed a potential hang caused by a particular pattern of data arriving from the client.</td>
</tr>
<tr>
<td>2003-04-11</td>
<td>9101</td>
<td>REF6371: Calling a DEFEVENT as if it were a method was leaking memory if LOCAL DIM was used in the event body.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Changed KI_WRITE_RAW so that any BLOB IDs are automatically blanked out.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Changed KI_WS_START so that words in the index excluded list are ignored if they are in the supplied list of words to search for.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6392: Rebinding a column using KI_BIND_COL to different variables without unbinding the previous variable first didn't work correctly.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6391: HALT and RESET did not work in the console window of the workbench.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6390: CNUM() returned wrong value for CNUM(FLD(SYM(*FLD(Buffer$.ArraySym))$(1).ifld$)) when substring was all '0' characters.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6384: NPL program names can be at most 8 characters long. Clip and throw a D82 if longer.</td>
</tr>
<tr>
<td>2003-04-14</td>
<td>9104</td>
<td>ENH: Dropped obsolete utilities from Unix IMAGE files.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6388: KI_REBUILD failed due to an optimization to do with the delayed loading of table schemas.</td>
</tr>
<tr>
<td>2003-04-15</td>
<td>9105</td>
<td>REF6355: If a grid EditRowNotify event handler displayed a child form, then focus was not always returning to the grid when the child form terminated.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Linestats indicates whether the current form was downloaded or came from cache.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6393: Support client licences must not override NOPROG environment variable.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6394: berror if we try to evaluate variables that don't exist.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6396: Grid LastChar$ property could be incorrect with a Unicode KClient.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Add a .INFO_HAND.handle field to KI_INFO record to allow a program to extract the integer handle number used by KCMLs prior to 6.20.</td>
</tr>
<tr>
<td>2003-04-16</td>
<td>9106</td>
<td>REF6398: Fixed a memory overwrite in KI_COMP.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6397: Local DEFRECORDs appearing in workbench function browser caused crash when trying to expand.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added option to restore KClient preferences to their default values.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6100: Could lose a click event after editing a gridcell and then clicking a button triggering a slow EndEdit event.</td>
</tr>
<tr>
<td>2003-04-17</td>
<td>9107</td>
<td>REF6398: Fixed a bad indent in workbench latter causing a crash.</td>
</tr>
<tr>
<td>2003-04-22</td>
<td>9112</td>
<td>REF6401: Don't add SOFT_RETURN for semicolon comment, if SOFT_RETURN character is NULL.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6404: It was not possible to tab through elements in a Microsoft HTML OCX control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6402: Grid EditReason property is correctly set to 6 when ending a grid cell edit by clicking another control.</td>
</tr>
<tr>
<td>2003-04-24</td>
<td>9114</td>
<td>REF6412 Improved Ctr-G in workbench for non $compliant code.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Allow a record to be embedded in another record using it's SYM value such that its contents can then be accessed using a notation like FLD(a$.b.c). Subscripting for array elements is allowed as in FLD(a$.b&lt;n&gt;.c) where FLD(a$.b) was set to SYM(x$()). As a consequence of this change compiled programs containing FLD subscript expressions like FLD(a$.b&lt;n&gt;) will not be backward compatible with previous versions of KCML which will fail to LOAD them.</td>
</tr>
<tr>
<td>2003-04-28</td>
<td>9118</td>
<td>REF6416 Workbench, Don't try to browse DEFRECORDs in empty programs.</td>
</tr>
<tr>
<td>2003-04-29</td>
<td>9119</td>
<td>REF6413 Workbench, Syntax errors involving DEFSUBs that returned strings could truncate exisitng code.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6421: Fixed a potential crash when a subroutine is called with the wrong arguments and some of the arguments contain string expressions (such as concatenation). Now a run-time error correctly occurs.</td>
</tr>
<tr>
<td>2003-04-30</td>
<td>9120</td>
<td>REF6424 Having non-default text-mode colours in a Unicode KClient could lead to invalid settings being written to the registry.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6425 CVS Operators caused cursor offset problems within the workbench.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Type 7 word search now splits multi ocurrence string columns into individual strings rather than treating as one large string.</td>
</tr>
<tr>
<td>2003-05-1</td>
<td>9121</td>
<td>ENH: Trap window context menu option to goto Trap Statement.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Change to implementation of FLD(a$.b.c) introduced in build 9114 so that is is now backward compatible with previous versions of KCML.</td>
</tr>
<tr>
<td>2003-05-02</td>
<td>9122</td>
<td>REF6432: Rebuilding a word search index could dump under certain circumstances because of a memory overwrite.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6414: REF6419: Minor grid paint issues.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6410: Add Copy as Hex to copy data out of large var display in the Form Hex(202020).</td>
</tr>
<tr>
<td>2003-05-08</td>
<td>9128</td>
<td>REF6437: Tooltipping of truncated label text did not work if the label was on a tab page.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6438: Multiple KCML/KForm32 sessions could lead to corruptions when editing or saving back a form.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6439: On a dbedit with a drop-down and DropDownFilled not set, a drop down event could previously only be triggered if there was at least one element in the list (this is normally the case, so that the description of the current text is displayed). Now the drop down event will also be called if the list is empty.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6436: Tabbing through a multiline data aware edit that had AlwaysValidate set could insert blank lines.</td>
</tr>
<tr>
<td>2003-05-09</td>
<td>9129</td>
<td>REF6442: Any attempt to open a form in an Exit event handler or after the .Terminate() method has been used will now error. Previously not all circumstances were caught.</td>
</tr>
<tr>
<td>2003-05-12</td>
<td>9132</td>
<td>REF6444: Byte 29 of $PSTAT (DEVice awaited) will now be set to HEX(FD) while KCML is waiting on a $IF statement.</td>
</tr>
<tr>
<td>2003-05-14</td>
<td>9134</td>
<td>REF6448: Assigning multiline text to a form text property with a string concatenation would expand 0x0D line breaks into 0D0A pairs. eg.
<p>a$ = $PRINTF("Hello\n")<br />
b$ = "World"<br />
c$ = a$ &amp; b$<br />
.Control.Text$ = a$ &amp; b$<br />
</p>
.Control.Text$ did not equal c$ as it had an extra 0x0A inserted.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6450: Trap window would crash if a variable trap was added.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Use memory mapping to allocate heap memory on Linux.</td>
</tr>
<tr>
<td>2003-05-15</td>
<td>9135</td>
<td>ENH: KClient supports URLs in the form of "kclient://host%20-o%20option"</td>
</tr>
<tr>
<td>2003-05-16</td>
<td>9136</td>
<td>REF6441: Revert to generating old pcode for a$ = $UPPER(b$) so that code compiled in KCML 6.20 can be taken back to KCML 6.00 systems. As a consequence a$ = $UPPER(b$) &amp; c$ which was permitted previously in KCML 6.20 is now a syntax error as it was in KCML 6.00. However this cab be worked around with a$ = "" &amp; $UPPER(b$) &amp; c$</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6440: A problem with a RECORD FLD type being corrupted by the new FLD(a$.b.c) usage has been fixed.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: To be compatible with the KCML7 convention, '_Init and '_Enum functions for record fields will return field names without any trailing $ or trailing parenthesis. This effectively means that the base name for a field should be unique i.e. don't have a FLD a and a FLD a$ in the same record.</td>
</tr>
<tr>
<td>2003-05-19</td>
<td>9139</td>
<td>REF6454: Workbench Form browser could cause crash. This would happen as source file is loaded.</td>
</tr>
<tr>
<td>2003-05-20</td>
<td>9140</td>
<td>ENH: Can now generate MetaPhone phoneme keys by using $PACK(E="META") phoneme$ FROM source$</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Improved resizing when putting stock icons on a large toolbar. Icons now look smoother.</td>
</tr>
<tr>
<td>2003-05-21</td>
<td>9141</td>
<td>REF6457: Kerridge uninstaller broken.</td>
</tr>
<tr>
<td>2003-05-22</td>
<td>9142</td>
<td>ENH: Comments on the same line are now allowed with the // form of <a href="/REM.htm">REM</a>.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6460:Default dbedit has no length restriction on Win NT. OS imposed 30,000 char limit remains on Win 9X.</td>
</tr>
<tr>
<td>2003-05-28</td>
<td>9148</td>
<td>REF6461: Kservadm could display a corrupted status for an uninstalled service on Win 95/98.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6462: Fix for potential KClient crash involving drop down lists in dbedits.</td>
</tr>
<tr>
<td>2003-06-03</td>
<td>9154</td>
<td>REF6471: On a form where the first control is a dbedit with EditAlwaysValidate set, then could get a spurious validate event after a message box is popped up.</td>
</tr>
<tr>
<td>2003-06-04</td>
<td>9155</td>
<td>REF6470: Pressing Return when focus was on a boolean edit would not action the default button on the form.</td>
</tr>
<tr>
<td>2003-06-05</td>
<td>9156</td>
<td>REF6472: Clear in workbench console would cause crash.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6474: The server IP address in $MACHINE is now the address as used by the client when it initially connected rather than the server's own IP address as they may be a NAT router between them translating the addresses.</td>
</tr>
<tr>
<td>2003-06-06</td>
<td>9157</td>
<td>ENH: Allow environment variables in tablespace locations.</td>
</tr>
<tr>
<td>2003-06-09</td>
<td>9160</td>
<td>REF6478: Mismatched FOR/NEXT could undeflow the stack and cause an ASSERT. Also add specific syntax error for A$=FLD(B$..C$) which also caused an ASSERT.</td>
</tr>
<tr>
<td>2003-06-10</td>
<td>9161</td>
<td>REF6479: Dbedit labels are drawn using the form's text colours rather than those of the edit.</td>
</tr>
<tr>
<td>2003-06-11</td>
<td>9162</td>
<td>REF6476: Workbench font options were being stored in a format that was incompatible with previous workbench versions. Have resumed using the old format.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Allow environment variables in the &lt;catalogue&gt;, &lt;permsfile&gt;, &lt;include&gt;, &lt;try_include&gt; and &lt;get_include&gt; tags of <em>kconf.xml</em>. The &lt;location&gt; tag of a database tablespace can also use environment variables.</td>
</tr>
<tr>
<td>2003-06-12</td>
<td>9163</td>
<td>REF6482: A word serach failure during a KI_WRITE could corrupt the whole table.</td>
</tr>
<tr>
<td>2003-06-13</td>
<td>9164</td>
<td>REF6482: Previous fix was incomplete.</td>
</tr>
<tr>
<td>2003-06-16</td>
<td>9167</td>
<td>REF6483: A crash on an illegal use of a sym of an object as if it were a sym of a string now correctly run-time errors.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6484: Workbench font options were being stored in a format that was incompatible between UNICODE and ANSI versions of the client.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6485: Workbench function browser could cause crash while browsing records in an unresolved program.</td>
</tr>
<tr>
<td>2003-06-23</td>
<td>9174</td>
<td>REF6490: Change KI_READ_HOLD_NEXT to ignore deleted rows in the same way that KI_READ_NEXT does.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6491: Fixed a potential crash in the graph control.</td>
</tr>
<tr>
<td>2003-06-24</td>
<td>9175</td>
<td>SOAP redim of sclar strings containing HEX(00) characters failed</td>
</tr>
<tr>
<td>2003-06-25</td>
<td>9176</td>
<td>REF6497: Workbench Large Variable Display copy could cause crash.</td>
</tr>
<tr>
<td>2003-06-27</td>
<td>9178</td>
<td>ENH: Add Name$ property to tab pages to return the name of the tab page.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added a variant of the grid DataAwareRow() method, that allows both the grid row and the record buffer to be specified.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6495: Modifiying the text of a menu item created using the CreateMenuItem() method was not updating the displayed menu.</td>
</tr>
<tr>
<td>2003-06-30</td>
<td>9181</td>
<td>REF6500: Workbench function browser could crash depending on library contents.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6498: Workbench vertical scroll bar could be incorrectly set to inactive while debugging library code.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added basic proxy tunneling support to KClient.</td>
</tr>
<tr>
<td>2003-07-02</td>
<td>9183</td>
<td>REF6505: Result from KCMLGetServerIPport in the wrong byte order.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6504: Scrolling a grid with the mouse wheel while editing a cell could break the grid's validate event.</td>
</tr>
<tr>
<td>2003-07-03</td>
<td>9184</td>
<td>REF6507: MAT SEARCH into a zero element numeric locator array could dump on AIX.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6503: XML panic files might be malformed if an exception is thrown during the LIST DT or LIST RETURN sections.</td>
</tr>
<tr>
<td>2003-07-04</td>
<td>9185</td>
<td>REF6510: Fixed workbench crash if stepping into/over a LOAD statement when the file name was invalid.</td>
</tr>
<tr>
<td>2003-07-08</td>
<td>9189</td>
<td>REF6514: Initialize TS6 fields to ALL(00) not spaces.</td>
</tr>
<tr>
<td>2003-07-09</td>
<td>9190</td>
<td>REF6515: Fixed minor KClient resource leaks</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6516: Word search indices could be corrupted on volatile tables due to an error in the insertion algorithm.</td>
</tr>
<tr>
<td>2003-07-10</td>
<td>9191</td>
<td>REF6517: Dbedit labels could be drawn using an incorrect font.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6513: Pressing Ctrl-L in the Workbench console window would hang.</td>
</tr>
<tr>
<td>2003-07-15</td>
<td>9196</td>
<td>REF6518: Scrolling a grid with the mouse wheel would leave CursorRow and CursorCol incorrect within an EditRowNotify event.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Insert a HEX(09) tab character before // comments in programs saved as ASCII. Controlled by byte 7 of <a href="/$OPTIONS_LIST.htm#BYTE7">$OPTIONS LIST</a>. Byte 6 of $OPTIONS LIST controls the column at which these comments are displayed in the workbench. The default is 40.</td>
</tr>
<tr>
<td>2003-07-16</td>
<td>9197</td>
<td>REF6523: A grid with the TabThrough style set consumed Ctrl-Tab keystrokes even though it took no action, preventing any tab control using Ctrl-Tab as a hotkey.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6524: The Connection Manager could sometimes set <strong>$GLOBAL_ID</strong> to an incorrect value.</td>
</tr>
<tr>
<td>2003-07-17</td>
<td>9198</td>
<td>ENH: Allow transparent use of an SSL tunnel by the SOAP client when the new TUNNEL option is used in <a href="/CREATE.htm#soap">CREATE</a> to remap WSDL and endpoint URLs.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6520: Panic files were not expanding the variable sections in a browser if there was the name of a DEFSUB in common due to SYM() being used on it.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6522: Allow BREAK to break out of a FOR/NEXT which encloses a TRY block from within which the BREAK is issued.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6492: $PACK(E="ENUM(8,5)")a$ FROM a was not calculating the required size correctly and spuriously erroring.</td>
</tr>
<tr>
<td>2003-07-23</td>
<td>9204</td>
<td>REF6527: Conditional Traps didn't work when placed on DEFSUB/DEFEVENT/DEFFN.</td>
</tr>
<tr>
<td>2003-07-24</td>
<td>9205</td>
<td>REF6529: Reserve the 0x10 bit in $MACHINE byte 60 for application use.</td>
</tr>
<tr>
<td>2003-07-25</td>
<td>9206</td>
<td>REF6530: The .Parent and .Page properties for a form control were not being given magic sym values and so would not compare equal to the Sym property of the tab or tab page control.</td>
</tr>
<tr>
<td>2003-07-28</td>
<td>9209</td>
<td>REF6534: The selfid utility could partially read replies back from a KClient running on NT4.</td>
</tr>
<tr>
<td>2003-07-29</td>
<td>9210</td>
<td>REF6535: DIM a(b(1)) and DIM a(c(1,1)) would dump if b() or c() were not in common.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6536: The FORM END operator could hide any text appearing after it in workbench. This could lead to confusing results from searches. We now display this text in the workbench.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6538: Make sure menu, toolbar and Euro button are disabled when their parent form is busy.</td>
</tr>
<tr>
<td>2003-07-31</td>
<td>9212</td>
<td>REF6525: fixed a potential dbedit crash.</td>
</tr>
<tr>
<td>2003-08-01</td>
<td>9213</td>
<td>ENH: Added service name to workbench title bar.</td>
</tr>
<tr>
<td>2003-08-05</td>
<td>9217</td>
<td>REF6542: Workbench could crash if blanks lines with line numbers were pasted in.</td>
</tr>
<tr>
<td>2003-08-07</td>
<td>9219</td>
<td>ENH: The Connection Manager and kiodbc will now use PAM authentication on HP-UX 11, Linux and Solaris.</td>
</tr>
<tr>
<td>2003-08-08</td>
<td>9220</td>
<td>REF6546: Function keys did not work as accelerators to regular controls, only menus.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6547: Implemented Sym property for menu items created with the CreateMenuItem() method.</td>
</tr>
<tr>
<td>2003-08-13</td>
<td>9225</td>
<td>KI_READ_RAW of more than one row across extent boundaries was not working</td>
</tr>
<tr>
<td>2003-08-18</td>
<td>9230</td>
<td>REF6553: Possible under certain circumstances for a toolbar button to display the wrong image or text.</td>
</tr>
<tr>
<td>2003-08-20</td>
<td>9232</td>
<td>REF6558: KDB locking of type 7 tables outside of a database caused an error.</td>
</tr>
<tr>
<td>2003-08-26</td>
<td>9238</td>
<td>REF6559: Fixed possible flickering when using editgroups placed inside tab controls.</td>
</tr>
<tr>
<td>2003-08-29</td>
<td>9241</td>
<td>REF6488: LIST DT display for type6 word search tables could be corrupt after $SPACE.</td>
</tr>
<tr>
<td>2003-09-02</td>
<td>9245</td>
<td>REF6582: Function keys could accelerate unwanted controls.</td>
</tr>
<tr>
<td>2003-09-05</td>
<td>9248</td>
<td>ENH: Support CLOB as a synonym for BLOB as a KDB datatype. Both currently act as character BLOBs but BLOB will treat trailing blanks as significant in 6.30+.</td>
</tr>
<tr>
<td>2003-09-10</td>
<td>9253</td>
<td>REF6593: The Connection Manager will now only show links to create and remove a <em>.kcmlLogin</em> file if we have access to the user's home directory.</td>
</tr>
<tr>
<td>2003-09-11</td>
<td>9254</td>
<td>REF6596: KI_WS_START now includes words shorter than the minimum word length defined for the index to be searched for. This allows single/double digit numbers to be searched for.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6597: Fixed a crash when ALL() was passed a negative length.</td>
</tr>
<tr>
<td>2003-09-12</td>
<td>9255</td>
<td>REF6575: Client DDE broken in Unicode builds.</td>
</tr>
<tr>
<td>2003-09-15</td>
<td>9258</td>
<td>REF6601: Fixed a problem when setting gridcell text colour to certain stock colours.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6595: Do not generate a tree click event from a keypress if there is no currently selected item.</td>
</tr>
<tr>
<td>2003-09-19</td>
<td>9262</td>
<td>REF6604: The rules for interpreting the #ifdef conditional operator did not agree with the documentation.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6605: Fixed a problem with KISAM logging on AIX involving large files and 32/64bit processors</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6606: Fixed bogus warnings about exceptions in LIST DT output in XML panic files from NT servers.</td>
</tr>
<tr>
<td>2003-09-22</td>
<td>9265</td>
<td>REF6608: Allow names of signal actions in bkstat's -K flag argument.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6607: Handle disabled accounts under Windows NT.</td>
</tr>
<tr>
<td>2003-09-25</td>
<td>9268</td>
<td>REF6610: Make BLOB and CLOB both synonyms so that we can read tables from KCML 6.30+. All BLOBs will be considered to be CLOB character blobs. If a 6.30 table is opened then any binary blobs in the schema will be considered to be character blobs. Any tables created will use the 6.30 CLOB character blob datatype whether they were created as BLOB or CBLOB. The new type information added to 6.30+ schemas will be silently ignored.</td>
</tr>
<tr>
<td>2003-09-29</td>
<td>9272</td>
<td>REF6613: KI_WS_CREATE could crash when attempting to extact a large number of fields.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6614: kc6 was not able to load compiled programs saved with UTF-8 encoding.</td>
</tr>
<tr>
<td>2003-09-30</td>
<td>9273</td>
<td>REF6612: Include logical partition (LPAR) number, if available, in the machine ID for AIX.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6615: Fixed a potential crash when moving from a form to a text window.</td>
</tr>
<tr>
<td>2003-10-01</td>
<td>9274</td>
<td>REF6617: Fixed KI_WS_START to ignore a wordlist that is a single space character.</td>
</tr>
<tr>
<td>2003-10-03</td>
<td>9276</td>
<td>ENH: Change to KDB logging which could give performance improvement in some situations</td>
</tr>
<tr>
<td>2003-10-06</td>
<td>9279</td>
<td>REF6621: Can get a crash if libraries with private functions of the same name are loaded, called and removed in succession.</td>
</tr>
<tr>
<td>2003-10-07</td>
<td>9280</td>
<td>REF6623: Workbench forms browser could crash client.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6622: Using the workbench replace dialog. To replace REMs with // in collapsed DEFEVENT statements left the code in an unexpected state.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6620: Was adding '\n' to blank lines in #if #endif blocks.</td>
</tr>
<tr>
<td>2003-10-08</td>
<td>9281</td>
<td>Added -x flag to kmake to specify an alternative directory to build to than that specified by the KBIN environment variable in kconf.xml. The obsolete alternatives to KBIN (MODULES and LIBRARIES) are no longer supported. The -q option is no longer supported.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6625: KI_WRITE_PTR with bound BLOB would ASSERT on debug builds</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6626: Pasting into workbench could gobble spaces that followed continuation characters.</td>
</tr>
<tr>
<td>2003-10-09</td>
<td>9282</td>
<td>REF6624: MOVE dir TO dir.old failed</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6627: The declaration PRIVATE DIM .Fred would not make .Fred private, although PRIVATE DIM .Fred=(1, "I4") would. Other variable types are not affected.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6628: Modifying a private dimmed fld variable could cause a crash.</td>
</tr>
<tr>
<td>2003-10-14</td>
<td>9287</td>
<td>REF6633: Workbench Local variable window could cause a crash when stoppping in for loop.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6634: The Connection Manager could hang when processing a CGIScript alias which referenced a KCML source program.</td>
</tr>
<tr>
<td>2003-10-15</td>
<td>9288</td>
<td>REF6616: Fixed a potential hang in direct connections.</td>
</tr>
<tr>
<td>2003-10-16</td>
<td>9289</td>
<td>REF6636: a = $RELEASE LOAD RUN could cause a crash (Unix only)</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6642: Bkstat now errors if the -x and -y values are different, as this could cause KCML to dump (Unix only)</td>
</tr>
<tr>
<td>2003-10-17</td>
<td>9290</td>
<td>REF6643: SELECT with index read join combined with IN ( ... ) clause could produce an empty result set</td>
</tr>
<tr>
<td>2003-10-20</td>
<td>9293</td>
<td>REF6645: Protect against a COM method that returns a string returning NULL.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The Remote Licence daemon now supports the generic licence protocol.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The Connection Manager will now display a generic licence table.</td>
</tr>
<tr>
<td>2003-10-21</td>
<td>9294</td>
<td>ENH: COPY and MOVE now preserve the permissions of files. (Unix only)</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6646: Fixed the Connection Manager's CGIDirectory alias type.</td>
</tr>
<tr>
<td>2003-10-22</td>
<td>9295</td>
<td>ENH: KClient will now pass the hostname to the Connection Manager which then sets the <strong>SERVER_NAME</strong> CGI environment variable.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6649: <em>kwebserv -i</em> will now error to the system log if a <strong>get_include</strong> file could not be loaded.</td>
</tr>
<tr>
<td>2003-10-24</td>
<td>9297</td>
<td>REF6655: Now possible to use Ctrl+Alt or Alt Gr to compose characters useable by the grid Char() event.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6656: Fixed a problem that could sometimes (but not always) cause a crash when calling a record function (such as '_Init_recname) for a LOCAL DEFRECORD in a library.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6647: Fixed a problem where setting enumerated property in the create event had no apparent effect (such as (oControl1.DropListStyle = &amp;.Simple).</td>
</tr>
<tr>
<td>2003-10-27</td>
<td>9300</td>
<td>REF6660: SOAP client failed to spot some illegal UTF-8</td>
</tr>
<tr>
<td>2003-10-28</td>
<td>9301</td>
<td>REF6654: Fixed a problem with the EditForm method that could cause stray characters to appear on the end of the edited string (Unicode client only).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6661: Fixed a problem with a spurious error when duplicating an OCX control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6659: On the first expansion of a node on a tree control, both the Expand and ExpandChange events were being generated, contrary to the documentation which states that only the Expand event will happen.</td>
</tr>
<tr>
<td>2003-10-29</td>
<td>9302</td>
<td>REF6664: Creating an empty menu object with CreateControl and never adding items to it will raise a runtime error.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6665: KClient would detach from the Connection Manager if the service name contained POST or GET.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6666: Adding traps in the workbench when no code had been edited could cause problems. You would ASSERT when drag-drop DEFRECORDs from the FN browser on to form definitions.</td>
</tr>
<tr>
<td>2003-11-04</td>
<td>9308</td>
<td>REF6667: It was possible that two Help$ tooltips could appear on a tree control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6669: kwho and bkstat -F could produce badly formatted output.</td>
</tr>
<tr>
<td>2003-11-05</td>
<td>9309</td>
<td>REF6672: Producing an error in workbench console, would then stop you being able to continue execution.</td>
</tr>
<tr>
<td>2003-11-06</td>
<td>9310</td>
<td>ENH: Enhancements to the Connection Manager's built-in web server.
<ul>
<li>Aliases can now reference environment variables.</li>
<li>Allow per-service aliases, referenced using a URL of the form <strong>http://host:790/serviceName/aliasName</strong></li>
<li>Aliases can now optionally require authentication.</li>
</ul></td>
</tr>
<tr>
<td>2003-11-07</td>
<td>9311</td>
<td>REF6675: Fixed a potential hang if a form contained a groupbox the same size or larger than itself.</td>
</tr>
<tr>
<td>2003-11-10</td>
<td>9314</td>
<td>ODBC table scan across extent boundaries was not working</td>
</tr>
<tr>
<td>2003-11-11</td>
<td>9315</td>
<td>ENH: The $KCML_PSTAT_SIZE environment variable can be used to initialise the size of $PSTAT</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6679: The Connection Manager was not evaluating ${VAR-otherval} expressions in an included XML file.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The Connection Manager will now error if an &lt;include&gt; directive tries to load a XML file that doesn't exist.</td>
</tr>
<tr>
<td>2003-11-12</td>
<td>9316</td>
<td>REF6681: Kservice will now pass back an error message back to KClient if a 3rd party WinSock layer has broken socket inheritance.</td>
</tr>
<tr>
<td>2003-11-13</td>
<td>9317</td>
<td>REF6680: Allow BYREF a$b as an argument to a DEFSUB so that the length of the string passed can be checked. Useful for records.</td>
</tr>
<tr>
<td>2003-11-14</td>
<td>9318</td>
<td>REF6687: Expansion of PATH=$dir1;$dir2 was broken in the Connection Manager.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6688: The environment of a per-service &lt;validuser&gt; can now overrride the environment of the &lt;service&gt;</td>
</tr>
<tr>
<td>2003-11-17</td>
<td>9321</td>
<td>REF6684: The environment variable $KCML_TERM_LIC can be used to limit the number of licences a terminal can use.</td>
</tr>
<tr>
<td>2003-11-19</td>
<td>9323</td>
<td>REF6676: The expression FLD(a$.b) &amp;=  ... was not yielding the same result as the longer equivalent FLD(a$.b) = FLD(a$.b) &amp; ... It now does, but programmers must remember that FLD(a$.b) will have the full width of the fld including trailing blanks and so all concatenations will overflow and have no visible effect. It is recommended that FLD(a$.b) = RTRIM(FLD(a$.b)) &amp; ... be used instead (this construct is not affected by this bug).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6696: The Connection Manager process info pages could crash on some AIX machines.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6697: Bkstat would attempt to log a user out of a shell if the -x and -y values were different.</td>
</tr>
<tr>
<td>2003-11-20</td>
<td>9324</td>
<td>ENH: The syntax FLD(($OPTIONS #x).options_hash_readmode) is now supported and is recomnended over using the STR in the expression FLD(STR($OPTIONS #x).options_hash_readmode).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The syntax DEFSUB 'MyFunction(BYREF a$()_my_rec) is now supported.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6700: Fixed problem with grid not retaining focus if its containing form loses and regains active window status.</td>
</tr>
<tr>
<td>2003-11-21</td>
<td>9325</td>
<td>ENH: Programs that have been compiled with KCML 6.20 are no longer backwards compatible with KCML 6.00.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6704: DIM a(b(1)) where the b() was not previous DIMmed would dump during resolve.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Size calculations for truncated text tooltips in grid cells will accomodate multiline text.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6427: Workbench could ASSERT after CTRL-Y to delete a statement. It depended on statement and layout of program.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6701: Clear in Workbench F2 Bar could lead to numerous ASSERTs and then a hang.</td>
</tr>
<tr>
<td>2003-11-24</td>
<td>9328</td>
<td>REF6706: SOAP client/server failed to spot some invalid UTF-8.</td>
</tr>
<tr>
<td>2003-11-25</td>
<td>9329</td>
<td>REF6708: Opening some tables with .sq schemas via ODBC could lead to a corrupted list of column names. Only seen on AIX.</td>
</tr>
<tr>
<td>2003-11-26</td>
<td>9330</td>
<td>REF6714: The Connection Manager would not display a PANIC file after signalling a partition.</td>
</tr>
<tr>
<td>2003-11-27</td>
<td>9331</td>
<td>ENH: The Connection Manager will now show the list of child processes of a process.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6501: A field variable defined in a DIM or a FLD should define the case, but references to a field in other circumstances was also erroneously defining the case.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6557: Workbench would ASSERT then possibly crash when doing Ctrl-G on last line of program.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6445: In workbench. Current PC line could move if you expanded or collapsed DEFEVENTs.</td>
</tr>
<tr>
<td>2003-11-28</td>
<td>9332</td>
<td>REF6725: Fixed a timing problem in the NT Server installer.</td>
</tr>
<tr>
<td>2003-12-01</td>
<td>9335</td>
<td>REF6728: Setting focus in the Validate event of a ValidateSelChange dropdown dbedit had no effect.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6682: When hiding/showing grouped edit controls which are also in an editgroup make sure any labels are placed correctly.</td>
</tr>
<tr>
<td>2003-12-02</td>
<td>9336</td>
<td>REF6732: An illegal FLD defintion containing an occurs of 0 (eg FLD a(0)) was not being errored and could later cause a crash in KCML.</td>
</tr>
<tr>
<td>2003-12-03</td>
<td>9337</td>
<td>REF6737: Possible in rare circumstances for keyboard acceleration to fail.</td>
</tr>
<tr>
<td>2003-12-04</td>
<td>9338</td>
<td>ENH: Support the syntax FLD symofrec = SYM(_record_name). To state in code that a fld should contain the SYM of a string of the specified record type. No checking is done in KCML6.20 but this is likely to be added to future versions of KCML.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6733: Raise a runtime error for a malformed form definition containing multiple forms.</td>
</tr>
<tr>
<td>2003-12-08</td>
<td>9342</td>
<td>REF6735: Problem showing a message box with a Japanese IME window active.</td>
</tr>
<tr>
<td>2003-12-09</td>
<td>9343</td>
<td>REF6740: Console commands that printed form string properties could cause ASSERTs.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added <em>-l &lt;log_level&gt;</em> flag to superkill.</td>
</tr>
<tr>
<td>2003-12-11</td>
<td>9345</td>
<td>REF6743: Do not allow a disabled busy-mode form to be resized.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6742: Fixed repaint issues when changing label text of an edit in an edit group.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6744: Minimise memory usage for MODULE ADD.</td>
</tr>
<tr>
<td>2003-12-12</td>
<td>9346</td>
<td>REF6745: Comments between &lt;service&gt; definitions in kconf.xml could confuse the Connection Manager's adminitration pages.</td>
</tr>
<tr>
<td>2003-12-15</td>
<td>9349</td>
<td>REF6746: The Connection Manager could crash if the last child of a kconf.xml node was a comment.</td>
</tr>
<tr>
<td>2003-12-17</td>
<td>9351</td>
<td>ENH: Support BYREF OBJECT for DEFSUB parameters.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6748: Fix for core dump on Linux in a client SOAP method call passing a single REDIM scalar string argument where that string had no space allocated (zero LOCAL DIM).</td>
</tr>
<tr>
<td>2003-12-22</td>
<td>9356</td>
<td>REF6750: Fix problem with evaluating attribute methods in a SAX2 callback method handler on Linux.</td>
</tr>
<tr>
<td>2004-01-07</td>
<td>10007</td>
<td>REF6752: Superkill would not signal a process on some versions of Unix.</td>
</tr>
<tr>
<td>2004-01-08</td>
<td>10008</td>
<td>REF6754: Fix bad build number check for $CONVERT.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6751: Fixed IME display problem when entering Korean text into a dbedit.</td>
</tr>
<tr>
<td>2004-01-13</td>
<td>10013</td>
<td>REF6758 / ENH: Relaxed restriction that table name suffix can only be two characters long.</td>
</tr>
<tr>
<td>2004-01-15</td>
<td>10015</td>
<td>REF6761: Install script now sets superuser permissions bit on bkstat.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added <em>-e kconf.new</em> flag to examine the Connection Manager's configuration file for errors.</td>
</tr>
<tr>
<td>2004-01-16</td>
<td>10016</td>
<td>REF6764: Wordsearch sequence set could get corrupted when doing large numbers of deletions.</td>
</tr>
<tr>
<td>2004-01-19</td>
<td>10019</td>
<td>REF6765: Fixed version number test when invoking KForm</td>
</tr>
<tr>
<td>2004-01-21</td>
<td>10021</td>
<td>REF6305: Word-search code now ignores blanks in non-alpha characters.</td>
</tr>
<tr>
<td>2004-02-03</td>
<td>10034</td>
<td>REF6784: Fixed hang when removing all opportunities for controls on a form to have focus.</td>
</tr>
<tr>
<td>2004-02-11</td>
<td>10042</td>
<td>REF6791: Clearing the installer's <strong>Add to Start Menu</strong> checkbox had no effect.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6747: Trim trailing zeroes from graph value labels.</td>
</tr>
<tr>
<td>2004-02-13</td>
<td>10044</td>
<td>ENH: The MAC address of a client is now visible from $PSTAT().</td>
</tr>
<tr>
<td>2004-02-19</td>
<td>10050</td>
<td>REF6798: ALL(string$,0) now no longer errors.<br />
PRINT ALL(string$, 0) could product corrupt output.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6801: The EditRowNotify() event was not being generated at the end of complicated sequence of events.</td>
</tr>
<tr>
<td>2004-02-20</td>
<td>10051</td>
<td>REF6802: Fixed Rich edit cursor placement issue.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6803: SHELL cmd$ would leak a handle on NT.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6800: The workbench could corrupt form definitions. This would only happen if you dragged a FLD onto a form in KFORM and that FLD had a TAB in its // comment.</td>
</tr>
<tr>
<td>2004-02-23</td>
<td>10054</td>
<td>REF6793: Fixed printing to clipboard in Unicode clients.</td>
</tr>
<tr>
<td>2004-02-24</td>
<td>10055</td>
<td>REF6810: If the programmer does a MoveCursor() to a cell that is autoedit but has the cursor disabled then the cell will not go into edit mode and so an EditRowNotify() event should not be generated.</td>
</tr>
<tr>
<td>2004-02-27</td>
<td>10058</td>
<td>REF6777: READ # could crash when reading on a closed stream.</td>
</tr>
<tr>
<td>2004-03-09</td>
<td>10069</td>
<td>REF6822: A 6.00 KClient could appear to hang when the Connection Manager was prompting for a new password.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Allow <em>passwd</em> to be SHELLed, even if pseudo-tty support is disabled.</td>
</tr>
<tr>
<td>2004-03-10</td>
<td>10070</td>
<td>REF6824: Unicode and ASCII Kclient installers now install the shared library as <em>kclient.dll</em>.</td>
</tr>
<tr>
<td>2004-03-16</td>
<td>10076</td>
<td>REF6821: Permit array() = CON(0).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6832: Fixed SOAP client crashes caused by include/imports in the wsdl.</td>
</tr>
<tr>
<td>2004-03-17</td>
<td>10077</td>
<td>REF6834: Kservadm can now create a deep panic directory tree.</td>
</tr>
<tr>
<td>2004-03-18</td>
<td>10078</td>
<td>REF6833: 'KCMLStringMD5 was only computing checksum up to first HEX(00) character in the string.</td>
</tr>
<tr>
<td>2004-03-22</td>
<td>10082</td>
<td>REF6835: KClient could hang when shelling out to unix prompt via workbench console window.</td>
</tr>
<tr>
<td>2004-03-24</td>
<td>10084</td>
<td>REF6836: $UPPER("?") was asserting on debug builds as that character has no upper case equivalent defined by the Unicode Consortium. Now just leave the character unchanged.</td>
</tr>
<tr>
<td>2004-03-30</td>
<td>10090</td>
<td>REF6840: $ALERT SCREEN could crash if given a bad partition number.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6846: Fixed a redraw problem with OCX controls</td>
</tr>
<tr>
<td>2004-03-31</td>
<td>10091</td>
<td>REF6843: Fixed a crash when using the DisplayScreen method to display a form dump containing a grid with DataPending set.</td>
</tr>
<tr>
<td>2004-04-01</td>
<td>10092</td>
<td>REF6850: Problems with some characters when printing to the device clipboard.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6851: <em>kwho</em> and <em>bkstat -F</em> could produce truncated output.</td>
</tr>
<tr>
<td>2004-04-02</td>
<td>10093</td>
<td>REF6845: READ # could crash on some versions of Linux</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6856: $RELEASE fn children were adding to the [KCML] user count</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: ODBC now supports pack image 15.2</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6857: Using RESTORE LINE to a label was not working when used in a library.</td>
</tr>
<tr>
<td>2004-04-05</td>
<td>10096</td>
<td>ENH: The Connection Manager and kiodbc will now use PAM authentication on AIX 5.2.</td>
</tr>
<tr>
<td>2004-04-06</td>
<td>10097</td>
<td>REF6859: The Connection Manager could crash when listing internet services on NT.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6829: KI_COMP could crash on some TIFF images that were already compressed.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6860: The Connection Manager's panic directory listing could crash if there was a corrupt panic file present.</td>
</tr>
<tr>
<td>2004-04-13</td>
<td>10104</td>
<td>ENH: Use memory mapping to allocate heap memory on AIX 5.2.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6863: The Connection Manager's administration pages will now sort access control lists.</td>
</tr>
<tr>
<td>2004-04-14</td>
<td>10105</td>
<td>REF6869: The <em>Refresh</em> and <em>Up to higher level</em> links on the Connection Manager's directory listings didn't work for a per-service alias.</td>
</tr>
<tr>
<td>2004-04-15</td>
<td>10106</td>
<td>REF6872: Do not allow an ERROR DO to follow a FOR statement.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6873: CLEAR P could casue crash if you were executing in library code.</td>
</tr>
<tr>
<td>2004-04-20</td>
<td>10111</td>
<td>REF6877: Workbench Form browser crash when viewing COM controls.</td>
</tr>
<tr>
<td>2004-04-22</td>
<td>10113</td>
<td>REF6879: Fixed a potential memory leak when attempting to write a message to syslog.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6880: Fixed a Unicode issue with COM events in the ANSI client.</td>
</tr>
<tr>
<td>2004-04-28</td>
<td>10119</td>
<td>REF6884: The form placement style RelativeToParent was broken.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6885: Was not adding the &lt;user&gt; tag to PANIC files when executed via the Connection Manager.</td>
</tr>
<tr>
<td>2004-04-29</td>
<td>10120</td>
<td>REF6764: Fixed an obscure crash in KI_REWRITE on type 7 database tables.</td>
</tr>
<tr>
<td>2004-05-11</td>
<td>10132</td>
<td>REF6901: Fixed a problem where an EditRowNotify() event was not being generated when coming off a grid because of the user clicking on a LeftTool button on the toolbar.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6904: Conditional TRAPs entered via console window may fail. Dependant on execute statement.</td>
</tr>
<tr>
<td>2004-05-13</td>
<td>10134</td>
<td>REF6905: Possible to get invalid text in a drop-down dbedit by deleting characters or over-typing a selection.</td>
</tr>
<tr>
<td>2004-05-17</td>
<td>10138</td>
<td>REF6911: CLOSE was not deselecting an auto-allocated stream.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6912: An application making very many LIBRARY ADD and LIBRARY REMOVE calls could run out of symbols due to a failure to release all symbols when a library is removed.</td>
</tr>
<tr>
<td>2004-05-18</td>
<td>10139</td>
<td>ENH: Fixed a problem with locks being lost on Unix where a file was opened on two handles.</td>
</tr>
<tr>
<td>2004-05-24</td>
<td>10145</td>
<td>REF6926: Workbench file browser, file properties had several problems, including crash in release builds.</td>
</tr>
<tr>
<td>2004-05-25</td>
<td>10146</td>
<td>REF6934: Setting traps on internal KCML functions would crash.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6936: Fixed a crash when using redirected console input to perform an immediate mode LOAD.</td>
</tr>
<tr>
<td>2004-06-01</td>
<td>10153</td>
<td>REF6945: Dyndom.sl library on HP-UX had a hardwired location for the Xerces library.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6946: Bkstat -M could produce a negative memory usage on a system with a large number of KCML processes running on it.</td>
</tr>
<tr>
<td>2004-06-03</td>
<td>10155</td>
<td>REF6947: Fixed a crash in COPY OBJECT on some HP-UX systems.</td>
</tr>
<tr>
<td>2004-06-07</td>
<td>10159</td>
<td>ENH: Stricter Ethernet address check on Linux.</td>
</tr>
<tr>
<td>2004-06-10</td>
<td>10162</td>
<td>REF6955: Pseudo-tty support could hang.</td>
</tr>
<tr>
<td>2004-06-18</td>
<td>10170</td>
<td>REF6966: Fixed various problems with 64-bit disk access versions of the Connection Manager on NT.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6967: Fixed file locking problems, under Windows NT, for 64-bit disk access versions.</td>
</tr>
<tr>
<td>2004-06-21</td>
<td>10173</td>
<td>REF6968: Applying a trap to a program line containing the current DATA statement and then continuing without restarting the program could lead to a crash on a subsequent read.</td>
</tr>
<tr>
<td>2004-06-23</td>
<td>10175</td>
<td>REF6970: Possible for Validate events not to fire correctly on numeric DBedits</td>
</tr>
<tr>
<td>2004-06-30</td>
<td>10182</td>
<td>REF6974: $END in workbench while running under UNIX via telnet connection. Could cause window corruption.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6975: Crash in Workbench large variable display.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Connection Manager enhancements:
<ul>
<li>XML Include files can now include other XML files.</li>
<li>Aliases and the Access Control Lists can now be defined in XML include files.</li>
<li>Error messages from the XML parser will be displayed if kconf.xml or an include file is corrupt.</li>
</ul></td>
</tr>
<tr>
<td>2004-07-05</td>
<td>10187</td>
<td>REF6977: Setting $SHELL in a service's &lt;environment&gt; section appeared to have no effect.</td>
</tr>
<tr>
<td>2004-07-08</td>
<td>10190</td>
<td>REF6987: Can now delete the entry for a included access control list. Clear out an empty access control list.</td>
</tr>
<tr>
<td>2004-07-12</td>
<td>10194</td>
<td>REF6982: After displaying a 132 column screen that needed to be shrunk to fit on screen KClient could remember an incorrect narrow font size.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF6989: Fixed redraw issue when changing the text of a transparent picture button.</td>
</tr>
<tr>
<td>2004-07-16</td>
<td>10198</td>
<td>REF6994: HEXPRINT + Output format was incorrect.</td>
</tr>
<tr>
<td>2004-07-20</td>
<td>10202</td>
<td>REF7001: Interrogating a service's database catalogue, via the Connection Manager's admin pages, could fail if it was not the currently selected service.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7000: Workbench. Breakpoint bitmap could be corrupted when changing fonts.</td>
</tr>
<tr>
<td>2004-07-21</td>
<td>10203</td>
<td>REF7002: Fixed a crash when setting a service's &lt;soapstart&gt; value.</td>
</tr>
<tr>
<td>2004-07-22</td>
<td>10204</td>
<td>REF7003: Workbench create form dialog wasn't appearing.</td>
</tr>
<tr>
<td>2004-07-23</td>
<td>10205</td>
<td>REF7004: kmake now reports back errors from the the XML parser if <em>kconf.xml</em> is corrupt.</td>
</tr>
<tr>
<td>2004-07-27</td>
<td>10209</td>
<td>REF7008: On a grid cell the EditRowNotify event was not being called correctly if the pressed a hot key to accelerate to a button on the form.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7013: In the statement DIM a(1), b(a(1)) a run-time error would result because the variable a() would not have been initialised. Now no longer error, to be compatible with KCML 6.0.</td>
</tr>
<tr>
<td>2004-07-30</td>
<td>10212</td>
<td>REF7020: Fixed a crash in <em>kwebserv -e configFile</em>.<br />
ENH: If the <em>-s service</em> flag is used in conjunction with the <em>-e configFile</em> flag, then check the service's include files as well.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Specifying '.' as the user name on KClient's command line acts as a shorthand for the current Windows user name.</td>
</tr>
<tr>
<td>2004-08-02</td>
<td>10215</td>
<td>REF7021: Added Backspace shift to workbench keyboard shortcuts.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7022: Workbench tooltips now take // comments around DEFSUBs into account.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7017: Workbench variable display window. Focus should be set to editor window after this is destroyed.</td>
</tr>
<tr>
<td>2004-08-03</td>
<td>10216</td>
<td>REF7006: Fixed potential spurious runtime errors when using KClient DisplayScreen method to display a forms screen dump.</td>
</tr>
<tr>
<td>2004-08-09</td>
<td>10222</td>
<td>REF7026: Fixed workbench evaluate window to display (C)OM, (D)IM, (L)OCAL DIM correctly.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7024: Workbench would allow you to create forms in debug mode.</td>
</tr>
<tr>
<td>2004-08-10</td>
<td>10223</td>
<td>REF7029: Fixed KClient print to clipboard.</td>
</tr>
<tr>
<td>2004-08-12</td>
<td>10225</td>
<td>REF7030: Fixed possible screen corruption when mixing ANSI and Wang display modes.</td>
</tr>
<tr>
<td>2004-08-18</td>
<td>10231</td>
<td>REF7035: Prevent KClient control characters being sent to SHELLed command.</td>
</tr>
<tr>
<td>2004-08-20</td>
<td>10233</td>
<td>REF7042: Kwebserv now handles HTTP caching.</td>
</tr>
<tr>
<td>2004-08-23</td>
<td>10236</td>
<td>REF7043: Fixed possible stack corruption when an object method call errors.</td>
</tr>
<tr>
<td>2004-08-24</td>
<td>10237</td>
<td>REF7050: Possible for KClient to display malformed error messages when logging in.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7051: The Connection Manager's 'System Commands' page was not displaying non-zero return codes correctly.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7038: Problems invoking large variable display from toolbar.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7052: The Connection Manager no longer locks <em>/etc/passwd</em> while authenticating a user's password.</td>
</tr>
<tr>
<td>2004-08-25</td>
<td>10238</td>
<td>REF7053: The Connection Manager didn't detect that a user's password had been expired with the <em>passwd -f</em> command on UnixWare.</td>
</tr>
<tr>
<td>2004-08-26</td>
<td>10239</td>
<td>ENH: KClient 'licence expiry pending' message specifies how many users will expire rather than implying they all will.</td>
</tr>
<tr>
<td>2004-08-31</td>
<td>10244</td>
<td>REF7061: In Unicode builds could lose the last character of a string value returned from a client-side $DECLARE if its buffer was DIMed exaclty large enough to hold the string.</td>
</tr>
<tr>
<td>2004-09-01</td>
<td>10245</td>
<td>REF7063: Fixed the install script to create suitable PAM configuration files on SuSE-Linux.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7064: The Connection Manager would fail to list a system log whose entry in <em>/etc/syslog.conf</em> used the '-' no-sync flag.</td>
</tr>
<tr>
<td>2004-09-02</td>
<td>10246</td>
<td>REF7067: Potential error starting KClient on server versions of Windows without Terminal Services running.</td>
</tr>
<tr>
<td>2004-09-07</td>
<td>10251</td>
<td>REF7040: Where a form inherits from another form that does not appear in the current program, kcml could sometimes crash instead of erroring, both at run-time and when the form is edited.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7072: The Connection Manager's directory listing of a per-service alias could contain bad links.</td>
</tr>
<tr>
<td>2004-09-20</td>
<td>10264</td>
<td>REF7083: Don't attempt to create a pseudo-tty when attempting to SHELL "passwd"</td>
</tr>
<tr>
<td>2004-09-23</td>
<td>10267</td>
<td>REF7090: Fixed a problem where output would be lost when SHELL'ing the bkstat utility from inside a text-mode application.</td>
</tr>
<tr>
<td>2004-09-24</td>
<td>10268</td>
<td>REF7092: A protected save of a program line with more than 32K of code could lead to a corrupted program that would not reload.</td>
</tr>
<tr>
<td>2004-09-27</td>
<td>10271</td>
<td>REF7095: Sorting a directory listing by file size didn't work for files over 2Gb in size.</td>
</tr>
<tr>
<td>2004-09-29</td>
<td>10273</td>
<td>REF6797: The <em>sql</em> utility could crash when querying type 6 database files with a .sq dictionary.</td>
</tr>
<tr>
<td>2004-09-30</td>
<td>10274</td>
<td>REF7098: Fixed a crash when attempting to list the columns in a database table using <em>sql -C</em>.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7104: Workbench database browser could crash when displaying column information.</td>
</tr>
<tr>
<td>2004-10-01</td>
<td>10275</td>
<td>REF7119: Column labels were missing the last character in the database browser.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7120: Workbench database browser could corrupt the environment variable list.</td>
</tr>
<tr>
<td>2004-10-04</td>
<td>10278</td>
<td>REF7121: Fixed crash using "&lt;&gt;=" as POS( operator.</td>
</tr>
<tr>
<td>2004-10-05</td>
<td>10279</td>
<td>REF7027: Fixed crash using workbench's global text search.</td>
</tr>
<tr>
<td>2004-10-07</td>
<td>10281</td>
<td>REF7130: Ignore $USEMALLOC and the -y flag on Linux and AIX5.2.</td>
</tr>
<tr>
<td>2004-10-11</td>
<td>10285</td>
<td>REF7128: When changing the name of a blank form in KForm it was not reflected by the workbench.</td>
</tr>
<tr>
<td>2004-10-12</td>
<td>10286</td>
<td>ENH: Add Thai (<a href="mk:@MSITStore:kcmlrefman.chm::/LanguageCodes.htm">language code</a>=16) to the list of supported languages.</td>
</tr>
<tr>
<td>2004-10-13</td>
<td>10287</td>
<td>ENH: Use memory mapping to allocate heap memory on HP-UX 11.</td>
</tr>
<tr>
<td>2004-10-15</td>
<td>10289</td>
<td>REF7132: Fixed potential hang after executing SHELL.</td>
</tr>
<tr>
<td>2004-10-19</td>
<td>10293</td>
<td>REF7134: Allow commas in pack images defining fields.</td>
</tr>
<tr>
<td>2004-10-25</td>
<td>10299</td>
<td>ENH: Use the Ethernet card's MAC address in a licence file's machine ID for Unixware.</td>
</tr>
<tr>
<td>2004-10-27</td>
<td>10301</td>
<td>REF7016: KI_LOCK_OWNER was broken on 64bit file I/O builds</td>
</tr>
<tr>
<td>2004-11-01</td>
<td>10306</td>
<td>REF7143: Fixed $DEVICE to work with network printer shares and LPT1 on Windows.</td>
</tr>
<tr>
<td>2004-11-03</td>
<td>10308</td>
<td>REF7151: LOAD RUN will no longer be supported in the Workbench F2 buffer.</td>
</tr>
<tr>
<td>2004-11-04</td>
<td>10309</td>
<td>REF7150: Fixed potential corruption when transmitting certain byte patterns to the client.</td>
</tr>
<tr>
<td>2004-11-15</td>
<td>10320</td>
<td>REF7139: Not correctly updating pictures in the client if running with caching disabled.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7171: Fixed potential hang after displaying a form in a $RELEASE'd KCML</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added form DropFile event and DropFileList$ property to return a list of files drag &amp; dropped onto a form.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Improve efficiency when creating forms with large numbers of controls.</td>
</tr>
<tr>
<td>2004-11-18</td>
<td>10323</td>
<td>REF7184: Fixed memory leak in SHELL, Windows only.</td>
</tr>
<tr>
<td>2004-11-22</td>
<td>10327</td>
<td>REF7187: The Connection Manager could show a partial process list on NT.</td>
</tr>
<tr>
<td>2004-12-01</td>
<td>10336</td>
<td>REF7522: Fixed a problem setting focus to a Group control when the group is on an inactive tab page.</td>
</tr>
<tr>
<td>2004-12-07</td>
<td>10342</td>
<td>REF7553: Fixed a problem showing &amp; hiding controls in a Group control</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7167: Changing a tab page's ear text did not persist the new text.</td>
</tr>
<tr>
<td>2004-12-08</td>
<td>10343</td>
<td>REF7559: Add any error message from the XML parser if <em>kcml -s serviceName</em> fails.</td>
</tr>
<tr>
<td>2004-12-09</td>
<td>10344</td>
<td>REF7563: Fixed potential KClient crash moving focus to a DBedit.</td>
</tr>
<tr>
<td>2004-12-13</td>
<td>10348</td>
<td>REF7567: Support negative RANGE values when parsing a .sq schema.</td>
</tr>
<tr>
<td>2004-12-17</td>
<td>10352</td>
<td>REF7577: Convert Unicode Euro character HEX(20AC) into Windows specific HEX(80) for E="UTF-8" mode of $PACK and $UNPACK irrespective of locale.</td>
</tr>
<tr>
<td>2004-12-22</td>
<td>10357</td>
<td>REF7569: Ensure variable filtering in panic file stylesheet works for Firefox, Mozilla and IE6.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7570: Programmed VT100 function keys not being sent</td>
</tr>
<tr>
<td>2004-12-23</td>
<td>10358</td>
<td>REF7574: Use of FLD(row$.langfld$(x)) as a receiver generated the wrong offset for the language in use.</td>
</tr>
<tr>
<td>2005-01-13</td>
<td>11013</td>
<td>REF7617: Could not edit a service from the <em>Interrogate Services</em> page if its name contained a space character.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7619: Console command RENAME was not setting the modified flag for the workbench source window. So Ctrl-S (Save) might think you have an unmodified program.</td>
</tr>
<tr>
<td>2005-01-18</td>
<td>11018</td>
<td>REF7629: Fixed CTRL-SHIFT-G.</td>
</tr>
<tr>
<td>2005-01-21</td>
<td>11021</td>
<td>ENH: Disabled Nagle algorithm for SOAP</td>
</tr>
<tr>
<td>2005-01-24</td>
<td>11024</td>
<td>REF7641: Support dateTime datatype in SOAP client</td>
</tr>
<tr>
<td>2005-01-26</td>
<td>11026</td>
<td>REF7645: Do not expand environment variables that have been escaped by a '\'.</td>
</tr>
<tr>
<td>2005-02-07</td>
<td>11038</td>
<td>REF7669: KClient could size a text mode window incorrectly if its toolbar was displayed.</td>
</tr>
<tr>
<td>2005-02-16</td>
<td>11047</td>
<td>REF7702: The Installer now adds Start Menu entries under <em>Kerridge-&gt;KCML 6.20</em></td>
</tr>
<tr>
<td>2005-02-18</td>
<td>11049</td>
<td>ENH: The Connection Manager supports a list of excluded users in &lt;validusers&gt; by prefixing the user names with '!'</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7712: Fixed an incompatibility with the Windows XP Service Pack 2 Data Execution Protection feature.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7713: Fixed a problem with spurious data aware error using a fld in a library that is not otherwise referenced</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7717: Support KDB type BOOL as ODBC type BIT</td>
</tr>
<tr>
<td>2005-02-21</td>
<td>11052</td>
<td>REF7720: Problem extending tables greater than 2Gb</td>
</tr>
<tr>
<td>2005-02-22</td>
<td>11053</td>
<td>REF7695: bad null value for dates in ORDER BY</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7718: Fixed potential KClient resource leak when resizing grids containing cells with drop-down lists.</td>
</tr>
<tr>
<td>2005-02-23</td>
<td>11054</td>
<td>REF7729: Fixed installation of KCC service for AIX5.1</td>
</tr>
<tr>
<td>2005-03-01</td>
<td>11060</td>
<td>REF7750: Fixed file type mask in KClient connection wizard icon picker.</td>
</tr>
<tr>
<td>2005-03-03</td>
<td>11062</td>
<td>REF7771: Fixed minor KClient resource leak.</td>
</tr>
<tr>
<td>2005-03-04</td>
<td>11063</td>
<td>ENH: KDB KI_READ_NEXT and KI_DELETE combination could lead to bogus KE_DATADAMAGED and KE_NOTFOUND errors.</td>
</tr>
<tr>
<td>2005-03-07</td>
<td>11066</td>
<td>REF7766: In a mixed text/GUI application KClient's text mode toolbar would stop working after a GUI form with a toolbar had been displayed.</td>
</tr>
<tr>
<td>2005-03-10</td>
<td>11069</td>
<td>REF7785: Emptying a word search sequence set page and then re-inserting onto that page caused a word search index corruption.</td>
</tr>
<tr>
<td>2005-03-14</td>
<td>11073</td>
<td>ENH: KDB KI_MOVE_TABLE and KI_COPY_TABLE used on systems with a database journal could crash.</td>
</tr>
<tr>
<td>2005-03-15</td>
<td>11074</td>
<td>REF7794: If a form has a multi-pane status bar, control Help$ text will appear only in the first pane and leave the style of the status bar unchanged.</td>
</tr>
<tr>
<td>2005-03-15</td>
<td>11074</td>
<td>ENH: Support LAT=Y clause in $DEVICE for printers to convert UTF-8 to Latin-15</td>
</tr>
<tr>
<td>2005-03-18</td>
<td>11077</td>
<td>REF7806: Kwebserv wasn't setting up $KCML_SOURCES properly when exec'd from a script.</td>
</tr>
<tr>
<td>2005-03-22</td>
<td>11081</td>
<td>REF7823: Fix for possible looping process if panic that follows a core dump itself causes a core dump.</td>
</tr>
<tr>
<td>2005-03-23</td>
<td>11082</td>
<td>ENH: Better KDB error messages</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7623: 'KCMLStringMD5 could return a blank string on Red Hat ES3</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH7697: Optimise traffic sent from KCML to KClient.</td>
</tr>
<tr>
<td>2005-04-04</td>
<td>11094</td>
<td>REF7821: Fixed a problem that could lead to a hang or crash when fetching back very large amounts of data using a COM object method (such as retrieving text from several thousand cells from a spreadsheet in one method call).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7839: Clearing the KClient password cache may not clear all passwords where there are multiple passwords stored for a single server.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7070: When printing in text mode ($DEVICE option DIR=N) KClient will use a font with a character set matching the current locale.</td>
</tr>
<tr>
<td>2005-04-05</td>
<td>11095</td>
<td>REF7846: Tree item OpenImage image was displayed when the item was selected instead of when the item was expanded.</td>
</tr>
<tr>
<td>2005-04-06</td>
<td>11096</td>
<td>REF7850: Moving a boolean DBedit could fail under certain obscure circumstances.</td>
</tr>
<tr>
<td>2005-04-07</td>
<td>11097</td>
<td>REF7807: Fixed pseudo-tty support for Linux 2.6 kernel.</td>
</tr>
<tr>
<td>2005-04-08</td>
<td>11098</td>
<td>REF7856: Resetting a DBedit's text to its orginal value after a failed Validate event did not work.</td>
</tr>
<tr>
<td>2005-04-11</td>
<td>11101</td>
<td>REF7860: Kmake could crash on Linux when executed from the command-line or via a script.</td>
</tr>
<tr>
<td>2005-04-12</td>
<td>11102</td>
<td>REF7864: Listing a service's default tablespace didn't always work.</td>
</tr>
<tr>
<td>2005-04-14</td>
<td>11104</td>
<td>REF7871: Fixed a crash when terminating a KCML partition with <em>kservadm -p &lt;partno&gt;</em></td>
</tr>
<tr>
<td>2005-04-20</td>
<td>11110</td>
<td>ENH: On AIX5.2, use <em>/dev/ptc</em> to create the pseudo-tty for SHELL and the interactive ! shell.</td>
</tr>
<tr>
<td>2005-04-21</td>
<td>11111</td>
<td>REF7888: Using Ctrl-Tab in a multi-line dbedit to insert a tab character would cause the next character entered to be lost.</td>
</tr>
<tr>
<td>2005-04-27</td>
<td>11117</td>
<td>ENH: Reduce the memory requirements on Unix by statically linking kcml.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7909: Fixed crash, on Unixware, when using kmake's -p switch.</td>
</tr>
<tr>
<td>2005-05-09</td>
<td>11129</td>
<td>REF7942: Fixed a problem with a spurious error about a DataSource$ buffer not being found if the form is contained in a library that contains no other reference to that buffer varaible.</td>
</tr>
<tr>
<td>2005-05-10</td>
<td>11130</td>
<td>REF7948: Updating environment variables using kwebserv's /admin pages could occasionally fail on AIX4.3 &amp; 5.1</td>
</tr>
<tr>
<td>2005-05-12</td>
<td>11132</td>
<td>REF7952: Fixed potential looping KCML process when KClient disconnects unexpectedly.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7953: $MALLOCSPACE did not have an effect on AIX4.3</td>
</tr>
<tr>
<td>2005-05-13</td>
<td>11133</td>
<td>REF7956: Report PAM config errors to syslog.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7955: KClient could crash if pictures or colours were created outside of the Create event using the CreateControl or Duplicate methods.</td>
</tr>
<tr>
<td>2005-05-17</td>
<td>11137</td>
<td>ENH: The Connection Manager's webserver will now log the HTTP referer when a web page cannot be found.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7962: Kwebserv could crash when KClient connected to a service whose name contained a space character.</td>
</tr>
<tr>
<td>2005-05-18</td>
<td>11138</td>
<td>REF7963: DBedits in associated edit groups on different tab pages may not line up correctly until all the tab pages have been shown.</td>
</tr>
<tr>
<td>2005-05-19</td>
<td>11139</td>
<td>REF7966: Fixed heap corruption if there was not enough memory for MAT REDIM.</td>
</tr>
<tr>
<td>2005-05-20</td>
<td>11140</td>
<td>REF7968: If we used up all the pages in a memory-mapped heap we could corrupt $PSTAT.</td>
</tr>
<tr>
<td>2005-05-24</td>
<td>11144</td>
<td>REF7972: Setting text in a DBedit control on a tab page had no effect unless the page had been displayed.</td>
</tr>
<tr>
<td>2005-05-25</td>
<td>11145</td>
<td>REF7973: Fixed a problem processing input from KClient under certain circumstances which could lead to a hang or spurious error message.</td>
</tr>
<tr>
<td>2005-05-26</td>
<td>11146</td>
<td>REF7978: If a grid was reset inside an EditRowNotify event it could fail to display correctly afterwards.</td>
</tr>
<tr>
<td>2005-06-01</td>
<td>11152</td>
<td>REF7980: Fixed buffer overflow when changing the case of UTF-8 strings with $UPPER and $LOWER.</td>
</tr>
<tr>
<td>2005-06-07</td>
<td>11158</td>
<td>REF7546: A form.Terminate() event could corrupt the stack.</td>
</tr>
<tr>
<td>2005-06-10</td>
<td>11161</td>
<td>REF7989: Withdraw use of PAM on AIX 5.2.</td>
</tr>
<tr>
<td>2005-06-30</td>
<td>11181</td>
<td>REF8019: Fixed a potential crash after calling the Explode() method on an empty graph.</td>
</tr>
<tr>
<td>2005-07-04</td>
<td>11185</td>
<td>REF7834: Problem with local variables in the forked screen saver partition could cause silent core dumps.</td>
</tr>
<tr>
<td>2005-07-08</td>
<td>11189</td>
<td>REF8030: Upgrading of KClient by a non-admin user on Windows XP could fail because of strict permissions on the install directory.</td>
</tr>
<tr>
<td>2005-07-11</td>
<td>11192</td>
<td>REF8035: KClient will only send a single CursorMove event for a scroll operation on a grid, even if multiple lines or pages were scrolled.</td>
</tr>
<tr>
<td>2005-07-14</td>
<td>11195</td>
<td>REF8042: CGI scripts could get an incorrect $PATH when running on an ASP server.</td>
</tr>
<tr>
<td>2005-07-19</td>
<td>11200</td>
<td>REF7951: Fixed a potential KClient hang when displaying a new form under certain circumstances.</td>
</tr>
<tr>
<td>2005-07-22</td>
<td>11203</td>
<td>REF8051: Dragging of files from MS Outlook Express broken.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8053: Fixed a crash <strong>CREATE "SOAP", url$</strong> when the URL was badly formed.</td>
</tr>
<tr>
<td>2005-07-28</td>
<td>11209</td>
<td>REF8027: Fixed a potential KClient crash displaying malformed forms containing duplicate control IDs.</td>
</tr>
<tr>
<td>2005-08-04</td>
<td>11216</td>
<td>ENH: Type-7 database handles can now use less memory.</td>
</tr>
<tr>
<td>2005-08-05</td>
<td>11217</td>
<td>REF8081: Fixed an infrequent problem where multiple logins from a single client machine may consume too many user licenses.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Add IP_TOS call to allow users to change the TOS field in IP headers.</td>
</tr>
<tr>
<td>2005-08-08</td>
<td>11220</td>
<td>REF8079: If was possible for the client to have unvalidated text in an edit control if the user started to click the cancel button after entering text, but moved the mouse cursor away from the button before completing the click. This would have abandoned the Validate() event on the assumption that a Cancel() event was pending. Now the Validate() will be rethrown if a click on a cancel button does not complete.</td>
</tr>
<tr>
<td>2005-08-15</td>
<td>11227</td>
<td>REF8102: Updating <em>kconf.xml</em> with the Connection Manager's admin pages could fail with 'missing serial value'.</td>
</tr>
<tr>
<td>2005-08-16</td>
<td>11228</td>
<td>REF8071: Fixed buffer overrun when attempting to report syntax errors from a KCML script.</td>
</tr>
<tr>
<td>2005-08-17</td>
<td>11229</td>
<td>REF8088: CLEARing a program which contained DATA statements could cause a subsequent LOAD to crash.</td>
</tr>
<tr>
<td>2005-08-19</td>
<td>11231</td>
<td>REF8114: The Connection Manager could fail to authenticate a user if their password did not have a date expiry.</td>
</tr>
<tr>
<td>2005-08-23</td>
<td>11235</td>
<td>REF8117: SHELL could crash, on Windows, if given a long filename.</td>
</tr>
<tr>
<td>2005-08-24</td>
<td>11236</td>
<td>REF8120: The XML parser could crash when processing bad XML data.</td>
</tr>
<tr>
<td>2005-09-02</td>
<td>11245</td>
<td>REF7613: LOAD RUN could attempt to open "START .src"</td>
</tr>
<tr>
<td>2005-09-06</td>
<td>11249</td>
<td>REF8128: Fixed SOAP support in the Connection Manager.</td>
</tr>
<tr>
<td>2005-09-08</td>
<td>11251</td>
<td>REF8136: Raised the level of crash syslog messages so that they get redirected to the AIX error log.</td>
</tr>
<tr>
<td>2005-09-09</td>
<td>11252</td>
<td>REF8138: Normally when assigning to a control property KCML does not re-send the value to the client if it is unchanged. However we must always send properties to an OCX control on assignment even if they are unchanged as we cannot know how the OCX will handle them.</td>
</tr>
<tr>
<td>2005-09-16</td>
<td>11259</td>
<td>REF8105: XML file handle's opened with CALL's are now displayed correctly when tooltiping in the workbench.</td>
</tr>
<tr>
<td>2005-09-20</td>
<td>11263</td>
<td>REF8149: Memory leak. NT Only.</td>
</tr>
<tr>
<td>2005-09-26</td>
<td>11269</td>
<td>REF8153: OPEN now errors when all streams are in use.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8159: $OPEN could hang on on unreliable networks.</td>
</tr>
<tr>
<td>2005-09-28</td>
<td>11271</td>
<td>REF8162: $PSTAT's DEV field was not being set when waiting for input.</td>
</tr>
<tr>
<td>2005-09-30</td>
<td>11273</td>
<td>REF8145: Problem resetting grid properties after calling Reset() or Clear().</td>
</tr>
<tr>
<td>2005-10-04</td>
<td>11277</td>
<td>REF8172: Mandatory KDB lock checking could fail in systems that don't use catalogues.</td>
</tr>
<tr>
<td>2005-10-05</td>
<td>11278</td>
<td>REF8177: ODBC and SQL access to KDB type6 tables with extents could produce truncated results.</td>
</tr>
<tr>
<td>2005-10-06</td>
<td>11279</td>
<td>REF8176: Improved error messages for <em>kcml</em> &amp; <em>kmake</em> when they fail to load <em>kwebserv.so</em></td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8178: KDB type6 table locks could fail in complicated situations involving more than one handle open on a table and more unlocks than locks.</td>
</tr>
<tr>
<td>2005-10-11</td>
<td>11284</td>
<td>REF8185: A syntax error in a multi-statement line entered with the console line editor truncated the line.</td>
</tr>
<tr>
<td>2005-10-18</td>
<td>11291</td>
<td>REF8197: Improved error messages for <em>kc6</em> &amp; <em>kmake</em> when they fail to execute <em>kcml</em></td>
</tr>
<tr>
<td>2005-10-21</td>
<td>11294</td>
<td>REF8202: LIMITS # would report an incorrect size on a file larger than 2Gb.</td>
</tr>
<tr>
<td>2005-10-26</td>
<td>11299</td>
<td>REF8214: Report error strings for failure of NTLM authentication to the event log.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH8215: Added 'KCMLSetClientIP_TOS $DECLARE to allow seting of IP header Type Of Service fields for data sent by the client.</td>
</tr>
<tr>
<td>2005-11-02</td>
<td>11306</td>
<td>REF8227: Caseless SORT was broken.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8219: Help$ tooltips did not always appear for controls on a tab page.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8230: Fixed a potential crash in numeric edits with a vary large number of characters.</td>
</tr>
<tr>
<td>2005-11-07</td>
<td>11311</td>
<td>REF8234: Fixed a zero precision format specifier in $PRINTF.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8236: The <em>compile</em> utility now ignores the value of $CWD.</td>
</tr>
<tr>
<td>2005-11-09</td>
<td>11313</td>
<td>REF8063: Sometimes debug information in a panic file could be incomplete.</td>
</tr>
<tr>
<td>2005-11-16</td>
<td>11320</td>
<td>REF8044: MAT REDIM SYM(*p)$s was only legal syntax at the end of a line</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8046: Sometimes unable to scroll a grid after clicking a cursor disabled cell if much of the grid is cursor disabled.</td>
</tr>
<tr>
<td>2005-11-28</td>
<td>11332</td>
<td>REF8271: Setting Help$ on a menu control itself rather than one of its items could crash the client.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8273: The Connection Manager will log the reason to the NT Event Log when it fails to execute a server process.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8272:Fixed crash in specific SOAP object method call when using complex types.</td>
</tr>
<tr>
<td>2005-11-29</td>
<td>11333</td>
<td>REF8274: If we fail to create a pseudo-tty for SHELL, then log the reason to the Unix syslog.</td>
</tr>
<tr>
<td>2005-12-05</td>
<td>11339</td>
<td>REF8279: The setup program for KClient could occasionally hang when installing <em>kclient.ttf</em>.</td>
</tr>
<tr>
<td>2005-12-09</td>
<td>11343</td>
<td>ENH: Support session tracking cookies in SOAP client. Support SSL for sockets and SOAP clients on AIX5.2, Linux and Windows.</td>
</tr>
<tr>
<td>2005-12-20</td>
<td>11354</td>
<td>REF8211: Support mouse scroll wheel in grids and dbedits.</td>
</tr>
<tr>
<td>2006-01-03</td>
<td>12003</td>
<td>ENH: Improve performance of mouse wheel scrolling on complicated grids.</td>
</tr>
<tr>
<td>2006-01-13</td>
<td>12013</td>
<td>REF8319: Picture buttons without TabStop set should never take keyboard focus. However this could happen if the button was activated by a keyboard accelerator</td>
</tr>
<tr>
<td>2006-01-16</td>
<td>12016</td>
<td>REF8324: Support Keep-Alive headers in the SOAP server to allow client to determine when the connection is broken.</td>
</tr>
<tr>
<td>2006-01-18</td>
<td>12018</td>
<td>REF8326: If a single click event handler creates a child form and the single click is actually part of a double click the double click event should be dropped. This did not always happen.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8332: Where a control has both single and double click event handlers it was possible for the double click event to be difficult for the user to trigger. Especially when running over a slow network.</td>
</tr>
<tr>
<td>2006-01-23</td>
<td>12023</td>
<td>REF8337: KCML style buttons are drawn with square corners when on a form with a background image.</td>
</tr>
<tr>
<td>2006-01-25</td>
<td>12025</td>
<td>REF8341: Fixed creation of new &lt;include&gt; files from the Connection Manager's /admin pages.</td>
</tr>
<tr>
<td>2006-02-01</td>
<td>12032</td>
<td>REF8351: KClient 'Empty Cache' button in preferences did nothing on Pocket PC</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8348: On Pocket PC the option to show/hide a form's toolbar didn't work for child forms.</td>
</tr>
<tr>
<td>2006-02-09</td>
<td>12040</td>
<td>REF8362: Grid DropDown event was broken.</td>
</tr>
<tr>
<td>2006-02-10</td>
<td>12041</td>
<td>REF8366: More efficient use of Windows resources where a grid has unpopulated drop down lists.</td>
</tr>
<tr>
<td>2006-02-14</td>
<td>12045</td>
<td>REF8369: Fixed hang in $CLOSE on a pipe.</td>
</tr>
<tr>
<td>2006-02-15</td>
<td>12046</td>
<td>REF8349: Fixed a potential KClient crash when LOADing a program from within the Create event of a form.</td>
</tr>
<tr>
<td>2006-02-22</td>
<td>12053</td>
<td>REF8378: Fixed a workbench crash while scolling.</td>
</tr>
<tr>
<td>2006-02-27</td>
<td>12058</td>
<td>REF8374: On Pocket PC KClient added a 'Quit' option to the connection broker notification message.</td>
</tr>
<tr>
<td>2006-03-01</td>
<td>12060</td>
<td>REF8385: Better syslog message when accessing /admin pages with WEBADMIN not set to <em>true</em>.</td>
</tr>
<tr>
<td>2006-03-16</td>
<td>12075</td>
<td>REF8405: Fixed a compatibility problem running a 6.20 KClient against a 5.50 KCML</td>
</tr>
<tr>
<td>2006-03-21</td>
<td>12080</td>
<td>REF8407: Fixed an editgroup sizing problem where edits in the same row have very different sizes.</td>
</tr>
<tr>
<td>2006-03-24</td>
<td>12083</td>
<td>REF8415: Ignore UTF-8 byte order marking when parsing XML with XML_OPEN or XML_PARSE_BUFFER.</td>
</tr>
<tr>
<td>2006-03-27</td>
<td>12086</td>
<td>REF8412: SQL combination of -s and SUBSTRING() could crash</td>
</tr>
<tr>
<td>2006-03-28</td>
<td>12087</td>
<td>REF8421: Kwebserv could produce two sets of HTTP headers for text files downloaded via a <em>FileText</em> alias.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8422: SQL dynamic parameters on multiple tables could crash on Windows</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8423: KI_INITIALISE of a type7 table with a WS index could corrupt the table</td>
</tr>
<tr>
<td>2006-03-30</td>
<td>12089</td>
<td>REF8425: 'KCMLStringMD5 should return the hash string as RETURN DIM()</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8020: Using Ctrl+C to copy text from a dbedit set the edit's modified state leading to a spurious Validate event.</td>
</tr>
<tr>
<td>2006-03-31</td>
<td>12090</td>
<td>REF8414: It was possible for a parent form to remain enabled if it created the child form in its Show() event and also had an edit SelChange() event handler.</td>
</tr>
<tr>
<td>2006-04-04</td>
<td>12094</td>
<td>REF7699: It was possible to use a DBedit's context menu to paste into a string formatted read-only edit.</td>
</tr>
<tr>
<td>2006-04-05</td>
<td>12095</td>
<td>ENH8307: The mouse wheel will scroll the control under the cursor where appropriate.</td>
</tr>
<tr>
<td>2006-04-06</td>
<td>12096</td>
<td>REF8438: NTLM authentication was broken</td>
</tr>
<tr>
<td>2006-04-12</td>
<td>12102</td>
<td>ENH8443: Added KClient FormColorBorderThreshold method to add a thin border around KCML style controls when they are coloured such that they have poor contrast with the background.</td>
</tr>
<tr>
<td>2006-04-20</td>
<td>12110</td>
<td>REF8450: Fixed a potential KClient crash displaying certain PNG format images.</td>
</tr>
<tr>
<td>2006-04-24</td>
<td>12114</td>
<td>ENH: On AIX4.3, use <em>/dev/ptc</em> to create the pseudo-tty for SHELL and the interactive ! shell.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8453: Fixed a potential KClient crash under Windows 98.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH8446: Added grid Outline selection style which shows selection as a thick border around the cell rather than a solid block of colour.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH8454: Allow the colour of the contrast border around KCML style controls to be changed independently of the form text colour.</td>
</tr>
<tr>
<td>2006-04-25</td>
<td>12115</td>
<td>REF8458: Fixed a potential crash when using oObject.Method(NUM(11.1)) style calls.</td>
</tr>
<tr>
<td>2006-04-27</td>
<td>12117</td>
<td>REF8461: Kwebserv could fail to read a HTTP header on AIX.</td>
</tr>
<tr>
<td>2006-04-28</td>
<td>12118</td>
<td>REF8465: When editing a form in KCML style KForm will use the same colour scheme as KClient.</td>
</tr>
<tr>
<td>2006-05-03</td>
<td>12123</td>
<td>REF8462: KI_DCOMP of a junk buffer would correctly error, but a subsequent dump was also possible</td>
</tr>
<tr>
<td>2006-05-05</td>
<td>12125</td>
<td>REF8476: Fixed a potential KClient crash during login.</td>
</tr>
<tr>
<td>2006-05-08</td>
<td>12128</td>
<td>REF8477: Fixed a drawing glitch on group-like tabs with a blank caption.</td>
</tr>
<tr>
<td>2006-05-12</td>
<td>12132</td>
<td>ENH: Use memory mapped codepage/Unicode conversion tables on Unix for $PACK(E="UTF8").</td>
</tr>
<tr>
<td>2006-05-22</td>
<td>12142</td>
<td>ENH: Fixed SSL support on Windows 2000 &amp; AIX5.</td>
</tr>
<tr>
<td>2006-05-24</td>
<td>12144</td>
<td>REF8503: Allow the font size and name to be specified when using KClient text mode printing via SetPrinterFontSize and SetPrinterFontName methods.</td>
</tr>
<tr>
<td>2006-05-25</td>
<td>12145</td>
<td>REF8493: SQL ORDER BY was not working correctly with UNION (DISTINCT)</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8499: ODBC SQL set functions on integers did not handle NULL sets correctly</td>
</tr>
<tr>
<td>2006-06-05</td>
<td>12156</td>
<td>REF8512: When the connection broker is run from a startup script networking may not be immediately ready. In that case the broker will retry creating its listen socket.</td>
</tr>
<tr>
<td>2006-06-08</td>
<td>12159</td>
<td>REF8515: Don't validate SOAPAction HTTP header line in the SOAP server to improve interoperability with non-conformant clients.</td>
</tr>
<tr>
<td>2006-06-12</td>
<td>12163</td>
<td>ENH: Support doc/lit styles in SOAP server.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8522: Fixed hang in connection broker.</td>
</tr>
<tr>
<td>2006-06-15</td>
<td>12166</td>
<td>ENH8531: On a unicode KClient external $Declares will only call the unicode version of the function if KCML is using UTF-8. This is to aid compatibility with older applications which may not be aware of the unicode Windows API.</td>
</tr>
<tr>
<td>2006-06-19</td>
<td>12170</td>
<td>ENH: Reduce memory usage of CALL XML_NEXT.</td>
</tr>
<tr>
<td>2006-06-21</td>
<td>12172</td>
<td>REF8538: Fixed an intermittent disconnect when logging in using a Pocket PC</td>
</tr>
<tr>
<td>2006-06-27</td>
<td>12178</td>
<td>REF8543: Added .Header$ property to set/get SOAP Headers.</td>
</tr>
<tr>
<td>2006-07-06</td>
<td>12187</td>
<td>REF8551: Improved Windows event log messages for KCML login failures.</td>
</tr>
<tr>
<td>2006-07-07</td>
<td>12188</td>
<td>REF8455: Improved connection broker reconnect times on Pocket PC when using a VPN over a GPRS link.</td>
</tr>
<tr>
<td>2006-07-10</td>
<td>12191</td>
<td>REF8552: A multi-column list box will automatically size its columns to fit the text.</td>
</tr>
<tr>
<td>2006-07-14</td>
<td>12195</td>
<td>REF8562: $RELEASE fn children were adding to the user count.</td>
</tr>
<tr>
<td>2006-07-17</td>
<td>12198</td>
<td>REF8565: LIMITS " ", s, e, c, rc would return an incorrect result on Unix.</td>
</tr>
<tr>
<td>2006-07-21</td>
<td>12202</td>
<td>REF8548: Where a virtual network device returns a bogus MAC address do not use this address to identify the client to KCML. If several client machines return the same MAC address then multiple KClient sessions on the affected machines will consume a licence slot for each session.</td>
</tr>
<tr>
<td>2006-07-28</td>
<td>12209</td>
<td>ENH: KI_STATFS was not always detecting NFS filesystems correctly.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8582: Ctrl+char hotkeys did not work on the Pocket PC soft keyboard.</td>
</tr>
<tr>
<td>2006-08-01</td>
<td>12213</td>
<td>ENH8416: On Pocket PC support backing up of Today screen KClient connections to flash memory (if present). A re install will restore them in case the device lost power and data.</td>
</tr>
<tr>
<td>2006-08-04</td>
<td>12216</td>
<td>REF8587: Fixed a compatibility issue between KClient and Compuware QARun</td>
</tr>
<tr>
<td>2006-08-14</td>
<td>12226</td>
<td>REF8596: Kservadm running under an RDP session would not display KCML partitions.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: $OPEN, on Unix, will use $WORKSPACE for its temporary lock files.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8592: XML_NEXT no longer redimensions the attribute value array to a size of zero.</td>
</tr>
<tr>
<td>2006-08-18</td>
<td>12230</td>
<td>ENH8600: Allow applications to force a large toolbar on a Pocket PC device using a new KClient forms method SmallScreenLargeToolBar. Usually a small toolbar is used to save space.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7555: Fixed an intermittent problem on Windows XP where after minimising and restoring a form which had a child form, the child form would be disabled.</td>
</tr>
<tr>
<td>2006-08-23</td>
<td>12235</td>
<td>REF8610: $KEYBOARD remapping did not work when mapping to certain keys such as 'Reset'</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8611: $TRAN /001 had no effect if $KEYBOARD was set</td>
</tr>
<tr>
<td>2006-08-25</td>
<td>12237</td>
<td>REF8632: Fixed a potential crash in the connection broker</td>
</tr>
<tr>
<td>2006-08-29</td>
<td>12241</td>
<td>REF8631: KClient will never show a separator as the first item in a form's toolbar.</td>
</tr>
<tr>
<td>2006-09-01</td>
<td>12244</td>
<td>REF8636: Potential for installers to hang if denied registry access.</td>
</tr>
<tr>
<td>2006-09-06</td>
<td>12249</td>
<td>ENH: Added CALL KI_COMPFILE/KI_DCOMPFILE to compress/decompress a file directly.</td>
</tr>
<tr>
<td>2006-09-13</td>
<td>12256</td>
<td>REF8648: KI_CREATE of tables with huge index areas could fail.</td>
</tr>
<tr>
<td>2006-09-14</td>
<td>12257</td>
<td>ENH: Setting KCML_DEBUG_HANDLE gives extra LIST DT information for investigating application problems.</td>
</tr>
<tr>
<td>2006-09-18</td>
<td>12261</td>
<td>REF8653: Caseless pattern matching did not always work.</td>
</tr>
<tr>
<td>2006-09-21</td>
<td>12264</td>
<td>REF8656: KI_LOCK_OWNER could fail to report on a lock owned by last partition in $PSTAT.</td>
</tr>
<tr>
<td>2006-09-25</td>
<td>12268</td>
<td>ENH: Dropped the &lt;soapstart&gt; tag from <em>kconf.xml</em> and replaced it with a list of SOAP services. This allows a Connection Manager service to define more than one SOAP interface.</td>
</tr>
<tr>
<td>2006-09-26</td>
<td>12269</td>
<td>REF8660: SOAP client will now return a meaningful error message if it could not connect to the server.</td>
</tr>
<tr>
<td>2006-09-27</td>
<td>12270</td>
<td>REF8663: Kiodbc will now report an expired password to syslog.</td>
</tr>
<tr>
<td>2006-10-05</td>
<td>12278</td>
<td>ENH: Correctly sort access control lists when installing <em>kconf.xml</em></td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The Connection Manager's web server could generate a bad timestamp in the HTTP header.</td>
</tr>
<tr>
<td>2006-10-13</td>
<td>12286</td>
<td>REF7965: Support resizeable forms on Pocket PC devices. This allows the application to make better use of screen real estate when the user shows and hides the soft keyboard or changes the screen orientation.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8662: Fixed a drawing problem on Pocket PC 2005 where a form could overlap the soft buttons at the bottom of the screen.</td>
</tr>
<tr>
<td>2006-10-27</td>
<td>12300</td>
<td>REF8711: Length limited dbedits did not always correctly limit text entry when using the non-Unicode KClient in multibyte character set locales.</td>
</tr>
<tr>
<td>2006-10-30</td>
<td>12303</td>
<td>REF8714: Unable to minimize a text mode application window.</td>
</tr>
<tr>
<td>2006-11-07</td>
<td>12303</td>
<td>REF8729: Fixed a potential grid drawing problem on 120 DPI displays.</td>
</tr>
<tr>
<td>2006-11-13</td>
<td>12317</td>
<td>REF8737: KClient failed to connect through a proxy tunnel that required authentication.</td>
</tr>
<tr>
<td>2006-11-15</td>
<td>12319</td>
<td>REF8745: Allow wider PID column for bkstat -a display.</td>
</tr>
<tr>
<td>2006-11-17</td>
<td>12321</td>
<td>ENH8736: Support IPv6 connectivity in KClient and KCML services on Windows platforms which support it.</td>
</tr>
<tr>
<td>2006-11-22</td>
<td>12326</td>
<td>REF8752: KCML server install program could hang if a service failed to stop.</td>
</tr>
<tr>
<td>2006-11-24</td>
<td>12328</td>
<td>REF8751: Fixed a crash on Windows if KCML is unable to create $PSTAT shared memory.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8749: Fixed compatibility issues with Windows Vista and the KCML installer.</td>
</tr>
<tr>
<td>2006-11-27</td>
<td>12331</td>
<td>ENH8736: Added supprt for IPv6 sockets in the ODBC driver and Connection Manager.</td>
</tr>
<tr>
<td>2006-12-01</td>
<td>12335</td>
<td>REF8657: List boxes did not always show a scrollbar when required.</td>
</tr>
<tr>
<td>2006-12-07</td>
<td>12341</td>
<td>REF8767: Dbedit drop down lists appear in the correct position when the control is not in the primary display.</td>
</tr>
<tr>
<td>2006-12-14</td>
<td>12348</td>
<td>REF8774: If a SOAP method call failed with an O30 error it was not tidying up the return stack so, if enclosed in a loop, a subsequent BREAK would error.</td>
</tr>
<tr>
<td>2006-12-15</td>
<td>12349</td>
<td>REF8777: Workbench function browser didn't display the all the DEFSUB's in a library.</td>
</tr>
<tr>
<td>2007-01-02</td>
<td>13002</td>
<td>REF8788: Bkstat -a/-w will now show full user IDs.</td>
</tr>
<tr>
<td>2007-01-19</td>
<td>13019</td>
<td>ENH: Reduce number of Unix system calls during database I/O.</td>
</tr>
<tr>
<td>2007-01-24</td>
<td>13024</td>
<td>REF8816: On Pocket PC, when restoring Today screen KCML connections from flash confirm before overwriting any which have changed since the backup.</td>
</tr>
<tr>
<td>2007-01-31</td>
<td>13031</td>
<td>REF8825: Under certain circumstances it was possible for a button to receive the 'up' of a press on the spacebar, incorrectly clicking the button. Now require both the 'down' and 'up' of the keypress to click a button.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8827: Fixed a minor grid redraw problem.</td>
</tr>
<tr>
<td>2007-02-01</td>
<td>13032</td>
<td>REF8829: Multi-line text sent to KCML from the client had 0x0D 0x0A line breaks instead of just 0x0D.</td>
</tr>
<tr>
<td>2007-02-05</td>
<td>13036</td>
<td>ENH: Windows versions of KCML now support files &gt; 2Gb.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8833: Extra long user names could cause the the client machine name to be misidentified during login resulting in KCML terminating with exit code 146.</td>
</tr>
<tr>
<td>2007-02-07</td>
<td>13038</td>
<td>ENH8837: Where a server and user name are set on the command line or in a shortcut the appropriate edits in the KClient login dialog are made read-only.</td>
</tr>
<tr>
<td>2007-02-08</td>
<td>13039</td>
<td>REF8834: Default installation directory is now <em>C:\ADP\KCML</em>.</td>
</tr>
<tr>
<td>2007-02-14</td>
<td>13045</td>
<td>REF8844: Allow restricted users to run KServadm with reduced functionality under Windows Vista</td>
</tr>
<tr>
<td>2007-02-16</td>
<td>13047</td>
<td>REF8848: $ALARM used to interrupt a SOAP CREATE was not recoverable in ERROR DO</td>
</tr>
<tr>
<td>2007-02-20</td>
<td>13051</td>
<td>REF8852: The 'Connect as user' option on a KClient desktop connection was broken.</td>
</tr>
<tr>
<td>2007-02-23</td>
<td>13054</td>
<td>REF8857: SOAP servers can now be licensed independently of from foreground sessions.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8858: Fixed a drawing issue under KCML style with nested group boxes when one is hidden.</td>
</tr>
<tr>
<td>2007-02-28</td>
<td>13059</td>
<td>REF8856: Fixed a grid display issue using ShowSelection NoColor when the highlight text color and the cell's background color are similar.</td>
</tr>
<tr>
<td>2007-03-06</td>
<td>13065</td>
<td>ENH: Load <em>kconf.xml</em> etc by using memory mapping.</td>
</tr>
<tr>
<td>2007-03-07</td>
<td>13066</td>
<td>REF8869: ALL("") did not behave like ALL(" ")</td>
</tr>
<tr>
<td>2007-03-08</td>
<td>13067</td>
<td>REF8864: Using the non-Unicode KClient the EditForm() method could occasionally pass the form incorrectly to KForm.</td>
</tr>
<tr>
<td>2007-03-13</td>
<td>13072</td>
<td>REF8881: <em>kwebserv -e mykconf.xml -s myService</em> will now check a service's database catalogue, tablespaces and aliases lists.</td>
</tr>
<tr>
<td>2007-03-21</td>
<td>13080</td>
<td>ENH: Added a page to the Connection Manager that lists the members of a Unix group.</td>
</tr>
<tr>
<td>2007-03-30</td>
<td>13089</td>
<td>REF8899: Work around Unixware bug where shadow password strings are &gt; 13 chars.</td>
</tr>
<tr>
<td>2007-04-04</td>
<td>13094</td>
<td>ENH: Use memory mapped heap on Solaris.</td>
</tr>
<tr>
<td>2007-04-10</td>
<td>13100</td>
<td>REF8902: The default panic directory for KCML was set by the installer to be the temporary directory of the installing user. Now it is under the common application data directory.</td>
</tr>
<tr>
<td>2007-04-13</td>
<td>13103</td>
<td>REF8907: Connection Manager could crash when attempting to authenticate on Solaris.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF7927: Fixed a potential problem identifying KClients connected via Windows Terminal Services.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF8909: Fixed a directory permissions problem with the licence server used by the Net WKCML product.</td>
</tr>
<tr>
<td>2007-04-16</td>
<td>13106</td>
<td>REF8910: Under Windows Vista the machine ID derived for licensing was not consistent with other versions of KCML.</td>
</tr>
<tr>
<td>2007-04-25</td>
<td>13115</td>
<td>ENH8855: Changes to the setup program:
<ul>
<li>Allow users without administrative rights to perform a private install of KClient.</li>
<li>Default installation folder is under 'Program Files' for an all-users install.</li>
<li>Files and directories are installed with sensible default permissions and limited users do not have write access. Instead of upgrading the all-users install, limited users will install their own private copy.</li>
</ul></td>
</tr>
<tr>
<td>2007-04-27</td>
<td>13117</td>
<td>REF8922: The Connection Manager would fail to load a page if its filename contained a '+' character.</td>
</tr>
<tr>
<td>2007-05-08</td>
<td>13123</td>
<td>ENH: Added support for OASIS Web Service Security on outgoing SOAP client messages.</td>
</tr>
<tr>
<td>2007-05-10</td>
<td>13129</td>
<td>REF8931: Large variable display could fail to display a scroll bar.</td>
</tr>
<tr>
<td>2007-05-15</td>
<td>13135</td>
<td>REF8938: Limit the number of SOAP instances with $KCML_SOAP_LIC.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Allow for longer documentation strings in SOAP WSDL</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Speed up panic directory listsing in KservAdm and the Connection Manager.</td>
</tr>
<tr>
<td>2007-05-16</td>
<td>13136</td>
<td>REF8940: The Connection Broker is now shipped in Unix IMAGE files.</td>
</tr>
<tr>
<td>2007-05-18</td>
<td>13138</td>
<td>REF8943: Fixed potential problem recreating library code.</td>
</tr>
<tr>
<td>2007-05-21</td>
<td>13141</td>
<td>REF8944: $OPEN would fail on Windows 95/98/Me</td>
</tr>
<tr>
<td>2007-05-23</td>
<td>13143</td>
<td>ENH: Load <em>lic.txt</em> by using memory mapping.</td>
</tr>
<tr>
<td>2007-06-04</td>
<td>13155</td>
<td>ENH8962: Added ReadOnly property to the Rich Edit control.</td>
</tr>
<tr>
<td>2007-06-05</td>
<td>13156</td>
<td>REF8966: Connection Manager was ignoring a user's PW_NOCHECK flag on AIX.</td>
</tr>
<tr>
<td>2007-06-12</td>
<td>13163</td>
<td>REF8973: Graphs were not correctly redrawn after updating axis labels or legends.</td>
</tr>
<tr>
<td>2007-06-14</td>
<td>13165</td>
<td>REF8979: Fixed bad WSDL format.</td>
</tr>
<tr>
<td>2007-06-19</td>
<td>13170</td>
<td>REF8982: Expired password check for /etc/shadow was a day late.</td>
</tr>
<tr>
<td>2007-07-03</td>
<td>13184</td>
<td>REF8991: Fixed text corruption in dbedits in locales using the Windows input method editor.</td>
</tr>
<tr>
<td>2007-07-10</td>
<td>13191</td>
<td>REF9000: Problems starting KCML connections under Windows Vista</td>
</tr>
<tr>
<td>2007-07-13</td>
<td>13194</td>
<td>REF9008: Setting text-mode text color had no effect unless at least the background color was also set at the same time.</td>
</tr>
<tr>
<td>2007-07-18</td>
<td>13199</td>
<td>REF8751: Direct KCML sessions were unable to create $PSTAT shared memory under Windows Vista.</td>
</tr>
<tr>
<td>2007-07-19</td>
<td>13200</td>
<td>REF9014: 132 column text mode switch did not work if the application was interrupted and re-run without switching back to 80 column mode first.</td>
</tr>
<tr>
<td>2007-07-24</td>
<td>13205</td>
<td>REF9015: Fixed to work under x64 MS Windows.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Enhancements to the Connection Manager's administration pages:
<ul>
<li>Duplicate entries in TERMFILE are now highlighted.</li>
<li>Added a page to display processor load on HPUX11, AIX5, Linux and Windows (XP onwards).</li>
<li>Allow user to specify the range of syslog records to search through.</li>
<li>Allow user to specify the maximum size of the result set when searching a syslog.</li>
<li>Use memory mapping to speed up the parsing of a Unix syslog.</li>
<li>Process info page now shows memory map stats on Linux.</li>
<li>Panic directory listing shows the program name.</li>
</ul></td>
</tr>
<tr>
<td>2007-07-30</td>
<td>13211</td>
<td>ENH9019: Better protection against corrupt entries in KClient's cache.</td>
</tr>
<tr>
<td>2007-07-31</td>
<td>13212</td>
<td>REF9020: Double click events could be unreliable over slow networks when a toolbar is present on the form.</td>
</tr>
<tr>
<td>2007-08-02</td>
<td>13214</td>
<td>REF9022: Maximum $BREAK delay is no longer restricted to +255.<br />
Fixed misleading error messages for P34.1 and P34.2 errors.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9023: PANIC in SOAP method did not terminate KCML</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH9024: Added EnableUserPreferences KClient COM method to allow or deny the user access to KClient's preferences settings.</td>
</tr>
<tr>
<td>2007-08-13</td>
<td>13225</td>
<td>REF8584: A menu item could still be actioned by hot key even when one of its ancestors was disabled.</td>
</tr>
<tr>
<td>2007-08-22</td>
<td>13234</td>
<td>REF9039: Use PAM authentication on AIX5.3 or later.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9036: The <em>kcmlinst</em> script now updates <em>/etc/pam.conf</em> on AIX5.3 with rules for the Connection Manager.</td>
</tr>
<tr>
<td>2007-09-03</td>
<td>13246</td>
<td>ENH: Fixed potential buffer overrun in UTF-8 $UPPER.</td>
</tr>
<tr>
<td>2007-09-06</td>
<td>13249</td>
<td>REF9046: Installer setting incorrect permissions on non English systems.</td>
</tr>
<tr>
<td>2007-09-07</td>
<td>13250</td>
<td>REF9047: The Connection Manager could hang when servicing a request from a simple HTTP client.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Memory allocation errors from REDIM are now recoverable.</td>
</tr>
<tr>
<td>2007-09-12</td>
<td>13255</td>
<td>ENH: The Connection Manager's web server now uses memory mapping to read files.</td>
</tr>
<tr>
<td>2007-09-17</td>
<td>13260</td>
<td>REF9051: When passing contatenated strings into a DEFSUB with a presized string argument, don't ignore the original size.</td>
</tr>
<tr>
<td>2007-09-24</td>
<td>13267</td>
<td>REF9058: Color depth issues displaying Jpeg images on Pocket PCs</td>
</tr>
<tr>
<td>2007-09-25</td>
<td>13268</td>
<td>ENH9056: Added CameraCapture KClient COM method to access the camera on Windows Mobile 5 devices so equipped.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9060: Fix potential KClient crash related to editgroups.</td>
</tr>
<tr>
<td>2007-09-26</td>
<td>13269</td>
<td>REF9061: KClient GPF report in a PANIC file could be truncated.</td>
</tr>
<tr>
<td>2007-10-02</td>
<td>13275</td>
<td>REF9050: Value labels on bar charts could sometimes be clipped.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9052: Pressing the Cancel button on a form after changing the text in an edit failed to restore the edit's text to its previous value.</td>
</tr>
<tr>
<td>2007-10-23</td>
<td>13296</td>
<td>REF9075: More robust detection of KClient in the Connection Manager.</td>
</tr>
<tr>
<td>2007-11-06</td>
<td>13310</td>
<td>REF9080: Report write failures, caused by insufficient disk space, to the system log.</td>
</tr>
<tr>
<td>2007-11-08</td>
<td>13312</td>
<td>ENH: The Connection Manager can now display syslog messages that have been redirected to the AIX error log.</td>
</tr>
<tr>
<td>2007-11-13</td>
<td>13317</td>
<td>REF8216: Potential fix for running out of licences when starting lots of background processes.</td>
</tr>
<tr>
<td>2007-11-22</td>
<td>13326</td>
<td>ENH: Added code-page map tables for Arabic, Greek, Baltic and Cyrillic character sets.</td>
</tr>
<tr>
<td>2007-12-04</td>
<td>13338</td>
<td>REF8013: Changing the image on an expanded tree item had no effect until the node was collapsed.</td>
</tr>
<tr>
<td>2007-12-06</td>
<td>13340</td>
<td>REF8317: When editing a grid cell the text alignment property of the cell is honoured.</td>
</tr>
<tr>
<td>2007-12-11</td>
<td>13345</td>
<td>REF9094: Right-aligned plain text dbedits line up correctly with right-aligned numeric dbedits.</td>
</tr>
<tr>
<td>2008-01-11</td>
<td>14011</td>
<td>REF9107: Connection broker could fail with an unhandled SIGPIPE signal in some circumstances.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9106: KCML SOAP server will now reply with a SOAP error when terminating abnormally.</td>
</tr>
<tr>
<td>2008-01-14</td>
<td>14014</td>
<td>ENH: A KCML SOAP server that is waiting for a request will now have a $PSTAT DEV value of HEX(FA).</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9109: SOAP CREATE failed if the WSDL location is specified using an absolute path under UNIX.</td>
</tr>
<tr>
<td>2008-01-15</td>
<td>14015</td>
<td>REF9112: Could crash when parsing a <em>kconf.xml</em> whose size was an exact multiple of the system's page size.</td>
</tr>
<tr>
<td>2008-01-24</td>
<td>14024</td>
<td>REF9120: If <em>kplicserver -r</em> fails to send a refresh packet to the broadcast address, try sending the packet to localhost instead.</td>
</tr>
<tr>
<td>2008-01-25</td>
<td>14025</td>
<td>ENH9070: Support Transport Layer Security (TLS/SSL) between KClient and KCML.</td>
</tr>
<tr>
<td>2008-01-28</td>
<td>14028</td>
<td>REF9125: Fixed a problem programatically setting a form's width/height after the form had been resized by the user.</td>
</tr>
<tr>
<td>2008-01-30</td>
<td>14030</td>
<td>REF9127: Avoid $PSTAT locks while communicating with the client.</td>
</tr>
<tr>
<td>2008-02-04</td>
<td>14035</td>
<td>REF9129: KClient could sometimes fail to display a GUI prompt when a password had expired.</td>
</tr>
<tr>
<td>2008-02-05</td>
<td>14036</td>
<td>REF9131: The Connection Manager could set a corrupt value of $SERVER_NAME.</td>
</tr>
<tr>
<td>2008-02-08</td>
<td>14039</td>
<td>REF9135: The Remote Licence Daemon prevented the KPrint Editor starting if the licence file had no queues.</td>
</tr>
<tr>
<td>2008-02-13</td>
<td>14044</td>
<td>REF9138: BIN() would return inconsistent results when a number was too large.</td>
</tr>
<tr>
<td>2008-02-28</td>
<td>14059</td>
<td>REF9148: If an existing picture file was overwritten at the server it was possible that the updated image would not be sent to KClient.</td>
</tr>
<tr>
<td>2008-03-03</td>
<td>14063</td>
<td>REF9150: Only create a Unix pseudo-tty in SHELL when bit 8 in byte 37 of $OPTIONS RUN is set.</td>
</tr>
<tr>
<td>2008-03-06</td>
<td>14066</td>
<td>REF9149: Don't parse types schema in literal mode.</td>
</tr>
<tr>
<td>2008-03-27</td>
<td>14087</td>
<td>REF9185: Problem with LIBRARY REMOVE ALL.</td>
</tr>
<tr>
<td>2008-03-28</td>
<td>14088</td>
<td>REF9114: Trim trailing space to object SOAP create URL.</td>
</tr>
<tr>
<td>2008-04-01</td>
<td>14092</td>
<td>REF9188: Very rarely, KCML could crash closing a tree control.</td>
</tr>
<tr>
<td>2008-04-02</td>
<td>14093</td>
<td>REF9189: The setup dialogue for the ODBC driver could be confused by simliar database names.</td>
</tr>
<tr>
<td>2008-04-03</td>
<td>14094</td>
<td>REF9191: Allow $DECLARE on KClient to support the non-standard calling convention used by MS Visual Studio rather the proper WINAPI covention by appending '!' to the function name, e.g. $DECLARE 'CCall()="Module.Function!"</td>
</tr>
<tr>
<td>2008-04-04</td>
<td>14095</td>
<td>REF9192: Ignore PANIC/broadcast message signal when SHELL'ing a child process.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The SOAP server will now set the LastAccess timestamp in $PSTAT when it processes a request.</td>
</tr>
<tr>
<td>2008-04-07</td>
<td>14098</td>
<td>REF9193: Failed to authenticate with PAM on HP-UX 11.11.</td>
</tr>
<tr>
<td>2008-04-15</td>
<td>14106</td>
<td>REF9204: Default fixed-pitch form font was incorrectly set to 'Courier New' for all locales.</td>
</tr>
<tr>
<td>2008-04-17</td>
<td>14108</td>
<td>REF9140: Fixed a grid repaint problem when scrollbars are removed and added in the same event to a grid that has stretched columns.</td>
</tr>
<tr>
<td>2008-04-22</td>
<td>14113</td>
<td>REF9210: Fixed partial licence expiry in kiodbc.</td>
</tr>
<tr>
<td>2008-04-23</td>
<td>14114</td>
<td>REF9215: Fixed case HTTP header token.</td>
</tr>
<tr>
<td>2008-04-30</td>
<td>14121</td>
<td>ENH9220: KClient displays messages such as password expiry warnings received at login in a balloon tooltip in the notification area. These tooltips are only supported in Windows 2000 and better or Pocket PC.</td>
</tr>
<tr>
<td>2008-05-16</td>
<td>14137</td>
<td>REF9235: Fixed a crash if the Ctrl key was held down when moving the mouse wheel with focus inside a dbedit with scroll bars.</td>
</tr>
<tr>
<td>2008-05-28</td>
<td>14149</td>
<td>REF9241: $PRINTF was not expanding \x00.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9232: More support for Web Service Security. Allows interfacing with MS.net SOAP services using WSE 3.0</td>
</tr>
<tr>
<td>2008-05-30</td>
<td>14151</td>
<td>ENH: Added execution profiling timers 'KCMLStartExecTimer() &amp; 'KCMLStopExecTimer().</td>
</tr>
<tr>
<td>2008-06-03</td>
<td>14155</td>
<td>REF9246: PersistFormSize incorrectly remembered the sizes of child forms. Only top level form sizes should be persisted.</td>
</tr>
<tr>
<td>2008-06-06</td>
<td>14158</td>
<td>REF9248: Cached WSDL from a persistent SOAP server could be out of date.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9254: Fixed memory overwrite parsing XML via Expat.</td>
</tr>
<tr>
<td>2008-06-11</td>
<td>14163</td>
<td>REF9258: The 'Connect via' dropdown on the Options page of a desktop KCML connection's properties could be placed incorrectly.</td>
</tr>
<tr>
<td>2008-06-12</td>
<td>14164</td>
<td>REF9259: A blank form title could display garbage text under some circumstances.</td>
</tr>
<tr>
<td>2008-06-25</td>
<td>14177</td>
<td>REF9275: Missing namespace prefix on some SOAP requests.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Global library partitions now show, in $PSTAT, how much memory they have used instead of their maximum size.</td>
</tr>
<tr>
<td>2008-06-30</td>
<td>14182</td>
<td>ENH: Connection Manager now supports CIDR masks in the &lt;validclients&gt; ACL.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Use memory mapped heap on AIX4.3</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9280: Fixed bogus "not compiled for this operating system" error message when installing KCML on some Linux systems.</td>
</tr>
<tr>
<td>2008-07-07</td>
<td>14189</td>
<td>REF9283: Cancelling a form while entering text into a dbedit will not clear the edit's text so long as it has no Validate() event. This allows the cancel to be rejected and editing to continue.</td>
</tr>
<tr>
<td>2008-07-24</td>
<td>14206</td>
<td>REF9299: KClient not honouring text mode printing setting in user preferences.</td>
</tr>
<tr>
<td>2008-07-25</td>
<td>14207</td>
<td>ENH9301: Allow a form to be created invisible and then shown later.</td>
</tr>
<tr>
<td>2008-08-01</td>
<td>14214</td>
<td>REF9312: Fixed a potential crash when scrolling a grid.</td>
</tr>
<tr>
<td>2008-08-04</td>
<td>14217</td>
<td>REF9313: Fixed SOAP transport over HTTP for 'Chunked' encoding.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9231: SOAP client now supports SSL via a basic HTTP proxy.</td>
</tr>
<tr>
<td>2008-08-06</td>
<td>14219</td>
<td>ENH: The Remote Licence Daemon now supports CIDR masks in the &lt;validclients&gt; ACL.</td>
</tr>
<tr>
<td>2008-09-10</td>
<td>14254</td>
<td>REF9348: Increase the maximum number of children per parent node in <em>kconf.xml</em> to 10000.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH9317: If a dbedit has a Type$ that specifies a number of lines and the WrapText property is set then the control will word wrap based on Type$</td>
</tr>
<tr>
<td>2008-09-12</td>
<td>14256</td>
<td>REF9346: Fixed potential crash in dbedit currency conversion code.</td>
</tr>
<tr>
<td>2008-09-15</td>
<td>14259</td>
<td>REF9354: Increased method parameter limit.</td>
</tr>
<tr>
<td>2008-09-16</td>
<td>14260</td>
<td>ENH9337: Added support for AES, DES, MD5 and SHA-1 encryption.</td>
</tr>
<tr>
<td>2008-10-21</td>
<td>14295</td>
<td>ENH9384: In VT220 mode when dynamic screen sizing is not enabled the font will scale to fill the display.</td>
</tr>
<tr>
<td>2008-10-29</td>
<td>14303</td>
<td>REF9398: Fix a potential crash switching between two instances of KClient.</td>
</tr>
<tr>
<td>2008-10-30</td>
<td>14304</td>
<td>REF9365: SOAP client support for HTTP redirect headers.</td>
</tr>
<tr>
<td>2008-11-06</td>
<td>14311</td>
<td>REF9404: Fixed problems minimizing when mixing forms with text windows.</td>
</tr>
<tr>
<td>2008-11-21</td>
<td>14326</td>
<td>ENH: Added ODBC -q -u flags</td>
</tr>
<tr>
<td>2008-11-26</td>
<td>14331</td>
<td>REF9416: $RELEASE fn children were adding to the [KClient] user count</td>
</tr>
<tr>
<td>2008-12-30</td>
<td>14365</td>
<td>ENH: Added KDB6 ROWID checking</td>
</tr>
<tr>
<td>2008-12-30</td>
<td>14365</td>
<td>ENH: Added KDB6 per-file-journal</td>
</tr>
<tr>
<td>2009-01-08</td>
<td>15008</td>
<td>REF9428: Fixed potential infinite loop after COM CLEAR varname or LIBRARY REMOVE.</td>
</tr>
<tr>
<td>2009-01-12</td>
<td>15012</td>
<td>REF9431: Include workload partition (WPAR) key, if available, in the machine ID for AIX6.</td>
</tr>
<tr>
<td>2009-01-21</td>
<td>15021</td>
<td>REF9438: The Connection Manager could consume an excessive amout of processor time if the network failed while a user was authenticating.</td>
</tr>
<tr>
<td>2009-01-27</td>
<td>15027</td>
<td>REF9509: COM CLEAR / LOAD RUN</td>
</tr>
<tr>
<td>2009-02-02</td>
<td>15033</td>
<td>TS_PD/9515: Allow applications to start SSL on an existing plain socket.</td>
</tr>
<tr>
<td>2009-02-09</td>
<td>15040</td>
<td>REF9519: Problem editing CVS conflicts in the workbench.</td>
</tr>
<tr>
<td>2009-02-12</td>
<td>15043</td>
<td>TS_DB/9525: The Connection Manager could fail to authenticate when using a combination of KClient's "Application Command Line" option and a fully qualified hostname.</td>
</tr>
<tr>
<td>2009-02-18</td>
<td>15049</td>
<td>REF9530: Pressing the delete key in a dbedit with a description could sometimes remove two characters.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9533: Some arithmetic operations with very large (&gt;=13 digits) could produce a rounding error in the least significant digit. On AIX only.</td>
</tr>
<tr>
<td>2009-02-19</td>
<td>15050</td>
<td>REF9528: Fixed workbench cursor problem with very long lines.</td>
</tr>
<tr>
<td>2009-02-26</td>
<td>15057</td>
<td>REF6830, 9537: Fixed crash with autoedit and datafield$ set on grid.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Improved tooltipping of objects representing items on form controls such as listbox items, tree items and tab pages.</td>
</tr>
<tr>
<td>2009-02-27</td>
<td>15058</td>
<td>REF9538: Produce workaround for applications that close forms in the Idle event to suppress all subsequent events on the form exceot for the Exit event. This allows for the fact that the form is still active during an Idle event and so user activity can raise events.</td>
</tr>
<tr>
<td>2009-03-02</td>
<td>15061</td>
<td>REF9541: Stripping the xml prefix twice from SOAP server arguments.</td>
</tr>
<tr>
<td>2009-03-16</td>
<td>15075</td>
<td>REF9550: More robust handling of corrupt/invalid icons in KClient.</td>
</tr>
<tr>
<td>2009-03-20</td>
<td>15079</td>
<td>TS_PD/9517: SOAP Server chunked transfer encoding support</td>
</tr>
<tr>
<td>2009-03-26</td>
<td>15085</td>
<td>REF9554: Fixed the install script to create suitable PAM configuration files for RedHat ES5.</td>
</tr>
<tr>
<td>2009-03-30</td>
<td>15089</td>
<td>REF9560: Fixed a login problem when using escaped characters in a Bookmark string.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9561: Fixed a problem printing Thai characters from KClient</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9521: Rendering Thai text incorrectly when using a fixed-pitch font.</td>
</tr>
<tr>
<td>2009-04-03</td>
<td>15093</td>
<td>REF9566: Set LD_LIBRARY_PATH in the xinetd.d configuration files so that we always load the correct shared libraries.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Fixed the install script to create suitable PAM configuration files for SuSE &amp; Ubuntu.</td>
</tr>
<tr>
<td>2009-04-08</td>
<td>15098</td>
<td>REF9568: Fixed a KClient crash where a form that was terminated in its Enter() event was replaced by a text window. The crash would occur after repeating this process twice.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Better checks for corrupt KDB7 tables</td>
</tr>
<tr>
<td>2009-04-09</td>
<td>15099</td>
<td>ENH9391: SOAP client supports decoding of gzip/deflate encoded bodies.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>TS_DB/9571: Fixed crash in workbench search.</td>
</tr>
<tr>
<td>2009-04-28</td>
<td>15118</td>
<td>ENH: SOAP server supports gzip/deflate encoding of responses.</td>
</tr>
<tr>
<td>2009-04-29</td>
<td>15119</td>
<td>REF9585: Fixed crash in $PRINTF</td>
</tr>
<tr>
<td>2009-04-30</td>
<td>15120</td>
<td>ENH9526: Form tooltips now work under Wine</td>
</tr>
<tr>
<td>2009-05-01</td>
<td>15121</td>
<td>REF9587: Fixed potential grid crash in auto-edit cells with drop down lists.</td>
</tr>
<tr>
<td>2009-05-07</td>
<td>15127</td>
<td>REF9592: $LOGNAME was not correct for SOAP servers on AIX.</td>
</tr>
<tr>
<td>2009-05-08</td>
<td>15128</td>
<td>REF9596: Fixed HTTP 1.0 support in SOAP server.</td>
</tr>
<tr>
<td>2009-05-14</td>
<td>15134</td>
<td>REF9607: Fixed poor performance on SSL connections.</td>
</tr>
<tr>
<td>2009-05-15</td>
<td>15135</td>
<td>REF9608: Could sometimes fail to action a double click event when connected by a slow link such as dial-up or a VPN.</td>
</tr>
<tr>
<td>2009-05-18</td>
<td>15138</td>
<td>REF9610: Support OCX expressions such as oControl.ocxprop1.ocxprop2 as well as form.control.ocxprop1.ocxprop2</td>
</tr>
<tr>
<td>2009-05-26</td>
<td>15146</td>
<td>REF9521: Rendering Thai text incorrectly when using a fixed-pitch font.</td>
</tr>
<tr>
<td>2009-06-04</td>
<td>15155</td>
<td>REF9644: XML_CLOSE did not close the handle if XML_NEXT had not been called.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9640: The AddEvent method can be used on tab pages.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9642: Fixed race condition when utilities access $PSTAT.</td>
</tr>
<tr>
<td>2009-06-05</td>
<td>15156</td>
<td>REF9648: An event raised by an OCX when the form is in a terminating mode is now ignored.</td>
</tr>
<tr>
<td>2009-06-08</td>
<td>15159</td>
<td>REF9647: When shelling out to a VT100 text mode application the num-pad enter key did not work.</td>
</tr>
<tr>
<td>2009-06-12</td>
<td>15163</td>
<td>REF9110: Defer sending RowRequests from a grid on a form that is busy.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH9612: Grid right-click copy to clipboard feature will first fill the grid if DataPending is set.</td>
</tr>
<tr>
<td>2009-06-17</td>
<td>15168</td>
<td>REF9652: A secure network connection could be dropped when a KCML process received a signal.</td>
</tr>
<tr>
<td>2009-06-19</td>
<td>15170</td>
<td>REF9654: $ERR could truncate long error messages.</td>
</tr>
<tr>
<td>2009-07-10</td>
<td>15191</td>
<td>REF9669: Secure socket reads could fail under Windows.</td>
</tr>
<tr>
<td>2009-07-17</td>
<td>15198</td>
<td>REF9673: Use CP*.map tables to convert strings passed to/from Xerces when in codepage mode.</td>
</tr>
<tr>
<td>2009-08-03</td>
<td>15215</td>
<td>REF9679: Parse the config file when requesting a WSDL.</td>
</tr>
<tr>
<td>2009-08-04</td>
<td>15216</td>
<td>REF7686: Fixed running bkstat from the pseudo-tty shell, also support interrupt, suspend and EOF control keys.</td>
</tr>
<tr>
<td>2009-08-24</td>
<td>15236</td>
<td>REF9691: Problem displaying controls in an editgroup association chain if the first group in the chain was empty.</td>
</tr>
<tr>
<td>2009-10-8</td>
<td>15281</td>
<td>REF9519: Support TOCONN/TOREAD for SOAP objects.</td>
</tr>
<tr>
<td>2009-10-13</td>
<td>15286</td>
<td>ENH9740: Added KClient $DECLARE KCMLEnableGridCopy(INT()) to disable grid copy to clipboard feature</td>
</tr>
<tr>
<td>2009-10-19</td>
<td>15292</td>
<td>REF9732: ODBC could only use IFNULL( in single column SELECT</td>
</tr>
<tr>
<td>2009-10-21</td>
<td>15294</td>
<td>REF9737: Problem breaking into code during a $DECLARE</td>
</tr>
<tr>
<td>2009-11-02</td>
<td>15306</td>
<td>REF9767: Fixed problem extending KDB type 6 tables beyond 4Gb.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9764: Fixed hang in the SOAP client.</td>
</tr>
<tr>
<td>2009-11-16</td>
<td>15320</td>
<td>REF9762: Broadcast message corrupting workbench lines.</td>
</tr>
<tr>
<td>2009-11-30</td>
<td>15334</td>
<td>REF9802: Connection Manager no longer downloads text files as HTML.</td>
</tr>
<tr>
<td>2009-12-23</td>
<td>15357</td>
<td>ENH: Enable secure SSL/TLS sockets on legacy systems.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9823: Seed OpenSSL's random number generator on legacy systems.</td>
</tr>
<tr>
<td>2009-12-24</td>
<td>15358</td>
<td>REF9826: Fixed a problem where a trap on a variable with a conditional test could crash when executing.</td>
</tr>
<tr>
<td>2010-01-12</td>
<td>16012</td>
<td>REF9832: $HELP path was limited to 95 characters.</td>
</tr>
<tr>
<td>2010-01-13</td>
<td>16013</td>
<td>REF9834: Fixed SSL connections under Windows. Could supply wrong credentials.</td>
</tr>
<tr>
<td>2010-01-20</td>
<td>16020</td>
<td>REF9844: Fixed problem loading SSL libraries on OpenSuSE Linux.</td>
</tr>
<tr>
<td>2010-02-03</td>
<td>16034</td>
<td>REF9859: Expand the login 'new password' dialog if there is a large amount of descriptive text.</td>
</tr>
<tr>
<td>2010-02-09</td>
<td>16040</td>
<td>REF9854: KI_DF &amp; KI_STATFS now supports file systems upto 4TB.</td>
</tr>
<tr>
<td>2010-02-15</td>
<td>16046</td>
<td>REF9869: Keyboard acceleration and tabbing through a form could sometimes not work correctly after a toolbar has been shown.</td>
</tr>
<tr>
<td>2010-03-09</td>
<td>16068</td>
<td>REF9890: Support changing a toolbar image after the toolbar has been shown.</td>
</tr>
<tr>
<td>2010-03-10</td>
<td>16069</td>
<td>ENH9892: Make tabbing in a form skip any read-only controls.</td>
</tr>
<tr>
<td>2010-03-12</td>
<td>16071</td>
<td>REF9896: Incorrect text in error messages from kservadm.exe.</td>
</tr>
<tr>
<td>2010-03-17</td>
<td>16076</td>
<td>REF9551: If a dbedit has both a Type$ with a non-zero scale and WrapText set show a vertical scroll bar.</td>
</tr>
<tr>
<td>2010-03-31</td>
<td>16090</td>
<td>REF9910: Fixed KClient crash printing large amounts of text to the clipboard.</td>
</tr>
<tr>
<td>2010-04-09</td>
<td>16099</td>
<td>ENH: Retrofit of Chinese DBCS word parsing logic from KCML 6.90.</td>
</tr>
<tr>
<td>2010-05-04</td>
<td>16124</td>
<td>REF9937: Fixed SIG_PIPE errors not being trapped on Linux (could lead to program termination).</td>
</tr>
<tr>
<td>2010-05-27</td>
<td>16147</td>
<td>REF9961: Fixed a potential problem where a parent form could send an event to the KCML of a child form running in a $RELEASE'd partition.</td>
</tr>
<tr>
<td>2010-06-09</td>
<td>16160</td>
<td>ENH: Retrofit of DBCS_WORD_LEN env var to enable Chinese Word search. Fix for problem with Chinese WS failing in KI_WS_READ. Include runs of digits before and after DBCS strings as candidates for inclusion in the string.</td>
</tr>
<tr>
<td>2010-06-25</td>
<td>16176</td>
<td>REF9974: Fixed hang making SOAP client calls over SSL connections.</td>
</tr>
<tr>
<td>2010-06-28</td>
<td>16179</td>
<td>REF9981: Clicking the web link in KClient's 'About' dialog could open many web browser tabs.</td>
</tr>
<tr>
<td>2010-07-16</td>
<td>16197</td>
<td>REF9995: kwebserv -i did not set umask from $UMASK environment variable.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9996: Install script for kplicserver could get the filename of the boot script wrong on RedHat ES 5.4</td>
</tr>
<tr>
<td>2010-07-19</td>
<td>16200</td>
<td>REF9998: Fixed spurious X79.23 error when starting kcml for the first time.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF9999: Fixed a redraw problem when setting the text or changing pages of a groupbox style tab control.</td>
</tr>
<tr>
<td>2010-07-22</td>
<td>16203</td>
<td>REF9982: Fixed race condition in SHELL which could lead to a hang.</td>
</tr>
<tr>
<td>2010-07-26</td>
<td>16207</td>
<td>REF10008: Installing KCML into a new directory could overwrite <em>.kcmlLogin</em> files.</td>
</tr>
<tr>
<td>2010-08-04</td>
<td>16216</td>
<td>REF10017: Fixed SOAP server memory leak.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Added -z option to AIX5.2 version of kwebserv to add <em>/opt/freeware/lib</em> to $LIBPATH and the re-exec itself so that it <strong>inherits</strong> the correct value of the environment variable. Required when using secure KClient connections on AIX5.3 with OpenSSL 0.9.7 &amp; 0.9.8 installed.</td>
</tr>
<tr>
<td>2010-08-10</td>
<td>16222</td>
<td>REF10021: Fixed a focus problem when a form is a child of an invisible form.</td>
</tr>
<tr>
<td>2010-08-17</td>
<td>16229</td>
<td>REF10026: SOAP server could return incorrect namespace.</td>
</tr>
<tr>
<td>2010-08-23</td>
<td>16235</td>
<td>REF10031: Register kplicserver's boot script with yast on OpenSuSE 11.</td>
</tr>
<tr>
<td>2010-09-01</td>
<td>16244</td>
<td>REF10020: Changing a dbedit's Type$ property did not redraw the control.</td>
</tr>
<tr>
<td>2010-09-10</td>
<td>16253</td>
<td>REF10058: Do not add symbolic link for a start script to <em>/etc/rc6.d</em>.</td>
</tr>
<tr>
<td>2010-09-14</td>
<td>16257</td>
<td>REF10059: If a graph had a slow Click event a double click could be lost.</td>
</tr>
<tr>
<td>2010-09-23</td>
<td>16266</td>
<td>REF10066: KClient resource leak when hiding a popup menu.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF10086: Fixed a potential connection problem when using $RELEASE on an encrypted connection.</td>
</tr>
<tr>
<td>2010-11-10</td>
<td>16314</td>
<td>REF10102: Children of $RELEASE could have an incorrect value of the $PSTAT 'P' column.</td>
</tr>
<tr>
<td>2010-11-16</td>
<td>16320</td>
<td>REF10091: Support MS .Net 4 WS-Security for SOAP client.</td>
</tr>
<tr>
<td>2010-11-19</td>
<td>16323</td>
<td>REF10113: Fixed HTTP redirects.</td>
</tr>
<tr>
<td>2010-11-26</td>
<td>16330</td>
<td>REF10121: Fixed HTTP redirects.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF10120: kiodbc could incorrectly return a NULL column when using WHERE clause.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF10123: Register kplicserver's boot script using <em>update-rc.d</em> on Debian.</td>
</tr>
<tr>
<td>2010-12-22</td>
<td>16349</td>
<td>REF10132: Allow a NUMERIC scale of up to 7 (rather than 6) in SQL CREATE TABLE statements. Fixes an ODBC issue with preexisting tables that expect 7 digits.</td>
</tr>
<tr>
<td>2010-12-23</td>
<td>16357</td>
<td>REF10134: The domain and the computer name are used to uniquely identify the machine to the kiodbc licensing, but some logins such as the SYSTEM account were not identifying the normal domain name.</td>
</tr>
<tr>
<td>2011-01-24</td>
<td>17024</td>
<td>Miscellaneous licencing fixes.</td>
</tr>
<tr>
<td>2011-01-25</td>
<td>17025</td>
<td>REF10147: Added ability to set cookies for the SOAP client object.</td>
</tr>
<tr>
<td>2011-01-27</td>
<td>17027</td>
<td>REF10153: Generate a UUID for the WS-Addressing message id.</td>
</tr>
<tr>
<td>2011-02-08</td>
<td>17039</td>
<td>REF10168: SHELL command could occasionally hang on AIX.</td>
</tr>
<tr>
<td>2011-02-15</td>
<td>17046</td>
<td>REF10178: Could not view database table information from the Connection Manager.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF10176: Allow custom HTTP headers to be added to SOAP request.</td>
</tr>
<tr>
<td>2011-02-25</td>
<td>17056</td>
<td>REF10183: ODBC could fail to load column information on large database tables.</td>
</tr>
<tr>
<td>2011-02-28</td>
<td>17059</td>
<td>REF10184: Fixed a problem where in certain cases a KI_WS_READ on AIX systems only could take a very long time.</td>
</tr>
<tr>
<td>2011-03-16</td>
<td>17075</td>
<td>REF10199: Fixed crash in SOAP Security XML parser.</td>
</tr>
<tr>
<td>2011-03-22</td>
<td>17081</td>
<td>REF10201: On Windows Mobile devices after clicking on the scroll bar of a large dbedit dropdown list clicking away from the list did not dismiss it.</td>
</tr>
<tr>
<td>2011-03-24</td>
<td>17083</td>
<td>REF9824, 10080: Escape XML entities when updating <em>kconf.xml</em></td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF10207: Extra sanity checks when attempting to load a malformed icon.</td>
</tr>
<tr>
<td>2011-03-25</td>
<td>17084</td>
<td>ENH10192: Allow KClient alternative currency mode to be set via SetAltCurrencyMode client COM method.</td>
</tr>
<tr>
<td>2011-03-28</td>
<td>17087</td>
<td>REF10213: Files &amp; directories on Windows are now created with a valid ACL.</td>
</tr>
<tr>
<td>2011-04-07</td>
<td>17097</td>
<td>REF10222: The Windows Mobile version of KClient can display 32 bit per pixel icons although it does not support the alpha channel.</td>
</tr>
<tr>
<td>2011-04-12</td>
<td>17102</td>
<td>REF10224: If currency enabled dbedits were present only on a tab page not yet visible the form would not enable alternative currency mode until the tab page was shown.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Connection Manager can now show processor load on Solaris.</td>
</tr>
<tr>
<td>2011-05-04</td>
<td>17124</td>
<td>REF10239: Dragging a grid control's scroll bar thumb didn't work when there were more than 65536 rows.</td>
</tr>
<tr>
<td>2011-05-12</td>
<td>17132</td>
<td>ENH: Compatibility fixes Ubuntu 11.
<ul>
<li>Install script would produce a warning when it restarted xinetd</li>
<li>Server-side $DECLAREs of C-runtime APIs would fail</li>
</ul></td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: The kcmlinst script was not configuring <em>/etc/pam.conf</em> when installing KCML compiled for AIX5.3.</td>
</tr>
<tr>
<td>2011-05-16</td>
<td>17136</td>
<td>REF10246: A KCML lic.txt containing a DEALER section with users=14 will no longer permit access to the workbench unless the KClient has a correct client support licence.</td>
</tr>
<tr>
<td>2011-06-06</td>
<td>17157</td>
<td>ENH: Added support for Vietnamese code page 1258.</td>
</tr>
<tr>
<td>2011-06-13</td>
<td>17164</td>
<td>REF10233: KClient uses Windows default permissions when creating registry keys.</td>
</tr>
<tr>
<td>2011-06-17</td>
<td>17168</td>
<td>REF10245: Clear dead partitions when kcml starts.</td>
</tr>
<tr>
<td>2011-06-23</td>
<td>17174</td>
<td>REF9328: Fixed obscure and very rare crash doing a form operation.</td>
</tr>
<tr>
<td>2011-06-30</td>
<td>17181</td>
<td>REF10268: On Linux only some CONVERT conversions of very large (&gt;=14) digit numbers to strings could be 1 out.</td>
</tr>
<tr>
<td>2011-07-05</td>
<td>17185</td>
<td>REF10270: Some arithmetic operations with very large (&gt;=13 digits) could produce a rounding error in the least significant digit. On HP and SUN machines only.</td>
</tr>
<tr>
<td>2011-07-15</td>
<td>17196</td>
<td>REF10276: Fixed SOAP canonicalization.</td>
</tr>
<tr>
<td>2011-07-15</td>
<td>17196</td>
<td>REF10281: Fixed long HTTP header lines in the SOAP client.</td>
</tr>
<tr>
<td>2011-07-15</td>
<td>17196</td>
<td>REF10162: Support 2000 SOAP security spec.</td>
</tr>
<tr>
<td>2011-08-10</td>
<td>17222</td>
<td>REF10273:Fixed .Duplicate() of a dataaware controls.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>REF10309:Fixed a rare P34 error involving a complicated sequence of events involving a specific form using $RELEASE and minimizing and restoring a form.</td>
</tr>
<tr>
<td>2011-08-15</td>
<td>17227</td>
<td>REF10306: Fixed a hanging problem when a session $RELEASEd and then the child $RELEASEd again when using SSL encryption.</td>
</tr>
<tr>
<td>2011-08-19</td>
<td>17231</td>
<td>REF10095: In a $RELEASE child ignore any properties belonging to a form in the parent KCML.</td>
</tr>
<tr>
<td>2011-08-22</td>
<td>17234</td>
<td>REF10300: Improve SOAP client support for wsdl:import.</td>
</tr>
<tr>
<td>2011-09-05</td>
<td>17248</td>
<td>REF10330: Fixed workbench hang on HPUX-11.</td>
</tr>
<tr>
<td>2011-09-07</td>
<td>17250</td>
<td>REF10329: Fixed problem with KI_EXTEND and data greater than 4GB.</td>
</tr>
<tr>
<td>2011-09-07</td>
<td>17250</td>
<td>REF10315: Fixed problem calling WINDOW OPEN in background process.</td>
</tr>
<tr>
<td>2011-09-23</td>
<td>17266</td>
<td>REF10350: Connection Manager did not cope with space characters in a URL for a SOAP server.</td>
</tr>
<tr>
<td>2011-09-27</td>
<td>17270</td>
<td>REF10355: Fixed a crash in PRINTUSING with Arabic text.</td>
</tr>
<tr>
<td>2011-09-30</td>
<td>17273</td>
<td>REF10267: <em>superkill</em> &amp; <em>bkstat</em> had theorectical chance of signalling a recycled process ID.</td>
</tr>
<tr>
<td>2011-11-11</td>
<td>17314</td>
<td>TS_DB/10373: return identical results instead of NULL based on two logically identical SQL statement.</td>
</tr>
<tr>
<td>2011-11-11</td>
<td>17314</td>
<td>TS_DB/10372: Allow display on SQL statement of SELECT an integer AS, when none value is selected.</td>
</tr>
<tr>
<td>2011-11-29</td>
<td>17333</td>
<td>TS_DB/10392: Added SOAP MTOM support.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>TS_DB/10266: Added SOAP tracing support.</td>
</tr>
<tr>
<td>2011-12-12</td>
<td>17346</td>
<td>TS_DB/10444: Broken PROXY support in fix for TS_DB/10392.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>TS_DB/10308: Fixed endpoint generation for SOAP servers.</td>
</tr>
<tr>
<td>2012-01-06</td>
<td>18006</td>
<td>TS_DB/10447: Fixed sql utility running SELECT using LEFT OUTER JOIN</td>
</tr>
<tr>
<td>2012-01-09</td>
<td>18009</td>
<td>Fixed sql utility running SELECT using BETWEEN AND on date type check</td>
</tr>
<tr>
<td>2012-01-16</td>
<td>18016</td>
<td>ENH: Install the KCML 7.04 Connection Manager &amp; broker for the Linux 2.6, AIX5.3 &amp; Solaris 10 versions of KCML 6.20.<br />
<strong>Note:</strong> Will require <em>session</em> to be added to the PAM configuration on Linux &amp; AIX.<br />
See: <strong>PAM Authentication</strong> in the KCML 7 Reference Manual.</td>
</tr>
<tr>
<td>2012-01-31</td>
<td>18031</td>
<td>TS_DB/10462: Add checking UNION ALL of sub queries in Optimisation, set the biggest packlen as heading column</td>
</tr>
<tr>
<td>2012-02-02</td>
<td>18033</td>
<td>TS_DB/10477: Fixed handle leak in REMOVE DIR.</td>
</tr>
<tr>
<td>2012-2-10</td>
<td>18041</td>
<td>Fixed TS_DB/10479, KI_WRITE could insert key incorrectly.</td>
</tr>
<tr>
<td>2012-2-14</td>
<td>18045</td>
<td>Fixed TS_DB/10486, Allow SOAP reconnects without error.</td>
</tr>
<tr>
<td>2012-2-20</td>
<td>18051</td>
<td>Fixed TS_DB/10489, Fixed support for KSSL_PASSWD enviroment variable. Used when opening PEM certificates.</td>
</tr>
<tr>
<td>2012-2-24</td>
<td>18055</td>
<td>TS_DB/10484. On input to the Korean IME if entering characters such that the last one may not be fully composed, then the string may not be stored correctly in the Validate event if clicking rather than tabbing onto another control.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>TS_DB/10476: On Korean IME not always switching to correct input mode when tabbing between controls.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>TS_DB/10427: On Japanese IME not always switching to correct input mode when tabbing between controls. input control.</td>
</tr>
<tr>
<td>2012-03-09</td>
<td>18069</td>
<td>TS_DB/10462 extenstion issue: Fixed corrupt output for query statement using "SELECT '121312' AS" with UNION ALL</td>
</tr>
<tr>
<td>2012-03-13</td>
<td>18073</td>
<td>TS_DB/10501: On AIX only, when using the kar to provide a single bundle for libraries, the bundle was being reloaded on a $RELEASE. If the bundle had been rebuilt since KCML had started then it could be out of sync. with the loaded libraries and cause a crash.</td>
</tr>
<tr>
<td>2012-03-26</td>
<td>18087</td>
<td>TS_DB/10513: Fixed SOAP Server Document/Literal request handling.</td>
</tr>
<tr>
<td>2012-04-13</td>
<td>18104</td>
<td>TS_DB/10521: Fixed a hang issue when conenct to a KClient 6.20 with build &lt; 16327 in the case where a form with an idle event that did a flush and the idle event processed whilst KClient was not application in focus.</td>
</tr>
<tr>
<td>2012-04-23</td>
<td>18114</td>
<td>TS_DB/10535: RTF Print/PrintStatus and form Idle could cause a hang.</td>
</tr>
<tr>
<td>2012-04-27</td>
<td>18118</td>
<td>TS_DB/10481: Fixed expired password support in the HP-UX 11 version of the Connection Manager.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>TS_DB/10540: SOAP server is now compatibale with KCML 7.04 Connection Manager.</td>
</tr>
<tr>
<td>2012-04-23</td>
<td>18137</td>
<td>TS_DB/10559: Fixed object error that could occur after setting traps in workbench.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>TS_DB/10549: Fixed field/record error that could occur after setting traps in workbench.</td>
</tr>
<tr>
<td>2012-06-06</td>
<td>18158</td>
<td>TS_DB/10530: Enhancement to remove local symbols from symbol space when KCML_CLEAR_LOCALS environment variable is set.</td>
</tr>
<tr>
<td>2012-06-08</td>
<td>18160</td>
<td>TS_DB/10459: Added 'KCML_Lic_Acquire() &amp; 'KCML_Lic_Release()</td>
</tr>
<tr>
<td>2012-07-09</td>
<td>18191</td>
<td>TS_DB/10591: Background processes could attempt to renegotiate SSL after $RELEASE.</td>
</tr>
<tr>
<td>2012-07-23</td>
<td>18205</td>
<td>REF10604: Use an inherited ACL when creating directories on Windows.</td>
</tr>
<tr>
<td>2012-08-14</td>
<td>18227</td>
<td>TS_DB/10609: The codepage used for converting UTF-8 to Hungarian in $UNPACK was incorrect.</td>
</tr>
<tr>
<td>2012-08-16</td>
<td>18229</td>
<td>TS_DB/10627: Incorrect undimmed variable warnings.</td>
</tr>
<tr>
<td>2012-08-20</td>
<td>18233</td>
<td>TS_DB/10611: Fixed KCML crash using KCML_CLEAR_LOCALS</td>
</tr>
<tr>
<td>2012-09-04</td>
<td>18248</td>
<td>TS_DB/10635: Fixed KCML crash using KCML_CLEAR_LOCALS</td>
</tr>
<tr>
<td>2012-10-19</td>
<td>18293</td>
<td>TS_PD/9522: Add new support roles of ADPOSLOW, ADPOSHIGH, DISTLOW and DISTHIGH.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>TS_DB/10665: Improved DBCS support in forms.</td>
</tr>
<tr>
<td>2012-10-26</td>
<td>18300</td>
<td>TS_DB/10664: Fixed a crash when clicking on empty graphs.</td>
</tr>
<tr>
<td>2012-11-21</td>
<td>18326</td>
<td>TS_DB/10696: Create an <em>/etc/inittab</em> entry with a <strong>start</strong> parameter to <em>kplicserver's</em> boot script on AIX.</td>
</tr>
<tr>
<td>2012-11-29</td>
<td>18334</td>
<td>TS_DB/10697: Fix memory leak after child of $RELEASE had terminated when using an SSL connection.</td>
</tr>
<tr>
<td>2012-12-12</td>
<td>18347</td>
<td>TS_DB/10661: <em>kcmlinst</em> could attempt to set permissions on files that may not exist.</td>
</tr>
<tr>
<td>2013-01-22</td>
<td>19022</td>
<td>TS_DB/10741: Detect ethernet devices on Fedora Core 16+.</td>
</tr>
<tr>
<td>2013-02-15</td>
<td>19046</td>
<td>TS_DB/10759: bkstat -S did not show the state of the krecover semaphore when $KLOGKEY was set.</td>
</tr>
<tr>
<td>2013-02-19</td>
<td>19050</td>
<td>TS_DB/10771: Fixed a crash in printing when converting Arabic text.</td>
</tr>
<tr>
<td>2013-02-27</td>
<td>19058</td>
<td>TS_DB/10773: Server-side fix for a hang when using Telephony integration where a child form has an idle event and the parent form produces Telephony events.</td>
</tr>
<tr>
<td>2013-03-07</td>
<td>19066</td>
<td>TS_DB/10283: Support KCML_SOAP_LIC=0.</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>ENH: Install the KCML 7.05 Connection Manager &amp; broker for the Linux 2.6, AIX5.3 &amp; Solaris 10 versions of KCML 6.20.<br />
<strong>Note:</strong> Will require <em>session</em> to be added to the PAM configuration on Linux &amp; AIX.<br />
See: <strong>PAM Authentication</strong> in the KCML 7 Reference Manual.</td>
</tr>
<tr>
<td>2013-03-13</td>
<td>19072</td>
<td>TS_DB/10797: $DEVICE LPD option now supports a filename value.</td>
</tr>
<tr>
<td>2013-03-14</td>
<td>19073</td>
<td>TS_DB/10789: Fixed a small KClient memory leak when calling Form.Flush() if there is a grid control on a tab page that has not been displayed yet.</td>
</tr>
<tr>
<td>2013-03-21</td>
<td>19080</td>
<td>TS_DB/10814: A centred form does not straddle two displays on a multiple monitor system.</td>
</tr>
<tr>
<td>2013-04-08</td>
<td>19098</td>
<td>TS_DB/10821: SUM would throw an error when executed by kiodbc.</td>
</tr>
<tr>
<td>2013-04-09</td>
<td>19099</td>
<td>TS_PD/9534: Strip white space from a base64 string before decoding.</td>
</tr>
<tr>
<td>2013-04-10</td>
<td>19100</td>
<td>TS_DB/10824: $DEVICE did not strip option from "file.txt,ALF=N"</td>
</tr>
<tr>
<td>2013-05-22</td>
<td>19142</td>
<td>TS_DB/10856: Fixed index corruption using KI_DELETE with type 6 tables.</td>
</tr>
<tr>
<td>2013-05-23</td>
<td>19143</td>
<td>TS_DB/10869: Fixed a potential hang if many dbedit SelChange events are sent at the same time a child form is opened.</td>
</tr>
<tr>
<td>2013-05-24</td>
<td>19144</td>
<td>TS_DB/10690: Added support for extended $DECLARE syntax.</td>
</tr>
<tr>
<td>2013-06-27</td>
<td>19178</td>
<td>TS_DB/10482: ODBC could fail to send a large result set.</td>
</tr>
<tr>
<td>2013-07-15</td>
<td>19196</td>
<td>ENH: Windows versions of KCML now use OpenSSL 1.0</td>
</tr>
<tr>
<td>2013-07-25</td>
<td>19206</td>
<td>TS_DB/10889: $UNPACK could crash when decoding a large base-64 encoded string.</td>
</tr>
<tr>
<td>2013-07-26</td>
<td>19207</td>
<td>TS_DB/10921: LINPUT LINE could go into an infinite loop when reaching EOF.</td>
</tr>
<tr>
<td>2013-07-30</td>
<td>19211</td>
<td>TS_DB/10925: Fixed MIME handling in SOAP object.</td>
</tr>
<tr>
<td>2013-08-05</td>
<td>19217</td>
<td>TS_DB/10929 &amp; TS_DB/10931: Fixed the KCML 6.20 Connection Manager to be compatible with the KCML 7 ODBC driver.</td>
</tr>
<tr>
<td>2013-08-14</td>
<td>19226</td>
<td>TS_DB/10941: Added a new .Encoding$ property to the soap object to override the Content-Types/charset header.</td>
</tr>
<tr>
<td>2013-08-23</td>
<td>19235</td>
<td>ENH: Install the KCML 7.06 Connection Manager &amp; broker for the Linux 2.6, AIX5.3 &amp; Solaris 10 versions of KCML 6.20.<br />
<strong>Note:</strong> Will require <em>session</em> to be added to the PAM configuration on Linux &amp; AIX.<br />
See: <strong>PAM Authentication</strong> in the KCML 7 Reference Manual.</td>
</tr>
<tr>
<td>2013-11-15</td>
<td>19319</td>
<td>TS_DB/11037: 'KCMLObjectGetHeader("SOAP") could return invalid strings.</td>
</tr>
<tr>
<td>2013-11-20</td>
<td>19324</td>
<td>TS_DB/11045: $RELEASE could hang on Solaris &amp; HP-UX 11</td>
</tr>
<tr>
<td>2014-03-28</td>
<td>20087</td>
<td>TS_US/178: Added server-side 'KCML_Build_GetInfo() $DECLARE which returns compilation information about KCML.</td>
</tr>
<tr>
<td>2014-04-02</td>
<td>20092</td>
<td>TS_US/178: Added server-side 'KCML_File_Stat() $DECLARE which returns information about the given file.</td>
</tr>
<tr>
<td>2014-04-16</td>
<td>20106</td>
<td>TS_DB/11295: Fixed race condition in KI_WS_REWRITE</td>
</tr>
<tr>
<td> </td>
<td> </td>
<td>TS_US/216: Added server-side 'KCML_Lic_Count() $DECLARE which returns the number of application licences in use.</td>
</tr>
<tr>
<td>2014-04-22</td>
<td>20112</td>
<td>TS_DB/11306: Sorting the Connection Manager's partition table by user ID could crash.</td>
</tr>
<tr>
<td>2014-05-06</td>
<td>20126</td>
<td>TS_DB/11349: Add guard pages to protect $PSTAT.</td>
</tr>
<tr>
<td>2014-05-08</td>
<td>20128</td>
<td>TS_DB/11225: Stack overflow with unimplmented ClientCOM events.</td>
</tr>
<tr>
<td>2014-08-06</td>
<td>20218</td>
<td>TS_DB/11522: $PSTAT's PID field could be incorrect when starting lots of processes simultaneously.</td>
</tr>
<tr>
<td>2014-12-10</td>
<td>20344</td>
<td>TS_DB/11777: Kwebserv could return an incorrect Content-Type for XML files.</td>
</tr>
<tr>
<td>2014-12-23</td>
<td>20357</td>
<td>TS_DB/11788: $LIC now supports expired key values.</td>
</tr>
<tr>
<td>2015-01-11</td>
<td>21042</td>
<td>TS_DB/11844: 'KCML_Lic_Acquire &amp; 'KCML_Lic_Count did not return the correct values when $RELEASE was in effect.</td>
</tr>
<tr>
<td>2015-04-20</td>
<td>21110</td>
<td>TS_US/436: KCML 6.20 for AIX 5.4 &amp; Linux 2.6 now requires OpenSSL 1.0.1</td>
</tr>
<tr>
<td>2015-04-28</td>
<td>21118</td>
<td>TS_DB/12011: Fixed buffer overrun in CONVERT string$ TO nVal</td>
</tr>
</tbody>
</table>
