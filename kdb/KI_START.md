KI_START

Sets the current sequential pointer for the result set to point **before** the row indexed by the supplied key, which need not itself be in the index. A subsequent [KI_READ_NEXT](KI_READ_NEXT.htm) will read the first row with a key greater than or equal to the supplied key.

If however, path is negative, then the current pointer for the index ABS(path) is set to point **after** the required key on the key path. A subsequent [KI_READ_NEXT](KI_READ_NEXT.htm) on the same negative path will read the last row with a key less than the supplied key. Using 'KI_START to position with a positive path and then calling ['KI_READ_NEXT](KI_READ_NEXT.htm) with a negative path, will skip the row before the row specified in the start, and then a new call to 'KI_START should be issued when changing direction.

Always succeeds if table is open.
