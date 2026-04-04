LIST DIM

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
<img src="bitmaps/listdim.gif" data-align="BOTTOM" data-border="0" alt="LIST DIM" />\
Where:

> title = alpha_variable or a literal string

</div>

------------------------------------------------------------------------

The LIST DIM statement lists either a specific variable or all the variables currently dimensioned with their current dimensions and contents. This function can be also be performed within the KCML Workbench with the ListDimView key or the LIST DIM menu option.

The flag in the first column indicates whether the variable is common, non-common or local. Variables appear in the order of declaration, except that all common variables are listed first, non-common second and local variables last. The display for each variable is restricted to one line; therefore, long strings or large arrays may be truncated. Non-printing characters in a string are shown as periods. Numeric fields have the start position followed by the [Field specifier](tmp/xp.htm).

Example:


    LIST DIM
    C Fred$16     "Aard-vark       "
    C N(12)       1,2,3,2,12,22,12,11,34,56,78,98
    C a9          1.8
    C color$(2)8  "Red<_><_>","Blue<_><_>"
    D q6$1        " "
    D hx$7        "...A..."
    D .Type       (4, NUM(9,2))
    D .Name$      (30, CHAR(25))
    D Big$10000   -
    D Z           Out of scope
    L temp$(2)10  "..........",".........."
    L big(10)     0,0,0,0,0,0,0,0,0,0

In the example above the variable hx\$ contains three non-printable hexadecimal characters followed by the letter \`A' followed by another three non-printable characters. The variable Big\$ has no value displayed against it because it has yet to be references in the program and no space has been allocated for its value. The variable z is shown as *Out of scope* because it exists in the program only as a local variable and at the time of the LIST DIM the defining DEFSUB was not active.

<span id="pattern"></span>

If a pattern is specified instead of the optional variable name, LIST DIM will search for a range of variables matching the pattern. The pattern may be a regular expression with the following wildcard characters:

<div class="indent">

|  |  |
|----|----|
| \* | Match any string of characters including a null string. |
| ? | Match any single character. |
| \[...\] | Match any of the characters enclosed. A pair of characters separated by a minus sign will match any character lexically between the pair. |

</div>

Thus LIST DIM "A\*" would match A, A(, A\$, APPLE\$, etc., while LIST DIM "A\[0-9\]\$" would match A0\$, A1\$ up to A9\$.

Syntax examples:

LIST DIM\
LIST COM type\$\
LIST DIM "?variable\$("

See also:

[COM](COM.htm), [DIM](DIM.htm), [DIM(](DIM(.htm), [LOCAL DIM](LOCAL_DIM.htm), [LIST LOCAL](LIST_LOCAL.htm), [LIST V](LIST_V.htm)
