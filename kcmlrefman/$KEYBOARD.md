\$KEYBOARD

------------------------------------------------------------------------

General Form:\
\
1.      \$KEYBOARD = alpha_expression\
\
2.      alpha_receiver = \$KEYBOARD\
\

------------------------------------------------------------------------

\$KEYBOARD allows a KCML program to redefine keys sent by the client by establishing a mapping between the PC keycode and the desired [KCML function key](keycodes.htm) or regular key. If defined in a program this mapping will add to the normal TERMINFO mapping. If the mappings conflict then \$KEYBOARD will replace the TERMINFO mapping for the conflicting key.

The definition string must start with the characters "KCML5" and should be followed by one or more groups of four bytes each defining one character mapping. The four byte group is made up of

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Byte</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Windows Virtual Keycode or <a href="vkcodes.htm">VK code</a></td>
</tr>
<tr>
<td>2</td>
<td>Shift state bit mask<br />
00 no shift<br />
01 SHIFT<br />
02 CTRL<br />
04 ALT</td>
</tr>
<tr>
<td>3</td>
<td>KCML <a href="keycodes.htm">key value</a></td>
</tr>
<tr>
<td>4</td>
<td>Function key indicator<br />
00 regular key<br />
01 function key</td>
</tr>
</tbody>
</table>

You can build up a string with an easy to use utility [editkb](editkb.htm), which runs under Windows and ships with the Windows version of KCML, and then paste the completed string into the Workbench.

Example

\$KEYBOARD = "KCML5" & HEX(1B00 BD00 D500 8200)

maps the Esc key to CANCEL and the Enter key to EXECUTE. To revert to the default keyboard mapping send the "KCML5" header on its own e.g.

\$KEYBOARD = "KCML5"

Compatibility

There is also a compatibility mode for legacy applications that used a 576 byte string with a different mapping for DOS keycodes. This is still supported for applications that require it and does not confict as the new usage requires the string "KCML5" at the start of the mapping string.
