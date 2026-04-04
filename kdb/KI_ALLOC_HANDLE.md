KI_ALLOC_HANDLE

This must be called to allocate a rowset handle for use in opening a table or issuing a query. As of KCML 6.20 handle numbers are non-zero, postive huge numbers which act as opaque tokens. They can be converted into the small integers in the range 1 to [\_KDB_MAX_HANDLES](mk:@MSITStore:kcmlrefman.chm::/tmp/KdbConstantsHelp.htm) that were returned by previous version of KCML by using [KI_INFO](tmp/KI_INFO.htm) as shown [below](#convert). How the handle is allocated depends on the supplied *handle* argument:

- If *handle* is a positive number then KCML will close any handle open on that number and assign it as a new handle returning it again in *newhand*.
- If *handle* is \_KDB_AUTO_HANDLE then KCML will autoallocate a handle number from the first free handle in the pool and return it in *newhand*.
- If *handle* is \_KDB_TEMP_HANDLE then KCML will again autoallocate a handle, this time from the highest free handle in the pool, mark it as a temporary handle and return its value in *newhand*. A temporary handle will be closed and freed automatically on a [LOAD](mk:@MSITStore:kcmlrefman.chm::/LOAD.htm) or [RUN](mk:@MSITStore:kcmlrefman.chm::/RUN.htm) or if a [KI_CLEAR_HANDLES](KI_CLEAR_HANDLES.htm) call is made.

Handles allocated with this call should have their resources freed with [KI_FREE_HANDLE](KI_FREE_HANDLE.htm).

Converting a handle to an integer

To convert the opaque token returned by KI_ALLOC_CONNECT into a small integer compatible with KCMLs prior to version 6.20, use KI_INFO e.g.


        DIM info$_KDB_INFO_HANDLE, h, s, oldh
        CALL KI_ALLOC_HANDLE _KDB_AUTO_HANDLE, conn TO h, s
        IF (s) THEN STOP
        CALL KI_INFO h, 0, SYM(info$) TO s
        IF (s) THEN STOP
        oldh = FLD(info.HANDLE_INFO_handle)
