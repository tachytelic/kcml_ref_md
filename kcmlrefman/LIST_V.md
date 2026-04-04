LIST V

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/listv.gif" data-align="BOTTOM" data-border="0" alt="listv.gif" />\
Where:\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST V statement finds instances of a variable in a program. Only one variable can be searched for at once. If no variable is supplied then all variables will be listed. For arrays only the opening parenthesis is required. If the optional @ sign precedes the reserved word LIST, then the listing will be taken from the currently selected global partition, if any.

Variable search operations are best performed from the search dialog box in the KCML Workbench.

If an asterisk follows the V then all references to the variables will be LISTed in full, for example. Leading colons (:) are inserted before each statement to show the exact position of the variable within the line, for example:

LIST V\* new\$\
new\$                - 01010 ::'Create(new\$)\
               - 21000 :::MAT REDIM new\$(256)nw

without the asterisk the output would be as follows:

LIST V new\$\
NEW\$                - 01010 21000

Adding the COM or DIM reseved word immediately after the V will only list variables that are referenced in the foreground partition, in [LIST DIM](LIST_DIM.htm) format.

If a pattern is used, it may include the same pattern matching wildcard characters as [LIST DIM](LIST_DIM.htm).

Syntax examples:

LIST V\
@LIST V \* new_variable\$(

See also:

[LIST DIM](LIST_DIM.htm)

 
