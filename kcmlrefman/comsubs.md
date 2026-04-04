### <span id="Subroutines">Subroutines</span>

Objects can be passed as arguments to subroutines and subroutines can return objects. It is necessary to prefix the object symbol name with the keywork OBJECT in both the calling [GOSUB](GOSUB.htm) and in the placeholder of the [DEFSUB](DEFSUB.htm) as in


    OBJECT Sheet = 'CreateExcelObject()
    'DoExcelStuff(OBJECT Sheet)
    DEFSUB 'DoExcelStuff(OBJECT s)


    DEFSUB 'CreateExcelObject()
    LOCAL DIM OBJECT a
    
    RETURN OBJECT a

Objects are allowed to be passed into [DEFSUB](DEFSUB.htm)s only (not [DEFFN](DEFFNquote.htm)s) and as the object will therefore be local its object reference lifetime will be only for the lifetime of the routine.
