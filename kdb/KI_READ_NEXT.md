KI_READ_NEXT

Reads the next sequential row from the index path *path* using the row buffer whose symbol index is supplied as *sym* but if *path* is negative, then the previous row is read for index ABS(*path*). However, if a path of 0 is passed the read continues on the same path and in the same direction as specified in the [KISTART](KI_START.htm). In addition, if the read was successful, the stub variable *key\$* is set to the value of the key read and *rowid\$* is set to the ROWID of the row. If the symbol index *sym* is zero, then the data will not be read but *key\$* and *rowid\$* are updated, allowing a later GOSUB ['KI_READ_PTR](KI_READ_PTR.htm) to fetch the data.

Note that for type 7 tables *rowid\$* must be at least 6 bytes long.

The row is read relative to the current sequential pointer which can be established only with a start. A direct read by key or by ROWID does not modify the pointer. If there are no more rows, the *ki_status* is set to 2 and the row buffer is not updated.

Changing the direction of a read without re-issuing a [KI_START](KI_START.htm) is not recommended, as the definition of the current row is the row that has just been read, rather than the row that is about to be read. [KI_START](KI_START.htm) for a given key on a positive path, positions before the required row, ready for a ['KI_READ_NEXT](KI_READ_NEXT.htm) on the positive path. Changing direction will therefore cause the row before the key used in the start, to be skipped, and the row before that will be read.
