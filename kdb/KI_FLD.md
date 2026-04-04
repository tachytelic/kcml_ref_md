KI_FLD

This function initializes a number of [field symbols](mk:@MSITStore:kcmlrefman.chm::/TutorialFields.htm) in the current programs symbol table corresponding to the columns in the table. Each field symbol will define an offset into the row buffer and a data type and can be used for data awareness or in conjunction with the [FLD()](mk:@MSITStore:kcmlrefman.chm::/FLD(.htm) operator to acess the row buffer. The names used will be generated from a prefix and the column short name taken from the tables embedded schema. The IPREFIX clause used in the [CREATE TABLE](../CREATE_TABLE.htm) statement that created the table is automatically pre-pended to the column name. Any explicitly supplied prefix replaces the IPREFIX that has been automatically added.

The number of field symbols initialized, that is the number of columns less any columns with an unsupported datatype, will be returned in *cols* and an appropriate size for the row buffer will be returned in *reclen*.

A table created with CREATE TABLE XX00test ( name VARCHAR(10), deptno NUMERIC(4)) will initialize fields .XX_name\$ .XX_deptno if a call to 'KI_FLD(h, "XX\_", BYREF reclen, BYREF cols) is made. The same effect can be achieved with

CREATE TABLE XX00test ( name VARCHAR(10), deptno NUMERIC(4)) IPREFIX 'XX\_' 'KI_FLD(h, "", BYREF reclen, BYREF cols)

This is a better approach as it encapsulates all the information about the table and data awareness in one place.

Further, a call to 'KI_FLD(h, "ZZ\_", BYREF reclen, BYREF cols) on the above table will generate fields .ZZ_name\$ .ZZ_deptno

To work with a native KCML database table, the table must have been created using a [CREATE TABLE](../CREATE_TABLE.htm) SQL statement and not a [KI_CREATE](KI_CREATE.htm) function as the latter does not define column information.

This function can also be used with the results of SQL queries parsed by [KI_PREPARE](KI_PREPARE.htm).
