\$OPTIONS LIST

------------------------------------------------------------------------

<div class="Generalform">

General Form:

1.  \$OPTIONS LIST = alpha_expression
2.  alpha_receiver = \$OPTIONS LIST

Where:

- alpha_receiver = a minimum of 64 characters

</div>

------------------------------------------------------------------------

Form 1 of \$OPTIONS LIST is used to allow KCML programs to modify the value of the \$OPTIONS LIST system variable which is an array of bit flags and constants that control the way KCML recreates and lists programs.

Form 2 allows the contents of \$OPTIONS LIST to be examined.

Any byte of this variable can be preset at the time KCML starts up by use of the [OPTIONS_LIST_XX](EnvVars.htm#OPTIONS_LIST) environment variable.

For example, to instruct KCML to recreate certain statements in the same form as they appear in BASIC-2 the following would be used:

STR(\$OPTIONS LIST,1,1)=HEX(01)

It important that \$OPTIONS LIST is modified directly in this way as the number of bytes in \$OPTIONS LIST may be increased in a future KCML version.

Note that many of the bytes in \$OPTIONS RUN are Booleans and therefore can be be set any value, i.e. HEX(01), to select the option. However the use of HEX(01) as the value for TRUE is recommended as protection against the definition being extended in the future. Setting the byte to HEX(00) reverts back to the default FALSE setting.

Any of the bytes in \$OPTIONS LIST can be preset by defining the environment variable OPTIONS_LIST_xx (where xx is the decimal byte number) in the connection manager before KCML is started and setting it to the two HEX digits required.

**Available settings for \$OPTIONS LIST**

Byte(s)

Description

1

A Boolean parameter used to set the COMPAT2200 flag.

2

A Boolean parameter used to set the COMPATNIAKWA flag.

3

A Boolean parameter used to set the blank line behaviour in the KCML6 workbench. If set to HEX(00) it allows the programmer to freely place blank lines wherever desired in a program. These blank lines are saved with the program. No automatic blank lines (e.g. after [GOTO](GOTO.htm) or [RETURN](RETURN.htm) are provided in the Workbench. This feature allows the programmer much greater control over the program layout, typically separating out into functional groups statements within subroutines. However this feature is not backwards compatible with previous versions of KCML, and so the default setting is HEX(01) which will produce the behaviour of previous KCML versions.

4

The maximum length of a statement line sent to the Windows clipboard. Lines longer than this will be split using a continuation character but can be pasted back into the workbench transparently. This splitting helps to stop unpredicatable wrapping of program lines when program fragments are sent by email programs. The default length is 48 characters, i.e. HEX(30). To disable this mechanism set the length to HEX(00).

5

The character to be used as the continuation character when program lines are split when posting to the Windows clipboard. By default this is the backslash character.

6

The column to start same line // comments and [REM](REM.htm) comments that follow [FLD](FLD.htm) statements in the workbench editor. It defaults to 40.

7

The character to precede // comments when SAVEing or LISTing programs. Ignored in the editor. Defaults to a HEX(09) tab character. If set to HEX(00) no character will be inserted.

8-18

Reserved

19

Controls the length of the [LIST RETURN](LIST_RETURN.htm) program list. The default is HEX(0A) for 10 programs.

20

Sets the number of spaces used by LIST to indent [WHILE](WHILE.htm), [REPEAT](REPEAT.htm) and FOR loops and [SELECT CASE](SELECT_CASE.htm) statements. If not set the default indent is 4.

40

Controls the preservation of mixed case variables

|  |  |
|----|----|
| HEX(00) | Default. Preserve variable and subroutine case from the definition statement (DIM, COM, LOCAL DIM and DEFFN', DEFSUB', \$DECLARE') |
| HEX(01) | Force lower case |

\$OPTIONS LIST as a record

KCML defines a [KCML_OPTIONS_LIST](tmp/kintfld.htm#KCML_OPTIONS_LIST) built in [DEFRECORD](DEFRECORD.htm) that can be used to access the fields in \$OPTIONS_LIST e.g.


    FLD($OPTIONS_LIST.OPTIONS_LIST_ClipLength) = 255

See Also:

<div class="listing">

[\$OPTIONS]($OPTIONS.htm), [\$OPTIONS RUN]($OPTIONS_RUN.htm), [Internal structures](tmp/kintfld.htm)

</div>
