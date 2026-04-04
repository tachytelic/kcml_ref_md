### <span id="Lifetime">Object lifetime</span>

Because objects have an independent existence outside of a KCML process it is important to tidy them up when no longer required. Some objects can be explicitly terminated with special methods defined for them. Others, such as OCXs embedded in forms, will be implicitely terminated by KCML when their parent is terminated. In general objects will be destroyed only when no reference exists to them. KCML will track references internally and will destroy [LOCAL DIM](LOCAL_DIM.htm)ed objects when they go out of scope. Objects that are not declared in a subroutine and have global scope will only be destroyed when a non-common object variable is freed on a [LOAD](LOAD.htm) or on a [CLEAR](CLEAR.htm).

An object can be explicitly released at any time by setting it to [NULL](NULL.htm) as in

    OBJECT TempObj = NULL
