KCML key codes

The [KEYIN](KEYIN.htm) function can return either regular keys corresponding to the normal keyboard characters in the terminals code page or function keys for special keys used for editing. The distinction is blurred by the fact that keys like RETURN, BACKSPACE and keys invoked with CTRL are all considered to be regular keys. However such special keys are all between HEX(00) and HEX(1F). As KCML5 supports the 8 bit ANSI Latin 1 code page by default the regular keys can have any value above HEX(20) and may be greater than HEX(80) in some locales e.g. HEX(F6) for Ö on a German keyboard.

KCML virtual key coding allows for up to 32 numbered function keys (HEX(00) to HEX(1F). On [Kclient](TextTermKclient.htm) with a 12 key keyboard to get all of these keys requires the use of SHIFT and CTRL.

Function keys also include some special keys for word processing no longer found on modern keyboards. The editing function keys are coded thus

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th width="80">Code</th>
<th width="100">TERMINFO<br />
Keyword</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td>HEX(42)</td>
<td>prev</td>
<td></td>
</tr>
<tr>
<td>HEX(43)</td>
<td>next</td>
<td></td>
</tr>
<tr>
<td>HEX(4A)</td>
<td>insert</td>
<td></td>
</tr>
<tr>
<td>HEX(49)</td>
<td>delete</td>
<td></td>
</tr>
<tr>
<td>HEX(46)</td>
<td>north</td>
<td></td>
</tr>
<tr>
<td>HEX(45)</td>
<td>south</td>
<td></td>
</tr>
<tr>
<td>HEX(4C)</td>
<td>east</td>
<td></td>
</tr>
<tr>
<td>HEX(4D)</td>
<td>west</td>
<td></td>
</tr>
<tr>
<td>HEX(4F)</td>
<td>dectab</td>
<td>Obsolete, often CTRL-T</td>
</tr>
<tr>
<td>HEX(48)</td>
<td>pferase</td>
<td>Clears rest of the line, usually CTRL-E</td>
</tr>
<tr>
<td>HEX(50)</td>
<td>shiftcancel</td>
<td>Usually SHIFT-HOME</td>
</tr>
<tr>
<td>HEX(52)</td>
<td>shiftprev</td>
<td></td>
</tr>
<tr>
<td>HEX(53)</td>
<td>shiftnext</td>
<td></td>
</tr>
<tr>
<td>HEX(5A)</td>
<td>shiftinsert</td>
<td></td>
</tr>
<tr>
<td>HEX(59)</td>
<td>shiftdelete</td>
<td></td>
</tr>
<tr>
<td>HEX(56)</td>
<td>shiftnorth</td>
<td></td>
</tr>
<tr>
<td>HEX(55)</td>
<td>shiftsouth</td>
<td></td>
</tr>
<tr>
<td>HEX(5C)</td>
<td>shifteast</td>
<td></td>
</tr>
<tr>
<td>HEX(5D)</td>
<td>shiftwest</td>
<td></td>
</tr>
<tr>
<td>HEX(5F)</td>
<td>recall</td>
<td>Obsolete</td>
</tr>
<tr>
<td>HEX(61)</td>
<td>Autoinsert</td>
<td>CTRL-A</td>
</tr>
<tr>
<td>HEX(62)</td>
<td>Paste</td>
<td>CTRL-V</td>
</tr>
<tr>
<td>HEX(63)</td>
<td>Mark</td>
<td>CTRL-K</td>
</tr>
<tr>
<td>HEX(7B)</td>
<td>cuatab</td>
<td>This is sent by the TAB key in CUA mode</td>
</tr>
<tr>
<td>HEX(7C)</td>
<td>gl</td>
<td>usually CTRL-G</td>
</tr>
<tr>
<td>HEX(7D)</td>
<td>shiftgl</td>
<td>usually CTRL-Z</td>
</tr>
<tr>
<td>HEX(7E)</td>
<td>tab</td>
<td>This is actually sent by SHIFT TAB in CUA mode</td>
</tr>
<tr>
<td>HEX(7F)</td>
<td>shifttab</td>
<td>This is sent by the Esc key in CUA mode and SHIFT TAB key otherwise.</td>
</tr>
<tr>
<td>HEX(F0)</td>
<td>Cancel</td>
<td>Home</td>
</tr>
</tbody>
</table>

Kclient operates in CUA mode by default though it is possible to change the TERMINFO database entry for it to revert to the KCML3 mode. In this mode TAB behaves differently and the Esc key sends HEX(7F) while SHIFT TAB sends what used to be TAB i.e. HEX(7E). A new HEX(7B) key is sent by TAB.

Certain keys were used by the old pre-KCML4 editor which are ambiguous with an 8 bit code page.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th width="80">Code</th>
<th width="100">TERMINFO<br />
Keyword</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td>HEX(81)</td>
<td>clear</td>
<td></td>
</tr>
<tr>
<td>HEX(82)</td>
<td>execute</td>
<td>CTRL-X</td>
</tr>
<tr>
<td>HEX(84)</td>
<td>continue</td>
<td>CTRL-F</td>
</tr>
<tr>
<td>HEX(A1)</td>
<td>load</td>
<td></td>
</tr>
<tr>
<td>HEX(E5)</td>
<td>shifterase</td>
<td>CTRL-BACKSPACE</td>
</tr>
</tbody>
</table>

The mouse in KClient can be sensed using KEYIN when it will send the following function keys

| Left Click | Left Double Click | Left Drag | Right Click | Right Double Click | Right Drag |
|----|----|----|----|----|----|
| 0xF1 at DOWN event. 0xF2 at UP event. | 0xF1 at DOWN event. 0xF2 at UP event. Followed by 0xF3. | 0xF1 at DOWN event. 0xF7 while dragging. 0xF2 at UP event. | 0xF4 at DOWN event. 0xF5 at UP event. | 0xF4 at DOWN event. 0xF5 at UP event. Followed by 0xF6. | 0xF4 at DOWN event. 0xF7 while dragging. 0xF5 at UP event. |
