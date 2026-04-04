### <span id="Instantiation">Instantiating objects</span>

Instantiation is the name given to the process of creating an object. This is done with the [CREATE](CREATE.htm) statement using the following grammar

OBJECT *objname* = CREATE *strexpr1*, *strexpr2*

Where *objname* is an object symbol defined in an earlier DIM OBJECT or LOCAL DIM OBJECT statement. The first argument *strexpr1* defines the type of object. Currently [ServerCOM](ObjCOM.htm), [ClientCOM](ObjCOM.htm), [Corba](ObjCorba.htm) and [SOAP](ObjSOAP.htm) are supported.

For COM objects the alpha expression *strexpr2* on the right must be either a ProgId or a string ClassId defining the object in the appropriate registry. For example

OBJECT Doc = CREATE "ClientCOM","Word.Basic" OBJECT rsTable = CREATE "ServerCOM", "ADODB.Recordset" OBJECT rsTable = CREATE "ServerCOM","{00000535-0000-0010-8000-00AA006D2EA4}"

For Corba objects the alpha expression*strexpr2* on the right must be either the object name in the naming service, or an *Interoperable Object Reference* (IOR). KCML must know how to find the naming service with which the object is registered. There are two ways of specifying the location of the naming service, either using the [command line switch](kcml.htm) '-q' to KCML, or specifying additional arguments to **CREATE**. The exact syntax of the parameters depends on the ORB KCML is using.

Note that you can currently only connect to one ORB, so if you have already called **CREATE** before, or used the -q option, the additional arguments to **CREATE** are ignored

An example using MICO would be:

OBJECT Add = CREATE "Corba","Add", "-ORBNamingAddr", "inet:evb:9876"

Or KCML could be started with "`kcml -q -ORBNamingAddr inet:evb:9876`", and the object created using only the name: OBJECT Add = CREATE "Corba","Add" OBJECT Add = CREATE "Corba","kerridge/my_context/Add/Object/" The two object names above are equivalent, as KCML assumes a context name of "kerridge", with a type of "my_context" unless both the name and type are given, so if the object name is "Add", with a type of "Object", the name should be "Add/Object/"
