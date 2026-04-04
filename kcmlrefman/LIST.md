LIST

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

\[@\]LIST \[title\] \[S\]\[D\] \[start_line_number \[,\] \] \[,end_line_number\]\

</div>

\
Where:\
\

<div class="indent">

title = alpha_variable or a literal string\
\

</div>

</div>

------------------------------------------------------------------------

The LIST statement displays the program text currently in memory in line sequence. LIST will automatically insert page breaks if the listing is to be displayed on the screen (/005). If the optional @ sign precedes the reserved word LIST, then the listing will be taken from the currently selected global partition, if any.

If using the KCML full screen editor and debugger the functions described below are all available either from a menu option or with a series of simple keyboard or mouse operations. Refer to the separate documentation on the KCML full screen editor and debugger for more information.

- If LIST is entered with no parameters specified, the program will be listed in structured form. Loops are indented, and each statement of a multi-statement line is listed on a separate line. Adding the S and D parameters performs the same function as a standard LIST. The number of spaces used to indent loops is 4 unless the KINDENT environment variable specifies otherwise. If LIST is followed by the S parameter then the program is listed in unstructured form, i.e. multi-statement lines are not separated into individual lines.
- If LIST is followed by a starting line number, then only the line specified is listed. If a starting line number is followed by a comma, then all lines from the specified line to the very last line of the program are listed.
- If LIST is immediately followed by a comma and an ending line number, then all of the lines up to and including the specified line are listed. If both the start line number and the ending line number are specified, separated with a comma, then all lines starting from the start line up to and including the ending line number will be listed.
- If an optional title is entered immediately after the LIST command, a heading will be then be entered at the top of the first page of the listing.
- If the S parameter is used without the D parameter, then listings will be produced in unstructured form. Subroutine entry points and [REMed](REM.htm) text will not be highlighted.

The output from the LIST command can be redirected to a printer or to any Unix/DOS device or file with the [SELECT LIST](SELECT_LIST.htm) command.

Examples:

|  |  |
|----|----|
| LIST 1000 | List only line 1000. |
| @LIST 1000,5000 | List lines 1000 to 5000 from the currently selected global partition. |
| LIST ,900 | List all lines up to an including line 900. |
| @LIST "test" 1000 | List line 1000 from the currently selected global partition with the word "test" as the title. |
| LIST S 10,50 | Produce an unstructured list for lines 10 through to 50. |

See also:

[SELECT LIST](SELECT_LIST.htm) [SELECT LIBRARY](SELECT_MODULE.htm)
