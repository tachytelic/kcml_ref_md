### <span id="Enumerations">COM Constants and enumerations</span>

COM type libraries can also define symbolic constant and enumerations (or lists of legal values). These can be passed to, or returned from, method calls on COM objects. They can also be used as property values. In KCML they must be distingushed from regular variables by the use of the **ENUM** prefix as in:

rsTable.CursorType = ENUM .adOpenKeyset record.Open("Customers", OBJECT connect, ENUM adOpenForwardOnly)

Enumerated constants can only be used in method and property expressions. They cannot be used outside of the context of the object that defines them. In particular KCML considers them as symbols and is unaware of their actual value so they cannot be converted to or from proper KCML variables.
