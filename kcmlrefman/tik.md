tik

General Form:\
\
tik \[-vmb\] \[-t *termname*\] *source_file*\

The *tik* utility converts a source text file created by a text editor into a number of *TERMINFO* keyboard/screen definition files or *GPDINFO* printer definition files in the same directory. Generally text mode terminals are only used on Unix systems but they can also be used with NT servers by connecting through a terminal server. This utility, and the terminal database, is not generally shipped with NT systems but it is available for download from the [kcml.com](http://www.kcml.com) website.

The *source_file* is a free format text file conventionally called *TERMINFO/src* for the Terminal Information database and *GPDINFO/src* for the General Printer Driver database. It consists of a number of sections starting with section names enclosed in \[\]s e.g. \[vt220\]. The section name corresponds to the terminal/printer type described inside the section. Terminal types are specified by the environment variable *KTERM* which must be set and exported before **KCML** is executed. Some terminals/printers are similar but known by several names and in these cases the alternative names can be listed in the section name separated by \`\|' characters e.g. \[wyse30\|wyse50\]. *tik* will create a file with the same name as the section name in the same directory as the source file. **KCML** expects to find these files in the directory *TERMINFO* or *GPDINFO* which must be in one of the directories specified in the *PATH* environment variable. So for a Wyse 60 terminal with a *KTERM* of wy60 then **KCML** will search its path for the file TERMINFO/wy60. UNIX links are used for those descriptions that have alternative names. Typically for terminals the source file will be /usr/lib/kcml/TERMINFO/src and the usual way of compiling it will be

tik /usr/lib/kcml/TERMINFO/src

which will leave the new terminal description files in the directory /usr/lib/kcml/TERMINFO.

The switches available with the *tik* utility are as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="100">Switch</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>-b</td>
<td>Generate NPL type $KEYBOARD files from the specified source file.</td>
</tr>
<tr>
<td>-m</td>
<td>If specified, will cause tik to merge any description taken from the UNIX <em>/usr/lib/terminfo</em> database with the source file when compiling.</td>
</tr>
<tr>
<td>-p</td>
<td>If specified, will compile the GPDINFO database.</td>
</tr>
<tr>
<td>-v</td>
<td>If specified instructs <em>tik</em> to run in verbose mode.</td>
</tr>
<tr>
<td>-t <em>termname</em></td>
<td>If specified, will default a description for the terminal specified by <em>termname</em> from the UNIX <em>/usr/lib/terminfo</em> database. The description is sent to the standard output in a form that can be appended to a <strong>KCML</strong> TERMINFO/src file e.g.<br />
<br />
tik -t $TERM &gt;&gt;/usr/lib/kcml/TERMINFO/src<br />
<br />
when run on a new type of terminal will add a minimal description for that terminal. Usually this will specify only a few function keys, insert, delete and the arrow keys. However most of the screen controlling parameters should be defined and any missing capabilities can be later added by hand with an editor.</td>
</tr>
</tbody>
</table>

See also:

[tiklist](tiklist.htm), Terminal support
