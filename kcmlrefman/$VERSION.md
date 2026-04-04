\$VERSION function

------------------------------------------------------------------------

General Form:

\$VERSION

------------------------------------------------------------------------

The \$VERSION alpha function returns the version string of the KCML server. This string includes the six digit version number and the four digit build number. It is legal anywhere an alpha expression is legal.

Syntax examples:

FLD(heading\$.kcml_version\$) = \$VERSION IF (\$VERSION \< "05.00.00.0000") .control.text\$ = \$VERSION END IF

See also:

[\$CLIENTVERSION]($CLIENTVERSION.htm)
