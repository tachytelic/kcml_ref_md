LIST OBJECT

------------------------------------------------------------------------

General Form:\
\

LIST \[title\] OBJECT \[obj \| objname\]

\
Where:\

title = alpha_variable or a literal string\
obj = a specific object to be displayed\
objname = a pattern to be matched against the objects name

\

------------------------------------------------------------------------

If used with no option argument this statement lists in the console window all the non-NULL objects in the current program showing their internal handle number, the object type (clientCOM, serverCOM, etc.), the symbol name, the object description from its type library. E.g. :LIST OBJECT 2 ClientCOM Rows (\_RecordSet) 8 ClientCOM Cols (Field) 10 SOAP s (http://www.kcml.com/soap/test.wsdl) :

However if passed a specific object or a pattern string to be matched then extra information about the methods and or properties will be listed against each object. See [LIST DIM](LIST_DIM.htm#pattern) for more about pattern matching variable names.
