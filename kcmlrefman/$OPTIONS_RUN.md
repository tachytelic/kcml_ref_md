\$OPTIONS RUN

------------------------------------------------------------------------

<div class="Generalform">

General Form:

1.  \$OPTIONS RUN = alpha_expression
2.  alpha_receiver = \$OPTIONS RUN

Where:\

- alpha_receiver = a minimum of 64 characters

</div>

------------------------------------------------------------------------

Form 1 of \$OPTIONS RUN is used to allow KCML programs to modify the value of the \$OPTIONS RUN system variable which is an array of bit flags and constants that control the runtime behaviour of KCML. It extends the [\$OPTIONS]($OPTIONS.htm) variable which is supported for compatibility with other language variants. There is a similar [\$OPTIONS LIST]($OPTIONS_LIST.htm) variable to control how programs are recreated in the KCML Workbench.

Form 2 allows the contents of \$OPTIONS RUN to be examined.

Any byte of this variable can be preset at the time KCML starts up by use of the [OPTIONS_RUN_XX](EnvVars.htm#OPTIONS_RUN) environment variable.

For example:

<div class="listing">

STR(\$OPTIONS RUN,20,1)=BIN(1)

</div>

It important that \$OPTIONS RUN is modified directly in this way as the number of bytes in \$OPTIONS RUN may be increased in a future version.

Note that many of the bytes in \$OPTIONS RUN are Booleans and therefore can be set any value, i.e. HEX(01), to select the option. However the use of HEX(01) as the value for TRUE is recommended as protection against the definition being extended in the future. Setting the byte to HEX(00) reverts back to the default FALSE setting.

Any of the bytes in \$OPTIONS RUN can be preset by defining the environment variable OPTIONS_RUN_xx (where xx is the decimal byte number) in the connection manager before KCML is started and setting it to the two HEX digits required.

<table>
<caption><em>Available byte settings for $OPTIONS RUN</em></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="60">Byte(s)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td id="BYTE1" width="60">1</td>
<td>A Boolean parameter used to set the <a href="EnvVars.htm#COMPAT30">COMPAT30</a> flag.</td>
</tr>
<tr>
<td id="BYTE2">2</td>
<td>A Boolean parameter used to set the <a href="EnvVars.htm#UNIXPROGS">UNIXPROGS</a> flag.</td>
</tr>
<tr>
<td id="BYTE3">3</td>
<td>Reserved</td>
</tr>
<tr>
<td id="BYTE4">4</td>
<td>A Boolean parameter used to set the <a href="EnvVars.htm#TOMFILE">TOMFILE</a> flag.</td>
</tr>
<tr>
<td id="BYTE5">5</td>
<td>A Boolean parameter used to set the <a href="EnvVars.htm#TOMDIR">TOMDIR</a> flag.</td>
</tr>
<tr>
<td id="BYTE6">6</td>
<td>A Boolean parameter used to set the <a href="EnvVars.htm#NOENDDOERROR">NOENDDOERROR</a> flag.</td>
</tr>
<tr>
<td id="BYTE7">7</td>
<td>A Boolean parameter used to set the <a href="EnvVars.htm#DOSELECT">DOSELECT</a> flag.</td>
</tr>
<tr>
<td id="BYTE8">8</td>
<td>A Boolean parameter used to set the <a href="EnvVars.htm#BREAK30">BREAK30</a> flag.</td>
</tr>
<tr>
<td id="BYTE9">9</td>
<td>Reserved</td>
</tr>
<tr>
<td id="BYTE10">10</td>
<td>Reserved</td>
</tr>
<tr>
<td id="BYTE11">11</td>
<td>A Boolean parameter used to set the <a href="EnvVars.htm#KEEPSHARED">KEEPSHARED</a> flag.</td>
</tr>
<tr>
<td id="BYTE12">12-13</td>
<td>Reserved</td>
</tr>
<tr>
<td id="BYTE14">14</td>
<td>If set to HEX(01), KCML removes files before a <a href="RESAVE.htm">RESAVE</a> is performed. The implication is that any links are broken and the file is ownership, permissions and date-stamp are set for the current user.</td>
</tr>
<tr>
<td id="BYTE15">15</td>
<td>Reserved</td>
</tr>
<tr>
<td id="BYTE16">16</td>
<td>A Boolean parameter used to set the <a href="EnvVars.htm#COMPAT32">COMPAT32</a> flag.</td>
</tr>
<tr>
<td id="BYTE17">17</td>
<td>Sets the keys used to change between the Edit/Debug window and the Console Window. Setting this byte to HEX(FF) will disable the full screen editor/debugger. The default value is HEX(7E) for the TAB key.</td>
</tr>
<tr>
<td id="BYTE18">18-19</td>
<td>Used to set the programming mode password. A value of zero means that programming mode passwords are not in use.</td>
</tr>
<tr>
<td id="BYTE20">20</td>
<td>Used to select the language when <a href="TutorialLangs.htm">multi-language strings</a> are being used. To make KCML software more interoperable the standard KCML <a href="LanguageCodes.htm">language codes</a> are the recommended settings for this variable.</td>
</tr>
<tr>
<td id="BYTE21">21-22</td>
<td>Reserved</td>
</tr>
<tr>
<td id="BYTE23">23</td>
<td>Defines the character used to start a <a href="$HELP.htm">$HELP</a> special sequence. By default this byte is set to a ‘{‘.</td>
</tr>
<tr>
<td id="BYTE24">24</td>
<td>Defines the character used to end a <a href="$HELP.htm">$HELP</a> special sequence. By default this byte is set to a ‘}’.</td>
</tr>
<tr>
<td id="BYTE25">25-26</td>
<td>Stores the value of the highest available partition number, taken from the <a href="EnvVars.htm#BCDPART">BCDPART</a> environment variable. This value was used when KCML started up and is copied here for information only. Directly modifying these bytes will have no effect on partition numbers allocated to subsequent KCML processes</td>
</tr>
<tr>
<td id="BYTE27">27</td>
<td>Soft return character, HEX(83) by default, used when loading ASCII source in order to preserve Niakwa style line terminators in ‘;’ comments. Can be set to HEX(00) to suppress this function.</td>
</tr>
<tr>
<td id="BYTE28">28</td>
<td>Replacement character for the ‘@’ sign at the beginning of variables when compiling ASCII source when importing from environments where the ‘@’ prefix does not denote a global variable. The default character is the ‘@’ sign for no replacement. If set to HEX(00) the value of the environment variable <a href="EnvVars.htm#ATREPLACE">ATREPLACE</a> will be substituted if it exists.</td>
</tr>
<tr>
<td id="BYTE29">29</td>
<td>Changes the maximum number of statements that can be held in the immediate mode command history buffer of the line editor. Defaults to 16.</td>
</tr>
<tr>
<td id="BYTE30">30</td>
<td>Changes the maximum number of program lines that can be held in the program line modification history buffer of the line editor. Defaults to 16.</td>
</tr>
<tr>
<td id="BYTE31">31</td>
<td>Changes the maximum number of items held in the immediate mode cut/paste history buffer of the line editor. Defaults to 16.</td>
</tr>
<tr>
<td id="BYTE32">32</td>
<td>A Boolean parameter used to set the HANGUP flag.</td>
</tr>
<tr>
<td id="BYTE33">33</td>
<td>Setting this byte to HEX(01) enables Niakwa compatibility mode at runtime. This byte is automatically set if KCML is started with the -n command line parameter. It disables the special treatment of global variables with an '@'; prefix, forces 24 lines for <a href="INPUT_SCREEN.htm">INPUT SCREEN</a> on terminals with more than 24 lines and disables scrolling in <a href="PRINT_AT(.htm">PRINT AT(</a>.</td>
</tr>
<tr>
<td id="BYTE34">34</td>
<td>Modified mouse behaviour. Setting this byte to HEX(01) instructs KCML to use Niakwa style mouse drags. This byte is automatically set if KCML is started with the -n flag. Normally <a href="KEYIN.htm">KEYIN</a> does not process any mouse operations but passes them straight through. All mouse drags (unless this byte is set) are returned as drag North.</td>
</tr>
<tr>
<td id="BYTE35">35</td>
<td>Changes the way that KCML handles execution of Windows routines defined by the <a href="$DECLARE.htm">$DECLARE</a> statement and called with the <a href="GOSUBquote.htm">GOSUB'</a> statement. This byte uses a bit pattern mechanism to set the various options. The valid bits are as follows:
<table>
<tbody>
<tr>
<td width="60">HEX(00)</td>
<td>Always wait for a reply from the routine, this is the default case</td>
</tr>
<tr>
<td>HEX(01)</td>
<td>Do not wait for a reply from the routine. With this bit set the routine must be called from a <a href="GOSUBquote.htm">GOSUB’</a> statement and not from within an expression.</td>
</tr>
<tr>
<td>HEX(02)</td>
<td>Tests for the availability of the routine only. No attempt is made to actually execute the routine. If the routine does not exists the GOSUB’ statement will error with a recoverable P38 Remote function not found error.</td>
</tr>
<tr>
<td>HEX(80)</td>
<td>Forces calls to <a href="$DECLARE.htm">$DECLARE</a> to execute on the server and not the client</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td id="BYTE36">36</td>
<td>If set to HEX(01) all programming functionality is disabled. If a STOP or END statement is executed or if the program errors then KCML will automatically execute a <a href="PANIC.htm">PANIC</a> statement.</td>
</tr>
<tr>
<td id="BYTE37">37</td>
<td>Used to determine how <a href="SHELL.htm">SHELL</a> is executed.
<table>
<tbody>
<tr>
<td width="60">HEX(01)</td>
<td>Under KCML4 setting this determined if DOS boxes were minimized. Not used in KCML5.</td>
</tr>
<tr>
<td>HEX(02)</td>
<td>Force execution without using command processor.</td>
</tr>
<tr>
<td>HEX(04)</td>
<td>Force execution in a separate visible window. Note that this may not be visible if the server is a different machine.</td>
</tr>
<tr>
<td>HEX(08)</td>
<td>Create a pseudo-tty to execute an interactive Unix command.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td id="BYTE38">38</td>
<td>A Boolean parameter used to set the COMPAT40 flag.</td>
</tr>
<tr>
<td id="BYTE39">39</td>
<td>In versions of KCML &gt; 04.00 any modifications to environment variables performed with the <a href="ENV(.htm">ENV(</a> function are exported to any child processes. Setting this byte to HEX(01) disables this action and therefore reverts back to the non-exporting method used by older versions of KCML.</td>
</tr>
<tr>
<td id="BYTE40">40</td>
<td>Options that control <a href="$COMPILE.htm">$COMPILE</a> and, in some circumstances, <a href="SAVE.htm">SAVE</a> and <a href="LOAD.htm">LOAD</a>. This byte uses a bit pattern mechanism to set the various options which can therefore be combined.
<table>
<tbody>
<tr>
<td width="60">HEX(00)</td>
<td>Perform a normal compilation</td>
</tr>
<tr>
<td>HEX(01)</td>
<td>Forces $COMPILE to assume that all files are compiled program files when loading.</td>
</tr>
<tr>
<td>HEX(02)</td>
<td>All programs saved to native files with $COMPILE will be saved in ASCII format. This does not affect SAVE.</td>
</tr>
<tr>
<td>HEX(04)</td>
<td>All programs saved to native files as ASCII will have ".src" added as an extension. This affects LOAD and SAVE as well as $COMPILE. When LOADing ".src" is added to the filename before it is loaded.</td>
</tr>
<tr>
<td>HEX(08)</td>
<td>When saving or loading ASCII program automatically translate spaces in filename to underscores. This affects LOAD and SAVE as well as $COMPILE.</td>
</tr>
<tr>
<td>HEX(10)</td>
<td>When $COMPILEing back to a platter translate filenames to lowercase.</td>
</tr>
<tr>
<td>HEX(20)</td>
<td>Used in conjunction with the HEX(02) to force $COMPILE to create ASCII files in <a href="LIST.htm">LIST S</a> format.</td>
</tr>
<tr>
<td>HEX(40)</td>
<td>Forces $COMPILE to overwrite destination files if they exist, otherwise any error is reported.</td>
</tr>
<tr>
<td>HEX(80)</td>
<td>Does not add the ".src" extension when saving $COMPILEd programs.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td id="BYTE41">41</td>
<td><a href="$HELP.htm">$HELP</a> options. This byte uses a bit pattern mechanism to set the various options, the valid bits are as follows:
<table>
<tbody>
<tr>
<td width="60">HEX(01)</td>
<td>Suppress <a href="$HELP.htm">$HELP</a> functionality entirely.</td>
</tr>
<tr>
<td>HEX(02)</td>
<td>Enable support for multi-page help file with Next and Back buttons.</td>
</tr>
<tr>
<td>HEX(04)</td>
<td>Instructs KClient/WKCML to spawn a Windows browser to display the Help files. This requires the <a href="EnvVars.htm#HELPSERVER">HELPSERVER</a> environment variable to be set.</td>
</tr>
<tr>
<td>HEX(08)</td>
<td>Used in conjunction with the HEX(04) to instruct the Windows browser not to check for the file on the local machine.</td>
</tr>
<tr>
<td>HEX(10)</td>
<td>Instructs KClient/WKCML to spawn MS Windows Help (WINHELP) to view a .HLP file from the local PC.</td>
</tr>
<tr>
<td>HEX(20)</td>
<td>Instructs KCML to display HTML help as a text window event when a form is up. Useful if it is known that the client machine does not have an HTML browser installed.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td id="BYTE42">42</td>
<td>Size in MB of the memory buffer used by <a href="FSORT_BU.htm">FSORT</a> and KI_REBUILD. Defaults to 4 NT systems. On Unix systems it defaults to 8 for 32bit file access systems and 64 for 64bit systems.</td>
</tr>
<tr>
<td id="BYTE43">43</td>
<td>Reserved</td>
</tr>
<tr>
<td id="BYTE44">44</td>
<td>Maximum number of lines used to <a href="LIST_DIM.htm">LIST DIM</a> a variable in a <a href="PANIC.htm">PANIC</a> listing.</td>
</tr>
<tr>
<td id="BYTE45">45</td>
<td><a href="SELECT_@PART.htm">SELECT @PART</a> " " options
<table>
<tbody>
<tr>
<td>HEX(00)</td>
<td>Keep global partition mapped</td>
</tr>
<tr>
<td>HEX(01)</td>
<td>Detach global partition</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td id="BYTE46">46</td>
<td>Options for <a href="LOAD.htm">LOAD</a>ing and <a href="SAVE.htm">SAVE</a>ing programs. Does not affect <a href="$COMPILE.htm">$COMPILE</a>.
<table>
<tbody>
<tr>
<td width="60">BIN(0)</td>
<td>The default value. Just LOAD "file". A runtime check will be made to see if the program is compiled or in source form. SAVE will save the program in compiled format.</td>
</tr>
<tr>
<td>BIN(1)</td>
<td>Try LOAD "file.src" then LOAD "file". Always SAVE as source.</td>
</tr>
<tr>
<td>BIN(2)</td>
<td>Try LOAD "file" then LOAD "file.src". SAVE will save the program in compiled format.</td>
</tr>
<tr>
<td>BIN(3)</td>
<td>Try LOAD "file.src" only. Always SAVE as source.</td>
</tr>
<tr>
<td>BIN(4)</td>
<td>Always LOAD compiled "file" but SAVE both "file" and "file.src". If "file.src" is newer that "file" then compile before LOADing.</td>
</tr>
<tr>
<td>BIN(5)</td>
<td>As per BIN(1), try LOAD "file.src" then LOAD "file". If the file is recognized as an text source file then it will be loaded using the <a href="NEWASCII.htm"><em>text format</em></a> rules. When SAVEing only the source file with a .src extension will be saved. This option was introduced in KCML6.10.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td id="BYTE47">47</td>
<td><a href="PRINTUSING.htm">PRINTUSING</a> and <a href="PRINTUSING_TO.htm">PRINTUSING TO</a> options
<table>
<tbody>
<tr>
<td width="60">HEX(01)</td>
<td>No count in first two bytes of buffer</td>
</tr>
<tr>
<td>HEX(02)</td>
<td>Put a Tab character between columns</td>
</tr>
<tr>
<td>HEX(10)</td>
<td>Enables the use of dollar signs to replace hashes within <a href="PRINTUSING.htm">PRINTUSING</a> images. Used in conjunction with the <a href="$CONVERT.htm">$CONVERT</a> statement to enable automatic currency conversion within <a href="PRINTUSING.htm">PRINTUSING</a> output.</td>
</tr>
<tr>
<td>HEX(20)</td>
<td>Indicates if the native or alternative currency has been selected by the user. If set then the alternative currency is being used. This bit is set when the client connects to the server, and is updated when the client changes the current currency.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td id="BYTE48">48</td>
<td>Start of current century. Defaults to 32 so years 0 to 31 will be assumed to be 2000 to 2031. Year 32 will be considered as 1932.</td>
</tr>
<tr>
<td id="BYTE49">49</td>
<td>Global field variable options
<table>
<tbody>
<tr>
<td width="60">HEX(00)</td>
<td>Ignore (this was the default prior to 6.20)</td>
</tr>
<tr>
<td>HEX(01)</td>
<td>If not in local symbol table then lookup in global.</td>
</tr>
<tr>
<td>HEX(03)</td>
<td>Save global value in local symbol table.</td>
</tr>
<tr>
<td>HEX(04)</td>
<td>All undefined fields are looked up in the global at resolve time and copied to the local symbol table. This option is necessary if using <a href="$COMPLIANCE.htm">$COMPLIANCE</a> to check for all undimmed variables.</td>
</tr>
</tbody>
</table>
As of KCML 6.20 the default is HEX(03) for a runtime lookup of undefined fields.</td>
</tr>
<tr>
<td id="BYTE50">50</td>
<td>Language table for <a href="$UPPER(.htm">$UPPER</a>, <a href="$LOWER(.htm">$LOWER</a> and <a href="$STRCOLL(.htm">$STRCOLL</a> on non-Unicode systems where <a href="EnvVars.htm#USING_UTF8">USING_UTF8</a> is not set<br />
HEX(00) US ASCII 7 bit code page (default)<br />
HEX(01) ISO Latin-1 code page<br />
HEX(02) User defined code page<br />
If HEX(00) then HEXPRINT+ will use '.' for the character representation of all characters above HEX(7F) as well as those below HEX(20). Otherwise it will assume that characters above HEX(7F) are printable.</td>
</tr>
<tr>
<td id="BYTE51">51</td>
<td><a href="$REWIND.htm">$REWIND</a>/<a href="$CLOSE.htm">$CLOSE</a> options. The default setting is HEX(03).<br />
HEX(01) implied <a href="$REWIND.htm">$REWIND</a> in <a href="$CLOSE.htm">$CLOSE</a><br />
HEX(02) explicit <a href="$REWIND.htm">$REWIND</a></td>
</tr>
<tr>
<td id="BYTE52">52</td>
<td><a href="WRITE_LOG.htm">WRITE LOG</a> threshold. Defaults to zero for all levels, i.e. 1, 2 and 3.<br />
HEX(01) restrict logging to level 1 (Warnings)<br />
HEX(02) restrict logging to level 2 (Errors)<br />
HEX(03) restrict logging to level 3 (Information)<br />
See <a href="WRITE_LOG.htm">WRITE LOG</a> for more information.</td>
</tr>
<tr>
<td id="BYTE53">53</td>
<td>Controls the actions of statements such as <a href="$END.htm">$END</a>, <a href="PANIC.htm">PANIC</a> and <a href="TRY.htm">CATCH</a> in a running interactive program if programming is enabled, HALT is enabled and the programmer has previously invoked the debugger. It is a bit mask field with bits set controlling different statements thus:<br />
HEX(01) set then $END will drop into the editor instead of terminating the session.<br />
HEX(02) set then a PANIC will be treated as a special A08.41 error and no file will be produced. PANIC can still be typed in immediate mode in the console window to generate a file after the error.<br />
HEX(04) set then an error inside a TRY block which would be caught and handled by an outer CATCH clause in another subroutine will still error but continue will be allowed and will resume execution in the CATCH block. This allows the programmer to see why control has transferred to another subroutine.<br />
The default value is HEX(07).</td>
</tr>
<tr>
<td id="BYTE54">54</td>
<td>If set to HEX(01) then <a href="SAVE_ASCII.htm">SAVE ASCII</a>, or <a href="SAVE.htm">SAVE</a> operating in ascii mode (see byte 40 above), will create a backup file with a .bak extension before overwriting the previous version of the program. The default is HEX(00) which causes the previous file to be clobbered.</td>
</tr>
<tr>
<td id="BYTE55">55-56</td>
<td>Stores the value of the minimum available terminal and partition number, taken from the <a href="EnvVars.htm#BCDPART">BCDPART</a> environment variable. This value was used when KCML started up and is copied here for information only. Directly modifying these bytes will have no effect on terminal and partition numbers allocated to subsequent KCML processes</td>
</tr>
<tr>
<td id="BYTE57">57</td>
<td>Reserved</td>
</tr>
<tr>
<td id="BYTE58">58</td>
<td>Controls the formatting of <a href="LIST_RETURN.htm">LIST RETURN</a>. Setting the HEX(01) bit will list programs loaded without the platter or directory to be consistent with KCML 5.02 and before. Unsetting it (the default) display the full absolute path name.</td>
</tr>
<tr>
<td id="BYTE59">59</td>
<td>This byte controls the use of symbolic constants which are numeric symbols with a leading underscore e.g. _BUFSIZE. If this byte is HEX(00) then they are treated as regular variables for compatibility with previous versions of KCML (constants were introduced in KCML 6.0). If the HEX(01) bit is set then KCML will parse such tokens as constants as disallow any statement other than DIM or COM which attempts to set the value. See <a href="TutorialConstants.htm">Constants</a> in KCML programs. Starting with KCML 6.10 constants are enabled by default. Prior to this it was disabled by default.</td>
</tr>
<tr>
<td id="BYTE60">60</td>
<td>This byte controls the code page used by the client to interpret the text on forms. On most systems the default value (0 meaning to use the default code page) will do because the default code page on the client's system will support the same language as the text on the forms. Where the default code page is different to the language the wrong characters will be displayed. This is only likely to occur on a small number of test systems using a different code page to the language. (Most of Western Europe uses Latin1, much of Eastern Europe uses Latin2 and there various DBCS character sets for individual languages in the Far East.) You may need to set this byte if you need to display Latin2 characters on a US system for instance. Clearly the client must also have suitable fonts installed. If non-zero the byte must be set one of the standardized <a href="LanguageCodes.htm">language codes</a> as used by <a href="#BYTE20">$OPTION RUN byte 20</a>. Note that these exact codes must be used even if you are using a non-standard numbering for the strings in chevrons.</td>
</tr>
<tr>
<td id="BYTE61">61</td>
<td>This byte controls the encoding used by the extended form of <a href="$PACK.htm">$PACK</a> and <a href="$UNPACK.htm">$UNPACK</a> to convert to and from <a href="TutorialUnicode.htm">UTF-8</a> and UTF-16. This has a default value of 0 meaning the current server locale (usually the C locale for Unix) unless the USING_UTF8 environment variable is set when it is defaulted to HEX(FF) meaning data is encoded in UTF-8 so no translation in and out of UTF-8 is needed. If non-zero the byte must be set to the required <a href="LanguageCodes.htm">language code</a> as used in <a href="#BYTE20">byte 20 here</a> for chevron strings. Note that these exact codes from the table must be used even if you are using a non-standard numbering for the strings in chevrons.</td>
</tr>
<tr>
<td id="BYTE62">62</td>
<td>This byte controls the reporting of some errors for backward compatibility. These errors trap programming conditions that are wrong, but would have silently failed in previous versions of KCML. Because they are known to introduce run-time errors in applications that previously worked, these errors are by default disabled. They may be enabled using this byte, and developers are encouraged to do so. Currently two bits are defined:
<table>
<tbody>
<tr>
<td width="60">HEX(01)</td>
<td>Error attempts to retrieve properties from the grid cells that are not stored on the server (they are sent directly to the client). See grid cell properties to see what properties are available (this is dependent on the version of KCML).</td>
</tr>
<tr>
<td>HEX(02)</td>
<td>Error illegal grid cell references. This means cells where the row is negative or greater than rows, or the column is negative or greater than cols.</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

\$OPTIONS RUN as a record

KCML defines a [KCML_OPTIONS_RUN](tmp/kintfld.htm#KCML_OPTIONS_RUN) built in [DEFRECORD](DEFRECORD.htm) that can be used to access the fields in \$OPTIONS_RUN e.g.


    klang = FLD($OPTIONS_RUN.OPTIONS_RUN_Language)

<div class="h5">

See also:

<div class="listing">

[\$OPTIONS]($OPTIONS.htm), [\$OPTIONS LIST]($OPTIONS_LIST.htm), [Internal structures](tmp/kintfld.htm)

</div>

</div>
