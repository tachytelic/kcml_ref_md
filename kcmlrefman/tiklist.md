tiklist (Unix)

General Form:\
\
tiklist *keyfile*\

The *tiklist* utility is used to list the *TERMINFO* information, in ASCII text form, for the specified terminal type. The *keyfile* specifies the full path name of the *TERMINFO* file, normally these files reside within the */usr/lib/TERMINFO* directory. The output from *tik*list can be used as input to *tik*. For example, to list the **KCML** *TERMINFO* information for the vt220 terminal the following would be used:

tiklist /usr/lib/kcml/TERMINFO/vt220

See also:

[tik](tik.htm)
