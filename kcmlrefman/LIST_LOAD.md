LIST LOAD

------------------------------------------------------------------------

General Form:\
\
     LIST \[title\] LOAD\
\
Where:\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST LOAD statement lists the names of the programs currently in memory along with their line number ranges. The output will also indicate whether lines have been modified, added or removed.

For example:

LIST LOAD\
PROGS/SL/pmenu\
now contains lines 10000-19999 originally 10000-19999\
loaded with - LOAD "SL/pmenu" 10000,19999\
program is pure\
\
PROGS/SL/MENU\
now contains lines 1100-3000 originally 1000-2090\
loaded with - LOAD "SL/MENU"\
program lines have been removed,added

shows that the program PROGS/SL/MENU has had lines added and removed since it was originally loaded and that the program PROGS/SL/pmenu is unchanged.

See also:

[LIST ADD](LIST_ADD.htm)

 
