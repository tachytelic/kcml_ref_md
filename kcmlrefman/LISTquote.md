LIST '

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/listtick.gif" data-align="BOTTOM" data-border="0" alt="listtick.gif" />\
Where:\
\
     subroutine_name           = number, subroutine label\
\
     title                = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST' statement finds all references to a given defined subroutine in a program. LIST' without a subroutine name finds all subroutines in a program. If the optional @ sign precedes the reserved word LIST, then the listing will be taken from the currently selected global partition, if any. The same pattern matching wildcard characters can be used as with [LIST DIM](LIST_DIM.htm).

Subroutine label search operations are best performed from the search dialog box within the KCML Workbench.

Placing an asterisk after the subroutine name will list the [DEFFN'](DEFFNquote.htm), [DEFSUB'](DEFSUB.htm) or [\$DECLARE']($DECLARE.htm) statement in full showing the arguments within the parentheses, the [GOSUB'](GOSUBquote.htm) references to the routine are also LISTed in full. Leading colons (:) are inserted before each statement to show the exact position of the statement within the line, for example:

LIST 'open_file\$ \*\
1000 DEFFN' open_file\$(handle, name\$, initial\$())\
       - 00100 :::'Open_file\$(fd,tmp\$, nm\$())\
       - 00900 ::a\$='Open_file\$(newfd,tmp\$,user\$)

Without the optional asterisk the output would appear as follows:

LIST 'open_file\$\
01000 DEFFN ' OPEN_FILE\$\
          - 00100 00900

Syntax examples:

LIST '\
@LIST '16\
LIST 'numeric\
LIST '"sort_f????"\
@LIST title\$ 'openfile\$ \*

 
