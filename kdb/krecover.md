krecover utility

This utility is used to control the journalling daemon.

The command line switches are:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="15%">Switch</th>
<th width="100%">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>-i</td>
<td>logging information</td>
</tr>
<tr>
<td>-e</td>
<td>enable logging</td>
</tr>
<tr>
<td>-n</td>
<td>enable huge log</td>
</tr>
<tr>
<td>-d</td>
<td>disable logging</td>
</tr>
<tr>
<td>-D</td>
<td>delete shared memory</td>
</tr>
<tr>
<td>-k</td>
<td>shutdown daemon</td>
</tr>
<tr>
<td>-K</td>
<td>kill daemon</td>
</tr>
<tr>
<td>-s</td>
<td>force a sync</td>
</tr>
<tr>
<td>-S</td>
<td>force syncing mode</td>
</tr>
<tr>
<td>-f</td>
<td>force recovery of recent logs ( &lt; 6 hours old )</td>
</tr>
<tr>
<td>-F</td>
<td>force recovery and don't check the age of the log</td>
</tr>
<tr>
<td>-T</td>
<td>force total recovery of huge log</td>
</tr>
<tr>
<td>-g <em>num</em></td>
<td>use num processes for per-file journal recovery</td>
</tr>
<tr>
<td>-j <em>dir</em></td>
<td>use directory dir for per-file journals</td>
</tr>
<tr>
<td>-J <em>name</em></td>
<td>tail per-file journal</td>
</tr>
<tr>
<td>-l <em>name</em></td>
<td>logging output filename</td>
</tr>
<tr>
<td>-m <em>num</em></td>
<td>set maximum size of log</td>
</tr>
<tr>
<td>-p <em>num</em></td>
<td>set sync pause to <em>num</em></td>
</tr>
<tr>
<td>-r <em>name</em></td>
<td>use <em>name</em> to read log</td>
</tr>
<tr>
<td>-w <em>name</em></td>
<td>use <em>nam</em>e to write file</td>
</tr>
<tr>
<td>-v <em>num</em></td>
<td>set verbose level<br />
where <em>num</em> is
<table>
<tbody>
<tr>
<td>== 0</td>
<td>silent - no error messages</td>
</tr>
<tr>
<td>&gt;= 1</td>
<td>error messages - default</td>
</tr>
<tr>
<td>&gt;= 2</td>
<td>status and file names</td>
</tr>
<tr>
<td>&gt;= 3</td>
<td>headers</td>
</tr>
<tr>
<td>&gt;= 4</td>
<td>sub headers</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>-x <em>num</em></td>
<td>set transaction mode to <em>num</em><br />
This is a bit field where,
<table>
<tbody>
<tr>
<td>0x01</td>
<td>KDB transaction logging ON</td>
</tr>
<tr>
<td>0x02</td>
<td>check that tables are locked</td>
</tr>
<tr>
<td>0x04</td>
<td>take transaction system lock</td>
</tr>
<tr>
<td>0x08</td>
<td>take KDB logging system lock</td>
</tr>
<tr>
<td>0x10</td>
<td>ERR if transaction locking is off</td>
</tr>
<tr>
<td>0x20</td>
<td>automatic KI_ROLLBACK on error</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>-u</td>
<td>unlock semaphore</td>
</tr>
<tr>
<td>-h</td>
<td>list command line switches</td>
</tr>
<tr>
<td>-t</td>
<td>tail journal log</td>
</tr>
<tr>
<td>-z</td>
<td>disable check for running KCMLs</td>
</tr>
<tr>
<td>-Z</td>
<td>zap current log file to nulls</td>
</tr>
</tbody>
</table>
