CREATE DATABASE

CREATE DATABASE database_name\
TYPE KDB\|VIRTUAL\
DEFAULT TABLESPACE tablespace_name\
\[DESCRIPTION string\]\
\[WITH PERMISSIONS\]

Creates a new database entry in the machine configuration file (kconf.xml). If the database is of type KDB then a catalog will also be created with the name *DATABASE_NAME*\_CAT.kdb in the 'system' tablespace, which **must** already exist **and** point to an existing directory. No catalog is created for a VIRTUAL database, and connections to such a database can only be used to issue further CREATE DATABASE or CREATE TABLESPACE commands.

The optional WITH PERMISSIONS syntax allows a new style [permissions](perms.htm) file to be created for the database. The file will be named *DATABASE_NAME*\_PERMS.kdb and will also be created in the 'system' tablespace.

It is recommended that the DEFAULT TABLESPACE, which must exist before CREATE DATABASE is executed, is a FLAT tablespace.

This function can be executed whilst connected to a 'virtual' database to allow boot-strapping of new systems. The KCML installer will create a default virtual database called 'system' with a default tablespace also called 'system' which will be a subdirectory of the KCML install directory. Note also that the user used to make the connection upon which the CREATE DATABASE statement is issued becomes the *dbauser* for the database, which has implications for any [permissions](perms.htm) checking that occurs.

Examples

CREATE DATABASE test TYPE KDB DEFAULT TABLESPACE temp DESCRIPTION 'Test database' CREATE DATABASE boot TYPE VIRTUAL DEFAULT TABLESPACE SYSTEM DESCRIPTION 'Bootstrap connection'

See also:

[CREATE TABLESPACE](CREATE_TABLESPACE.htm)
