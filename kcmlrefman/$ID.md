\$Id

------------------------------------------------------------------------

General Form:\
\
     \$Id:\$\
\

------------------------------------------------------------------------

The \$Id statement can be used to embed an RCS or CVS version tag in a program which will be automatically expanded out when the program is checked out of the source control repository. The statement is treated as a comment and is ignored inside KCML.

RCS version tags could not be enclosed in a REM because of the embedded colons nor in an image because only one image is permitted per line. The statement ends with a matching \$ sign. If the following is added to the program DISP.src 1000 \$Id:\$ REM display program

when booked out of the source control system RCS will expand this to 1000 \$Id: DISP.src,v 1.45 1999/02/18 19:46:21 pjc Exp \$ REM display program

showing the program name in the repository (DISP.src,v), its version (1.45), the date and time it was committed and the userid of the person who made the commit (pjc).

The case is important here and when initially added to the program it must be spelt exactly as \$Id:\$ with upper case I and lower case d.
