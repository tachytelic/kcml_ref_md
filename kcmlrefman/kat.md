kat

General Form:\
\
kat \[-acfhlrskunxv3\] \[-p *filename*\] \[-P *filename*\]\[-e *sectors*\] \[-i *sectors*\] \[-m *mask*\] \[-W *inplatter* \]\
        \[-w *outplatter* \] *filename* \[ *, filename* ... \]

The *kat* utility produces readable ASCII listings from compiled KCML programs; it is in some ways the inverse of the [compile](compile.htm) utility. The program files can be on a platter image (using the -W option) or UNIX/DOS files. The listings are written to the standard output.

Using *kat* with no options produces output suitable for loading into KCML with the [LOAD ASCII](LOAD_ASCII.htm) command; one line of output will contain a line number and all the statements for that line with no formatting.

*kat* also provides backward compatibility with BASIC-2 and BASIC-2C.

The *ucompile* script can be used to *kat* entire directories or platter images to ASCII files in a batch mode.

The options available with the *kat* utility are as follows:

Switch

Purpose

-3

Generate release 3.00 compatible code.

-a

Force all symbols to be in lowercase. This was the default prior to KCML5

-c

Specifying the \`-c' option causes the *kat* utility to generate source code for KCML versions \< release 2.00. E.g. \`==' will be recreated as \`='. This can only be performed if no new release 2 or release 3 statements have been added to the programs specified.

-e *sectors*

The \`-e' option should only be used if \`-w' has already been specified. The \`-e' option instructs *kat* to add the specified number of sectors to the file before it is placed onto the specified platter. A BASIC-2 header and trailer is also added to the file before it is added to the platter.

-f

Specifying the \`-f' option makes the output similar to that of the KCML [LIST](LIST.htm) command, with one statement per line.

-h

The \`-h' option causes each KCML program line to be preceded by the filename; this can be useful when using *kat* as input to the UNIX *fgrep* command and other UNIX tools. It probably does not make much sense to use both the \`-f' and \`-h' options.

-i *sectors*

The \`-i' option should only be used if the \`-w' option has already been specified. The \`-i' option instructs *kat* to create a platter with the specified number of index sectors, before any files are copied onto it. By default the platter will be created with 43 index sectors.

-k

If specified will prefix a decomposed listing with the line and statement number.

-l

The \`-l' option instructs *kat* to read filenames from the standard input device.

-m

mask

Can only be used with the \`-W' flag. Only files matching this mask are listed.

-n

This option should be used to produce output formatted in a way acceptable to BASIC-2C. It implies \`-c' and \`-f'. There is no checking for KCML extensions.

-p

Performs the same function as the *iskcml* utility.

-P

Performs the same function as a *iskcml -p*.

-r

Remove text from [REM](REM.htm) statements.

-r30

Check for KCML 3.0x compatibility

-r31

Check for KCML 3.1x compatibility

-r32

Check for KCML 3.2x compatibility

-r40

Check for KCML 4.0x compatibility

-R *n*

Report lines with more than n p-code operators

-s

Specifying the \`-s' option instructs *kat* to suppress any system error messages, for example, permission errors, program protection errors, warnings about [KEYIN](KEYIN.htm)s and \$GIOs etc.

-u

Unconditionally overwrite existing files.

-v

Display the version number of the *kat* utility.

-w *plat*

Specifying the \`-w' switch followed by the name of a platter image file instructs *kat* to generate a BASIC-2 compatible file in release 3 atomised form in that platter. The \`-i' and \`-e' options can be combined with\
\`-w'.

-W *plat*

Using the \`-W' switch followed by the filename of a platter image causes *kat* to use that platter as input with files looked up in its catalog.

-x

Produce a symbol cross reference only.

Example:

kat -h UT/\*\|grep 'DATA SAVE\[^:\]\*cd\$'\| pr -f -h "Saves of cd\$"\|lpr &

This will search the programs in the directory \`UT' for all lines including any statement performing a DATA SAVE on the variable \`cd\$'; all such lines will be printed to the spooler. (The UNIX *pr* command formats a file into pages, and the *lpr* command is the UNIX spooler.)

The pattern in the *grep* statement in this example says match the words DATA SAVE, followed by any characters except a colon followed by the variable \`cd\$'; that is, DATA SAVE DC followed by \`cd\$' in the same statement. Note that it will also match DATA SAVE DC abcd\$; the pattern could be made even more elaborate to avoid this.

kat -w D11.bs2 KI/\*

converts all the KCML programs in the \`KI' directory to 2200 atomised form and saves them in the platter image file \`D11.bs2'.

kat -n -W D11.bs2 SL/BATCH \>SL/BATCH.SRC

lists the file \`SL/BATCH' from the platter image file \`D11.bs2' and saves it in the current directory as \`SL/BATCH.SRC' in a format acceptable to BASIC-2C.

See also:

ucompile, iskcml
