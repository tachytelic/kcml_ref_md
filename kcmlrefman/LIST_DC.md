LIST DC

------------------------------------------------------------------------

General Form:\
\
     LIST \[title\] DC \[#stream\] \[strexpr\] \[W\]\
\
Where:\
\
     strexpr           = is optional mask expression.\
\
     title           = alpha_variable or a literal string.\
\

------------------------------------------------------------------------

The LIST DC statement produces a listing of files within platter images or files within a Unix/DOS directories.

If no stream is specified then directory currently selected to stream \`#0' will be listed.

Certain pattern matching characters may be used within the string expression. The characters available when listing files that are stored within the native operating system are operating system dependent. The following are available:

\*           Match any string of characters including a null string.

?           Match any single character.

\[...\]      Match any of the characters enclosed. A pair of characters separated with a minus sign will match any character lexically between the pair.

Example:

LIST DC "SL/P\*"

Will list all files in the "SL" directory that start with the letter P.

LIST DC "??/FILE2"

Will list all files in all sub-directories that are called FILE2.

LIST DC "ABC/DEF\[1-9\]"

Will list all files in the directory "ABC" that start with the string "DEF" and end with a number within the range 1 through to 9.

The display for Unix files is the same as that produced with the Unix \`ls -alR' command which recursively lists in sorted order the specified directory and any subdirectories. If a tailored display is required the command can be specified with the LISTDCT environment variable. The default corresponds to LISTDCT="ls -alR".

The display for DOS/Windows files is similar to the Unix default, however the LISTDCT environment variable is ignored.

Adding the \`W' parameter will list files and subdirectories, in columns.

The output from the LIST DC command can be redirected to a printer or to any Unix/DOS device or file with the [SELECT LIST](SELECT_LIST.htm) command.

Syntax examples:

LIST DC \#14 W\
LIST DC "??SMR\*"\
LIST DC "A\*"

See also:

[SELECT LIST](SELECT_LIST.htm)
