MOVE

------------------------------------------------------------------------

General Forms:\
\
     MOVE file_directory1 TO file_directory2\
\

------------------------------------------------------------------------

The MOVE statement is used to rename files or directories. This statement should always be used in preference to SHELLing out to the equivalent native operating system command.

If the files specified are on different filesystems then MOVE will copy and then delete the original.

Note that not all operating systems allow directories to be renam ed across filesystems.

Note that this statement works with respect to the current working directory, not the directory specified by a select disk.

Syntax examples:

MOVE file1 TO file2\$\
MOVE "WorkDir" TO "OldWorkDir"

See also:

[\$COMPILE]($COMPILE.htm)
