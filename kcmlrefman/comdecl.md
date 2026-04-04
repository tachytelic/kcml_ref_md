### <span id="Declaration">Declaring objects</span>

Objects look like scalar numeric symbols e.g. Range, Document, abc, etc. KCML distinguishes their type entirely from context or the use of an **OBJECT** prefix. They should be [DIM](DIM.htm)ed or [LOCAL DIM](LOCAL_DIM.htm)ed to establish scope though this is not currently mandatory. The grammar for [DIM](DIM.htm), [COM](COM.htm) and [LOCAL DIM](LOCAL_DIM.htm) has been enhanced to prefix the name with the new keyword **OBJECT** as in


    DIM s$100, OBJECT Range, OBJECT Cell

When declared in this way only a placeholder symbol is created and the object itself is not instantiated at resolve time or when a LOCAL DIM is executed. The object has an initial value of [NULL](NULL.htm).
