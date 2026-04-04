ACS terminal

KTERM=ACS

This terminal operates in two modes corresponding to the flow control selected. To work with **KCML** the terminal type should be set to ANSI unless your computer supports Wang flow control in which case you should set it to DW and consider the terminal to be a Wang 2336 with KTERM=wang.

The ACS has 16 function keys plus all the editing keys but in its ANSI mode some keys are incorrectly labelled:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="20%">Key</th>
<th width="60%">Description<br />
</th>
</tr>
</thead>
<tbody>
<tr>
<td>RESET</td>
<td>Not implemented, sends `@'.</td>
</tr>
<tr>
<td>SHIFT RESET</td>
<td>Not implemented, sends `?'.</td>
</tr>
<tr>
<td>HALT</td>
<td>The HALT key itself sends an XOFF character and will hang the terminal until CNTL-Q is pressed.</td>
</tr>
<tr>
<td>SHIFT HALT</td>
<td>Same as HALT key</td>
</tr>
<tr>
<td>CONTINUE</td>
<td>Not used, this key also sends XOFF.</td>
</tr>
<tr>
<td>RECALL</td>
<td>Sends `:', use PF15 instead.</td>
</tr>
<tr>
<td>SHIFT RECALL</td>
<td>Sends `;', use PF15 instead.</td>
</tr>
<tr>
<td>FN</td>
<td>Use TAB key.</td>
</tr>
<tr>
<td>SHIFT FN</td>
<td>Use key above TAB, labelled with braces.</td>
</tr>
<tr>
<td>SHIFT CANCEL</td>
<td>Sends CANCEL.</td>
</tr>
<tr>
<td>SHIFT DOWN ARROW</td>
<td>Sends FN, this is an ACS bug.</td>
</tr>
</tbody>
</table>

Because the [HALT](TextTermHalt.htm) key sends XOFF this key must not be used. Instead [HALT](TextTermHalt.htm) should be redefined as CTRL-C and [RESET](TextTermHalt.htm) as CTRL-R using *stty* in *.profile*

stty intr '^c' quit '^r'

This command is automatically added to the *.profile* file created by the *kcmladmin* installation program.

[CONTINUE](CONTINUE.htm) is defined as CTRL-F by the default *TERMINFO*.
