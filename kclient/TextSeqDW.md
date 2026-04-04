KCML text mode screen sequences

The following HEX codes can be sent from the server to a text mode client running in KCML emulation mode

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="10%">HEX Codes</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>HEX(00)</td>
<td>Ignored</td>
</tr>
<tr>
<td>HEX(01)</td>
<td>Moves the cursor home.</td>
</tr>
<tr>
<td>HEX(03)</td>
<td>Clears the screen and moves the cursor home</td>
</tr>
<tr>
<td>HEX(05)</td>
<td>Turns the cursor on (no blink).</td>
</tr>
<tr>
<td>HEX(02050F)</td>
<td>Makes the cursor blink.</td>
</tr>
<tr>
<td>HEX(06)</td>
<td>Turns the cursor off.</td>
</tr>
<tr>
<td>HEX(07)</td>
<td>Causes the terminal alarm to beep.</td>
</tr>
<tr>
<td>HEX(08)</td>
<td>Moves the cursor left one character nondestructively.</td>
</tr>
<tr>
<td>HEX(09)</td>
<td>Moves the cursor right one character nondestructively.</td>
</tr>
<tr>
<td>HEX(0A)</td>
<td>Moves the cursor down one line.</td>
</tr>
<tr>
<td>HEX(0C)</td>
<td>Moves the cursor up one line.</td>
</tr>
<tr>
<td>HEX(0D)</td>
<td>Moves the cursor to the beginning of the current line (carriage return).</td>
</tr>
<tr>
<td>HEX(02 03 00 0F)</td>
<td>Switches to VT220 mode whilst in KCML mode.</td>
</tr>
<tr>
<td>HEX(02 04 xx yy 0E)</td>
<td>Selects and activates a display attribute. Where <em>xx</em> is:
<table>
<tbody>
<tr>
<td>00</td>
<td>no bright, no blink</td>
</tr>
<tr>
<td>02</td>
<td>bright</td>
</tr>
<tr>
<td>04</td>
<td>blink</td>
</tr>
<tr>
<td>0B</td>
<td>bright and blink</td>
</tr>
</tbody>
</table>
<br />
and where <em>yy</em> is:
<table>
<tbody>
<tr>
<td>00</td>
<td>not reverse video and not underlined</td>
</tr>
<tr>
<td>02</td>
<td>reverse video</td>
</tr>
<tr>
<td>04</td>
<td>underline</td>
</tr>
<tr>
<td>0B</td>
<td>reverse video and underline</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>HEX(02 04 xx yy 0F)</td>
<td>Selects, but does not activate a display attribute.</td>
</tr>
<tr>
<td>HEX(0E)</td>
<td>Activates the display attribute chosen by the last (HEX 02 04...) sequence. The attribute remains valid for a maximum of one line until a carriage return or HEX(0F) is entered.</td>
</tr>
<tr>
<td>HEX(02 02 00 0F)</td>
<td>Chooses the graphic character set of normal characters from HEX(10) to HEX(7F) with underline.</td>
</tr>
<tr>
<td>HEX(02 02 02 0F)</td>
<td>Chooses the graphic character set for HEX(80) to HEX(FF).</td>
</tr>
<tr>
<td>HEX(02 08 09 0F)</td>
<td>Terminal self identification message.</td>
</tr>
<tr>
<td>HEX(02 0D 0C 03 0F)</td>
<td>Reinitialize terminal.</td>
</tr>
</tbody>
</table>

See also pages on [Programming function keys](TextSeqMagna.htm) and [ACS extensions](TextSeqACS.htm). Any of the sequences that are defined for the [VT220 mode](TextSeqVT.htm) can also be issued in KCML mode by prefixing them with a HEX(02).
