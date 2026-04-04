fsort (Unix)

General Form:\
\
<img src="bitmaps/fsort.gif" data-border="0" width="531" height="45" alt="General usage for fsort" />

The *fsort* utility is used to sort KCML data files in BA, BU or DC format, respectively. BA nd DC modes are only supported for backward compatibility with early versions of KCML. The sorting of files is also available directly from KCML with the [FSORT](FSORT_BU.htm) statement.

The parameters to both commands are similar. '*in_file*' is the name of the file to be sorted, and '*out_file'* is the name of the output file. If the '-o *in_file*' form is used, the input file will be overwritten with the sorted output.

The '*start_sec*' parameter is the sector number at which sorting is to start. The *fsort* utility also requires the size of each record, in bytes, and the number of sectors to sort. The BA record size must be an exact sub-multiple of 256 bytes.

The optional '-f' and '-r' parameters are used to specify sort keys; there may be up to ten. Each key specification is as follows:


    	-f start end
    or
    	-r start end

The *start* and *end* indicate the first and last significant character of the record in each comparison, starting at character 1 for the first byte of each record. The '-f' indicates forward lexicographic order for this key; '-r' reverses this order.

By default, records are sorted in forward lexicographic order on their entire length.

Specifying a start sector of zero implies that the sort should start at the beginning of the file. If '*start_sect*' is N, the contents of the first N sectors of the input are copied unchanged to the output. Information beyond the end of the sort, that is, beyond the end sector in a DC sort or after the required number of sectors in a BA sort, may be lost. Specifying zero as the number of sectors to be sorted in a BA sort will sort to the end of the file.

In a DC sort, administrative information is preserved. This means that if, for example, two 20-element string arrays were saved when creating the input file, then two 20-element string arrays can be loaded from the output. Note that elements of the original first array may now appear in the second array, and vice versa. All data in a file to be sorted DC should be string arrays of the same length; use the [SORT](SORT.htm) statement to sort numeric data.

Workspace for the sort is allocated in the directory '/tmp' unless overridden by the environment variable [WORKSPACE](EnvVars.htm#WORKSPACE).

See also:

[FSORT BU](FSORT_BU.htm),\
[SORT](SORT.htm)
