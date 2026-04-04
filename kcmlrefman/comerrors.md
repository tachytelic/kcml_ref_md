### <span id="Errors">Error handling</span>

Any object error, e.g. HRESULT not equal to S_OK for a COM object, or a Corba exception such as OBJECT_NOT_EXIST for a CORBA object, will result in an execution error inside KCML which can be trapped by an [ERROR](ERROR.htm) or [ON ERROR](ON_ERROR.htm) clause.

A new recoverable error code of O30 has been defined for this. KCML will return the COM/CORBA error message text as the text of the KCML error.
