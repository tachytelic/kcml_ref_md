DDE Server example

The following sample KCML program will act as a DDE server and process execute, poke and request commands. It will also trap when a connection is made, and will terminate as soon as the client terminates the conversation. In order to test this program, a special DDE client program was used that allows easy connections and tests of the different types of transactions.

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    $DECLARE 'KCMLDdeServerInit(INT())
    $DECLARE 'KCMLDdeGetTransactionData(RETURN DIM(28))
    $DECLARE 'KCMLDdeReturnData(INT())
    $DECLARE 'DdeCreateStringHandle(INT(),STR(),INT())="DdeCreateStringHandle"
    $DECLARE 'DdeNameService(INT(),INT(),INT(),INT())="DdeNameService"
    $DECLARE 'DdeFreeStringHandle(INT(),INT())="DdeFreeStringHandle"
    $DECLARE 'DdeUnInitialize(INT())="DdeUninitialize"
    $DECLARE 'DdeCreateDataHandle(INT(),DIM(),INT(),INT(),INT(),INT(),INT())="DdeCreateDataHandle"
    $DECLARE 'DdeQueryString(INT(),INT(),RETURN STR(),INT(),INT())="DdeQueryString"
    $DECLARE 'DdeGetData(INT(),RETURN STR(),INT(),INT())="DdeGetData"
    $DECLARE 'KCMLDdeGetData(INT(),RETURN DIM(),INT())
    REM Set up some local arrays
    DIM ddedata$28, reply$64, item$256, topic$64, service$64, pokedata$512, help$64, sysitems$64
    REM Declare useful DDEML constants
    appclass_standard = 0
    cbf_fail_advises = 0x4000
    cp_winansi = 1004
    cf_text = 1
    dns_register = 1
    dns_unregister = 2
    xtyp_request = 0x20B0
    xtyp_poke = 0x4090
    xtyp_connect = 0x1062
    xtyp_disconnect = 0x80C2
    xtyp_error = 0x8002
    xtyp_execute = 0x4050
    help$ = "Server application help"
    sysitems$ = "Help" & HEX(09) & "Formats" & HEX(09) & "SysItems"
    REM Initialise the DDEML system. Setting CBF_FAIL_ADVISES disables 
    REM support for the XTYP_ADVISE DDE messages that are used with hot links
    idinst = 'KCMLDdeServerInit(appclass_standard + cbf_fail_advises)
    IF (idinst == 0) THEN STOP
    REM Now register our server name
    hszserver = 'DdeCreateStringHandle(idinst, "Server", cp_winansi)
    REM Register any topics that our server will act on here
    hsztopic = 'DdeCreateStringHandle(idinst, "Topic", cp_winansi)
    IF ((hszserver == 0) OR hsztopic == 0) THEN STOP
    REM Register our server name with the DDEML system
    'DdeNameService(idinst, hszserver, 0, dns_register)
    REM Most DDE servers support the "System" topic. This topic can have   
    REM the following item strings associated with it - "Formats", 
    REM "Help", and "SysItems"
    REM If a client connects to the "System" topic and requests data on 
    REM the "SysItems" item, the server can return a TAB seperated list 
    REM of the system items it supports
    REM The "Formats" item is useful, as some client apps can support  
    REM different Clipboard formats. We are only interest in the "TEXT" 
    REM format
    hszsystem = 'DdeCreateStringHandle(idinst, "System", cp_winansi)
    hszformats = 'DdeCreateStringHandle(idinst, "Formats", cp_winansi)
    hszhelp = 'DdeCreateStringHandle(idinst, "Help", cp_winansi)
    hszsysitems = 'DdeCreateStringHandle(idinst, "SysItems", cp_winansi)
    REM Start of the main loop
    REM As soon as a DDE event has occurred, we will be forced out of the 
    REM KEYIN staement. We can then obtain the data structure associated 
    REM with the transaction
    REM NOTE. If you are using the dialog box support, then a call to 
    REM KCMLGetControl will return 0x7EFF to indicate that it is a DDE   
    REM event that has occurrred and NOT a control that has been actioned
    WHILE TRUE DO
    KEYIN a$
    REM A DDE transaction has occurred
    REM Fetch the transaction structure
    'KCMLDdeGetTransactionData(ddedata$)
    REM Unpack the transaction data
    REM type = the transaction type
    REM fmt = the format used (we only support CF_TEXT
    REM hsz1 = handle of string
    REM hsz2 = handle of string
    REM hdata = handle of global memory object
    REM dwdata1 = transaction specific data
    REM dwdata2 = transaction specific data
    $UNPACK(F=HEX(D004 D004 D004 D004 D004 D004 D004)) ddedata$ TO type, fmt, hsz1, hsz2, hdata, dwdata1, dwdata2
    REM See what type of transaction we have
    SELECT CASE type
    CASE xtyp_request
    REM A DDE client has requested some data on a particular 
    REM topic from us. We need to return either valid data or 
    REM NULL. We can check the data string by converting the item 
    REM handle hsz2 to a string, and check the topic 
    that the 
    REM item relates to by checking the value of hsz1
    'DdeQueryString(idinst, hsz1, topic$, 64, cp_winansi)
    'DdeQueryString(idinst, hsz2, item$, 256, cp_winansi)
    PRINT "Client requests data on topic '";topic$;"', item'";item$;"'"
    IF (hsz1 == hszsystem) THEN DO
    REM The client has requested data for an item
    REM associated with the "System" topic
    REM Return the Clipboard formats we support
    IF (hsz2 == hszformats) THEN hddedata = 'DdeCreateDataHandle(idinst, "TEXT", 5, 0, hszformats, cf_text, 0)
    REM Return some help text
    IF (hsz2 == hszhelp) THEN hddedata = 'DdeCreateDataHandle(idinst, help$, LEN(help$), 0, hszhelp, cf_text, 0)
    REM Return the "System" items we support. This is a
    REM TAB separated list
    IF (hsz2 == hszsysitems) THEN hddedata = 'DdeCreateDataHandle(idinst, sysitems$, LEN(sysitems$), 0, hszhelp, cf_text, 0)
    END DO
    ELSE DO
    REM A topic other than "System" was used. You can 
    REM check here that the topic passed by the client is 
    REM supported by your app
    IF (hsz1 == hsztopic) THEN DO
    REM Set up the data to return to the client
    reply$ = "Here is my reply to your DDE request"
    STR(reply$, LEN(reply$) + 1, 1) = HEX(00)
    REM Create a data handle for the reply
    hddedata = 'DdeCreateDataHandle(idinst, reply$, LEN(reply$) + 1, 0, hsz2, cf_text, 0)
    END DO
    ELSE DO
    REM We don't support this topic
    REM Don't forget - you can have multiple 
    REM topics! - this is just an example that uses 
    REM only one
    reply$ = "This topic is unsupported"
    REM If replying with a string as opposed to 
    REM data, we need to add the C NULL terminator 
    REM (and include this in the length of the data 
    REM being passed back - hence the LEN(reply$) + 1)
    STR(reply$, LEN(reply$) + 1, 1) = HEX(00)
    REM Create a data handle for the reply
    hddedata = 'DdeCreateDataHandle(idinst, reply$, LEN(reply$) + 1, 0, hsz2, cf_text\
    , 0)
    END DO
    END DO
    REM Return the data handle to the client app
    'KCMLDdeReturnData(hddedata)
    CASE xtyp - poke
    REM A DDE client has "poked" data at us. Lets turn the 
    REM data handle into a string and display it. Note that when 
    REM data is POKE'd at us, we do not need to frame a reply, as 
    REM in XTYP_REQUEST
    'DdeQueryString(idinst, hsz1, topic$, 64, cp_win\
    ansi)
    'DdeQueryString(idinst, hsz2, item$, 256, cp_win\
    ansi)
    PRINT "Client pokes data on topic '";topic$;"', item '";item$;"'"
    ret = 'DdeGetData(hdata, pokedata$, 512, 0)
    IF (ret) THEN PRINT "The data is '";pokedata$;"'"
    CASE xtyp_execute
    REM A DDE client has requested that we "execute" a 
    REM partcular command. We can get the command and display it. 
    REM This is very much like the XTYP_POKE type, but NO ITEM IS 
    REM ASSOCIATED!. Again, no reply is needed
    'DdeQueryString(idinst, hsz1, topic$, 64, cp_winansi)
    PRINT "Client sends execute command on topic '";topic$;"'"
    ret = 'DdeGetData(hdata, pokedata$, 512, 0)
    IF (ret) THEN PRINT "The command is '";pokedata$;"'"
    CASE xtyp_connect
    REM We get this message when a DDE client has connected to us
    PRINT "Client has connected"
    'DdeQueryString(idinst, hsz1, topic$, 64, cp_winansi)
    'DdeQueryString(idinst, hsz2, service$, 64, cp_winansi)
    PRINT "Topic = '";topic$;"', Service = '";service$;"'"
    CASE xtyp_disconnect
    PRINT "Client has disconnected"
    BREAK
    CASE xtyp_error
    PRINT "A low-memory error has occurred in the DDEML"
    END SELECT
    WEND
    REM Unregister any name servers with DDEML
    REM It is VERY important that we tidy up all registered strings, as    
    REM they could otherwise remain in memory and cause future DDE  
    REM sessions to fail
    'DdeNameService(idinst, 0, 0, dns_unregister)
    'DdeFreeStringHandle(idinst, hszserver)
    'DdeFreeStringHandle(idinst, hsztopic)
    'DdeFreeStringHandle(idinst, hszsystem)
    'DdeFreeStringHandle(idinst, hszformats)
    'DdeFreeStringHandle(idinst, hszhelp)
    'DdeFreeStringHandle(idinst, hszsysitems)
    'DdeUnInitialize(idinst)
