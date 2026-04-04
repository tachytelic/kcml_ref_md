\$OPTIONS

------------------------------------------------------------------------

<div class="Generalform">

General Form:

1.  \$OPTIONS = alpha_expression\
    \
2.  alpha_receiver = \$OPTIONS

Where:

- alpha_receiver = a minimum of 64 characters

</div>

------------------------------------------------------------------------

The \$OPTIONS system variable allows KCML programs to inspect and modify switches that control the general behaviour of the KCML runtime. Further such settings can be changed by [\$OPTIONS RUN]($OPTIONS_RUN.htm) and [\$OPTIONS LIST]($OPTIONS_LIST.htm).

Any byte of this variable can be preset at the time KCML starts up by use of the [OPTIONS_XX](EnvVars.htm#OPTIONS) environment variable.

For example, to change the replacement character for the dollar sign to a '£' sign in [PRINTUSING](PRINTUSING.htm) statements, the following could be used:

STR(\$OPTIONS,4,1)=HEX(A3)

It is important that \$OPTIONS is modified directly in this way as the number of bytes in \$OPTIONS may be increased in a future KCML version.

Any of the bytes in \$OPTIONS can be preset by defining the environment variable OPTIONS_xx (where xx is the decimal byte number) in the connection manager before KCML is started and setting it to the two HEX digits required.

*Available byte settings for \$OPTIONS*

Byte

Description

<span id="BYTE1"></span>

1

Color byte used to represent underline text in DOS text mode on PC Monitors. The default is HEX(1F) for white on blue. Obsolete.

<span id="BYTE2"></span>

2

Not used.

<span id="BYTE3"></span>

3

Not used.

<span id="BYTE4"></span>

4

Replacement character for the dollar sign '\$' in [PRINTUSING](PRINTUSING.htm) image statements. The default is HEX(24), i.e. '\$', for a £ sign use HEX(A3) or HEX(7C) if using a legacy 7 bit character set. This byte may also be set with the CURCHAR environment variable.

<span id="BYTE5"></span>

5

Replacement character for the comma in [PRINTUSING](PRINTUSING.htm) image statements. The default value is HEX(2C), i.e. ','. This byte may also be set with the SEPCHAR environment variable.

<span id="BYTE6"></span>

6

Replacement character for the decimal point in PRINT USING image statements. The default value is HEX(2E), i.e. '.'. This byte may also be preinitialized with the DOTCHAR environment variable.

<span id="BYTE7"></span>

7-11

Not used.

<span id="BYTE12"></span>

12

Switch to disable the RESET key (Ctrl+Alt+BREAK)\
HEX(01) disables the RESET key\
HEX(00) enables the RESET key

<span id="BYTE13"></span>

13

Switch to disable the interrupt key (Ctrl+BREAK)\
HEX(01) disables the interrupt key\
HEX(00) enables the interrupt key

<span id="BYTE14"></span>

14-16

Not Used.

<span id="BYTE17"></span>

17

132 column support. HEX(01) enables switching to [132 column mode](TextTerm132.htm), HEX(00) disables this feature.

<span id="BYTE18"></span>

18

The minimum allowed character code in [LINPUT](LINPUT.htm). HEX(00) implies HEX(10) for the first allowable character and HEX(7F) for the last. Only required for non-US character sets and may interfere with special keys like EXECUTE.

<span id="BYTE19"></span>

19

The minimum allowed character code in LINPUT. See previous byte.

<span id="BYTE20"></span>

20-35

Not used.

<span id="BYTE36"></span>

36

The [\$BREAK]($BREAK.htm) threshold held in binary.

<span id="BYTE37"></span>

37

If set to HEX(01) then [LINPUT](LINPUT.htm) will not echo typed characters. This is for use on X25 PAD terminals which locally echo.

<span id="BYTE38"></span>

38

The bits in this byte control [DIM](DIM.htm) and the resolve phase.

|  |  |
|----|----|
| HEX(01) | DIMing or all variables including numerics and fields becomes mandatory. |
| HEX(02) | Postpone checking for un-DIMed variables to runtime. |

<span id="BYTE39"></span>

39

Not used.

<span id="BYTE40"></span>

40

Determines whether the time and date stamp is saved in the last sector of DC data files. A non zero value suppresses this default. Obsolete.

<span id="BYTE41"></span>

41-43

Reserved

<span id="BYTE44"></span>

44

Setting the HEX(80) bit will map function keys '01 to '00, '02 to '01 etc.

<span id="BYTE45"></span>

45-64

Reserved

\$OPTIONS as a record

KCML defines a [KCML_OPTIONS](tmp/kintfld.htm#KCML_OPTIONS) built in [DEFRECORD](DEFRECORD.htm) that can be used to access the fields in \$OPTIONS e.g.


    FLD($OPTIONS_LIST.OPTIONS_DisableControlBreak) = TRUE

See also:

<div class="LISTING">

[\$OPTIONS LIST]($OPTIONS_LIST.htm), [\$OPTIONS RUN]($OPTIONS_RUN.htm), [Internal structures](tmp/kintfld.htm)

</div>
