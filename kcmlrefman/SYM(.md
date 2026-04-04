SYM(

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/sym.gif" data-align="BOTTOM" data-border="0" alt="sym.gif" />\
\

------------------------------------------------------------------------

The first form of the SYM( function is used to extract the index of a KCML string, numeric, field variable or array, or the index of a KCML subroutine. The index is returned as a unique number identifying the variable or subroutine, which can be used with the second form to recall the values or access the subroutine. The index number is valid only for the current program and may become invalid if a LOAD operation occurs. However the SYM of a common variable will be preserved across a LOAD and as of KCML 6.20 the SYM of a library subroutine will also be persisted. The index value returned is encoded in such a way that the Workbench can recognise SYM values and dereference them in tooltips.

The first form of the SYM( function is valid wherever a numeric expression is valid. The second form is valid within an alpha or numeric expression, depending on the variable type returned and everywhere 'subroutine is valid.

See below for some examples and explanations of the different uses for the SYM( function. Refer to the [Tutorial](TutorialSym.htm) for a more detailed explanation of this function.

The following tables show how to obtain and reuse the index of different variable and subroutine types:

Examples of the SYM( function.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th width="87">Symbol Type</th>
<th width="121">Obtaining the index value</th>
<th width="200">Usage example</th>
<th width="215">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Numeric</td>
<td>n=SYM(a)</td>
<td>SYM(*n)=100<br />
PRINT SYM(*n)</td>
<td>Sets the variable a to 100. Prints the value of a.</td>
</tr>
<tr>
<td>Alpha</td>
<td>n=SYM(a$)</td>
<td>SYM(*n)$="TEST"<br />
PRINT SYM(*n)$</td>
<td>Sets the variable a$ to "TEST".<br />
Prints the value of a$.</td>
</tr>
<tr>
<td>Numeric Field</td>
<td>n=SYM(.a)</td>
<td>.SYM(*n)=(4,"##.##")<br />
<br />
FLD(a$.SYM(*n))=100</td>
<td>Sets the field variable .a to start at position 4 with the specified image.<br />
Places the value 100 into the variable a$ using the field specification.</td>
</tr>
<tr>
<td>Alpha Field</td>
<td>n=SYM(.a$)</td>
<td>.SYM(*n)$=(4,10)<br />
<br />
FLD(a$.SYM(*n)$="TEST"</td>
<td>Sets the field variable .a$ to start at position 4 for a length of 10.<br />
Places the word TEST into the variable a$ at the position specified by the field specification.</td>
</tr>
<tr>
<td>Numeric Array</td>
<td>n=SYM(a())</td>
<td>SYM(*n)(1,4)=100<br />
PRINT SYM(*n)(1,4)</td>
<td>Sets element 1,4 of the array a() to 100.<br />
Prints the value of a(1,4).</td>
</tr>
<tr>
<td>Alpha Array</td>
<td>n=SYM(a$())</td>
<td>SYM(*n)$(1,4)="TEST"<br />
<br />
PRINT SYM(*n)$(1,4)</td>
<td>Sets element 1,4 of the array a$() to "TEST".<br />
Prints the value of a$(1,4).</td>
</tr>
<tr>
<td>Numeric Field Array</td>
<td>n=SYM(.a())</td>
<td>.SYM(*n)(1,4)=(4,"#.#")<br />
<br />
FLD(a$.SYM(*n)(1,4))=10</td>
<td>Sets element 1,4 of the field variable .a() to start at position 4 for the specified image.<br />
Places the value 10 into the variable a$ at the position specified by the field specification held in .a(1,4).</td>
</tr>
<tr>
<td>Alpha Field Array</td>
<td>n=SYM(.a$())</td>
<td>.SYM(*n)$(1,4)=(4,10)<br />
<br />
FLD(a$.SYM(*n)$(1,4))="TEST"</td>
<td>Sets element 1,4 of the field variable .a$() to start at position 4 for a length of 10.<br />
Places the word "TEST" into the variable a$ at the position specified by the field specification held in .a$(1,4).</td>
</tr>
<tr>
<td>Numeric Subroutine</td>
<td>n=SYM('sub1)</td>
<td>a= 'SYM(*n)(12,"A")<br />
<br />
'SYM(*n)(12,"A")</td>
<td>Assigns the numeric expression returned from the subroutine 'sub1 to the variable a.<br />
The number 12 and the letter A are passed into the subroutine. Branches to the subroutine 'sub1. The number 12 and the letter A are passed into the subroutine.</td>
</tr>
<tr>
<td>Alpha Subroutine</td>
<td>n=SYM('sub2$)</td>
<td>a$='SYM(*n)$("YZ")<br />
<br />
<br />
'SYM(*n)$("YZ")</td>
<td>Assigns the alpha expression returned from the subroutine 'sub2$ to the variable a$.<br />
The string "YZ" is passed into the subroutine. Branches to the subroutine 'sub2$. The string "YZ" is passed into the subroutine.</td>
</tr>
</tbody>
</table>

Note that 'SYM(\* cannot be used with the [ON GOSUB](ONGOSUB.htm) statement.

Example using the SYM( function with variables which avoid copying the huge buffer:

DIM buff\$(1000)1000\
'get_rec(hd,rec,SYM(buff\$()))\
...\
\
DEFSUB'get_rec(hd, rec, pointer_sym)\
RETURN READ \#hd,(rec) SYM(\*pointer_sym)\$\
END SUB

However this example might be more readable if [BYREF](BYREF.htm) were used instead.

DIM buf\$1000000\
'get_rec(hd, rec, BYREF buf\$)\
...\
\
DEFSUB'get_rec(hd, rec, BYREF buf\$)\
    RETURN READ \#hd,(rec) buf\$\
END SUB

The following contrived but more useful example shows the use of the subroutine form of [SYM(](SYM(.htm):

DIM numbers(10)\
MAT READ numbers()\
DATA 1,2,3,4,5,6,7,8,9,0\
p_odd = SYM('odd)\
p_even = SYM('even)\
'list_numbers(p_odd, 5)\
'list_numbers(p_even, 8)\
END\
\
DEFSUB 'list_numbers(pointer, top)\
    RETURN 'SYM(\*pointer)(top)\
END SUB\
\
DEFSUB 'odd(n)\
LOCAL DIM loop\
FOR loop = 1 TO n/2\
     PRINT numbers((loop\*2)+1)\
NEXT loop\
END SUB\
\
DEFSUB 'even(n)\
LOCAL DIM loop\
FOR loop = 1 TO n/2\
     PRINT numbers((loop\*2))\
NEXT loop\
END SUB

In the previous example the subroutine 'list_numbers first uses the 'SYM(\* of the subroutine 'odd to produce a list of odd numbers, then next time it is called it uses the 'SYM(\* of the subroutine 'even.

See also:

[Tutorial](TutorialSym.htm)\
[SYMNAME(](SYMNAME(.htm)
