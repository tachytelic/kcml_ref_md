\$COMPILE

------------------------------------------------------------------------

<div class="Generalform">

General Forms:\
<img src="bitmaps/compiled.gif" data-align="BOTTOM" data-border="0" alt="compiled.gif" />\
2. \$COMPILE Filename TO Filename\
\

</div>

------------------------------------------------------------------------

The \$COMPILE statement copies and compiles programs from one location to another. It has a similar function to the [MOVE](MOVE.htm) statement except that program files are re-compiled. It provides an easy way to compile ASCII source into KCML compiled code and vice versa. This statement is particularly useful for writing programs that need to generate compiled KCML code.

The first form of \$COMPILE is used to compile an entire directory, or a specified file within a directory to another directory. The source and destination directories are selected with the [SELECT \#](SELECT_DISK.htm) statement.

The second form is used to compile an individual file to another file. The destination file must not exist otherwise an error will result.

Examples:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="clear" width="338">$COMPILE "First" TO "/tmp/last"</td>
<td class="clear" width="229">Compile the file <em>First</em> to the file <em>/tmp/Second</em></td>
</tr>
<tr>
<td class="clear" width="338">SELECT #20 "/tmp/PROGS"<br />
SELECT #21 "PROGS"<br />
$COMPILE #20 TO #21</td>
<td class="clear" width="229">Compile all files from the directory /tmp/PROGS into the directory PROGS.</td>
</tr>
<tr>
<td class="clear" width="338">SELECT #20 "/tmp/PROGS"<br />
SELECT #21 "PROGS"<br />
$COMPILE #20, "FILE1" TO #21</td>
<td class="clear" width="229">Compile the file FILE1 from the directory /tmp/PROGS into the directory PROGS.</td>
</tr>
</tbody>
</table>

Specifying the optional 'R' parameter allows programs to have [REM](REM.htm) statements removed during the compilation. Some REM statements may remain as stubs if they are referred to in the program to avoid problems with missing lines.

Specifying the optional '!' parameter allows programs to be compiled and scrambled into the destination directory. The [SELECT PASSWORD](SELECT_PASSWORD.htm) statement must be executed before \$COMPILE to specify the password used to scramble the program.

Errors are sent to the TRACE device, which defaults to the screen but may be redirected to a file with [SELECT TRACE](SELECT_TRACE.htm), e.g. SELECT TRACE "/tmp/logfile". This means that \$COMPILE will never throw a run time error itself and an [ERROR](ERROR.htm) clause will never be invoked. From KCML 6.00 onwards it is also possible to check for syntax errors during the compile by inspecting the value of [ERR](ERR.htm) to see if it is nonzero after the compile. You ought to zero ERR by inspecting it before the compile.


        a=ERR
        $COMPILE infile$ TO outfile$
        PRINT (ERR <> 0 ? "FAILED" : "OK")

Byte 40 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE40) can be set to change the characteristics of \$COMPILE. This byte can be set from a combination of the following bits:

|  |  |
|----|----|
| HEX(00) | Perform a normal compilation |
| HEX(01) | Forces \$COMPILE to assume that all files are program files when loading. |
| HEX(02) | All programs saved to native files with \$COMPILE, [SAVE](SAVE.htm) and [RESAVE](RESAVE.htm) will be saved in ASCII format. |
| HEX(04) | All programs saved to native files as ASCII will have .SRC added as an extension. When [LOADing](LOAD.htm) .SRC is added to the filename before it is loaded. |
| HEX(08) | When saving or loading ASCII programs, automatically translate spaces in filenames to underscores. When compiling from native files to platters, underscores are changed to spaces. |
| HEX(10) | When \$COMPILEing back to a platter translate filenames to lowercase. |
| HEX(20) | Used in conjunction with the HEX(02) to force \$COMPILE to create ASCII files in [LIST S](LIST.htm) format. |
| HEX(40) | Forces \$COMPILE to overwrite programs if they exist, otherwise \$COMPILE will generate an error. |
| HEX(80) | \$COMPILE will not add a .src extension when saving compiled programs. |

For example, the following would force \$COMPILE to de-compile all programs into ASCII format and translate any spaces in the filenames to underscore characters.

<div class="listing">

STR(\$OPTIONS RUN,40,1)=HEX(0A)

</div>

See also:

<div class="LISTING">

[MOVE](MOVE.htm), [SELECT TRACE](SELECT_TRACE.htm), [SELECT PASSWORD](SELECT_PASSWORD.htm)

</div>
