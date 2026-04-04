KCMLDdeOpen(app\$, topic\$)

This function attempts to open a DDE conversation with another Windows application, and if successful, returns a conversation handle - basically a unique number that identifies this particular DDE conversation. The name of the application (app\$) and the topic to converse on (topic\$) are passed to this function. Applications that support DDE in server mode can accept data on numerous different 'topics' - a logical way of splitting up DDE requests into groups. Most DDE server applications support the 'system' topic, and can even supply a list of supported topics (and help text on each one) to a client application.

Even though DDE is a standard way for Windows applications to communicate, once the link is established, the standards quickly disappear. Each DDE server application expects commands in different formats. For example, controlling Excel via a DDE link involves executing commands from the Excel macro language, whereas to control Word for Windows requires using WordBasic commands.

Syntax

\$DECLARE'KCMLDdeOpen(STR(), STR())

Returns

If successful, the function returns a DDE conversation identifier that is used when making calls to transfer data. If a conversation cannot be established (if the DDE server is not loaded, for example) then the function returns zero.

Notes

Programs should make a call to [KCMLDdeLoad](KCMLDdeLoad.htm) prior to making this call, to make sure that the DDE server application is loaded. Once a conversation is no longer needed, an application should call the [KCMLDdeClose](KCMLDdeClose.htm) function.

Example

The following code will open a DDE conversation with the Windows Program Manager. Note that this program supports a general topic called 'progman'.

\$DECLARE 'KCMLDdeInit() \$DECLARE 'KCMLDdeOpen(STR(),STR()) \$DECLARE 'KCMLDdeClose(INT()) \$DECLARE 'KCMLDdeDestroy() ret = 'KCMLDdeInit() IF (ret != 0) dde = 'KCMLDdeOpen("progman", "progman") IF (dde != 0) PRINT "Conversation established OK" 'KCMLDdeClose(dde) END IF 'KCMLDdeDestroy() END IF
