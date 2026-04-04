sql utility

This is a command line utility which can execute SQL statements. Any result sets are emitted as text on standard output. This makes it suitable for scripting.

The SQL statement is the last argument on the line and should be quoted. You can also put it in a file referenced by the -y switch.

If no KCML_SOURCES environment variable is defined the utility will look for the [database sources file](sources.htm) in the directory where its binary is executed (usually /usr/lib/kcml on Unix systems).

CREATE TABLE and CREATE INDEX are handled specially and no actual data table is created if the commands come from a file specified by the -f flag. This is used for creating old data dictionary format files.

Example:

sql -d BENCH "SELECT \* FROM DATA1"

| Switch | Purpose |
|----|----|
| -a .sq_file | Absorb data definition into table |
| -c dir | Change directory |
| -C tablename | Display column information for the given table |
| -d dbase | Use specified database |
| -f filename | Take SQL from the file, special handling of CREATE |
| -h | HTML output |
| -I tablename | Column information for given table |
| -k | Convert sources file to INI format |
| -l num | Work in specified lang. The number is that used in [\$OPTIONS RUN](mk:@MSITStore:kcmlrefman.chm::/$OPTIONS_RUN.htm) byte 20 |
| -m | Permit modification |
| -n xsl_url | Use given URL in XML output |
| -o level | Set optimization level |
| -p pwd | Supply password to go with -u |
| -q | Create a ODBC_RW filename |
| -R | Use Rev8 filenames |
| -s | Use short column names |
| -t level | Set tracing level |
| -u user | Impersonate specified user |
| -v param | Supply a dynamic parameter |
| -w workdir | Specify directory to use as workspace |
| -x tablename | List table data as INSERT statements |
| -y filename | Take SQL from the file |
| -z | List tables in the database |
