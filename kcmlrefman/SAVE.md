SAVE

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

SAVE \[\<\[S\]\[R\]\[G\]\[!\]\>\] \[#stream,\] filename \[,start_line \[,end_line\]

</div>

Where:\
\

<div class="indent">

start_line, end_line = are valid program line numbers within the range 0 \< 32000

</div>

\

</div>

------------------------------------------------------------------------

The SAVE statement is used to create a file for the program currently held in memory within the current native operating system directory, or within the directory specified by the stream. If no stream is specified the file will be SAVEd to the directory that is [SELECT](SELECT_DISK.htm)ed to stream \#0. Any existing file of the same name must have been previously [REMOVE](REMOVE.htm)d, alternatively the [RESAVE](RESAVE.htm) statement can be used, otherwise a \`D83 File already exists' error will result.

SAVE will save the program in a binary compiled form for the most efficient LOAD. It is also possible to save the program in a text source format while developing. This can be of great benefit for text processing tools or source control. This can be done either with the special [SAVE ASCII](SAVE_ASCII.htm) command or by modifying the behaviour of LOAD and SAVE by setting byte 46 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE46).

- Specifying a start line number after the filename will save only program lines after and including the specified line number.
- Specifying a comma and an end line number will only save the lines up to and including the specified line number.
- Specifying both a start and an end line number will save only the specified lines and the intervening lines.

The behaviour of SAVE can be controlled using one or more optional parameters enclosed in \<\> brackets.

The optional 'G' parameter is used to create a global library. It will generally be issued within a running program and can only be executed from immediate mode if the program is resolved. It cannot be combined with any of the other optional parameters except '!',and no line number range can be used. However libraries built with kmake and kc6 are more functional and are to be preferred. SAVE\<G\> will not be be supported in future versions of KCML. For more details see the tutorial on [libraries](TutorialModules.htm).

If the optional 'R' parameter is specified, any [REM](REM.htm)ed text will be removed before the program is saved. The whole REM line is removed where possible but if a statement is the target of a GOTO then the word REM itself will be left as a stub.

To scramble a program so that it cannot be [LIST](LIST.htm)ed when [LOAD](LOAD.htm)ed, the '!' parameter is used in conjunction with the [SELECT PASSWORD](SELECT_PASSWORD.htm) command. See [SELECT PASSWORD](SELECT_PASSWORD.htm).

The optional 'S' parameter is supported only for BASIC-2 compatibility and is ignored as surplus spaces are always removed by the KCML.

Syntax examples:

SAVE "PROGONE"\
SAVE \#16,"GBPROG"\
SAVE \<R\>"/tmp/TEMP" ,4000\
SAVE file\$ 1000,4000\
SAVE \<!\>"TESTPROG"\
SAVE \<G\>"GB/lib"

See also:

[LOAD](LOAD.htm), [RESAVE](RESAVE.htm), [SAVE ASCII](SAVE_ASCII.htm), [SELECT PASSWORD](SELECT_PASSWORD.htm), [\$OPTIONS RUN]($OPTIONS_RUN.htm)
