KCMLDdeExec(conv, cmd\$)

This command will execute the command cmd\$ on the DDE conversation channel conv. The value for conv is obtained by calling the [KCMLDdeOpen](KCMLDdeOpen.htm) command, to start a DDE conversation with a pre-loaded server application. The contents of the actual command string cmd\$ will vary, depending on the server application. In Excel, for example, this could be an Excel macro (not Excel VBA), whereas as Word would expect some WordBasic commands.

Syntax

\$DECLARE'KCMLDdeExec(INT(), STR())

Returns

If successful, this function will return 0. If an error occurs, then -1 is returned.

Notes

The *cmd\$* string will be application dependent. For more information on how to control a DDE server, refer to the applications documentation.

Example

The following example program will load Excel, and execute two of the commands from its macro language - message and alert.

\$DECLARE 'KCMLDdeInit() \$DECLARE 'KCMLDdeOpen(STR(),STR()) \$DECLARE 'KCMLDdeClose(INT()) \$DECLARE 'KCMLDdeDestroy() \$DECLARE 'KCMLDdeExec(INT(),STR()) IF ('KCMLDdeInit()) dde = 'KCMLDdeOpen("excel", "system") IF (dde) 'KCMLDdeExec(dde, "\[message(1,""This is text on the status bar!"")\]") 'KCMLDdeExec(dde, "\[alert(""This is an alert box!"",1)\]") 'KCMLDdeClose(dde) END IF 'KCMLDdeDestroy() END IF

Excel macro commands that expect text need to be delimited by quotation marks. In order to perform this in KCML, and still keep the syntax correct, use two quotation marks instead. Thus, when Excel expects "Text", supply ""Text"".
