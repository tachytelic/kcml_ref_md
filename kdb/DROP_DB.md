DROP DATABASE

DROP DATABASE database_name

Drops a database by removing it's entry from kconf.xml, removing it's catalogue if it is a KDB database and removing it's permissions file, if one was created. A non-virtual database can only be dropped if all of it's tables have already been dropped.

See also:

[CREATE DATABASE](CREATE_DB.htm)
