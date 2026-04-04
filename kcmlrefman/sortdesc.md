Sort key descriptors

The [SORT](SORT.htm) and [FSORT](FSORT_BU.htm) commands can optionally take a KEY clause which describes how the sort is to be performed. The reserved work KEY is followed by a string expression which is interpreted as a list of 4 byte key segment descriptors. The list terminates either at the end of the string or at the first segment descriptor with a zero length.

The layout of a segment descriptor is as shown in the table.

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
<td>Length, zero marks end of descriptors</td>
</tr>
<tr>
<td>2,2</td>
<td>Start of segment, counted from 1</td>
</tr>
<tr>
<td>4</td>
<td>Bits defining how the segment is to be sorted. These bits can be added together
<table width="100%">
<thead>
<tr>
<th width="180">KCML constant</th>
<th>Bit</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>_SORT_DESCENDING</td>
<td>HEX(20)</td>
<td>Sort into descending order</td>
</tr>
<tr>
<td>_SORT_COLLATESEQ</td>
<td>HEX(40)</td>
<td>Use <a href="collate.htm">collating sequence</a></td>
</tr>
<tr>
<td>_SORT_CASEINSENSITIVE</td>
<td>HEX(80)</td>
<td>Case insensitive</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

Note that a case insensitive sort requires a [collating sequence](collate.htm) to be defined for the code page.
