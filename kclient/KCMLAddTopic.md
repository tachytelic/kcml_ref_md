KCMLAddTopic(topic\$)

This function is used to register the client as a DDE server application (see next section). You can supply a topic (topic\$) of your choice, and then wait for data requests to arrive from other DDE client programs.

Syntax

\$DECLARE 'KCMLAddTopic(STR())

Returns

This function returns TRUE if successful, FALSE if an error occurred.

Notes

See [Writing a DDE Server Application in KCML](DDE_server_principles.htm) for details on creating DDE server applications.
