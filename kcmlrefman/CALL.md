CALL

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

CALL ufn_name \[variable_list \[ TO receiver\_ list\]\]

</div>

\
\

</div>

------------------------------------------------------------------------

This facility has been introduced to extend the KCML language with built-in calls to user-written functions (UFNs) in a shared library written in a high level language such as C. This allows the faster execution of compiled subroutines to be combined with the ease of programming and debugging of KCML. UFNs can be used to access third party libraries such as database systems or for utility functions where execution time is more important than development time. This facility is only for those who are competent at writing in such languages. In particular the documentation supplied assumes you understand C.

This facility is not available for user written functions in the Windows environment where [\$DECLARE]($DECLARE.htm) is the natural way to access other functions in a DLL. \$DECLARE can also be used with most versions of Unix to call arbitrary functions in shared libraries. When compared to CALL, \$DECLARE has more overhead in interpreting the calling interface and passing parameters but, when available, \$DECLARE will generally be a easier way to invoke functions in external libraries where performance is not critical.

Programmers should consult the [SDK documentation](ufn.htm) and the sample supplied for information about compiling their own library. That is then introduced into the kcml environment by use of the -x switch to KCML when it is run e.g. the following might be used in the .profile


    kcml -x uf_samp.so START

If CALL is used to invoke external functions that make extensive use of heap memory managed by the malloc() C run time library call, then kcml should be invoked with the -y flag or the [USEMALLOC](EnvVars.htm#USEMALLOC) environment variable should be invoked to force KCML to use the same memory manager.

There are built in functions invoked with CALL in all versions of KCML for database access. These are documented in the [database manual](mk:@MSITStore:kdb.chm::/Intro.htm).

Example:


    CALL READ_NEXT handle,buffer$,length TO status

See also:

[LIST CALL](LIST_CALL.htm), [LIST U](LIST_U.htm), [\$DECLARE]($DECLARE.htm)
