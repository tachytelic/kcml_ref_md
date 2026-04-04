LIST LOCAL

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/listlocal.gif" data-align="BOTTOM" data-border="0" alt="listlocal.gif" />\
Where:\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST LOCAL statement lists either a specific local variable or all the currently defined local variables with their current dimensions and contents.

This operation can also be performed within the KCML Workbench by selecting the Variables option from the LIST RETURN dialog box.

Non-printing characters in a string are shown as periods.

Example:

LIST LOCAL\
L      FRED\$16           "Aard-vark      "\
L      NA(12)           1,2,3,2,12,22,12,11,34,56,78,98\
L      A9                1.8\
L      U6\$(2)8           "Red\<\_\>\<\_\>","Blue\<\_\>\<\_\>"\
L      Q6\$1                " "\
L      HX\$7                "...A..."\
L      .TYPE           (4,0X6002)\
L      .NAME\$           (30,25)

In the example above the variable HX\$ contains three non-printable hexadecimal characters followed by the letter \`A' followed by another three non-printable characters.

If a pattern is used, it may include the same pattern matching wildcard characters as [LIST DIM](LIST_DIM.htm).

See also:

[LIST DIM](LIST_DIM.htm), [DEFSUB'](DEFSUB.htm), [LOCAL DIM](LOCAL_DIM.htm)
