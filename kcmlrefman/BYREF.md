BYREF

------------------------------------------------------------------------

General Form:\
\
'func(BYREF arg)\
\
...\
\
DEFSUB 'func(BYREF arg)\
\

------------------------------------------------------------------------

The BYREF qualifier may be specified against a numeric, string or label argument, and has to be matched by a BYREF qualifier in the GOSUB' statement. This changes the behaviour so that instead of copying the value of the argument into a local copy used only in the routine, KCML will pass a reference to the original variable. Any changes made to the BYREF variable in the routine will be reflected back into the original argument as they both refer to the same object. This is very similar to passing the [SYM()](SYM(.htm) of the variable but the body of the routine does not then need any special constructs when referencing the variable.

BYREF can also be used to pass pointers to numbers into \$DECLAREd functions. This tells KCML to pass the address of the number rather than the value as would be the normal convention for numbers. Strings are always passed as pointers so BYREF is not needed for them. The keyword RETURN can also be used as an alternative to BYREF but its use for this purpose is now deprecated and BYREF is to be preferred.

Example:

aValue = 10\
aString\$ = "Hello"\
'aRoutine(BYREF aValue, BYREF aString\$)\
\
. . . . .\
DEFSUB 'aRoutine(BYREF Total, BYREF Name\$)\
Total += 100\
Name\$ = & " World!"\
RETURN\

See also:

[DEFSUB'](DEFSUB.htm), [GOSUB'](GOSUBquote.htm), [RETURN](RETURN.htm), [SYM()](SYM(.htm)
