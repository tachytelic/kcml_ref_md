\$RELEASE function

General Form:\
\
     \$RELEASE\
\
Valid wherever a numeric expression is valid.\
\

------------------------------------------------------------------------

The \$RELEASE function is used to clone the existing program and run it as a child process. The original program is suspended and its entire environment is unaffected by anything that might occur in the clone copy. The main use of this function is to allow the running of a second program which might destroy the value of common variables or overwrite program lines.

The parent process will be suspended until the child terminates by executing [\$END]($END.htm). The parent then receives the argument of the [\$END]($END.htm) and returns it as the value of the \$RELEASE function. The child always returns -1 as its value for the function and so the program can tell whether it is executing in the parents copy (\>= 0) or the childs copy (-1). If however the cloning operation fails, perhaps because some resource such as paging space is unavailable, the function may return -2. This indicates that there is still only one partition and the application should give an error.

The Unix implementation of \$RELEASE uses the fork system call to create a second duplicate process with a different process ID as well as a different partition number \#PART. Microsoft Windows does not support fork so the second partition is created inside the context of the original process. It has a different \#PART value but shares the same process ID.

While the parent process is blocked waiting on the child terminating its terminal status in \$PSTAT is set to 'F'. To avoid double counting in the Windows implementation the memory page count in \$PSTAT is set to zero for the parent while the child is active.

In the following example the child partition is started when the \$RELEASE function is executed. Control is returned to the parent partition when the child executes a [\$END]($END.htm) statement.

SELECT CASE \$RELEASE CASE -1 REM Now executing in the child copy COM CLEAR fred\$ LOAD "PROGONE" 1000 CASE -2 REM fatal error PANIC CASE ELSE REM Executing parent with child terminated ... END SELECT

Syntax examples:

test = \$RELEASE + 1\
PRINT \$RELEASE\
IF (\$RELEASE == -2)

See also:

[\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm), [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm), [\$RELEASE KEY]($RELEASE_KEY.htm), [\$END]($END.htm), [\$PSTAT]($PSTAT.htm)
