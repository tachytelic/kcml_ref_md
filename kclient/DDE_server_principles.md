Writing a DDE Server Application in KCML

Kclient supports the ability for KCML programs to act as full DDE server applications, allowing other Windows applications to connect to them and exchange data.

To enable a KCML program to act a a DDE server the program needs to make calls to various functions in the DDEML library, and also make use of 3 new embedded KCML type calls. All of these calls are made via the [\$DECLARE](mk:@MSITStore:kcmlrefman.chm::/$DECLARE.htm) protocol.

DDE Overview

The system works in a similar way to the old KCML4 Dialog box protocol, where a KCML program waits on a KEYIN statement, and is "forced" out of this by a DDE event in the Kclient. The KCML program can then make special calls to determine the type of DDE call that has been made by a client application. process it and then return or extract any necessary data.

DDE involves a client and a server application. A client application will attempt to "connect" to a server that has a unique name. Each server can register a number of supported "topics" with the DDEML library, and when a client attempts to connect, it will specify the name of the server and a topic name. If no matching server is found, or if the named server has not registered support for the specified topic name, then the DDEML manager will refuse the connection. For example, if a client wishes to connect to Microsoft Excel, it will specify "Excel" as the server name, and a workbook file as the topic (i.e. "Book1"). Assuming the Excel is running, and "Book1" is open, the connection will be granted.

Once a connection has been made, the DDE client can exchange data in one of 3 different ways - a Request, a Poke or an Execute command. These are covered in more detail in the following topics:

[DDERequest](DDE_Request.htm)\
[DDE Poke](DDE_Poke.htm)\
[DDEExecute](DDE_Exec.htm)

Example KCML DDE Server Program

The following sample KCML program will act as a DDE server and process execute, poke and request commands. It will also trap when a connection is made, and will terminate as soon as the client terminates the conversation. In order to test this program, a special DDE client program was used that allows easy connections and tests of the different types of transactions.

[Example program](DDE_Server.htm)

How the program works

The program makes all the relevant [\$DECLARE](mk:@MSITStore:kcmlrefman.chm::/$DECLARE.htm) declarations, DIMs some strings and sets up some useful contants that will be used later in the program. The first DDE command is a call to **[KCMLDdeServerInit](KCMLDdeServerInit.htm)**. This is passed a bitmask of flags that determine the type os server, and more importantly, the type of DDE messages that we will support. The CBF_FAIL_ADVISES flag will disable support for DDE "hot links" that are impractical and messy in this type of environment. This call returns a special identifier *idinst* that refers to the DDE session is used in further calls later in the program. Your DDE application may not want to be notified of executes, pokes or requests, so if not, you can use combinations of the following flags to disable events:

| Constant | Value | Description |
|----|----|----|
| CBF_FAIL_EXECUTES | 0x8000 | Prevents the server from receiving XTYP_EXECUTE transactions. Any client that attempts this will be refused. |
| CBF_FAIL_POKES | 0x10000 | Prevents the server from receiving XTYP_POKE transactions. Any client that attempts this will be refused. |
| CBF_FAIL_REQUESTS | 0x20000 | Prevents the server from receiving XTYP_REQUEST transactions. Any client that attempts this will be refused. |

The name we wish to give our server, and any topic strings that we support, have to be registered with the DDEML. This is done by calling the **DdeCreateStringHandle** function, and it is this that is done next in the code. This function returns a special "string handle" that identifies the string, and this needs to be stored for use later in the program. The function is described thus:

**DdeCreateStringHandle(idinst, string\$, codepage)**

|  |  |
|----|----|
| idinst | The identifier of the DDE session. This value is returned by a call to **KCMLDDEServerInit** |
| string\$ | The string that you wish to register |
| codepage | The code page used to render the string. CP_WINANSI should be specified here |
| Returns | The function returns a "string handle" that is used to identify the string in other DDE functions |

Once the server name and topic name strings have been registered, the program needs to register the server's name with the DDE library. This is done using the **DdeNameService** function, described here:

**DdeNameService(idinst, hsz1, reserved, flags)**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th>idinst</th>
<td>The identifier of the DDE session. This value is returned by a call to <strong>KCMLDDEServerInit</strong>.</td>
</tr>
<tr>
<th>hsz1</th>
<td>The handle of the service name string returned by a previous call to
DdeCreateStringHandle.</td>
</tr>
<tr>
<th>reserved</th>
<td>Reserved. Should be set to NULL.</td>
</tr>
<tr>
<th>flags</th>
<td>This can be either DNS_REGISTER (0x01) to register a service name, or DNS_UNREGISTER (0x02) to unregister it.</td>
</tr>
<tr>
<th>Returns</th>
<td>TRUE on success, FALSE on failure.</td>
</tr>
</tbody>
</table>

Next the KCML program registers 4 more strings - "System", "Help", "Formats" and "SysItems". Every well-written DDE server should support the "System" topic, with the following three special items:

- "Help" - when a XTYP_REQUEST is made on the "System" topic for this item, the server should return some form of help string.
- "Formats" - when a XTYP_REQUEST is made on the "System" topic for this item, the server should return a list of the Clipboard formats it supports (currently only "TEXT" is supported).
- "SysItems" - when a XTYP_REQUEST is made on the "System" topic for this item, the server should return a TAB seperated list of these three items.

Now the program falls into its main loop. Once a DDE transaction has occurred, that the server supports, Kclient will force the program out of the KEYIN statement. The KCML program can then make a call to **KCMLDDEGetTransactionData** to retrieve a 28 byte structure containing 7 DWORDs that can then be [\$UNPACK](mk:@MSITStore:kcmlrefman.chm::/$UNPACK.htm)ed into the relevent fields.

The fields that are unpacked are:

| Field   | Description                                           |
|---------|-------------------------------------------------------|
| type    | The type of DDE transaction that occurred.            |
| fmt     | The format used (currently only CF_TEXT is supported) |
| hsz1    | Handle of a string                                    |
| hsz2    | Handle of a string                                    |
| hdata   | Handle of a global memory object                      |
| dwdata1 | Transaction specific data                             |
| dwdata2 | Transaction specific data                             |

The values of most of the above fields depend on the transaction type.

Next, the KCML program enters a SELECT CASE statement, and handles each transaction type separately.

XTYP_REQUEST

This transaction type is received when the DDE client wants some data to be returned by the KCML program.

| Relevant Fields | Description                     |
|-----------------|---------------------------------|
| hsz1            | Handle of the topic name string |
| hsz2            | Handle of the item name string  |

Upon receiving this transaction, the KCML program first checks to see if the topic in question is the "System" topic, and it does this by comparing hsz1 with the hszsystem string handle that was registered earlier. If it is the same, then it then checks the hsz2 field against any of the "System" topic items that were registered, and creates the necessary data.

If the topic is not "System" then the KCML program compares hsz1 against its own registered topic string. If they are equal then it returns a data block to the DDE client. If they differ, then it returns an error message to the client instead.

The data that is to be returned must be converted into a special "data handle" by calling the **DdeCreateDataHandle** function, and this handle passed to the **KCMLDDEReturnData** function.

**DdeCreateDataHandle(idinst, buf\$, buflen, offset, item, format, flags)**

|  |  |
|----|----|
| idinst | The identifier of the DDE session. This value is returned by a call to **KCMLDDEServerInit**. |
| buf\$ | The buffer that will copied to the global memory object that will be returned to the client using the **KCMLDDEReturnData** function. |
| buflen | Lenght of buf\$. Note if this will be a string, it must be terminated with a NULL. |
| offset | The offset from the beginning of the source buffer |
| item | Handle of the item name string associated with this buffer. |
| format | The Clipboard data format. Ususally CF_TEXT. |
| flags | Reserved. Use zero here. |

The return value is a global data handle that will be passed to the client using the **KCMLDDEReturnData** function. Otherwise it is NULL.

XTYP_POKE

This transaction is received when the DDE client has passed some data associated with a particular topic and item, to the DDE server.

| Relevant Fields | Description                     |
|-----------------|---------------------------------|
| hsz1            | Handle of the topic name string |
| hsz2            | Handle of the item name string  |
| hdata           | Handle of data passed to server |

Once the KCML program has checked whether it wants the data, by checking the value of the topic name and the item name strings against its own registered ones, it can access the data by using the **DdeGetData** function.

**DdeGetData(hdata, buf\$, max, offset)**

hdata

Identifies the global memory object that contains the data to copy.

buf\$

The buffer that will receive the data.

max

The maximum amount, in bytes, of dtaa to copy to the above buffer. Typically this will be the size of the above buffer.

offset

Specifies an offset within the global memory object. Data is copied from the object beginning at this offset.

If the buf\$ parameter points to a buffer, then the return value is the size, in bytes, of the memory object, or the *max* paramater, whichever is lower. If the max parameter is NULL then the return value is the size, in bytes, of the memory object.

XTYP_EXECUTE

This transaction is received when a DDE client wants the server to execute a command. This like XTYP_POKE but no item string is assiciated. The command to execute can be copied into a buffer using the **DdeGetData** function (see XTYP_POKE).

| Relevant Fields | Description                     |
|-----------------|---------------------------------|
| hsz1            | Handle of the topic name string |
| hdata           | Handle of data passed to server |

XTYP_CONNECT

This transaction is received when a DDE client successfully connect with our server.

| Relevant Fields | Description                      |
|-----------------|----------------------------------|
| hsz1            | Handle of the topic name string  |
| hdata           | Handle of the Server name string |

XTYP_DISCONNECT

This transaction is passed when a DDE client disconnects from our server.

XTYP_ERROR

This transaction is passed when a low memory error has occurred in the DDEML.

The KCML program will quit the main WHILE loop when a XTYP_DISCONNECT transaction is passed. It will unregister its service name by making another call to **DdeNameService** and pass **0** as the hsz1 parameter and **DNS_UNREGISTER** as the flags parameter.

It is very important that ALL strings that were registered with a call to **DdeCreateStringHandle** are destroyed by calling **DdeFreeStringHandle**.

**DdeFreeStringHandle(idinst, hsz)**

|  |  |
|----|----|
| idinst | The identifier of the DDE session. This value is returned by a call to **KCMLDDEServerInit** |
| hsz | The string handle to free. |

This returns TRUE on success, FALSE on failure.

Finally, a call to **DdeUninitialize**, passing the *idinst* parameter that was originally returned by **KCMLDDEServerInit** must be called to free all resources from the DDEML associated with the application.
