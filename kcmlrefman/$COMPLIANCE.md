\$COMPLIANCE Language compliance level

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

\$COMPLIANCE compliance-level

</div>

\
To have any effect, this statement must be the very first statement in the program.

</div>

------------------------------------------------------------------------

The \$COMPLIANCE statement is used to set the language level with which the program complies. The \$COMPLIANCE statement only has any effect if it is one of the very first statement in the program or library (specifically, only [REM](REM.htm), [\$ID]($ID.htm) and blank lines may precede it). The compliance-level currently supports three values:

- **Level 0**

  This is the default and the level if no \$COMPLIANCE is found. No special compliance is expected.

- **Level 1**

  A level 1 compliant program complies with stricter rules:

  - All [DEFSUB](DEFSUB.htm) statements must have a matching ENDSUB statement. Because this implies that all subroutines are well-defined with clear beginning and end, it makes it possible to skip over a DEFSUB...ENDSUB and to nest one subroutine inside another. This has always been possible with [DEFEVENT](DEFEVENT.htm)...ENDEVENT.

  - [Nested DEFSUBs](DEFSUB.htm#nesting) are allowed.

  - [TRY/CATCH](TRY.htm) blocks are permitted.

- **Level 2**

  A level 2 compliant program comply with all level 1 criteria, plus the following:

  - All variables must be explicitly DIMed. The advantage of this over always enforcing this rule through [\$OPTIONS byte 38]($OPTIONS.htm#BYTE38) is that only programs declaring \$COMPLIANCE 1 need obey this rule. Thus new code can be written to this standard without having to modify existing software.

- **Level 3**

  A level 3 compliant program comply with all level 2 criteria, plus the following:

  - [GOTO](GOTO.htm), and all references to line numbers in statements like [RESTORE LINE](RESTORE.htm) or [\$OPEN]($OPEN.htm), are not permitted.

- Not currently enforced, but likely in a later release:

  - Use of out of scope [local variables](TutorialLocal.htm) will not be permitted, except through the nesting of subroutines. (Currently it may be observed that if 'A calls 'B which calls 'C, and 'B defines a local variable D, then within 'C the local variable D can still be referenced. This should only be permitted if 'C was contained withing the DEFSUB...ENDSUB of 'B.)

Future versions of KCML will support higher levels. The idea here is to encourage better programming standards, to discourage obsolete elements of the language and to remove some features that stop KCML operating more efficiently.

The \$COMPLIANCE level of the executing program can be inspected in byte 57 of [\$MACHINE]($MACHINE.htm#BYTE57).

See also:

[DEFSUB](DEFSUB.htm)
