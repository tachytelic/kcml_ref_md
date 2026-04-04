\#GOLDKEY

------------------------------------------------------------------------

General Form:\
\
     \#GOLDKEY\
\

------------------------------------------------------------------------

The \#GOLDKEY function returns a number ranging from 1-65535 that is specific to each KCML installation. \#GOLDKEY is intended to ensure that the application being used can only work with a particular copy of KCML. This function is valid wherever a numeric expression is valid.

<table>
<caption>Licence/Dongle types and #GOLDKEY values.</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Dongle</th>
<th>Operating<br />
system</th>
<th>KCML<br />
Version</th>
<th>#GOLDKEY value<br />
</th>
</tr>
</thead>
<tbody>
<tr>
<td>Branded versions</td>
<td>All</td>
<td>KCML5</td>
<td>Taken from licence file</td>
</tr>
<tr>
<td>Parallel DK12</td>
<td>Unix only</td>
<td>KCML4</td>
<td>Taken from the inode number of the file TERMFILE as set by the TERMFILE environment variable.</td>
</tr>
<tr>
<td>Parallel DK12</td>
<td>Single user DOS</td>
<td>KCML4</td>
<td>Taken from the Network Interface Card address, if no network card is installed then the serial number from the hard disk is used.</td>
</tr>
<tr>
<td>Parallel DK2<br />
PCMCIA DK38</td>
<td>Unix<br />
Networked DOS</td>
<td>KCML4</td>
<td>Taken from the dongle.</td>
</tr>
<tr>
<td>Serial DK96</td>
<td>Unix only</td>
<td>KCML4</td>
<td>Taken from the dongle.</td>
</tr>
</tbody>
</table>

Syntax example

number = \#GOLDKEY

See also:

[\#ID](_ID.htm), [\$SER]($SER.htm)
