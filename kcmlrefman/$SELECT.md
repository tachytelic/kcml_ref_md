\$SELECT

------------------------------------------------------------------------

General Forms:\
\
1.      \$SELECT alpha_expression\
\
2.      alpha_receiver = \$SELECT\
\

------------------------------------------------------------------------

The \$SELECT statement in its first form is used to change the current working directory in the native operating system. The \#0 stream is set to the specified directory. In versions of KCML prior to 6.10 the device table was cleared and all KDB tables were closed but the device table and the database is left unaltered.

The second form is used as a function to return the current working directory. This form is valid wherever an alpha function is valid.

Syntax examples:

\$SELECT "/user1/kcml"\
\$SELECT "C:"\
\$SELECT new_director\$\
cwd\$ = \$SELECT\
FLD(directory_list\$.current\$) = \$SELECT
