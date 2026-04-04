LOAD

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
<img src="bitmaps/load.gif" data-align="BOTTOM" data-border="0" alt="load" />\
Where:\
\

|  |  |
|----|----|
| start | = the number of the first line to be deleted from memory before the new program is loaded |
| end | = the number of the last line to be deleted from memory before the new program is loaded. |
| line | = the number of the line where execution is to begin after the new program has been loaded. |

</div>

------------------------------------------------------------------------

The LOAD statement loads a KCML format or ASCII program segment into memory from the specified directory. Once the program is loaded it is then executed. All non-common variables are cleared from memory and the return stack is emptied upon execution of a LOAD statement.

If no start and end line numbers are specified then the whole program currently in memory is removed before the new program is loaded. If only the start line number is specified then all lines after the specified line are removed. If both the start and end line numbers are specified then all lines between the two line numbers will be removed. If the end line number is less than the start line number then no lines are cleared.

If no device address or stream is specified then the directory or platter currently selected to \`#0' will be used.

If a line number is entered after the word BEG, then KCML will load the specified program, and continue execution at the specified line number. If BEG is not specified then execution will begin at the lowest line number in the program.

By specifying the \<num_expression\> and an alpha variable the LOAD statement can be instructed to load multiple programs at one time. The numeric expression specifies the number of programs to be loaded, and the alpha variable contains the names of the programs. In this case the program name is limited to 8 characters and must be padded with spaces if less than 8 characters. The maximum number of programs that can be loaded at once is 100.

Alternatively, from KCML 6.0 onwards, you can specify \<*str_expression*\> and an alpha variable to LOAD load multiple programs using a delimiter character in the first byte of the *str_expression*. Unlike the previous method, there is no special restriction on the length of a program name or in the number of programs that can be loaded at a time. Note however that no KCML program name, including the directory, can exceed 255 characters. Also, characters which routinely make up absolute path names, ie **. / \\** and **:** are not valid delimiter characters.

When loading multiple programs the complete program is only resolved after all the program segments have been loaded. It is not possible to use [ERROR](ERROR.htm) to programmatically recover from an error in a multiple LOAD unless the error occurs during the loading of the first program.

The behaviour of LOAD can be controlled to some extent by setting BYTE 46 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE46). Among the things that can be controlled are whether LOAD should append a ".src" extension to source file and whether it should look for source files before looking for a compiled file.

The HEX(04) and HEX(08) bits in byte 40 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE40), which normally governs \$COMPILE, can also affect LOAD. Setting HEX(04) will force a ".src" extension to be appended to a source file name and setting HEX(08) will translate spaces in filenames to underscores.

Compatibility

KCML6.10 introduced a new [text format](NEWASCII.htm) for source files which supports conditional compilation and does not require colons to separate statements.

Examples:

COM programs\$16\
programs\$ = "PROG001 PROG002"\
LOAD \#27,\<2\>programs\$\
\
LOAD \<","\> "file1,../specials/file2"

See also:

[SAVE](SAVE.htm)
