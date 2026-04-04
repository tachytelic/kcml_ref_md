KCMLDdePoke(conv, item\$, poke\$)

This command allows you to insert a value *poke\$*, at address *item\$* on the DDE conversation channel *conv*. The value for conv is obtained by calling the [KCMLDdeOpen](KCMLDdeOpen.htm) command, to start a DDE conversation with a pre-loaded server application. For example, using this command you can insert values at any row and column location in an Excel worksheet. Note that not all applications will support this feature.

Syntax

\$DECLARE 'KCMLDdePoke(INT(), STR(), STR())

Returns

This function returns 0 on success, -1 on failure.

Example

The following code extract will insert the text Test at row 1, column 1 of a pre-loaded Excel worksheet called Sheet1.

\$DECLARE 'KCMLDdeLoad(STR(),STR()) \$DECLARE 'KCMLDdeOpen(STR(),STR()) TO INT(4) \$DECLARE 'KCMLDdeExec(INT(4),STR()) \$DECLARE 'KCMLDdeClose(INT(4)) \$DECLARE 'KCMLDdePoke(INT(4),STR(),STR()) 'KCMLDdeLoad("excel", "excel.exe") chan = 'KCMLDdeOpen("excel", "sheet1") ret = 'KCMLDdePoke(chan, "r1c1", "test") 'KCMLDdeClose(chan)
