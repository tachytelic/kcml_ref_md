\$DECLARE

<div class="Generalform">

General Form:\
\
     \$DECLARE 'name\[(arg1\[, arg2\] ...) \] \[ TO retarg\] \[=dllspec\]\
\
Where:\

|  |  |
|----|----|
| name | = an alphanumeric description identifying the function. |
| arg1\[,arg2\]... | = DLL argument specifiers |
| retarg | = optional return value specifier |
| dllspec | = alpha expression for optional DLL module and entry point |

</div>

------------------------------------------------------------------------

The \$DECLARE statement provides direct access to native operating system functions. In the case of Windows NT or Windows 9x these functions lie within Dynamic Link Libraries (DLLs) on either the client or the NT server itself. On some Unix platforms, currently Unixware 7, Linux, HP-UX and AIX 4.2 or later, it is also possible to access functions in Unix shared libraries using \$DECLARE. On all KCML server platforms, both Unix and NT, it is possible to use \$DECLARE to access Windows DLL functions by directing the request through the client. The \$DECLARE statment formally defines the name and location of the remote function in its DLL and its calling interface in terms of the number and type of the expected arguments. Given this information the function can be invoked using a normal [GOSUB'](GOSUBquote.htm) call.

The *dllspec* string on the right hand side is an alpha expression which evaluates to a string defining the DLL module name or Unix shared library and the DLL entry point name in the form of "module.function". The module name is optional and can be omitted if the module is one of the standard modules (see below). On NT the module name case is not significant but it is for Unix shared libraries. The extension may be omitted if it is the standard for the platform (.DLL on Windows and .so on Unix). The function name must be spelt correctly in its intended case though it too can be omitted if the function name on the left hand side is spelt in the correct case. For example, the following would be used to define the [MessageBox](MessageBox.htm) function from the module USER32.EXE:

\$DECLARE 'MessageBox(INT(),STR(),STR(),INT())="USER32.MessageBox"

The module name may be omitted from the *dllspec* if the function is in one of the standard preloaded libraries. The standard library search list for Windows is

|              |
|--------------|
| USER32.DLL   |
| KERNEL32.DLL |
| GDI32.DLL    |
| SHELL32.DLL  |
| ADVAPI32.DLL |
| GSWDLL32.DLL |

and for Windows CE it is

|             |
|-------------|
| coredll.dll |
| gwes.exe    |

while for Unix is

|         |
|---------|
| libc.so |

The function name may also be omitted if it is spelt with the right case in the declaration and KCML is preserving case. Normally KCML preserves in the programs symbol table the case used in a \$DECLARE though this can be disabled with a [\$OPTIONS LIST]($OPTIONS_LIST.htm) setting. Thus all that is needed for the above definition is

\$DECLARE 'MessageBox(INT(),STR(),STR(),INT())

Executing on the server

By default \$DECLARE functions are executed by the client as this works for both Unix and NT servers. However a program can force a \$DECLARE function to execute on the server rather than the client by either prefixing the module name with an asterisk, i.e:

\$DECLARE ‘SQLAllocEnv(RETURN INT())="\*ODBC32.SQLAllocEnv"

The same effect can be achieved by setting the HEX(80) bit in byte 35 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE35) for the duration of the call. The former method defines the function as always executing on the server whereas the latter method allows a dual mode function that can execute on either the server or the client. This second method may be more flexible but it requires explicit programming to ensure that the bit is set appropriately for each call. It is also necessary to preserve the other bits in byte 35 when the HEX(80) bit is toggled. This is best done with code of the form

REM force server execution\
STR(\$OPTIONS RUN,35,1) = OR HEX(80)\
...\
REM force client execution\
STR(\$OPTIONS RUN,35,1) = AND HEX(7F)

Controlling how arguments are passed

If the function expects arguments or returns a value then KCML must be informed of their type and how to pass them to the DLL. This is done with arguments to \$DECLARE that define the type of the corresponding parameter in the GOSUB’ call using a number of keywords viz.

|  |  |
|----|----|
| INT(2) | Short (2 byte) integer. |
| INT(-2) | Signed short (2 byte) integer. |
| INT(4) | Long (4 byte) integer. |
| INT(-4) | Signed long (4 byte) integer. |
| INT() | Natural machine integer (2 bytes for 3.x, 4 bytes for NT) |
| INT(-) | Signed natural machine integer (2 bytes for 3.x, 4 bytes for NT) |
| NUM() | Double precision floating point. |
| STR() | Null terminated string (trailing blanks are automatically stripped). |
| DIM() | Structure (the parameter is passed in its entirety). |
| DIM(n) | Structure (the structure size must be greater than or equal to n). |

Prior to KCML6 there was also a STR(DIM) keyword which could be used to pass a KCML string array as an array of string pointers. Because of internal changes in KCML this functionality is no longer available and will result in an S24 error at runtime. Such strings should now be passed as a structure.

By default, arguments are passed by value to the remote function so that the values of arguments are not altered. Two prefixes are available for other behaviour:

|  |  |
|----|----|
| RETURN | No value is passed to the subroutine, but data is returned. This prefix may not be used on integral or floating-point types or with string arrays. |
| TO RETURN | Data is passed to the remote function and returned from it. This prefix may not be used on integral or floating-point types or with string arrays. |

<span id="RETURN in $DECLARE"></span>

If the argument is a pointer to an **int** or **double** then it is necessary to prefix the variable in the call with the [BYREF](BYREF.htm) or RETURN keyword to tell KCML to push the address before calling the function. This is only necessary for pointers to numbers as strings and structures are always passed as pointers whereas the default action for numbers is to pass the value. Note it is still necessary to specify RETURN or TO RETURN for this argument in the \$DECLARE definition if the object pointer to will be changed. Thus to open a registry key:

\$DECLARE 'RegOpenKey(INT(), STR(), RETURN INT())\
'RegOpenKey(HKEY_LOCAL_MACHINE, key\$, BYREF hkey)

Where strings or structures are expected by the DLL function it is permissable to pass 0 to indicate a NULL pointer.

If a function result is specified, it must be of numeric type. If none is specified, then **int** is assumed (the majority of functions are of type **int**). It is possible to use either GOSUB 'name or to use 'name() from within an expression to call a function, the return value being ignored in the case of a [GOSUB'](GOSUBquote.htm).

\$DECLARE is interpreted only at resolve time when an entry for the subroutine name is placed in the symbol table. A subsequent [LOAD](LOAD.htm) statement will remove the symbol. \$DECLARE statements in the currently selected global partition make the subroutines names available to the foreground partition according to the normal rules for finding subroutines in globals.

If the DLL function cannot be found at runtime within any of the search DLLs a P38 error will result. Incorrect or invalid arguments give an S24 error.

For more information about \$DECLARE see [\$DECLARE syntax]($DECLAREsyntax.htm) in this manual. For information about DLLs and the Windows API see the Microsoft Platform SDK documentation or the Microsoft Developer network CD. Details of special DLL functions exported by Kclient may be found in the [Developer Information](mk:@MSITStore:kclient.chm::/shared/introsplash.htm) section of the Kclient manual.

Example:

KCML can retrieve the current title and replace it with one of its own using the GetWindowText() and SetWindowText() functions in the Windows API:

\$DECLARE 'GetWindowText(INT(),RETURN STR(),INT())="GetWindowText"\
\$DECLARE 'SetWindowText(INT(),STR())="SetWindowText"\
\$DECLARE 'GetFocus()="GetFocus"\
\$DECLARE 'GetParent(INT())="GetParent"\
DIM old\$32,hwnd\
hwnd = 'GetParent('GetFocus())\
'GetWindowText(hwnd,old\$,len(str(old\$)))\
'SetWindowText(hwnd,"New title")

The use of 'GetParent() is necessary here as both KCML uses multiple overlapping windows and the window with focus is a child of the parent which owns the title bar.

Performance considerations:

To get the best performance out of calls to Windows routines in the client, byte 35 of the [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE35) system variable can be set to change the behaviour of calls to remote functions. This byte uses a bit pattern mechanism to set the various options. The available bits are as follows:

|  |  |
|----|----|
| HEX(00) | Always wait for a reply from the routine, this is the default case. |
| HEX(01) | Do not wait for a reply from the routine. With this bit set the routine must be called from a GOSUB’ statement and not from within an expression. |

For example, to instruct KCML to not wait for a reply from Windows remote functions where a return value is not required you could execute the following:

STR(\$OPTIONS RUN,35,1) = OR HEX(01)\
‘SetWindowText("Hello World!")\
STR(\$OPTIONS RUN,35,1) = AND HEX(FE)

This allows improved buffering and is considerably faster. However, you cannot use this asynchronous mode if a return value is necessary and the following program result in an S24 error at the value of title\$ must be returned:

STR(\$OPTIONS RUN,35,1) = OR HEX(01)\
‘GetWindowText(hwnd, title\$)\
STR(\$OPTIONS RUN,35,1) = AND HEX(FE)

Syntax examples:

\$DECLARE 'ourname=".GetParent"\
\$DECLARE 'GetWindowRect(INT(),RETURN DIM())\
\$DECLARE 'DisplayTif(STR())="TIFF.DisplayFile"\
\$DECLARE 'WinHelp(INT(), STR(), INT(),INT(4))\
\$DECLARE 'GetComputerName(RETURN STR(), TO RETURN INT())\
\$DECLARE 'HtmlHelp(INT(),STR(),INT(),INT())="hhctrl.ocx.HtmlHelp"\
\$DECLARE 'chmod(STR(), INT())="\*"

See also:

[GOSUB'](GOSUBquote.htm), [BYREF](BYREF.htm), [\$DECLARE syntax]($DECLAREsyntax.htm), ['MessageBox](MessageBox.htm)
