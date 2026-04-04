Constants in KCML

Numeric variables whose name begins with an underscore are presumed to be constants whose value cannot be changed after they have been declared in a [DIM](DIM.htm) or [COM](COM.htm) statement. The initialization, which allows simple numeric expressions, takes place at resolve time. The value can be used in other resolve time statements provided they follow the declaration. Thus the following is legal


     DIM _BUFSIZE=8*1024
     DIM buffer$(_BUFSIZE)

but these are not


     _BUFSIZE=1024
     DIM _SomeConstant

For compatibility with any KCML program that uses variables with a leading underscore already as regular variables, this functionality can be enabled and disabled when programs are being compiled from source using byte 59 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE59). The HEX(01) bit must be present in this byte for constant functionality to be present. It is enabled by default (as of KCML 6.10).

As a convenience constant definitions can appear in [LOCAL DIM](LOCAL_DIM.htm) statements when their value will be set at run time.

Constants can be defined in a [library](TutorialModules.htm) and referenced from the foreground or other libraries. They are initialized during the resolve phase so the library defining the constant must be visible at that time. Libraries that reference constants defined in other libraries should have the defining library loaded when they are saved and must be recompiled if the definition of the constant is changed.

Constants can be marked as PRIVATE when initialized in a [DIM](DIM.htm) statement in a library thus limiting their visibility to the library that defined them. They can be used in functions defined in the library but they cannot be referred to directly from another library or from the foreground.

Starting with KCML 6.10 some common constants are predefined and do not need a definition. To be exact, if a constant is not defined in the foreground the library list is searched for a definition and if not found there a built in list is consulted. For more about this list see the Workbench Function Browser or this [page](tmp/constindex.htm).

The [DEFRECORD](DEFRECORD.htm) statement creates a constant defining the size of the record. Thus


    DEFRECORD Fred
       FLD a
       FLD b
    END RECORD

will create a constant *\_Fred* which can then be used to dimension an instance of the record thus


    DIM FredRec$_Fred
