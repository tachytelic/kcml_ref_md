User functions in KCML

The UFN interface

The interface between KCML and the UFN's converts parameters from KCML internal form for example BCD number or fixed size string to a standard C form for example int, double, or null terminated string as specified by the UFN. It then puts the parameters into a table and calls the UFN with a pointer to the table. The UFN returns, possibly with an error status, and the interface converts the receiver parameters back to KCML internal format.

Support for UFN's is through two files, *uf_samp.c*, a C program external to KCML and *uf_pub.h*, a header file for *uf_samp.c*. The makefile uf_samp.mak can be used to build this sample.

The interface to UFN's is by a single call to uf_ext() during the initialization of KCML and direct calls to the UFN's when the [CALL](CALL.htm) statement is executed. This is so that dynamic linking can be used with Unix 5.4.

Initialization

The programmer must provide the a function in his library with the name and type of UFN_Spec \* UFN_API uf_ext(UFN_Subs \*p) { /\* return pointer to table \*/ return UFN_Table; }

KCML will call this during its initialisation to get a pointer to the table of UFNs specified in this library. The programmer can also perform any required one off initialization at this time. The argument passed into this reoutine is now obsolete but is preserved for compatibility.

The layout of the table whose address is returned is defined in the next section.

Specification of UFN

UFN's are defined in *uf_samp.c* which declares an array of UFN specifications for all the possible UFN calls. Each element of the array is of type UFN_Spec and it specifies the name by which the UFN is known in KCML, the entry point into the external C routine and a list of the parameters to be passed. The layout of this table is the responsibility of the programmer. It must be in sorted order of UFN name. When KCML starts up it calls the routine uf_ext() in *uf_samp.c* which returns a pointer to this table back to KCML.

The typedef for UFN_Spec may be found in uf_pub.h.

typedef struct UFN_Spec { CONST char name\[UFN_NAMELEN\]; /\* name CALL'ed in KCML \*/ UFN_RET (UFN_API \*function)(UFN_VALUE \*); /\* pointer to C function\*/ unsigned char Param\[MAXPARAMS\]; /\* parameter list \*/ };

The values in the elements of the parameter list specify the type of storage expected for that parameter by the C routine. High order bits can optionally be set by macro to indicate that the parameter value must be returned to KCML after the call. This RCVR() macro must be used for parameters that follow the TO in the CALL statement. Other bits are set for arrays and optional fields.

An example specification table follows:

UFN_Spec UFN_Table\[\] = { /\* { Comment "Name", function, Param\[1\], param\[2\], ... param\[MAXPARAMS\] }, \*/ { /\* convert DD/MM/CCYY to julian date \*/ "R7_DATE2J", r7_date2j, STR, RCVR(INT) }, { /\* convert julian date to DD/MM/CCYY \*/ "R7_J2DATE", r7_j2date, INT, INT, RCVR(STR) }, /\* last entry has an empty string name \*/ { 0 }, };

where, in uf_pub.h:

|  |  |
|----|----|
| MAXPARAMS | 12 - the maximum number of parameters allowed. Do not change this. |
| RCVR(x) | Marks x as a receiver parameter that must follow the TO. In the original UFN implementation the parameters before the TO were passed down to the function and only those after the TO had their values returned. In the current implementation any parameter changed in the function will be returned but you should still stick with this convention. |
| CSTR | Indicates the parameter is a C string (NULL terminated. May NOT contain NULLs). KCML will strip trailing blanks before sending down and will retore them if returned. |
| STR | Indicates the parameter is a KCML string (not NULL terminated. May contain NULLs). This can be used for structures. |
| INT | Indicates the parameter is a 4 byte signed integer. |
| DOUBLE | Indicates the parameter is a 8 byte double. |

The above code defined two routines

- R7_DATE2J which is passed a KCML string containing a date and returns an integer representing the corresponding Julian date
- R7_J2DATE is passed two ints for a Julain date and a length and returns the date of that length as a KCML string.

They could be called by the following program:

CALL R7_DATE2J "TODAY" TO todays_date PRINT todays_date CALL R7_J2DATE 2448188, width TO the_date\$ PRINT the_date\$

Which would have the output:

2448194 24/10/90

Note:

1.  The UFN_Table *must* be in sorted order by name. This is because a binary search is used to find the function. If this is not done KCML may not find the UFN_Table entry and error with 'P38 Undefined user function'.
2.  The UFN_Table must be terminated by an entry with a NULL name.
3.  For the compiler to insert a pointer to the UFN, the UFN routine must be declared in uf_samp.c before the declaration of UFN_Table. e.g. static UFN_RET UFN_API r7_date2j(UFN_ARGS);
4.  There are other types of parameters, not covered in this example, eg SYMBOL, OPTIONAL(x), ... see comments in *uf_pub.h*. Note that FD and ARRAY are obsolete.
5.  Truncation will occur if a KCML variable is passed to a function which requires an integer. eg 987.654 will be passed to an INT as 987, and 9.87e-10 as 0. The range of a 4 byte integer is <u>+</u> 2 147 483 647.
6.  There will also be problems if the variable is out of range of an integer. eg, 7.2354E26 passed to an INT will cause a C61 - Overflow number too large.
7.  Zero terminated C strings are provided as a convenience. KCML has to allocate space for the string and copy the string into that space in order to be able to insert the terminating '\0' after the last non-blank character so there is an overhead price to be paid. With KCML strings no copying is required and a pointer to the string is passed together with the defined length. If a C string is returned to KCML then it will be padded with blanks when copied into the receiver variable.

CALLing a User Defined Function.

A UFN is called with a pointer to an array of parameters held within KCML's data segment. The parameter block is of type UFN_value\[\]. where the UFN_Value is defined as:

typedef union UFN_Value { KCMLDOUBLE nval; /\* numeric value \*/ KCMLINT ival; /\* integer value \*/ UFN_Pstr s; /\* string \*/ UFN_Pna na; /\* numeric array \*/ UFN_Psa sa; /\* string array \*/ KCMLINT fd; /\* file descriptor \*/ UFN_Sym sym; /\* symbol \*/ } UFN_Value;

This is a union of all the possible representations of a parameter. The programmer should use the element appropriate to the type specified. To help with this a number of useful macros have been defined

\#define NVAL(x) (pb\[(x)\].nval) \#define IVAL(x) (pb\[(x)\].ival) \#define NINT(x) (IVAL(x)) \#define SVAL(x) (pb\[(x)\].s.sptr) \#define SLEN(x) (pb\[(x)\].s.slen) \#define SATTR(x) (pb\[(x)\].s.attr) \#define SYPTR(x) (pb\[(x)\].sym.sym_ptr)

KCML strings require information about the length of the string to be passed so a structure is required.

typedef struct UFN_Pstr { unsigned char \*sptr; /\* pointer to slen bytes \*/ unsigned int slen; /\* length of string \*/ }

The structures UFN_sa and UFN_na which define the dimensions of string and numeric arrays are defined in uf_pub.h.

For example the routine r7_date2j() starts

UFN_RET UFN_API r7_date2j(UFN_Value \*pb) { char \*dp; int dlen; ... }

Then the first argument *todays_date\$* which is a KCML string of type STR can be accessed inside the routine by :

dp = SVAL(0)

and its length can be found from

dlen = SLEN(0);

The returned parameter todays_date which was specified as RCVR(INT) could be set by

NINT(1) = 0;

Return value

The return value of the UFN routine can be used to produce KCML error messages. These are

Return value

Error message

0

success - no error

1

S24 - Wrong parameters supplied to user function

2

P46 - Error from user function.

3

S22 - Unrecoverable error in user function

\>3

X75 - Illegal number

Miscellaneous

There are two statements in KCML which can be used with UFNs

LIST U This lists all user defined functions and their usage, e.g.

LIST U R7_DATE2J str TO int R7_J2DATE int, int TO str

LIST CALL This prints a table of CALL commands against the lines on which they occur, e.g.

LIST CALL R7_DATE2J - 00010 R7_J2DATE - 00030

Linking KCML

To build the sample shared library you will need uf_samp.c, uf_pub.h and uf_samp.mak. These are all installed in the normal /usr/lib/kcml directory for Unix systems. Inspect the makefile uf_samp.mak and uncomment the CFLAGS compiler definitions appropraite to your platform then issue make -f uf_sampl.mak

to build the library which will usually be called uf_samp.so (except on HP-UX where it is uf_samp.sl). It can then be used changing the way KCML is invoked in .profile to add a -x switch e.g. kcml -x uf_samp.so START

Memory allocation

By default KCML uses its own memory allocator which is optimised for the typical memory requests that KCML makes. It also has the ability to release memory on Unix servers using the sbrk() system call. It reserves a small amount of memory (128kb but adjustable with the [MALLOCSPACE](EnvVars.htm#MALLOCSPACE) environment variable) for use by the C runtime library. This can cause a problem if you use a shared library on some versions of Unix and that library allocates significant amounts of memory. While KCML can coexist with an allocator that manipulates sbrk() the converse is not always true. Linux is one example.

To avoid these issues you should either set the [USEMALLOC](EnvVars.htm#USEMALLOC) environment variable or supply the -y [command line switch](kcml.htm#switch) to KCML if you use a shared library that allocates memory. This means that space will not be released on [\$SPACE]($SPACE.htm) or [LOAD](LOAD.htm).
