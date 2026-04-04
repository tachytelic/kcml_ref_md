\$DECLARE syntax

Functions

\$DECLARE can only be used to call DLL functions that are defined as FAR PASCAL, \_\_stdcall or WINAPI.

Passing by value

\$DECLARE can pass only integers and doubles by value. All other types of object, e.g. strings or structures, must be passed by reference. It is also possible to pass integers and doubles by reference using BYREF.

Return values:

Only integers and doubles can be returned as the value of a function.

In general if you do not intend to use the return value of a routine, then do not specify it in the \$DECLARE as this avoid an unnecessary copy being done on your behalf by KCML.

If no TO clause is present then the function will be assumed to return type INT() by default i.e. the unsigned natural integer for Windows (32 bits for Windows 9x and Windows NT). If the function returns void then it is up to the programmer not to use the return value which will be undefined. To return integers of a specific size use the TO INT(n) clause where n is 1,2 or 4 and to return signed integers use a unary minus.

To return an IEEE double use NUM().

Return values which are single precision floating point numbers, pointers to strings or structures are not supported.

| C declaration     | \$DECLARE equivalent         |
|-------------------|------------------------------|
| DWORD sub1(void)  | \$DECLARE 'sub1() TO INT(4)  |
| SWORD sub2(void)  | \$DECLARE 'sub2() TO INT(-2) |
| int sub3(void)    | \$DECLARE 'sub3() TO INT(-)  |
| double sub7(void) | \$DECLARE 'sub7() TO NUM()   |

Passing numbers as arguments:

When passing an integer by value to a \$DECLARE'd subroutine use INT() or INT(n). The former is the natural integer for the version of Windows. If the API call specifies a specific size n then use INT(n). If a signed rather than an unsigned integer is required then use a unary minus

|                        |                         |
|------------------------|-------------------------|
| void sub1(int arg)     | \$DECLARE 'sub1(INT(-)) |
| void sub2(DWORD arg)   | \$DECLARE 'sub2(INT(4)) |
| void sub3(double farg) | \$DECLARE 'sub3(NUM())  |

| C declaration  | \$DECLARE equivalent |
|----------------|----------------------|
| char           | INT(-1)              |
| int            | INT(-)               |
| short          | INT(-2)              |
| long           | INT(4)               |
| unsigned char  | INT(1)               |
| unsigned int   | INT()                |
| unsigned short | INT(2)               |
| unsigned long  | INT(4)               |
| double         | NUM()                |
| BYTE           | INT(1)               |
| WORD           | INT(2)               |
| DWORD          | INT(4)               |
| BOOL           | INT()                |
| HWND           | INT()                |
| HDC            | INT()                |
| HINSTANCE      | INT()                |
| HANDLE         | INT()                |

A summary of the C types in Windows.h and the corresponding types used in \$DECLARE definitions {width="100%"}

| C declaration | \$DECLARE equivalent |
|---------------|----------------------|
| UCHAR         | INT(1)               |
| SCHAR         | INT(-1)              |
| SWORD         | INT(-2)              |
| UWORD         | INT(2)               |
| SDWORD        | INT(-4)              |
| UDWORD        | INT(4)               |
| ULONG         | INT(4)               |
| SLONG         | INT(-4)              |
| RETCODE       | INT(2)               |

Other common C types used in Windows programs {width="100%"}

Passing null terminated strings to a function

Strings are always passed by reference, that is a pointer to the start of the string is pushed on the stack. Null terminated C strings can be passed to a function using STR(). This specification causes KCML to strip trailing blanks from the string and substitute a null character when copying the argument to the Windows stack. A NULL pointer can be passed as a numeric zero. For example to replace the window title of the active window a C programmer might write int GetWindowText(HWND hEnd, LPSTR szTextBuf, int buflen); HWND GetActiveWindow(void); char Title\[64\]; HWND hWnd; hWnd = GetActiveWindow(); GetWindowText(hWnd, Title, sizeof(Title)); SetWindowText(hWnd, "Hello World"); and a KCML programmer would do something like \$DECLARE 'GetWindowText(INT(), RETURN STR(), INT()) \$DECLARE 'SetWindowText(INT(), STR()) \$DECLARE 'GetActiveWindow() DIM title\$64, hwnd hwnd = 'GetActiveWindow() 'GetWindowText(hwnd, title\$, LEN(STR(title\$))) 'SetWindowText(hwnd, "Hello world")

If the string is passed back from Windows to the application then specify the RETURN prefix to STR() to tell KCML that the string is not to be sent to Windows but is to be copied back. If a structure is to be passed to a Windows function which will alter its contents so that the KCML variable has to be updated then the TO RETURN prefix is needed. In this case KCML will copy the structure down to Windows and then back again after the routine has executed. Only specify this prefix if you need the updated values as omitting it will make the call execute quicker. When RETURN STR() is used KCML will copy the string up to the null character into the string variable argument and blank fill the rest of the string.

| C declaration | \$DECLARE equivalent |
|---------------|----------------------|
| char \*       | STR()                |
| LPSTR         | STR()                |
| LPCSTR        | STR()                |

Typical C types and the \$DECLARE equivalents {width="100%"}

Passing other strings to a function

To pass a pointer to a fixed length string to a function KCML must be informed of its size using DIM(n). If the size is omitted e.g. DIM(), then KCML will use the size of the argument passed to the function.

Passing pointers to numbers

Sometimes a pointer to an integer is required. To do this you must prefix the number with BYREF in the actual call as well as using a RETURN in from of the parameter in the \$DECLARE to tell KCML to push the address rather than the value. For example in ODBC where SQLAllocEnv is defined as RETCODE SQLAllocEnv(HENV FAR \*henv);

a KCML programmer would write something like \$DECLARE 'SQLAllocEnv(RETURN INT(4)) TO INT(-2)="ODBC32.SQLAllocEnv" rc='SQLAllocEnv(BYREF phenv)

This example shows a peculiarity of ODBC API, designed in the 16-bit era, where functions return signed shorts rather than ints.

Passing the address of a structure to a function

One way to do this is to consider the structure as a fixed length string and use the DIM() keyword. This will work provided the structure does not contain any pointers. The structure size can be estimated as the sum of the sizes of the components of the structure or it can be determined in a C program with the sizeof operator. The default settings for all common Windows compilers do not pad structures. If the size is overestimated this will generally only affect performance as extra characters will have to be copied.

Structures may be represented in KCML as strings or string arrays. To access the components of a structure either fields or \$(UN)PACK can be used. When (un)packing integers from a structure use the HEX(D00x) format for unsigned and HEX(E00x) for signed integers as they are found in the structure in Intel byte order. To unpack floating point numbers use HEX(F308).

If the structure is passed back from Windows to the application then specify the RETURN prefix to DIM() to tell KCML that the string is not to be sent to Windows but is to be copied back. If a structure is to be passed to a Windows function which will alter its contents so that the KCML variable has to be updated then the TO RETURN prefix is needed. In this case KCML will copy the structure down to Windows and then back again after the routine has executed. Only specify this prefix if you need the updated values as omitting it will make the call execute quicker.

Structures can only be passed by reference. They can't be passed by value.

For instance, to get the size of the Windows desktop a C programmer would write something like HWND GetDesktopWindow(void); GetWindowRect(HWND hWnd, RECT FAR \*rc); RECT rc; int top, bottom; GetWindowRect(GetDesktopWindow(), &rc); top = rc.top; bottom=rc.bottom;

where the standard windows.h structure RECT is typedef struct tagRECT { int left; int top; int right; int bottom; } RECT;

and to do the same thing in KCML \$DECLARE 'GetDesktopWindow() \$DECLARE 'GetWindowRect(INT(), RETURN DIM()) DIM rect\$16, top, bottom, left, right 'GetWindowRect('GetDesktopWindow(), rect\$) \$UNPACK(F=HEX(E004 E004 E004 E0004))rect\$ to left, top, right, bottom Starting with KCML 5.03 it is possible to pass structures directly by spelling out the elements in the call. This is done by enclosing the structure definition within parentheses in the \$DECLARE definition. The above example could then be written as \$DECLARE 'GetDesktopWindow() \$DECLARE 'GetWindowRect(INT(), RETURN (INT(),INT(),INT(),INT())) DIM top, bottom, left, right 'GetWindowRect('GetDesktopWindow(), BYREF top, BYREF bottom, BYREF left, BYREF right)

Note that you add the delimiting parentheses in the definition and not the call. This technique has a major advantage over passing structures with DIM() in that these structures can contain pointers to strings. Nested structures are supported.

If a structure contains an integer member and it is altered by the function call, you need to use BYREF in the call in order to get the value. Normally this would imply passing by reference, i.e. that element was an int \* rather than an int, but as all structures are passed by reference there is no ambiguity. However it does mean that there is no way to specify that a structure element really is a pointer to an integer. To access such a member you will have to use DIM() and \$UNPACK as described above just for that member.

Because a structure is always passed by reference, all the elements of a structure are always sent to the client and returned without the necessity to specify RETURN or TO RETURN on the structure but if the element is itself a pointer, e.g. STR() or DIM(), the memory pointed to is not returned unless RETURN or TO RETURN is specified against the member. This may change in the future so for compatibility it is recommented that the structure itself is prefixed with RETURN or TO RETURN if the call will update elements and you want them copied back to the server.

A more complex example is looking up a keyword in a HtmlHelp file which requires passing the following structure as the last argument to the HtmlHelp function HWND WINAPI HtmlHelp(HWND hwndCaller, LPCSTR pszFile, UINT uCommand, DWORD \*dwData); typedef struct tagHH_AKLINK { int cbStruct; // sizeof this structure BOOL fReserved; // must be FALSE (really!) LPCTSTR pszKeywords; // semi-colon separated keywords LPCTSTR pszUrl; // URL to jump to if no keywords found (may be NULL) LPCTSTR pszMsgText; // Message text to display in MessageBox // if pszUrl is NULL and no keyword match LPCTSTR pszMsgTitle; // Message text to display in MessageBox // if pszUrl is NULL and no keyword match LPCTSTR pszWindow; // Window to display URL in BOOL fIndexOnFail; // Displays index if keyword lookup fails. } HH_AKLINK;

Note the embedded LPCTSTR string pointers.

DIM HH_KEYWORD_LOOKUP=0x0D \$DECLARE 'HtmlHelp(INT(),STR(),INT(),(INT(),INT(),STR(),STR(),STR(),STR(),STR(),INT()))="HHCTRL.OCX.HtmlHelp" 'HtmlHelp('GetDesktopWindow(), "kcmlrefman.chm", HH_KEYWORD_LOOKUP, 32, 0, "\$DECLARE'", 0, 0, 0, 0, 1)

The size of the structure passed in its first member was calculated to be 32 on the basis that the size of int, BOOL and LPSTR are all 4 bytes. The NULL pointers are passed as 0.

A still more complicated example is using Microsoft MAPI to send email. Click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard.

REM REM example of using Microsoft proprietary MAPI interface to send an email. Assumes you have a MAPI compliant email REM system e.g. Microsoft Outlook, Microsoft Exchange or Kerridge Kmail 3 REM REM implements this function. See MSDN for more details REM REM ULONG FAR PASCAL MAPISendMail( REM LHANDLE lhSession, REM ULONG ulUIParam, REM lpMapiMessage lpMessage, REM FLAGS flFlags, REM ULONG ulReserved REM ) REM REM note the pointer to the MapiMessage structure which is defined as REM typedef struct { REM ULONG ulReserved; REM LPTSTR lpszSubject; REM LPTSTR lpszNoteText; REM LPTSTR lpszMessageType; REM LPTSTR lpszDateReceived; REM LPTSTR lpszConversationID; REM FLAGS flFlags; REM lpMapiRecipDesc lpOriginator; REM ULONG nRecipCount; REM lpMapiRecipDesc lpRecips; REM ULONG nFileCount; REM lpMapiFileDesc lpFiles; REM } MapiMessage, \*lpMapiMessage; REM REM and which itself refers to two MapiRecipDesc structures and a MapiFileDesc struct (which we do not use here) REM REM typedef struct { REM ULONG ulReserved REM ULONG ulRecipClass; REM LPTSTR lpszName; REM LPTSTR lpszAddress; REM ULONG ulEIDSize; REM LPVOID lpEntryID; REM } MapiRecipDesc, \*lpMapiRecipDesc; REM REM typedef struct { REM ULONG ulReserved; REM ULONG flFlags; REM ULONG nPosition; REM LPTSTR lpszPathName; REM LPTSTR lpszFileName; REM LPVOID lpFileType; REM } MapiFileDesc, FAR \*lpMapiFileDesc; REM REM As usual all the ULONG, LHANDLE and FLAGS ty\\ pdefs can be assumed to be INT() while the REM LPTSTR string elements are represented by ST\\ R() REM \$DECLARE 'MAPISendMail(INT(),INT(),(INT(),STR(),\\ STR(),STR(),STR(),STR(),INT(),(INT(),INT(),STR()\\ ,STR(),INT(),INT()),INT(),(INT(),INT(),\\ STR(),STR(),INT(),INT()),INT(),(INT(),INT(),INT(\\ ),STR(),STR(),INT())),INT(),INT())="MAPI32.MAPIS\\ endMail" REM DIM \_MAPI_DIALOG=0x08 DIM \_MAPI_LOGON_UI=0x01 DIM \_MAPI_TO=1, \_MAPI_CC=2, \_MAPI_BCC=3 DIM ReturnCode DIM recipaddr\$100 recipaddr\$ = "SMTP:" & "peter@bigco.com" DIM recipname\$="Peter" DIM ulRecipClass=\_MAPI_TO DIM subject\$="Test MAPI email" DIM body\$="Hello from KCML" DIM flFlags=\_MAPI_DIALOG + \_MAPI_LOGON_UI REM many of these args can be zero DIM lhSession=0, ulUIParam=0, ulReserved=0 REM Currently there is no support for arrays of \\ structures DIM nRecipCount=1, nFileCount=0 ReturnCode = 'MAPISendMail(lhSession, ulUIParam, \\ ulReserved, subject\$, body\$, 0, 0, 0, 0, ulReser\\ ved, 0, 0, 0, 0, 0, nRecipCount, ulRes\\ erved, ulRecipClass, recipname\$, recipaddr\$, 0, \\ 0, nFileCount, 0, 0, 0, 0, 0, 0, flFlags, ulRese\\ rved) STOP

Casting and polymorphic functions

The \$DECLARE syntax fixes the exact calling sequence for a function but many real life functions can cope with arguments of more than type or even different numbers of arguments based on context in some way. A classic example is printf() in the C library or SendMessage() in the Windows API where the meaning of the wParam and lParam arguments depends on the message. To cope with this KCML allows the use of an ellipsis to denote a variable number of arguments and functions to force how KCML or Kclient will send an argument at runtime. As the extra parameters passed in place of an ellipsis are not typed in the \$DECLARE you must type the arguments using the following functions

| Function | Purpose |
|----|----|
| INT() | Force the numeric argument to be passed as a 32 bit signed integer. This is in fact the default for a numeric value and can be omitted. |
| NUM() | Force the argument to be passed as a 64 bit floating point number. |
| DIM() | When applied to a string array it forces the data to be copied as an array and not a single string as would be the normal KCML convention. |

An example of using an ellipsis is the 'KCMLOleMethod() call used in KCML 5.02 to access COM methods (in KCML 6.0 the OBJECT syntax has replaced this usage). \$DECLARE 'KCMLOleMethod(INT(),STR(),...) a = 'KCMLOleMethod(range, "Value", BYREF NUM(t)) a = 'KCMLOleMethod(range, "Value", REDIM a\$())

The prefix REDIM implies RETURN and can be used to tell KCML to adjust the dimensions of the array to fit the data supplied by the function.

Examples

void sub1(char \*str) \$DECLARE 'sub1(STR()) void SetText(LPSTR lpszTitle) \$DECLARE 'SetText(STR()) void GetRect(RECT \*rct) \$DECLARE 'GetRect(DIM(8))

The current window puzzle

Many DLL calls need to open windows of their own and need to be passed the window handle of the calling task in order to give them a parent. This is fine for an application that opened the window itself but for a KCML program the window was created during startup by the interpreter and the application programmer does not have the handle to hand. Often you can get by by passing zero, as by convention this is the handle of the desktop, but this is not satisfactory as it can cause focus to be lost by KCML. In particular it is then possible to minimise KCML leaving the new window on the screen or to ALT TAB the KCML window on top of the new window obscuring it with a window that will not accept input.

To get an actual handle the normal trick is to assume KCML has the focus and to use the GDI routine GetFocus() to get the window with the focus. This is not quite right however as KCML input is actually owned by a child window overlaid on the main window. This main window is the window handle required by routines that need to resize, move or adjust the style of the main window, e.g. GetWindowText(). This handle can be found by using GetParent() and passing it the child handle or more directly by calling GetActiveWindow().

Best of all is to use 'KCMLGetWindow() which will always return the correct parent window for Kclient.

Converting 16 bit \$DECLARE to 32 bit

Kclient is a 32 bit application and you may find that some existing \$DECLARE calls originally written for 16 bit WDW will not work. In 16 bit Windows 3.x the case of a function name was not significant but in Win32 it is. Programs written for KCML3 or KCML4 held the name of the function in uppercase though they usually rendered it in lower case when listing the program in the editor thus \$DECLARE 'setwindowtext(INT(), STR())

Alas most Windows API functions are actually mixed case.

Luckily, the \$DECLARE syntax allows us to specify an alternative function name, and as this will be enclosed in quotation marks, KCML will preserve the case. For example, to make the above call work, the syntax could need to changed to read: \$DECLARE 'SETWINDOWTEXT(INT(), STR())="SetWindowText"

Even easier you can make use of the fact that KCML5 can preserve the case of variables and type something like \$DECLARE 'SetWindowText(INT(), STR())

Note that the KCML/WDW specific functions (such as KCMLCreateControl, etc.) are handling internally within Kclient and will work regardless of case, but they should be changed to use the correct case in their declaration for future compatibility.

\$DECLARE and 32 bit Message Numbering

Another difference between 16 bit and 32 bit Windows is the ID's of some message numbers that are used with controls such as list boxes, combo boxes, edit controls, etc. For example, to add a string to a list box, you might have had legacy code that looks something like this: \$DECLARE 'senddlgitemmessage(INT(), INT(), INT(), INT(), STR()) LB_ADDSTRING = 0x0401 . . 'senddlgitemmessage(dialog_hwnd, listbox_id, LB_ADDSTRING, 0, "String to add")

Under 32 bit Windows, the message ID for LB_ADDSTRING has changed, so the code would have to be rewritten to look something like this: \$DECLARE 'SendDlgItemMessage(INT(), INT(), INT(), INT(), STR()) LB_ADDSTRING = 0x0180 . . 'SendDlgItemMessage(dialog_hwnd, listbox_id, LB_ADDSTRING, 0, "String to add")

defining the case of the function in \$DECLARE and using the new value for LB_ADDSTRING.
