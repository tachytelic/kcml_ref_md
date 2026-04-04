What is SQL?

SQL, or Structured Query Language, is a universally accepted and standardized query and data definition language for databases. It uses simple, self explanatory expressions to describe the operation required. The implementation in KCML is based on the X/Open SQL CAE specification of 1992, referred to in this document as SQL92. KCML SQL also implements the extensions to SQL92 defined in the Microsoft ODBC 2.0 specification.

There are two types of statements in the language:

- Statements in the Data Definition Language (DDL) define the structure of the database and its components (the database schema). These include [CREATE TABLE](CREATE_TABLE.htm), [CREATE INDEX](CREATE_INDEX.htm), [DROP TABLE](DROP_TABLE.htm), [DROP INDEX](DROP_INDEX.htm) and [ALTER TABLE](ALTER_TABLE.htm).
- Statements in the Data Manipulation language (DML) extract or alter the data held in the database. These include [SELECT](SELECT.htm), [INSERT](INSERT.htm), [DELETE](DELETE.htm) and [UPDATE](UPDATE.htm).

The KDB database schema is maintained exclusively through SQL DDL statements though the use of SQL for DML is optional as direct rowset APIs are available.

As security in the KCML database is based on the permissions concept the KCML SQL implementation does not support the SQL92 security functions in the DML so there is no GRANT or REVOKE. Nor currently is there a VIEW distinct from a table as this functionality is controlled by permissions.

Column names can be made unique by using the IPREFIX parameter in the [CREATE TABLE](CREATE_TABLE.htm) statement. If this option is used column names will need to be qualified with the IPREFIX in DML statements, but not in DDL statements or in calls to [KI_BIND_COL](KI_BIND_COL.htm). Additionally field symbols created with [KI_FLD](KI_FLD.htm) will automatically have the column names qualified with the IPREFIX, if it is present. So if we have the table definition CREATE TABLE CGR_TMP (PID INTEGER(4), SNAME VARCHAR(20)) TYPE 7, IPREFIX 'CG\_' we would create an index using CREATE UNIQUE INDEX CGR_TMP_A1 ON CGR_TMP (PID) However, to query from the table we would use SELECT CG_PID FROM CGR_TMP
