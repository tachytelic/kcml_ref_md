### Acting as a CORBA Server

Server support for the CORBA standard means that a KCML program can be easily called from other programming languages or from remote KCML programs. The KCML CORBA Server has full support for a Naming Service so that objects can be located and a Interface Repository, so that object methods published.

A KCML CORBA server runs as a daemon and must be started with the new -q flag which is usually followed by ORB specific parameters. The exact syntax of these parameters depends on the ORB KCML is using.

In the case of MICO, the Interface Repository daemon **ird** and the MICO POA/BOA daemon **micod** must be running prior to you starting your program, and if you are using a naming service, the Naming Service daemon **nsd** must either be running, or registered in the **micod** Implementation Repository so that it will start automatically.

Please consult the documentation for the ORB for more details of configuration parameters. In the case of MICO, with micod using port 9876 and ird using port 9999 on the machine "evb", the CORBA environment may have been started with something like


    # start interface repository
    ird -ORBIIOPAddr inet:evb:9999 &
    ird_pid=$!
    sleep 2

    # run BOA daemon
    micod -ORBIIOPAddr inet:evb:9999 -ORBIfaceRepoAddr inet:evb:9876 &
    micod_pid=$!
    sleep 4 

    # register naming service
    imr create NameService poa `which nsd` IDL:omg.org/CosNaming/NamingContext:1.0#NameService inet:evb:9876

and the KCML command string could then be:


    kcml -q -ORBImplRepoAddr inet:evb:9876 -ORBNamingAddr inet:evb:9876 -ORBIfaceRepoAddr inet:evb:9999 getadd.src

It is possible to leave out the -ORBNamingAddr flag on the command line if the object(s) exported do not need to be registered with a naming service. The choice of port numbers is arbitrary but they must not conflict with other network services on the machine. The various -ORB flags specifying port numbers can be held in a .micorc file in your home directory to avoid having to specify them on each command line.

#### Mapping of arguments and methods from OMG IDL to KCML

To publish the methods of your KCML object you will need to define them in the Interface Repository. The definitions are written in Interface Definition Language or IDL. The following rules can be used to express KCML conventions in IDL:

- The methods of an IDL object are mapped onto KCML DEFSUBs starting with the object name, followed by "\_" and the method name.
- Attributes are mapped to DEFSUBs starting with the object name, followed by "\_\_get\_" for getting the attribute and "\_\_set\_" and the attribute name.
- Read only attributes only need a "\_\_get\_" DEFSUB defined.
- A "\_\_set\_" DEFSUB takes one argument and returns TRUE, a "\_\_get\_" DEFSUB takes no arguments and should return the value of the attribute.
- Any *in* type arguments are mapped to either string or number as appropriate. Any *out* or *inout* arguments are mapped to BYREF strings or numbers as appropriate.

Below is an example IDL file:

    #ifndef __ADD_IDL__ 
    #define __ADD_IDL__ 

    #pragma prefix "kerridge.com/CORBA/test"
     
    interface Add 
    {
        attribute short myNumber; 
        short addShort(in short number1, in short number2); 
        boolean addNums(in double number1, in double number2, out double number3); 
        boolean addString(in string string1, in string string2, out string string3); 
        .... 
    }; 

    #endif 

This would map into the following KCML DEFSUBs:


    DEFSUB 'Add__get_myNumber()
    RETURN mynumber

    DEFSUB 'Add__set_myNumber(num1)
    mynumber = num1
    RETURN TRUE

    DEFSUB 'Add_addShort(value1,value2)
    RETURN value1+value2

    DEFSUB 'Add_addNums(value1,value2,BYREF value3)
    value3 = value1+value2
    RETURN TRUE

    DEFSUB 'Add_addString(string1$,string2$,BYREF string3$)
    string3$ = string1$ & string2$
    RETURN TRUE

The IDL file can then be fed to the repository with:


    idl -ORBIfaceRepoAddr inet:evb:9999 --feed-ir --no-codegen-c++ getadd.idl

#### \$DECLARE functions

KCML has 3 \$DECLARE functions for exporting CORBA objects:


         $DECLARE 'KCMLOBJECTExport(STR(),STR(),STR(),RETURN STR(),INT(), INT())
         $DECLARE 'KCMLOBJECTGetError(STR(),RETURN INT())
         $DECLARE 'KCMLOBJECTGetErrorString(STR(),INT(),RETURN STR())

To export an interface, in other words to expose it so that Corba clients can invoke it, call **'KCMLOBJECTExport()**. The arguments to 'KCMLOBJECTExport() are:

Parameter

Description

Object type

Must be "Corba"

ObjectName

The object name, also used as prefix for defsubs

ObjectID

The unique interface ID in the interface repository, starts with IDL:

Object IOR

The object reference (returned)

Name service

Should object be registered in the naming service?

Implementation Repository

Register object with Implementation Repository as type PERSISTENT?

The last two parameters, Name Service and Implementation Repository, should normally be TRUE.

The object **IOR** is the Interoperable Object reference for the object. This can be used to connect to the object directly if there is no Name Service available. Normally you would not use this returned string as it is valid only for this invocation of the server.

A KCML program can contain multiple interfaces. When you have called KCMLOBJECTExport for each interfaces, you should call [\$BREAK!]($BREAK.htm) to start receiving requests from clients. This \$BREAK! will never return.

The example below shows part of a KCML CORBA Server program that implements the addShort() method. Note how the third parameter to 'KCMLOBJECTExport() is the same as the interface repository ID defined in the IDL file with the prefix pragma.

**'KCMLOBJECTGetError()** is used to get the last Corba error code. That number can be converted to a message string by passing it, together with a suitable buffer to receive the string, in a call to **'KCMLOBJECTGetErrorString()**.

These \$DECLARE functions all return a boolean result which will be TRUE if the function succeeded and FALSE otherwise.


    REM CORBA server test getadd.src
    $DECLARE 'KCMLOBJECTExport(STR(),STR(),STR(),RETURN STR(),INT(), INT())
    $DECLARE 'KCMLOBJECTGetError(STR(),RETURN INT())
    $DECLARE 'KCMLOBJECTGetErrorString(STR(),INT(),RETURN STR())

    'Export("Add")
    $BREAK!
    REM should never get here
    $END

    DEFSUB 'Export(name$)
    LOCAL DIM rc, j, myIOR$1024, actualName$50
    actualname$ = "IDL:kerridge.com/CORBA/test/" & name$
    actualname$ = & ":1.0"
    rc = 'KCMLOBJECTExport("Corba", name$, actualname$, myior$, TRUE, TRUE)
    IF (rc==FALSE)
        REM failed
        rc = 'KCMLOBJECTGetError("Corba", RETURN j)
        PRINT "Unable to export: ";name$
        PRINT "CORBA Error code: ";j
        'KCMLOBJECTGetErrorString("Corba", j, tmp$)
        PRINT "CORBA Error :";tmp$
        $END 1
    END IF
    REM the object has been registered with the name server, but print IOR anyway
    PRINT myior$
    RETURN TRUE

    DEFSUB 'Add_addShort(value1,value2)
    RETURN value1+value2
    ...

#### Calling KCML CORBA objects from other languages

Note that when you export an object from KCML, the context id will be "KCML", the context kind will be blank, and the object kind will be "Object". The following extract from a C++ program shows how the id and kind is set:


        name[0].id   = (const char*) "kerridge";
        name[0].kind = (const char*) "";
        name[1].id   = (const char*) objName;
        name[1].kind = (const char*) "Object";
            ...
        obj = rootContext->resolve(name);

#### Calling KCML CORBA objects from KCML

The following example program could be used to invoke the addShort() method from another KCML program acting as a client. This assumes the client KCML was started with -q and the same ORB switches as the server.


    OBJECT Add = CREATE "Corba","Add"
    i = Add.addShort(2,5)
    IF (i<>7) THEN STOP
