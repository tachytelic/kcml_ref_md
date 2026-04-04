\$RELEASE KEY

------------------------------------------------------------------------

General Form:\
\
     \$RELEASE KEY = key_value\
\
Where:\
\
     key_value      = a function key 0 - 31, 126 (TAB), 127 (SHIFT TAB)\
\

------------------------------------------------------------------------

The \$RELEASE KEY statement allows the specified function key to act as a hot key which when pressed will automatically [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm) to the next available detached terminal which is waiting to attach. The screen is saved and will be restored when the partition regains control. The value of the \$RELEASE KEY is inherited by child processes created with [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm).

This statement has no effect if executed on Windows versions. It is also only relevant when developing text based applications.

Example:

\$RELEASE KEY = 31

defines function key 31 as a hot key.

See also:

[\$RELEASE]($RELEASE.htm), [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm), [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm)

 
