REMOVE DIR

------------------------------------------------------------------------

General Form:\
\
     REMOVE DIR directoryname\
\

------------------------------------------------------------------------

This statement is used to remove native operating system directories. This statement works with respect to the current working directory, not the directory specified by SELECT DISK.

Note that this statement also removes all files and subdirectories below the specified directory.

Syntax Example:

REMOVE DIR "/tmp/WorkDir"\
REMOVE DIR Directory\$
