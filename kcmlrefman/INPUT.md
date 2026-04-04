INPUT

------------------------------------------------------------------------

General Form:\
\
     INPUT \[literal_string\[,\]\] receiver \[\[, receiver\] ...\]\
\
Where:\
\
     receiver is either a string receiver or an alpha receiver\
\

------------------------------------------------------------------------

The INPUT statement allows text or numbers to be entered from the keyboard (or redirected INPUT device) directly into variables. The text to be entered can contain leading spaces, quotes and commas. The maximum number of bytes that can be received into an alpha variable is 1900.

This statement is only relevant when programming text based applications. It should be considered obsolete as its functionality is a minor subset of [LINPUT](LINPUT.htm) and [LINPUT+](LINPUTplus.htm)

When the INPUT statement is executed, the optional literal string is displayed on the CO device, followed by a question mark.

Example:

temp\$ = "ABCDEFGHIJKLMNOP"\
INPUT "Enter Text : " temp\$

Input is taken from the INPUT device which can be redirected with the [SELECT INPUT](SELECT_INPUT.htm) statement to allow input from a file or pipe. An X70 error occurs if INPUT reads beyond the end of the file. In the example below the [INPUT](SELECT_INPUT.htm) device is selected to read from the Unix date command. The output from the date command is then read into the variable act\$ on line 30:

Example:

DIM act\$64\
SELECT INPUT "date ^"\
INPUT act\$\
SELECT INPUT /001
