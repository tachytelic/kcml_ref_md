KCMLDdeRequest(conv, item\$, return\$)

This function is used to transfer data from a DDE server to a KCML program. The program simply asks for data on *item\$*, running a DDE conversation with an ID of *conv*, storing the returning data in *return\$*. The value for *conv* is obtained by calling the [KCMLDdeOpen](KCMLDdeOpen.htm) command, to start a DDE conversation with a pre-loaded server application.

Syntax

\$DECLARE 'KCMLDdeRequest(INT(), STR(), RETURN STR())

Returns

This function returns 0 on success, -1 on failure.

Notes

Make sure that the KCML string that you are returning data into is of sufficient size, otherwise it could cause the commands behaviour to be unpredictable and it may crash the client.

Example

The following program will request a list of program groups from Program Manager and display them on the screen.

DIM group\$512 \$DECLARE 'KCMLDdeLoad(STR(),STR()) \$DECLARE 'KCMLDdeOpen(STR(),STR()) \$DECLARE 'KCMLDdeRequest(INT(),STR(),RETURN STR()) \$DECLARE 'KCMLDdeClose(INT()) 'KCMLDdeLoad("progman", "progman") dde = 'KCMLDdeOpen("progman", "progman") 'KCMLDdeRequest(dde, "groups", group\$) 'KCMLDdeClose(dde) PRINT HEX(03);"Program Manager groups:" PRINT TAB(4); FOR i = 1 TO LEN(group\$) IF (STR(group\$, i, 1) \<\> HEX(0A)) THEN PRINT STR(group\$, i, 1); ELSE PRINT TAB(4); NEXT i

Program Manager returns a list of groups separated with a HEX(0D0A) pair. Additional information on how to communicate with Program Manager can be found in the Microsoft Developer documentation MSDN - including how to create, remove and modify groups of your own.
