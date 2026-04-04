KCML 5 database schema definition

The master definition of a KCML5 database was held in the **sources.txt** file which resides in the same directory as KCML itself thus guaranteeing there is only one such definition for each KCML installation. It was a free format ascii text file similar in structure to a Windows INI file. Blank lines and redundant whitespace will be ignored. Everything after a \# character up to the end of the line will also be ignored allowing comments.

The file is structured into one or more sections each preceeded by a section header name enclosed in \[\] characters. Section headers names are not case sensitive. There is one reserved section name of \[GENERAL\], the other sections are user defined section names which may include spaces. These define individual databases. The \[GENERAL\] section defines general system wide parameters and allows the specification of defaults for the other sections.

Each section consists of a number of keywords, an = sign and the associated value. There will not be any blanks in the keyword and it is case insensitive. The keywords currently supported are

| Keyword | Meaning |
|----|----|
| Description | A description for the database |
| Catalog | A table containing the table catalog for the database. This is required to define the section as a database. |
| Optimization | A numerical value between 0 and 9 determining how much optimization is done on SQL statements. The higher the value the more optimization is performed. Default value is 9. |
| Permissions | The [permissions table](perms.htm#kcml5) containing the authorized users and their permissions. If not present then no permissions based security will apply. |
| LongUserNames | A boolean (true/false) indicating the format of the permissions file. If false then the userid is assumed to be 5 characters. If true then it is assumed to be 8 characters. |
| ShortName | A boolean (true/false) indicating the way in which column names will be returned from the data dictionary. Default false. |
| TraceFile | A file to be used for logging and for debugging. Used if *TraceLevel* is nonzero. This file can get very large. |
| TraceLevel | A numerical value between 0 and 9 determining how verbose the tracing should be. If not present or if zero then no tracing takes place. The higher the value the more verbose the output. |
| Update | A boolean (true/false) indicating if update operations (INSERT, UPDATE, CREATE TABLE, DROP TABLE, etc.) are allowed on the database. |
| Workspace | A directory to be used for temporary tables used for sorting |

An example of a simple sources file on a Unix system might be \# This is a comment \[General\] Workspace = /user8/tmp \[Autoline\] Catalog=/user1/home/catfile Permissions=/user1/home/perms
