MAT SEARCH

------------------------------------------------------------------------

General Form:\
\

> MAT SEARCH \[ELEMENT\] search_var, operator search_string TO pointer_var \[STEP step\]

Where:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="clear">
<td>search_var</td>
<td>= an alpha_variable or literal containing the text to be searched.</td>
</tr>
<tr class="clear">
<td>search_string</td>
<td>= a string expression containing the text to be found.</td>
</tr>
<tr class="clear">
<td>pointer_var</td>
<td>= an alpha or numeric array variable containing pointers to occurrences of the search string in the search variable.</td>
</tr>
<tr class="clear">
<td>operator</td>
<td>= a string comparison operator, one of the following<br />
&lt;,  &lt;=,  ==,  &lt;&gt;,  !=,  &gt;=,  &gt;</td>
</tr>
<tr class="clear">
<td>step</td>
<td>= numeric expression between 0 and 65536.</td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

The MAT SEARCH statement is used to scan the specified alpha variable or alpha expression for substrings that satisfy the specified relational operator. The locations of the substrings are then placed into the pointer variable.

If an alpha pointer variable is used, each location is stored in the pointer variable as a two byte binary value specifying the position of the first character of the substring relative to the beginning of the search variable or literal. The search will end when either the whole search variable has been scanned or when the pointer variable is full. Clearly this limits the search string to a length of 64kb and so this usage is now discouraged.

If a numeric pointer variable is used, each location is stored in the pointer variable as a decimal value. Numeric pointer variables allow arrays of \>64k to be searched. The last entry in the pointer array is set to zero.

The optional STEP clause is used to specify the number of bytes to skip in the search variable to determine the start position of the next field to search. If no step parameter is used a default of 1 is assumed. The STEP clause must be a positive integer.

The optional ELEMENT clause determines the actual values for each location matching the search string. The ELEMENT clause would only be used where the number specified by the STEP clause is the same as the array element size. Therefore the value returned would be the actual number of the matching array element, in binary, rather than its relative byte position. See the example below.

It is important to understand that KCML will determine the length of the substring using the [LEN()](LEN(.htm) function internally and only that number of bytes will be considered in the comparisons. If there is a possibility that the substring may have trailing blanks then the [STR()](STR(.htm) or [FLD()](FLD(.htm) functions should be used to be explicit about the number of bytes to be used in the comparisons. This is a particularly important consideration when the subtring is a packed BCD number.

Note that the comma following the *search_var* is mandatory.

Example:

DIM source\$(5)6, point\$2\
source\$(1) = "steve"\
source\$(2) = "fred"\
source\$(3) = "alan"\
source\$(4) = "john"\
source\$(5) = "bill"\
name\$ = "alan"\
MAT SEARCH source\$(),= STR(name\$,,6) TO point\$ step 6\
PRINT "The relative position of the search string"; VAL(point\$,2)\
MAT SEARCH ELEMENT source\$(), = STR(name\$,,6) TO point\$ step 6\
PRINT "The array element containing the search string is ";VAL(point\$,2)\
\
The relative position of the search string is 13\
The array element containing the search string is 3

Syntax examples:

MAT SEARCH temp\$(), == STR(string\$,,5) TO pointer\$ STEP 5\
MAT SEARCH FLD(fi\$().nl\$),==FLD(fq\$.name\$) TO log\
MAT SEARCH fd\$, \<= STR(temp\$,,3) TO ptrs\$() STEP 10\
MAT SEARCH file\$(), == STR(string\$,,5) TO point()\
MAT SEARCH FLD(array\$().names\$), == STR(aname\$) TO hit
