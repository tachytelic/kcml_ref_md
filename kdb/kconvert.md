Table conversion utility

Converts a type 6 (or earlier table) to a type 7 table with the same columnar layout. The table(s) to be converted must be in a catalogue (except if the -f, -s switches are used) and must have a valid entry for a dictionary or .sq file in that catalogue. A copy of the original catalogue is made and the original datafiles are left in place with the extension '.kdb' appended to the name, the new datafiles are created in the same directory as the original with the name *oldfilename.kdb*. If an error occurs whilst creating the new table, or whilst copying the data to it from the old table the catalogue entry for the table is updated to point back to the old datafile and dictionary, and the corrupt table is left in place for later inspection/debugging, processing then proceeds with the next table specified on the command line. If an error occurs whilst trying to write/update the catalogue the application aborts.

The -f, -s combination allows a single file to be converted without recourse to a catalogue. Both -f and -s must be specified and any database supplied via -d is ignored. The name of the new datafile and the renaming of the old datafile are as above.

If index creation (-i) is specified any NON-UNIQUE indices are made unique by the addition of the ROWID as the last segment in the key.

kconvert \[switches\] table1 \[ table2 ...\]

The optional switches are:

| Switch | Purpose |
|----|----|
| -d database | Use the catalogue belonging to *database*. |
| -i | Create any indices on the type 7 table that were on the type 6 table. |
| -l logfile | Use *logfile* to write output to, by default messages go to stderr. |
| -f filename | Convert the single file *filename* without using a catalogue. |
| -s dictionary | Dictionary to be used when using the -f option, may be a .sq or .dd file. |
| -t | Set trace level for debugging. |

Tablenames may include wildcard characters so that multiple tables are converted at once. For example:

kconvert -i -l /tmp/kconvert.log -d BUGS "\*" will convert all of the tables in the BUGS database, creating appropriate indices and writing any output to /tmp/kconvert.log. kconvert -d LIVE "00\*" "01\*" 02_BR_BRANC

will convert tables starting with 00 or 01 and the table 02_BR_BRANC on the LIVE database, but will not create any indices and any messages will go to stderr. Note the use of quotes around tablenames which contain wildcards, this is to ensure that the command shell does not expand the wildcards. Note also that the tablenames are case insensitive, so that we could equally well have used 02_br_branc in the last example.

kconvert -i -f /data/MK/00/00.MK.Accnts -s /dicts/MK/Accnts.dd

converts the single file '/data/MK/00/00.MK.Accnts' using the dictionary '/dicts/MK/Accnts.dd', the new file will be in the same directory as the old file but with the extension '.kdb', the old file will now have the extension '.bak'. No catalogue is needed for this operation and any catalogue present will be left untouched.
