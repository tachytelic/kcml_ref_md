\$END

------------------------------------------------------------------------

General Form:\
\
     \$END \[integer_expression\]\
\
Where:\
\
     integer_expression      = an integer within the range 0-255\
\

------------------------------------------------------------------------

The \$END statement is used to exit KCML and return control to the Unix or Windows operating system. All currently open files are closed, and all locks released. An optional return code (between 0 and 255) may be returned to the parent process. Though KCML permits this integer to be in the range 0 to 255, KCML will return [internal errors](tmp/ExitCodes.htm) with numbers between 100 and 200. It is recommended that the return code is limited to the range 0 to 99 to avoid ambiguity. If no return code is specified then zero is returned unless KCML is terminated abnormally.

If the process has [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm) children in the background then they remain in the background but if the process itself is such a child and it has the foreground then it will give its parent the foreground.

Execution of a \$END also [\$CLOSEs]($CLOSE.htm) all currently open devices and deselects and [@UNLOCKs](@UNLOCK.htm) the currently selected global partition if any.

If the HEX(01) bit of [\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 53 is set, programming is enabled, HALT is enabled and the user has previously interrupted the program displaying the debugger, then a \$END executed within the program will not terminate the session but will drop back into the editor. The behaviour of \$END in immediate mode is not affected. This bit in \$OPTIONS is set by default so to revert to the behaviour prior to KCML 5.0 unset this bit in your program.

Syntax example:

\$END variable
