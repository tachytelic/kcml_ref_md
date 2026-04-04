CREATE TABLESPACE

CREATE \[GLOBAL \| LOCAL\] TABLESPACE tablespacename location TYPE {TREE \| FLAT \| TEMPORARY}

Creates a tablespace in the machine schema. A tablespace is a shorthand naming mechanism that allows tables to be created in specific directories without having to explicitly name the directory in the application. The *tablespacename* is case sensitive and the *location* must be a directory if it already exists, if it does not exist it is created as a directory. The location may contain environment variables.

The TREE tablespace type allows tables to be placed into a hierarchical directory with the minimum of effort, eg. CREATE TABLE NL_01_example (pid INTEGER(4), longname VARCHAR(20)) TYPE 7, TABLESPACE Data1 would create the file 'C:\Comm8\Data1\NL\01\NL_01_example.kdb' if the 'Data1' tablespace was created as in the example below. Alternatively, creating the table in the 'disk2' tablespace would yield the file '/disk2/NL_01_example.kdb'.

The TEMPORARY tablespace type allows temporary tables to be created. For more information see [temporary files](mk:@MSITStore:kcmlrefman.chm::/temporary.htm).

Tablespaces may be created globally, using the GLOBAL clause, in which case all databases in the kconf.xml configuration file will be able to use the tablespace. Or, the tablespace may be created locally, using the LOCAL clause, in which case the tablespace will only be useable by connections to the same database that the CREATE TABLESPACE statement was issued against. If no GLOBAL/LOCAL clause is used the default is to create a GLOBAL tablespace.

This function can be executed whilst connected to a 'virtual' database, to create GLOBAL tablespaces, to allow boot-strapping of new systems.

Examples

CREATE TABLESPACE disk2 '/disk2' TYPE FLAT CREATE GLOBAL TABLESPACE tmp '/tmp' TYPE TEMPORARY CREATE LOCAL TABLESPACE Data1 'C:\Comm8\Data1' TYPE TREE CREATE LOCAL TABLESPACE MyTables '\$HOME/tables' TYPE FLAT

See also:

[CREATE TABLE](CREATE_TABLE.htm), [CREATE DATABASE](CREATE_DB.htm),
