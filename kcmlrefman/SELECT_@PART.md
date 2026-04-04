SELECT @PART

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

SELECT @PART partition_name\$

</div>

\

</div>

------------------------------------------------------------------------

The SELECT @PART statement is used to specify the shared memory area from where the executing partition is to find its global variables and subroutines. If the partition name string is 8 characters or less then it is considered a simple string and another running global partition must have previously executed a [DEFFN @PART](DEFFN_@PART.htm) for the same name thus publishing it in the [\$PSTAT]($PSTAT.htm) table. The SELECT @PART statement will search this table for a matching name and if no match is found an X77 error will occur. If the statement succeeds then bytes 27 and 45-46 of this partition's \$PSTAT entry are set to the partition number of the global.

If the name is longer than 8 characters and contains an '=' sign, then SELECT @PART will attempt to parse the name as a global name of up to 8 characters followed by an '=' followed by a filename e.g.

SELECT @PART "GBlib=../gblib"

If the name can be parsed this way then KCML will attempt map the contents of the file directly into memory as a memory mapped file. No partition is associated with this type of global but it is inserted into the [library](MODULE.htm) list at the start and can be seen in a [LIST_M](LIST_M.htm). This avoids the need for a permanently running daemon process to own the shared memory. If multiple globals exist on a machine then it is essential that their base filenames are unique. This support for memory mapped files as globals is intended to be used for backward compatibility. An existing application can make use of memory mapped files, and thus avoid the management of a dedicated background partition, by just changing the name of the global. To fully exploit the potential for multiple mapped globals see the [LIBRARY](MODULE.htm) statement.

After the statement has been executed, defined subroutines in the global partition can be executed with the [GOSUB'](GOSUBquote.htm) statement and any global variables (that is variables whose names start with an '@') in the partition can be directly accessed.

Global partition selection is cleared with either a [CLEAR](CLEAR.htm) command, [LOAD](LOAD.htm), or [LOAD RUN](LOAD_RUN.htm) statement. It can also be deselected by specifying a blank partition name with this statement. Byte 11 of \$OPTIONS RUN, which is set non-zero if the environment variable KEEPSHARED exists, can be used to prevent [LOAD](LOAD.htm) deselecting the currently selected global partition. If this byte is non-zero it also changes the search strategy for finding subroutines.

To deselect the global partition a blank partition name should be specified, i.e.

SELECT @PART " "

Compatibility

Shared memory in memory mapped files is available with KCML 5.03 and later and is supported on both Unix and NT.

Syntax examples:

SELECT @PART"GLOBAL1"\
SELECT @PART new_partition\$\
SELECT @PART " "\
SELECT LIST /204, PRINT /204, @PART"KFAM2"

See also:

[ON...SELECT](ONSELECT.htm), [DEFFN @PART](DEFFN_@PART.htm), [LIBRARY](MODULE.htm)
