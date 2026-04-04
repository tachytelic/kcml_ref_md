# Registry keys

Kclient stores user preferences under the key

    HKEY_CURRENT_USER\SOFTWARE\Kerridge\Kclient

This key can safely be deleted to return to the freshly installed state.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Key</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>Forms</td>
<td>Settings for <a href="formprefs.htm">GUI form preferences</a> such as last position and colors.
<table>
<thead>
<tr>
<th>Value</th>
<th width="60">Type</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>EditableColor</td>
<td>DWORD</td>
<td>RGB color for editable text boxes</td>
</tr>
<tr>
<td>EnableEuroCurrency</td>
<td>DWORD</td>
<td>0 or 1 to disable or enable alternate currency support</td>
</tr>
<tr>
<td>ReadOnlyColor</td>
<td>DWORD</td>
<td>RGB color for read only text boxes</td>
</tr>
<tr>
<td>EuroReadOnly</td>
<td>DWORD</td>
<td>RGB color for read only text boxes in alternate currency mode</td>
</tr>
<tr>
<td>FetchPictures</td>
<td>DWORD</td>
<td>1 to cache pictures, 0 not cache them</td>
</tr>
<tr>
<td>LastPos</td>
<td>String</td>
<td>X and Y position of top left corner of last form</td>
</tr>
<tr>
<td>LargeToolbar</td>
<td>DWORD</td>
<td>1 for large toolbar icons, 0 for small</td>
</tr>
<tr>
<td>iTipType</td>
<td>DWORD</td>
<td>1 for enabled tooltips, 0 for disabled</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>HostList</td>
<td>The subkeys of this key contain a number of values for each of the hosts that have successfully connected. The login host combo box is initialized from this list.</td>
</tr>
<tr>
<td>Printer</td>
<td><a href="printerpreferences.htm">Printer settings</a> e.g. current local printer</td>
</tr>
<tr>
<td>Terminal</td>
<td>Settings for the <a href="textprefs.htm">Text Window terminal</a> emulation including position, colors etc.</td>
</tr>
</tbody>
</table>

Cache settings common to all instances of the client are stored the key

    HKEY_CURRENT_USER\SOFTWARE\Kerridge\Kclient

| Value  | Type   | Purpose          |
|--------|--------|------------------|
| Folder | String | directory to use |
