Compatibility between KCML versions

KCML programs saved by previous versions of KCML will execute on later versions with a few exceptions documented below. If you want to develop on a particular version of KCML, say on KCML 6.0, but execute it on an earlier version, then you need to set an environment variable appropriate to the target version. Then [SAVE](SAVE.htm) will warn if any construct that would not be supported in the target version is used in the program. The program will always be saved.

The parser may well generate different, compatible code, when you edit a line in the workbench, LOAD an ascii program or when you use \$COMPILE. Generally the code differences ensure that the program behaves consistently in the current KCML and in the target environment. For instance setting COMPAT32 will allow local variables passed back from subroutines to be referenced out of scope. To do this KCML must generate different code.

The runtime environment may also be affected by these compatibility flags making the modern KCML behave in a different, compatible way. For instance setting COMPAT40 will suppress the P41.6 error that results from RETURN CLEAR inside a function returning a value. This can lead to stack overflow problems so modern KCMLs error this but older software may rely on this behaviour.

Setting COMPAT40 environment variable implies setting COMPAT32 and COMPAT32 so you do not need to set all of them. These variables can also be set by flags specific bytes of [\$OPTIONS RUN]($OPTIONS_RUN.htm). This second method gives better control but can only be done inside the application.

KCML6.20 differences

- LIBRARY is now a keyword replacing MODULE which is still accepted
- PRIVATE and PUBLIC are now keywords
- The runtime lookup of fields in libraries is now the default. In other words byte 49 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE49) is set to HEX(03) by default
- KI_FLD no longer creates field variable. It can now only initialize existing variables.
- KI_DESCRIBE_COL now returns the new \$PACK text formats rather than the old 2 byte hex formats
- Some exotic \$PACK(F) formats for bit counting and Informix money formats now require \$PACK(E)
- The SY8 pack format introduced for KCML 6.0 is now FP.
- Constants are now enabled by default
- Direct telnet mode (kcml -l) has been dropped
- Loading boot programs from platters (kcml -w) has been dropped

KCML6 differences

Note that there is no COMPAT50 and any differences most be coded around to be compatible with both versions. The forms manual lists the differences between 5.02 and 6.0 [here](mk:@MSITStore:kcmlforms.chm::/tmp/new504.htm). The differences between 5.02 and the interim 5.03 limited release listed [here](mk:@MSITStore:kcmlforms.chm::/tmp/new504.htm) should also be considered. You will not be warned by SAVE if you use new KCML 6.00 properties or events in a program intended for KCML 5.x.

Other differences include:

- Some form properties are now read-only e.g. [CursorRow](mk:@MSITStore:kcmlforms.chm::/tmp/PROP_GRID_CROW.htm), [CursorCol](mk:@MSITStore:kcmlforms.chm::/tmp/PROP_GRID_CCOL.htm).
- Child forms cannot be opened in the [.Enter()](mk:@MSITStore:kcmlforms.chm::/tmp/PROP_FORM_ENTER.htm) or [.Exit()](mk:@MSITStore:kcmlforms.chm::/tmp/PROP_FORM_EXIT.htm) events.
- The semantics of setting [.ValidateText\$](mk:@MSITStore:kcmlforms.chm::/tmp/PROP_GRID_VALIDATETEXT.htm) have changed (5.03 to 6.00 difference).
- OCX's embedded in forms by the KCML6 workbench will not display all their properties and events if edited in KCML5
- [MODULE](MODULE.htm) and OBJECT are now reserved words.
- The fields in [\$PSTAT]($PSTAT.htm) at bytes (43,2), (45,2) and (47,2) that were used to track the currently executing partition are no longer maintained as they have no meaning with memory mapped globals or libraries.

<span id="#COMPAT40"></span>

COMPAT40 differences

If enabled, either with the environment variable [COMPAT40](EnvVars.htm#COMPAT40) or by setting byte 38 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE38), this will cause KCML 5.0 or later to behave differently in the following areas

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th width="70">Byte 38</th>
<th width="70">Affects</th>
<th>Controls</th>
</tr>
</thead>
<tbody>
<tr>
<td>HEX(01)</td>
<td>Runtime</td>
<td>SAVE will warn about constructs added after KCML 4.0, including 0xNN numeric literals</td>
</tr>
<tr>
<td>HEX(02)</td>
<td>Runtime</td>
<td>Normally a P41.6 error will be thrown if a <a href="RETURN_CLEAR.htm">RETURN CLEAR</a> is issued inside a subroutine which is involved in an arithmetic expression e.g.
<pre><code>
a = b + &#39;fred()</code></pre>
This error can be suppressed with this flag though this may lead to eventual stack overflow and the fatal termination of KCML.</td>
</tr>
<tr>
<td>HEX(04)</td>
<td>Parser</td>
<td>Programs will be SAVEd with their symbols in upper case. This was the convention prior to KCML 5.0 which allowed the preservation of mixed case in symbol names. The KCML4 editor and program LIST feature always lower cases variables.</td>
</tr>
<tr>
<td>HEX(08)</td>
<td>Parser</td>
<td>Empty string literals, e.g. "", are not allowed.</td>
</tr>
</tbody>
</table>

There are other KCML4 to KCML5 differences that are not covered by these compatibility flags:

- KCML5 allows numeric literals to be specified as hex digits using the 0x prefix.
- The database KI CALLs are quite different but applications which use the stub library should be insulated from these changes.
- BYREF, RTRIM(), LTRIM() are now reserved words.
- Environment variables set with [ENV()](ENV(.htm) are now exported to a child process environment by default. This behaviour can be reverted by unsetting byte 39 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE39)

<span id="#COMPAT32"></span>

COMPAT32 differences

If enabled, either with the environment variable [COMPAT32](EnvVars.htm#COMPAT32) or by setting byte 16 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE16), this will cause KCML 4.0 or later to behave differently in the following areas

| Byte 16 | Affects | Controls |
|----|----|----|
| HEX(01) | Runtime | SAVE will warn about constructs added after KCML 3.22 |
| HEX(02) | Runtime | The length of a program line is limited to 1900 bytes and checked after editing in the line editor. This can only be set using the COMPAT32 environment variable though it can be overridden using the [LINELEN](EnvVars.htm#LINELEN) environment variable. |
| HEX(04) | Parser | [LOCAL DIM](LOCAL_DIM.htm) works the same way as in KCML 3.2. This has a particular impact in the case of a function returning a LOCAL DIMed string where the program must be compiled with the COMPAT32 flag to keep the KCML 3.2x behaviour of allowing out of scope reference to such strings. |
| HEX(08) | Parser | [FALSE](FALSE.htm) is compiled differently to be compatible with what KCML 3.2 expected. |
| HEX(10) | Parser | Signed arguments are not allowed in [\$DECLARE]($DECLARE.htm) definitions e.g. no INT(-). This is a compile time check with a P23.8 error if parsed when COMPAT32 is set. |
| HEX(20) | Parser | [SYM(\*)\$()](SYM(.htm) is compiled differently as KCML3.2x did not support SYM of string arrays properly |
| HEX(40) | Parser | Code will be compiled for subroutines so that the GOSUB (optional in KCML4 and later) will be regenerated in KCML 3.2x. |

<span id="#COMPAT30"></span>

COMPAT30 differences

If enabled, either with the environment variable [COMPAT30](EnvVars.htm#COMPAT30) or by setting byte 1 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE1), this will cause KCML 3.2 or later to behave differently in the following areas

| Byte 1 | Affects | Controls |
|----|----|----|
| HEX(01) | Runtime | SAVE will warn about constructs added after KCML 3.0 |
| HEX(02) | Runtime | [STR()](STR(.htm) operator does not allow zero length substrings. |
| HEX(04) | Runtime | The recreator will strip () from [DEFFN'](DEFFNquote.htm) subroutines with no arguments |
| HEX(08) | Parser | The NEXT BREAK operator will not be recreated as [BREAK](BREAK.htm) but as the compatible NEXT BREAK. In KCML 3 NEXT BREAK was required to break out of a FOR loop. In later versions of KCML the BREAK operator was used. |
| HEX(10) | Parser | PTR() will be recreated instead of [SYM(\*)\$](SYM(.htm). In KCML 3 the PTR() operator was used to dereference string symbols. |
| HEX(20) | Parser | Normally KCML evaluates all the argument expressions of a [DEFFN'](DEFFNquote.htm) and then matches them. However for a 2200 compatible numeric function e.g. DEFFN'99(a, b(a)) code will be compiled differently allowing a later argument to depend on an earlier one as was the case with BASIC-2. Setting COMPAT30 will not treat these numeric functions differently. |
| HEX(40) | Parser | If set KCML will generate code to evaluate the start and end expressions of a [FOR](FOR.htm) loop completely before starting the loop as was the case in KCML 3.0. Starting with KCML 3.2, to be compatible with BASIC-2, code is compiled differently allowing the end expression to be revaluated on each iteration allowing end expressions that change as the loop is executed. |

<span id="#dropped"></span>

DOS Features dropped from KCML5 and later versions

A number of real mode DOS specific functions were dropped from KCML5 that were supported on KCML4.

- Access to raw floppy disks in [\$DEVICE]($DEVICE.htm) is no longer supported
- The \$REAL function used for communication with UFNs is no longer supported
