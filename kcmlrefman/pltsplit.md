pltsplit (UNIX)

General Form:\
\

pltsplit \[-psd\] \[-f mask \] platter directory\

The pltsplit utility is used to copy program or data files out from the specified platter image into the specified UNIX directory. It is the reverse of the pltglue utility. If the file is a KCML program, the BASIC-2 headers and trailers are removed before the file is created in UNIX. Data files and BASIC-2 programs are copied without changing the format of the file.

The flags used with the pltsplit utility are as follows:

|  |  |
|----|----|
| -d | The '-d' parameter is instructs pltsplit to convert data files only. |
| -f mask | The '-f' mask option limits input to those files matching the specified pattern. The pattern matching is limited, and does not allow true grep-like patterns. |
| -p | The '-p' parameter instructs pltsplit to convert only program files from the platter. With versions of KCML \< 2.06.08 this was necessary, now this task is better performed with the deatom utility. |
| -s | The '-s' option allows scratched files to be converted into UNIX files. |

Example:

pltsplit -dsv -f 'GB\*' D11.2200 D11.tmp

The above example would convert all data files, including scratched data files, from the platter 'D11.2200', into UNIX files held in the directory 'D11.tmp'. Only files which match the pattern would be converted.

See also:

[pltglue](pltglue.htm)
