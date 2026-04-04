### <span id="Enumeration">Enumerating collections of objects</span>

Some objects are defined as **collections**, that is they can be considered as an array of objects. To extract each one in turn the [FOR OBJECT](FOR_OBJECT.htm) statement, a new variant of [FOR](FOR.htm), is provided

For example in Microsoft ADO a row is a collection of columns or fields and you can get each one in turn with FOR OBJECT ... IN thus


    FOR OBJECT a IN rsTable.Fields()
        PRINT a.Name$, a.Value$
    NEXT OBJECT a

FOR OBJECT can be used with any collection object including KCML's built in objects. To enumerate the controls on a form and double their height you can use


    FOR OBJECT c IN Form1
        c.Height = c.Height * 2
    NEXT OBJECT
