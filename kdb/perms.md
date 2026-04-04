KDB Permissions

This is a table defining how access permissions for the various tables of a database should be implemented. It links the combination of userid, module and company to a specified priority within that combination.

In the KDB database there is the option to create a permissions file when the database is created using the WITH PERMISSIONS clause to the CREATE DATABASE statement. CREATE TABLE perms ( USERID VARCHAR(16) NAME 'User Id', MODULE VARCHAR(2) NAME 'Module', COMPANY VARCHAR(2) NAME 'Company' BRANCH VARCHAR(4) NAME 'Branch', TABLENAME VARCHAR(35) NAME 'Tablename', PRIORITY VARCHAR(1) NAME 'Priority', CANUPDATE VARCHAR(1) NAME 'Can Update', XFLAG VARCHAR(1) NAME 'Xflag'', } NAME 'Permissions' CREATE UNIQUE INDEX perms_A1 on perms (USERID, MODULE, COMPANY, BRANCH, TABLENAME, PRIORITY, CANUPDATE, XFLAG)

The table is not listed in the catalogue, - it is the responsibility of the application to populate this table. Permissions will not be checked for tables located in FLAT tablespaces and if the connection to the database is made by the *dbauser* then priority '9' will be returned for all tables.

<span id="kcml5"></span>

Permissions in KCML 5

In versions of KCML prior to KCML6 the permissions file has a simpler structure defined by the following SQL. Note the column names that conflict with SQL reserved words which therefore have to be enclosed in quotes. CREATE TABLE perms ( "KEY" VARCHAR(12) NAME 'Key' "USER" VARCHAR(8) OVERLAPS "KEY" OFFSET 1 NAME 'User ID' "MODULE" VARCHAR(2) OVERLAPS "KEY" OFFSET 9 NAME 'Module' "COMPANY" VARCHAR(2) OVERLAPS "KEY" OFFSET 11 NAME 'Company' "PRIORITY" VARCHAR(1) NAME 'Priority' VALIDATE C '123456789' ) NAME 'Permissions' CREATE UNIQUE INDEX perms_A1 ON perms ("KEY")

The USER column was originally VARCHAR(5) and the boolean keyword Rev8Perms in the KCML 5 [sources file](sources.htm) was used to determine whether the 5 character (false) or 8 character (true) definition is in use.

See also:

[CREATE DATABASE](CREATE_DB.htm)
