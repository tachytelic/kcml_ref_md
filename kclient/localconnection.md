# <span id="localconnection"></span> Local connection

Here is the main property page for a local connection. It will only be available for the WKCML product where both the client and the server are on the same computer.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/localconn.gif" data-border="0" alt="Local connection property page" />

</div>

The relevant fields are

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Control</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>Connection Type</td>
<td>'Connect locally'</td>
</tr>
<tr>
<td>KCML Command Line</td>
<td>This is an editable field in which you can supply a command line to be passed to the server containing <a href="commandlineswitches.htm">command line switches</a> and an optional initial program name. This is quite technical and error prone.<br />
<br />
For many applications it is sufficient to select from the drop down list one of the registered profiles. These are created in the registry by the application setup program and hide details of the exact command line from users. For more details of how profiles may be created see the -A switch in the appendix on <a href="commandlineswitches.htm">command line switches</a>.</td>
</tr>
<tr>
<td>Start directory</td>
<td>The directory to be the current working directory when KCML starts executing. If there is no KCML command line (see above) then this will be, by default, the current directory at the time. However if the KCML command line refers to an initial program then KCML will use that programs base directory as the default. By specifying an explicit directory here the default can be overridden.</td>
</tr>
<tr>
<td>Application command line</td>
<td>This is a string to be made available to the server via a special $DECLARE. The server can use it as a bookmark to determine an initial menu setting. See the -C flag in the <a href="commandlineswitches.htm">command line switches</a> appendix and also the section on <a href="implbmarks.htm">bookmarking</a>.</td>
</tr>
<tr>
<td>Disable Workbench</td>
<td>If checked this will make KCML use the original KCML4 editor rather than the KCML Workbench. The default is to use the Workbench.</td>
</tr>
</tbody>
</table>
