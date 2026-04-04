TERMINFO grammar

This section, and the other sections in this chapter, are probably only relevant to users of KCML running on UNIX platforms. However it is a possibility that you could connect a text mode terminal to an NT server using TERMINFO to describe its capabilities.

Within each section of the source file (*TERMINFO/src*) are a number of definitions for keys or for screen command sequences. A definition line is made up of three fields; a special definition code followed by an '=' sign followed by a definition string. A list of allowed definition codes is given in the next sections. Definition codes are not case sensitive. Some definition codes are followed by parentheses enclosing a number which can be in decimal, hexadecimal (starts with 0x) or octal (starts with 0) notation. Blanks and tabs are allowed before and after but not within each field. Entirely blank lines are ignored. Text following a '#' character is considered to be a comment and is ignored to the end of the line.

The definition strings contain ordinary characters or escaped characters which follow a backslash or caret. Recognised escapes codes are:

|          |                       |      |
|----------|-----------------------|------|
| \e or \E | Escape                | 0x1B |
| \r       | Carriage return       | 0x0D |
| \n       | Line feed or new line | 0x0A |
| \b       | Backspace             | 0x08 |
| \s       | Space                 | 0x20 |
| \t       | Tab                   | 0x09 |
| \\       | Backslash             |      |
| \\       | Caret ^               |      |
| \\       | Hash or pound sign \# | 0x23 |

A zero following a backslash starts an octal number which continues for 3 digits or until the next character that is not an octal digit. A hexadecimal number is represented by \x or \0x followed by two hexadecimal digits e.g. \x1F. Backslash is a general escape character and any character following a backslash, other than those listed above, is considered to represent itself. A character following a caret is considered as a CTRL character and is masked with 0x1F. e.g. ^h is equivalent to \b or \x08.

Some definitions are for Boolean properties and can be defined with a Boolean parameter such as '1' or 'true' for true and '0' or 'false' for false.

Other parameters are numeric (e.g. 'Lines' for the number of rows on a screen) and can be represented by unsigned integers between 0 and 255.

Parameterized screen commands are interpreted by KCML using a post fix operator notation and a small internal stack. There are also 26 static registers which can be used for long term storage (e.g. to hold information about the current font selected). At the start of the sequence the stack is empty. Special operators beginning with '%' signs push or pop characters using this stack. Any other characters are sent directly to the screen. The operators are:

|  |  |
|----|----|
| %% | Outputs '%'. |
| %p\[1-9\] | Pushes parameter 1 to 9 on the stack. |
| %c | Pops character from stack and outputs it. |
| %\[\[:\]flags\]\[width\[.precision\]\]\[doxX\] | Pops integer from stack and printf's it. |
| %{nn} | Pushes a decimal constant nn. |
| %'x' | Pushes a character constant 'x'. |
| %P\[a-z\] | Pop int and save in static variable \[a-z\]. |
| %g\[a-z\] | Read static variable \[a-z\] and push it. |
| %+ | Pop and add to new stack top. |
| %- | Pop and subtract new stack top. |
| %\* | Pop and multiply new stack top. |
| %/ | Pop and divide new stack top. |
| %m | Modulus. |
| %& | Bitwise AND. |
| %\| | Bitwise OR. |
| %^ | Bitwise XOR. |
| %~ | Bitwise NOT. |
| %= | Logical equals. |
| %\> | Logical \>. |
| %\< | Logical \<. |
| %A | Logical AND. |
| %O | Logical OR. |
| %! | Logical NOT. |
| %i | Add 1 to each parameter. |
| %r | Convert IBM PC colors to ANSI. |
| %?expr%t thenpart %e elsepart %; | IF THEN ELSE construct, *elsepart* is optional. |

A typical sequence is the cursor positioning sequence for a VT100

CurPos = \E\[%i%p1%d;%p2%dH

which uses the special '%i' operator to convert the row and column values passed to it into values counted from one rather than from zero. The first two characters '\E\[' are output directly. The '%p1' pushes the row value (already incremented by '%i') and '%d' pops it and *printfs* it as a decimal number. A semi-colon is output directly and the same process is repeated for the column in '%p2'.

A more complex sequence is the *AttribOn* sequence used to set attributes. Up to four attributes can be set and they are passed in the Boolean parameters

|     |              |
|-----|--------------|
| %p1 | bold         |
| %p2 | blink        |
| %p3 | reverse      |
| %p4 | underline    |
| %p5 | always false |

The '%?' construct can be used to test the Boolean parameters and issue sequences according to whether each parameter tests true or false. Again for the VT100

AttribOn=\E\[%?%p4%t;4%;%?%p3%t;7%;%?%p2%t;5%;%?%p1%t;1%;m

which initially issues '\E\[' then tests '%p4' and if true issues ';4' for underline. Similar tests can add other attributes before the final 'm'. In this example the optional else clause is not used. The '%p5' parameter is only used for if the description has been automatically converted from a UNIX TERMINFO description which uses a slightly more complex expression.
