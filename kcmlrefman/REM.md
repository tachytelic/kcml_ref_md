REM

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\
<img src="bitmaps/rem.gif" data-align="BOTTOM" data-border="0" alt="rem.gif" />\
\
Where:\
\

<div class="indent">

text = any string of characters (except a colon which indicates the end of a statement)

</div>

\

</div>

------------------------------------------------------------------------

The REM statement is used to insert comment lines into a program. The statement is skipped when the program is executed. The comment extends from the REM to the next colon or the end of the line, whichever comes first.

KCML always inserts a space after the REM. When the program is displayed in the workbench, text following REM is automatically highlighted. If a percent sign \`%' follows the REM statement, REM skips a line and prints the specified text string on the line below. Inserting a question mark after the REM statement causes KCML to ignore the REM ? and execute the statement following the question mark. This allows statements specific to KCML to be hidden on other dialects of BASIC-2.

To add a comment on the same line use two slash characters to start the comment text. This is especially useful for comments about the declaration of variables with [DIM](DIM.htm) and records with [DEFRECORD](DEFRECORD.htm). The comment then extends to the end of the line and may include colons. This is not a statement in its own right and should not be prefixed by a colon. Because the end of the line is important in defining the end of the comment, this form of comment means that you should not use colons to put more than one statement on a line. In particular if you use this form of comment you should also use the [new text format](NEWASCII.htm) for program source files.

The workbench will place the // comment itself so that they line up vertically on the screen. By default it will use column 40 but this can be changed by setting byte 6 of [\$OPTIONS LIST]($OPTIONS_LIST.htm#BYTE6).


    DIM _BUFSIZE=4096       // size of input buffer
    DIM buf$_BUFSIZE        // the input buffer

Compatibility

The // form for comments was introduced in KCML 6.20. A semicolon can also be used to start a comment which extends to the end of the line and may include a colon however this is supported only for compatibility with NPL. This will work only if the end of the line is well defined. Using semicolons for comments in KCML is not recommended and may not be supported in future versions.

Syntax examples:

REM Beginning of program\
REM %Main routine\
REM ? LINPUT LINE "Exit one two three", abc
