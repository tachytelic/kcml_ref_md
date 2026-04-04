KCMLDdeInit

This function will register KClient as a DDE client application with the Windows DDE manager. Once this has been done, KClient can initiate DDE conversations with other Windows applications. This function will be called automatically if a call is made to start a DDE conversation (using the [KCMLDdeOpen](KCMLDdeOpen.htm) function).

Syntax

\$DECLARE 'KCMLDdeInit()

Returns

The function returns TRUE on success, FALSE on failure.

Notes

Once an application has finished using DDE, the function [KCMLDdeDestroy](KCMLDdeDestroy.htm) should be called to unregister Kclient as a DDE client application.

Example

The following code excerpt registers Kclient as a client DDE application.

\$DECLARE'KCMLDdeInit() ret = 'KCMLDdeInit() IF ret == 1 THEN PRINT "Success" : ELSE PRINT "Failed"
