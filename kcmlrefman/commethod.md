### <span id="Methods">Object methods</span>

Most objects will expose methods which allow the KCML server to control them. The grammar is similar to a subroutine call e.g.

rsTable.MoveNext() List.AddString("Hello") a\$ = a.UpdateText(BYREF name\$) record.Open("Customers", OBJECT connect, ENUM adOpenForwardOnly) r.Value(REDIM t())

The **BYREF** prefix tells KCML to pass the variable by reference, in other words to permit the object method to modify the original variable. Normally scalar arguments are passed by value and the object method gets a copy of the argument and cannot modify the original. Constants are always passed by value. Strings and arrays are always passed by reference.

The **ENUM** prefix states that the argument is a special [enumerated constant](comconst.htm) exposed by a COM object. The enumerated values for a given method argument can be inspected using the [object browser](combrowse.htm) in the workbench.

The **REDIM** prefix applied to an array variable tells KCML to adjust the dimensions of the array to agree with the size of the corresponding argument in the method. This can be useful if you do not know the size in advance.

Methods can return objects as in

    OBJECT rsTable = cnConnect.Open("SALES")

Note that the keyword OBJECT is required to distinguish this from a simple numeric LET.

In general numbers are passed to objects by value as 32 bit integers and strings will be passed as zero terminated strings with any trailing blanks clipped. However there are a number of functions which can be used to coerce the type of an argument to a method.

| Function | Purpose |
|----|----|
| INT() | Force the argument to be passed as a 32 bit signed integer. This is however the default for numbers so this function in not generally necessary. |
| NUM() | Force the argument to be passed as a 64 bit floating point number. |
| DIM() | When applied to a string array it forces the data to be copied as an array and not a single string as would be the normal KCML convention. |

Here are some examples of these functions used in an Excel context to retrieve values from a worksheet worksheet.Range("A9").Value(BYREF NUM(t)) worksheet.Range("A3:D4").Value(DIM(a\$())) worksheet.Range("A10:D11").Value(REDIM NUM(t()))

When dealing with COM objects that represent Visual Basic or Visual Basic for Applications object it is sometimes necesssary to pass named parameters where the name of the parameter as well as its value is specified in the method. These sort of parameters may not be honored by all COM objects. The name is passed as a string literal before the actual parameter value as in:

chart.chartwizard(OBJECT range, ENUM xldoughnut, "title" = title\$, "extratitle" = "Hello")

Named parameters are also useful with SOAP objects where the case of the name is vital.
