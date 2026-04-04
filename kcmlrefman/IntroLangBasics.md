KCML Language Basics

Program structure

**KCML** programs are made up of a series of program lines, where each line contains almost any number of **KCML**statements. Program lines are allocated numbers by the user which are later used as reference points to allow programs to be overlaid or merged into specific areas. Line numbers are also used as reference points to allow branches to a specific point within the program. Line numbers can range between 0 and 32000.

Each program line can contain one or more **KCML** statements. When entering a line directly in **KCML**’s immediate mode, multiple statements can be entered on one line by separating each statement with a colon. **KCML** loop constructs and subroutine entry and exit points can span over multiple line numbers.

There is no limit to the length of a program line and it is quite possible to write programs disregarding lines altogether where the entire program is effectively one line. This is the style favored by the **KCML** Workbench which hides line numbers by default.

Statements, functions and operators

There are three classes of instruction that can be used to make up the **KCML** program.

- A **statement** is a programmable instruction that when combined with other statements make up the entire program. Each different statement instructs **KCML** to perform a different operation.
- A **function** is a programmable instruction used as part of a numeric or alphanumeric expression within a **statement**. The majority of **KCML** functions operate on the expression contained in the parentheses immediately following the function name.
- An **operator** is used to perform operations on alpha operands.

KCML variables

Variables are memory locations used to record the state of a program. The **KCML** language has two main types of variables, numeric variables which have a fixed size and which hold real numbers, and string or alphanumeric variables which have an arbitrary size and which hold characters. String variables are distinguished from numerics by having a ‘\$’ character at the end of their names. Because the size of string variables is not fixed by the language it will normally be necessary to declare the size in a [COM](COM.htm), [DIM](DIM.htm), [LOCAL DIM](LOCAL_DIM.htm) or [DEFSUB'](DEFSUB.htm) statement before the string is first used. If the variable is not declared **KCML** will automatically allocate 16 bytes.

Variables can be global if they are declared in a shared memory partition and have a name starting with a ‘@’ character. Global variables can be referenced from other partitions provided that partition uses a [SELECT @PART](SELECT_@PART.htm) statement to gain access to the shared memory partition. This is discussed further in the Global and background partitions chapter, (chapter 16) later in this volume.

There is also a special class of variables called field variables which are used to describe sub records within a string variable. They have names starting with a \`.' character and are discussed further in the Fields chapter, (chapter 7) in this volume.

Array variables can have up to two dimensions and must be declared with a [DIM](DIM.htm), [COM](COM.htm), [LOCAL DIM](LOCAL_DIM.htm) or [DEFSUB'](DEFSUB.htm) statement which can specify the number of dimensions and the range of subscripts allowed. Subscripts are enclosed in parentheses and count from one. Negative subscripts are not allowed.

**KCML** uses dynamic memory management techniques to allocate the memory used by variables. Every variable has an entry in the programs *symbol table* which holds information about the name of the variable and its attributes such as the number of dimensions, whether it is a numeric or a string variable and so on. As the variable name is only held in this one central place there is no overhead incurred by using long and meaningful names. The space for the variables contents is separately allocated from dynamic memory. This allocation takes place during the resolve phase just before the program starts executing. Dynamic memory allocation allows **KCML** to change the size and even the number of dimensions of an array at run time with the [MAT REDIM](MAT_REDIM.htm) statement. The size can be increased as well as decreased.

Variable names

**KCML** allows variable names of up to 120 characters, though they can only consist of characters within the range ‘A-Z’, ‘a-z’, ‘0-9’. The underscore character ‘\_’ may also be used though the name itself must always start with an alpha character as variables whose name starts with an underscore are considered constants. On some terminals the underscore character will appear as a left pointing arrow. The ‘@’ sign and the period ‘.’ are used before the variable name to define it as a global or field variable respectively, and the dollar ‘\$’ sign may be used at the end of any variable to signify a string variable. Arrays are indicated with parentheses. Note that an array variable cannot start with the letters ‘fn’. When using global field variables the period must precede the ‘@’ sign, see the examples below.

Typical variable names might be:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td width="100">Numerics</td>
<td>i<br />
counter<br />
days_in_the_month(12)<br />
sales_by_division(25,1024)<br />
@partitions_in_use<br />
@lock_table(256)</td>
</tr>
<tr>
<td>Strings</td>
<td>q6$<br />
surname$<br />
color_palette$(7)<br />
@message_of_the_day<br />
@lock_records$(32)</td>
</tr>
<tr>
<td>Fields</td>
<td>.color$<br />
.salary<br />
.name$(100)<br />
.counters(100)<br />
.@position<br />
.@title$(960)</td>
</tr>
</tbody>
</table>

Arrays occupy different name spaces to scalars. Thus

var\$\
var\$(1)

refer to two different variables, *var\$* and *var\$(* with the opening parenthesis effectively forming part of the name. No distinction is made between upper and lower case letters in a variable name. Either may be used when entering the name but when displaying a program **KCML** will always recreate variable names in lower case to distinguish them from [reserved words](resword.htm).

Array variables

KCML allows both alpha and numeric array variables to be defined with up to two dimensions. They must be explicitly dimensioned in DIM, COM or LOCAL DIM. Upon definition, array elements are automatically initialized to spaces for alpha arrays and zeros for numeric arrays.

Once an array has been defined it size can be increased and decreased under program control. For example:

COM references(0,0) MAT REDIM references (rows, columns)

would define the array *references()* and extend its size to the dimensions specified by the variables *rows* and *columns*. Initially sizing an array with zero elements ensures that no space is allocated for it. This is in fact quite good programming practice as the array can be extended to precisely the exact size required for the application. Later, when the contents of the variable are no longer required, the array can then be re-dimensioned back to a size of zero by zero to free all the space, again with the [MAT REDIM](MAT_REDIM.htm) statement. The shape of the array, that is the number of dimensions, can also be changed using MAT REDIM.

Common variables and non-common variables

Variables are removed from the symbol table and the memory they occupy is released when a new program is loaded. In some cases it is useful to have some variables retain their value across [LOAD](LOAD.htm)’s. To do this there is a special analogue of the [DIM](DIM.htm) statement called [COM](COM.htm) which puts the variables that it declares into a special list called the common chain. Variables appear in this list in the order they are declared and such variables have their values preserved by [LOAD](LOAD.htm). Variables declared with [DIM](DIM.htm) or implicitly dimensioned, again appear in order of declaration in a similar list called the non-common chain that immediately follows the common chain. Common variables at the end of the chain can also be changed to non-common variables with the [COM CLEAR](COM_CLEAR.htm) statement which moves the pointer that marks the end of the non-common chain.

Common variables defined by [COM](COM.htm) will only be cleared from memory on execution of a [CLEAR](CLEAR.htm), [CLEAR V](CLEAR.htm), or a [LOAD RUN](LOAD_RUN.htm) statement.

DIM sales(10) COM junk\$20, new\$

would reserve a space of 20 bytes in memory for *junk\$*. If no length is specified for a string, as is the case with the variable *new\$,* the system will automatically allocate 16 bytes.

Local variables

Local variables allow better and safer structured programming. Local variables are defined with the [DEFSUB'](DEFSUB.htm) and the [LOCAL DIM](LOCAL_DIM.htm) statements. Such variables are available only within the routine in which they were defined, once the routine is exited the variables and contents are forgotten and the original values of any non-unique variables are restored.

Initializing variables

Unlike other languages, variables in **KCML** do not have to be explicitly defined or initialized before they can be referenced, although it is good programming practice to do so. To encourage this the KCML workbench will underline variables that were not dimensioned. Constants whose name begins with an underscore must be defined and initialized. Alpha variables are automatically initialized to blanks and numeric variables are initialized to zero. Each element of an array is also initialized in the same way.

Scalar variables can be initialized within [DIM](DIM.htm) and [COM](COM.htm) statements. For numeric variables the initialising value can be any numeric expression that can be evaluated at resolve time. This means that if and numeric variables are to be included within the expression then they must have previously been defined as common and be set to the required value in a previous program. Variables can also be initialized outside of a COM or DIM statement with a regular assignment statement for example:

total = 0 result = new / old

Individual elements of an array can be set with a normal assignment statement. All elements of numeric arrays can be initialized to either zero or one by specifying the ZER and CON keywords, for example:

figures() = ZER totals() = CON

Alpha variables can also be initialized in the same way, although when initialising via the DIM or COM statements only a literal or HEX( value may be specified, string expressions are not allowed, for example:

DIM title\$ = "Number 1",esc\$ = HEX(1B)

Note that the size of the literal specified for string scalars determines the size of the variable. Entire alpha variables and arrays can be initialized to a specific value by specifying the ALL( function, for example:

contents\$() = ALL("A")

would set each byte of *contents\$()* to "A".

If multiple variables of the same type are all to be set to the same value then each variable can be separated by a comma, for example:

total, count, value = 100 first\$, last\$, next\$, previous\$ = "ABCDEFG"

Constants

Constants are either literals such as 2, 3.14, 1.5E10 or variables that start with an underscore such as \_BUFSIZE. These latter type of constants have their value set in a DIM or COM and they then cannot be used in an expression that might change it so DIM \_BUFZISE=1024 is allowed but \_BUFSIZE=2048 is not. There is a special constant \#PI for the value 3.14159265359.

The READ and DATA statements

As well as the conventional methods of initialising variables described above, variables can also be initialized by reading values from a list of static values stored by the [DATA](DATA.htm) statement.

When a [READ](READ.htm) statement is executed from within a program, the next sequential item held in the [DATA](DATA.htm) statements will be assigned to the variable(s) in the READ statement, the data pointer is then moved to the next item in the [DATA](DATA.htm) statements. Initially the data pointer is pointing at the first data statement in the program. The [RESTORE](RESTORE.htm) statement can be used to reset the data pointer back to the beginning of a specific [DATA](DATA.htm) statement. If there is insufficient data for the [READ](READ.htm) statement then an error will occur.

Pointers

Pointers allow the programmer to reference the contents of variables without knowing the variable name. Each **KCML** partition has a symbol table containing references to variables, constants, subroutine names etc. for the program currently held in memory. The [SYM(](SYM(.htm) function can be used to return a unique symbol index value of the specified variable. The index value is returned as an integer which can later be used with a second form of [SYM(](SYM(.htm) to access the variable wherever the variable type is valid. For example:

DIM abc\$110 var1=SYM(abc\$) SYM(\*var1)\$="HELLO WORLD" PRINT SYM(\*var1)\$

would print the words "HELLO WORLD!".

The symbol index can be obtained for alpha, numeric and field variables and arrays.

Pointers allow much more generalised subroutines to be written, which will also execute quicker as the contents of the variables do not need to be copied into and back from the subroutine.

Refer to the [Pointers chapter](TutorialSym.htm), in this volume for more information.

Reserved words and spaces

Since **KCML** permits multi-character variable names, spaces are often significant in separating words in program lines, and certain words (e.g. [PRINT](PRINT.htm), [READ](READ.htm), [LOAD](LOAD.htm) etc.) are reserved by **KCML** and cannot be used for variable names. A full [list of reserved words](resword.htm) can be found in the Appendix. For instance:

SELECTINPUTname\$

would error as there are no spaces to separate the reserved words. This could in fact be the start of a string assignment statement, or could be a [SELECT INPUT](SELECT_INPUT.htm) statement with the device name specified by the variable *name\$*.

As **KCML** compiles each line, it must recreate the source to allow the editor to display the code. To improve readability, spaces are inserted into the source when it is recreated. These spaces are not stored in the program itself. To make long variable names more readable they are displayed in lower case while **KCML** reserved words are in upper case.

Using double quotes (")

Double quotes are used to determine the start and end of text that is not a **KCML** instruction, i.e. text that is to be printed on the screen, filenames for I/O statements and commands, or text that is to be assigned to an alpha variable. E.g.

PRINT "This is a test!" tmp\$="Testing" SAVE "File99"

To display or assign the double quotes character itself two sets of double quotes must be entered, the first set is used to instruct **KCML** to ignore the next. For example:

PRINT "The double quote "" character!"

would print the following:

The double quote " character!

The following lines are also valid under **KCML**:

IF abc\$=="""" THEN ret = ‘Get_Next_Record() STR(zyx\$,99,2)=""""""
