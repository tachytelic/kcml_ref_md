### Acting as a COM Server

KCML has a certain amount of support to allow it to act as a COM server. It is implemented as an inprocess server using the kserver.dll DLL directly. In other words the KCML DLL is loaded as part of the callers address space. Because of this it is not possible to act as both a COM server and a COM client at the same time. The DLL is loaded on demand with the first reference and will unload when the reference count goes to zero. Initialisation is performed when the DLL is loaded using a program name taken from the registry entry for the object. The program can overlay and attach to libraries but must eventually block on a [\$BREAK!]($BREAK.htm) with the methods to be called visible as [DEFSUB](DEFSUB.htm) statements. When COM unloads the DLL it will first interrupt the \$BREAK and execute subsequent code which should tidy up and perform an orderly [\$END]($END.htm).

KCML implements only the default IDispatch interface used by scripting languages like VBScript, JavaScript, perl etc. It does not implement a Vtable interface. For Visual Basic this means that KCML objects must be declared a plain objects and a call to CreateInstance used to instantiate them.

A KCML program acting as a COM server must be capable of running standalone without relying on any environment variables or command line settings. It may overlay internally and can access global partitions or libraries but it must eventually execute a \$BREAK! with all its exposed methods callable.

As explained above, there can only be one interface which must be given a simple name and published with a KCMLOBJECTExport() \$DECLARE call. The COM rules require that once published an interface cannot change the details of its methods and any new methods can only be added. Therefore you must also specify a version.

The mapping of data types will generally be handled automatically by KCML which will convert integers and doubles to KCML numerics and Microsoft BSTR strings to KCML strings.

You must create a type library for the functions you plan to export. This requires access to the midl utility which ships with Microsoft tools such as Visual C and Visual basic. The functions must be described in the Microsoft IDL and compiled with this tool. Here is an example IDL implementing some simple functions:


    import "oaidl.idl";
    // GUID for the Interface
    [ uuid(10B96EB5-66C7-11d4-9CF6-0060080393F0) ] dispinterface Icomtest
    {
    properties:
        [id(0)] double  numprop;
        [id(1)] BSTR    strprop;
    methods:
        [id(3)] double  Sum([in] double x, [in] double y);
        [id(5)] double  Len([in] BSTR a);
        [id(6)] BSTR    *Upper([in] BSTR a);
    };
    [
    // GUID for type library
    uuid(10B96EB3-66C7-11d4-9CF6-0060080393F0), helpstring("Example KCML COM server"), version(1.0)
    ]
    library comtestlib
    {
        importlib("stdole32.tlb");
        interface Icomtest;
        // GUID for the class
        [ uuid(10B96EB1-66C7-11d4-9CF6-0060080393F0) ]
        coclass comtest
        {
            interface Icomtest;
        }
    };

Note the three GUID strings, in bold in the example, which uniquely identify the object. Each object you create should have its own unique strings which are also used to register the object. Do not reuse the GUID strings of this example or you may clash with someone else doing the same thing. To allocate a GUID you can use the Microsoft developer utility **guidgen.exe** or try the following <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">sample KCML program</a> based on it.


    DIM guid$16, olebuf$78, abuf$38, _CP_ACP=0
    - DEFFORM frmGuid()={.form,.form$,.Style=0x50c000c4,.Width=263,.Height=152,.Text$="Create GUID",.Id=1024},\
    {.cmdCopy,.button$,.Style=0x50010001,.Left=207,.Top=6,.Width=50,.Height=14,.Text$="&Copy",.__Anchor=5,.Id=1008,.Type=9,.Click()},\
    {.Cancel,.button$,.Style=0x50010000,.Left=207,.Top=49,.Width=50,.Height=14,.Text$="Exit",.__Anchor=5,.Id=2},\
    {.cmdNew,.button$,.Style=0x50010000,.Left=207,.Top=26,.Width=50,.Height=14,.Text$="&New GUID",.__Anchor=5,.Id=9,.Click()},\
    {.textControl1,.static$,.Style=0x50000000,.Left=13,.Top=9,.Width=189,.Height=24,.Text$="Choose the desired format below then select Copy to copy the results to the clipboard.  Press Exit when done...",.Id=1000},\
    {.frameResult,.groupbox$,.Style=0x50000007,.Left=11,.Top=112,.Width=238,.Height=33,.Text$="Result",.Id=1001},\
    {.frameFormat,.groupbox$,.Style=0x50000007,.Left=11,.Top=36,.Width=185,.Height=66,.Text$="Format",.Id=1002},\
    {.optButton1,.radio$,.Style=0x50010004,.Left=40,.Top=49,.Width=50,.Height=13,.Text$="&HEX",.Id=1003,.ButtonGroup=.grpFormat,.Click()},\
    {.optButton2,.radio$,.Style=0x50010004,.Left=40,.Top=66,.Width=50,.Height=13,.Text$="&Registry",.Id=1004,.ButtonGroup=.grpFormat,.Click()},\
    {.textResult,.static$,.Style=0x50000000,.Left=33,.Top=124,.Width=196,.Height=14,.Id=1005},\
    {.optButton3,.radio$,.Style=0x50010004,.Left=40,.Top=82,.Width=50,.Height=13,.Text$="&IDL",.Id=1006,.ButtonGroup=.grpFormat,.Click()}
    - DEFEVENT frmGuid.cmdNew.Click()
    REM get it as a struct
    'CoCreateGuid(guid$)
    REM convert to Unicode string
    'StringFromGUID2(guid$, olebuf$, LEN(STR(olebuf$)) / 2)
    REM convert to ascii
    'WideCharToMultiByte(_CP_ACP, 0, olebuf$, -1, abuf$, LEN(STR(abuf$)), 0, 0)
    IF (.optButton1.State)
        'ToHex()
    ELSE IF (.optButton2.State)
        'ToReg()
    ELSE
        'ToIDL()
    END IF
    END EVENT
    - DEFEVENT frmGuid.optButton1.Click()
    REM hex format
    'ToHex()
    END EVENT
    - DEFEVENT frmGuid.optButton2.Click()
    REM reg format
    'ToReg()
    END EVENT
    - DEFEVENT frmGuid.optButton3.Click()
    REM reg format
    'ToIDL()
    END EVENT
    - DEFEVENT frmGuid.cmdCopy.Click()
    REM copy to clipboard
    'KCMLWriteClipboard(.textResult.Text$)
    END EVENT
    FORM END
    frmGuid.Open()
    END
    DEFSUB 'ToHex()
    LOCAL DIM hex$37
    IF (guid$ <> " ")
        hex$ = "HEX("
        HEXUNPACK guid$ TO STR(hex$, 5)
        STR(hex$, 37, 1) = ")"
    END IF
    .textResult.Text$ = hex$
    END SUB
    DEFSUB 'ToReg()
    IF (guid$ <> " ")
        .textResult.Text$ = abuf$
    END IF
    END SUB
    DEFSUB 'ToIDL()
    IF (guid$ <> " ")
        .textResult.Text$ = STR(abuf$, 2, 36)
    END IF
    END SUB
    $DECLARE 'CoCreateGuid(RETURN DIM())="ole32."
    $DECLARE 'StringFromGUID2(DIM(),RETURN DIM(),INT())="ole32."
    $DECLARE 'WideCharToMultiByte(INT(),INT(),DIM(),INT(),RETURN STR(),INT(),STR(),STR())
    $DECLARE 'KCMLWriteClipboard(STR())

The object must be registered in the servers registry by creating a .REG file.
