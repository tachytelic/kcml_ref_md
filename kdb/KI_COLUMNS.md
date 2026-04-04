KI_COLUMNS

This function is used to set up a virtual result set enumerating the columns for a specified table. The handle must have been allocated with a [KI_ALLOC_HANDLE](KI_ALLOC_HANDLE.htm) and it can be used in subsequent [KI_FETCH](KI_FETCH.htm) calls to get the information. The result set contains the following columns

| Column number | Purpose     |
|---------------|-------------|
| 1             | Column name |
