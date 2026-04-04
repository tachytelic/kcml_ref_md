LIST ?

------------------------------------------------------------------------

General Form:\
\
     \[@\]LIST \[title\] ? \[\*\]\
\
Where:\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST ? statement will list all non-common variables which appear only once in the current program. If the variable is not in common then it is either not necessary or is a misspelling. If the optional @ sign precedes the reserved word LIST, then the listing will be taken from the currently selected global partition, if any.

If an asterisk immediately follows the (?) then all references to the variables will be LISTed in full. Leading colons (:) are inserted before each statement to show the exact position within the line, for example:

LIST ?\*\
NEW_RECORD\$      - 01010 :: GOSUB'create(new_record\$)\
TESTING(           - 12390 :::: MAT REDIM testing(x,y)\
X                - 12390 :::: MAT REDIM testing(x,y)\
Y                - 12390 :::: MAT REDIM testing(x,y)

without the asterisk the output would be as follows:

LIST ?\*\
NEW_RECORD\$                - 01010\
TESTING(                     - 12390\
X                          - 12390\
Y                          - 12390

 
