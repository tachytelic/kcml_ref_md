DEFOBJ

------------------------------------------------------------------------

General Form:\
\
DEFOBJ objname\$ ("REV7DD", ddname\$, colprefix\$)\
\

------------------------------------------------------------------------

The DEFOBJ statement was used prior to KCML 6.10 to name database tables that can be used for binding to data aware controls on forms. In this form the first parameter must be the case insensitive keyword "REV7DD". It is a declarative statement meaningful only at resolve time and can appear anywhere in the program.

A data-aware control on a form will be automatically populated when the form is opened (during the .Enter() event) and, if altered, will be updated back on the server when the OK button is clicked. To conserve bandwidth only changed columns are sent back to the server from the client. For more about data awareness see [Data Aware Forms](mk:@MSITStore:kcmlforms.chm::/DataAwareForms.htm) in the KCML forms manual.

The name, *objname\$*, is to be used as the **[DataSource](mk:@MSITStore:kcmlforms.chm::/tmp/PROP_DATASOURCE.htm)** property of any data aware control on the form. It must also be the name of the row buffer in the program. The **[datafield](mk:@MSITStore:kcmlforms.chm::/tmp/PROP_DATAFIELD.htm)** property should be set to the column name with the specified prefix *colprefix\$* prepended to make it unique. KCML will expect the program to contain field definitions (where the name is the same as the dictionary column name plus the prefix) for any data aware columns. It uses these definitions to discover the format and location of the column in the row buffer.

A program using a data aware form is expected to load the row buffers of any necessary tables and to establish the field definitions before opening the form. It has responsibility for writing any updated row buffers back to the database.

The forms designer in the KCML Workbench allows the programmer to drag columns from the table list onto the forms and can fill in these two data-aware properties automatically as well as size the control and generate a static text caption. The table list is generated automatically by scanning the program containing the form looking for DEFOBJ statements. The column names come from the data dictionary file specified in the *ddname\$* second parameter. Note that the dictionary is only used by the forms designer and it is not consulted at run time as field definitions are used to locate the columns in the row buffer.

Dictionaries can be either in a now deprecated KISAM binary format (conventionally with a .dd extension) or they can be simple text files containing the SQL [CREATE TABLE](mk:@MSITStore:kdb.chm::/CREATE_TABLE.htm) statement that defines the table (conventionally with a .sq extension). KCML can parse the SQL to deduce the table structure.

The third argument is an optional column prefix which may be applied to the column names found in the dictionary to produce the field names used in the datafield property. If blank no prefix will be applied.

KCML 6.10 introduced a new [DataBind](mk:@MSITStore:kcmlforms.chm::/tmp/DataBind.htm) object for forms which is used to bind [DEFRECORD](DEFRECORD.htm) records to buffers. This is described [here](mk:@MSITStore:kcmlforms.chm::/DataBinding.htm). DEFOBJ is still supported for compatibility but is now deprecated.

Syntax examples:

\
DEFOBJ mytable\$ ("Rev7dd", "../dicts/mytable.sq", "mt\_")

See also:

[DEFFORM](DEFFORM.htm) [FLD()](FLD(.htm)
