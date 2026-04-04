KCMLDdeClose(conv)

This function is used to close a DDE conversation, created with the [KCMLDdeOpen](KCMLDdeOpen.htm) call. It is important that all DDE conversations are closed using this function, as conversations that are left open will use up system resources, and can cause problems.

Syntax

\$DECLARE 'KCMLDdeClose(int())

Returns

This function always returns TRUE.
