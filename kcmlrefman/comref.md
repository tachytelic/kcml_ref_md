### <span id="Reference">Referencing existing objects</span>

You can get a reference to an existing object with an OBJECT LET where the right hand side expression should be another object, a method returning an object or a string expression representing the COM object Moniker registered and advertised by a running object.


    OBJECT a = b
    OBJECT Range = Sheet.Range()
    OBJECT Excel = "Sheet1"

An OBJECT LET is not copying the object but giving a second reference to the original object. Because KCML manages reference counts internally both the original object reference and the new one must be dropped before the object can be removed from memory. This may happen automatically by a local variable going out of scope or being cleared on a LOAD or it may happen explicitly by use of the [NULL](NULL.htm) function.
