## Debug mode

Programs are listed on a pale background in the same format used by the editor, with the currently executing statement clearly highlighted in a different contrasting color, usually dark red. To make the workbench mode clear it is a good idea to use different [scenes](scene.htm) for the editor and debugger.

All the navigation and object functions of the editor are still available in debug mode. Note that the cursor statement is distinct from the currently executing statement indicated with reverse video. The cursor may rove about the entire program (and any global) without disturbing the current execution position.

Editing functions are not allowed in debug mode but if you do wish to alter the program then F9 will switch back to edit mode, though this will mean that the altered program can not be resumed without a [RUN](mk:@MSITStore:kcmlrefman.chm::/RUN.htm) or [RUN STOP](mk:@MSITStore:kcmlrefman.chm::/RUN_STOP.htm). Provided the program is not changed while in edit mode it is possible to toggle between edit and debug modes with F9.

Since editing is not possible, normal keys can be used for most debug functions; generally these are mnemonic:

<span target="shortcuts"></span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Key</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr>
<td>space</td>
<td>STEP OVER (do not enter subroutines; skip DIM, COM, REM)</td>
</tr>
<tr>
<td>B</td>
<td>Toggle break/trap point</td>
</tr>
<tr>
<td>C</td>
<td>CONTINUE</td>
</tr>
<tr>
<td>F</td>
<td>FLIP (toggle to display execute window), also available on F4.</td>
</tr>
<tr>
<td>G</td>
<td>GOTO CURSOR (set a temporary trap at cursor then continue)</td>
</tr>
<tr>
<td>I</td>
<td>STEP INTO (HALT / STEP)</td>
</tr>
<tr>
<td>L</td>
<td>CONTINUE LOAD</td>
</tr>
<tr>
<td>N</td>
<td>CONTINUE NEXT</td>
</tr>
<tr>
<td>O</td>
<td>CONTINUE LOOP</td>
</tr>
<tr>
<td>R</td>
<td>CONTINUE RETURN</td>
</tr>
<tr>
<td>S</td>
<td>SET PROGRAM AT CURSOR<br />
(equivalent to immediate mode GOTO)</td>
</tr>
<tr>
<td>T</td>
<td>Terminate Debugging, same as F9</td>
</tr>
</tbody>
</table>
