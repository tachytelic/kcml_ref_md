\$CLIENTVERSION function

------------------------------------------------------------------------

General Form:

\$CLIENTVERSION

------------------------------------------------------------------------

The \$CLIENTVERSION alpha function returns the version string of the connected KClient. This string includes the six digit version number and four digit build number. It is legal anywhere an alpha expression is legal.

Syntax examples:

FLD(heading\$.kclient_version\$) = \$CLIENTVERSION IF (\$CLIENTVERSION \< "06.00.00.0001") .control.text\$ = \$CLIENTVERSION ENDIF

See also:

[\$VERSION]($VERSION.htm)
