ucompile (Unix)

General Form:\
\
ucompile \[-vcnu\] \[-w *in_platter*\] \[-e *sectors*\] \[-i *sectors*\] \[-W *out_platter*\]\
\[-d *find_list*\] \[-f *mask*\] \[-x *extension*\] \[ -p *find_pred*\]\[*directory*\] \[ *ascii-directory*\]

The *ucompile* utility is a Bourne shell script which uses the *kat* utility to de-compile an entire directory (including sub-directories) of KCML programs or a platter image containing KCML programs into ASCII form. ASCII programs have the '.asc' extension.

The *ucompile* utility works in two different modes depending on whether you are un-compiling from a platter image or from a directory. Some of the parameters are specific to platter operations, others to directory operations. And some are useful for both.

The parameters used with the *ucompile* command when working either with platter images or native operating system files, are as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="80">Switch</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>-c</td>
<td>Specifying the '-c' option causes the utility to generate source code for KCML versions &lt; release 2.00. E.g. '==' will be recreated as '='.</td>
</tr>
<tr>
<td>-e <em>sectors</em></td>
<td>The '-e' option should only be used if '-w' has already been specified. The '-e' option instructs <em>ucompile</em> to add the specified number of sectors to the file before it is placed onto the specified platter. A BASIC-2 header and trailer is also added to the file before it is added to the platter.</td>
</tr>
<tr>
<td>-f <em>mask</em></td>
<td>The '-f' option restricts the de-compilation to programs which match the mask.<br />
Note: If files are read from directories their names are considered to be the characters after the last slash, for example, D10/SU/MENU has a filename of MENU.</td>
</tr>
<tr>
<td>-i <em>sectors</em></td>
<td>The '-i' option should only be used if the '-w' option has already been specified. The '-i' option instructs <em>ucompile</em> to create a platter with the specified number of index sectors, before any files are copied onto it. By default the platter will be created with 43 index sectors.</td>
</tr>
<tr>
<td>-n</td>
<td>This option should be used to produce output formatted in a way acceptable to NPL. It implies '-c -x SRC'. There is no checking for KCML language extensions.</td>
</tr>
<tr>
<td>-u</td>
<td>Unconditionally overwrite any existing output files.</td>
</tr>
<tr>
<td>-v</td>
<td>The '-v' switch lists the program names on standard output as they are processed.</td>
</tr>
<tr>
<td>-w <em>platter</em></td>
<td>Specifying the '-w' switch followed by the name of a platter image file instructs <em>ucompile</em> to generate a BASIC-2 compatible file in release 2 atomised form in that platter. The '-i' and '-e' options can be combined with '-w'.</td>
</tr>
<tr>
<td>-x
extension</td>
<td>By default files are created with the filename extension of 'asc' ('SRC' if -n is specified). This extension can be changed with this switch.</td>
</tr>
</tbody>
</table>

The parameters used with the *ucompile* command when working with native operating system files, i.e. when the -W *platter* parameter is not specified, are as follows:

| Switch | Purpose |
|----|----|
| -p *find_pred* | The '-p' option allows any option available to the *find* command to be inserted after the 'p' parameter. This could allows only files with certain dates, etc. to be de-compiled. |
| -d *find_list* | *ucompile* recursively descends the directory hierarchy for each pathname in the *find_list* (that is, one or more pathnames). The default *find_list* is '\* .??\*' (i.e. all files and sub-directories). |

If no 'ascii-dir' is specified then the ASCII programs are left in the original directories.

The parameters used with the *ucompile* command when working with platter images, i.e. when the -W *platter* parameter is specified, are as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="80">Switch</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>-f <em>mask</em></td>
<td>The '-f' option restricts the de-compilation to programs which match the mask.</td>
</tr>
<tr>
<td>-W
platter</td>
<td>Programs can be un-compiled from a platter image file by use of this switch.</td>
</tr>
</tbody>
</table>

Examples:

ucompile -v D11 -w D11.bs2

will convert all the KCML programs in the directory 'D11' into 2200 atomised programs on the platter 'D11.bs2'.

ucompile -v -f 'NLMENU\*' D10 D10.asc

converts all programs with names starting 'NLMENU' in the 'D10' directory into ASCII form in the 'D10.asc' directory.

ucompile -n -W D11.bs2 D11.SRC

will de-compile all the programs in the platter image file 'D11.bs2' into separate ASCII text files in the directory 'D11.SRC'. All the files will have '.SRC' extensions.

ucompile -d 'SU PG' D10 D10.asc

will de-compile all the programs in the directories D10/SU and D10/PG into ASCII form in the directories D10.asc/SU and D10.asc/PG.

Compatibility notes:

The ability to de-compile from platter images and the ability to create BASIC-2 source was introduced in release 3.00.00.

See also:

[compile](compile.htm), [kat](%20kat.htm), [\$COMPILE]($COMPILE.htm)
