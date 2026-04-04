pltglue (UNIX)

General Form:\
\

pltglue \[-vru\] \[-e sectors \] \[ -i sectors \] platter source_files\

The pltglue utility is used to \`glue' UNIX files into platter images. It can glue KCML programs, Wang programs, and data files that were previously held as individual UNIX files into a platter image.

If the specified file is a KCML program then a Wang BASIC-2 header and trailer is added to the program before it is copied onto the platter image. Data files and Wang BASIC-2 programs are glued directly with no changes.

If the specified platter does not exist, it will be created with a default index size of 43 sectors (unless the \`-i' flag is used), and the end catalogue area will be set to the size of the file.

The flags used with the pltglue utility are as follows:

-e sectors

The \`-e' option instructs pltglue to add the specified number of sectors to the file, before it is glued to the platter image.

-i sectors

The \`-i' option instructs pltglue to create the platter with an index size of the specified number of sectors.

-r or -u

Overwrite files if they already exist.

-v

Verbose mode.

Example:

pltglue -v -i 101 -e 40 D40.bin ACCPROG

The above example would create the platter 'D40.bin', with an index size of 101. The file 'ACCPROG' would be placed on the platter with 40 sectors added to it.

See also:

[pltsplit](pltsplit.htm)
