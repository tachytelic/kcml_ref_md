INPUT SCREEN

------------------------------------------------------------------------

General Form:\
\
     INPUT SCREEN alpha_receiver \[ , AT(row, column) \] \[ , BOX(depth, width) \]\
\
Where:\
\
     row, column, height, width      = numeric expressions\
\

------------------------------------------------------------------------

The INPUT SCREEN statement is used to copy the specified portion of the screen currently being displayed into an alpha variable. The alpha variable can then later be used by the [PRINT SCREEN](PRINT_SCREEN.htm) statement to re-display the specified portion of the screen. This cycle has the same effect as the [WINDOW OPEN/CLOSE](WINDOW.htm) statements.

This statement is not relevant in a graphical forms environment and can therefore only be used within text only applications. It is not supported for systems using DBCS code pages or UTF-8 encoded Unicode.

The screen is read row by row starting at the specified co-ordinates for the specified number of rows and columns.

If the AT values are omitted, the following defaults are assumed:

|                                    |     |
|------------------------------------|-----|
| row (vertical start position)      | 0   |
| column (horizontal start position) | 0   |

If the BOX values are omitted, the following defaults are assumed:

|       |            |
|-------|------------|
| depth | MaxRow     |
| width | MaxCol - 1 |

where MaxRow is the number of rows on the screen and MaxCol is the number of columns as defined in the TERMINFO description for the terminal. Thus for a normal 24x80 screen

INPUT SCREEN a\$()\
INPUT SCREEN a\$(), AT(0,0),BOX(24,79)

are equivalent. Note that depth + 1 rows and width + 1 columns are copied. The depth and width are defined in this curious way for compatibility with BASIC-2C.

The information returned to the alpha variable from the INPUT SCREEN statement, consists of an 80-byte string containing header information about the display (see table 1.8), followed by three sections containing the actual characters, attribute and box graphic information, and color attribute information respectively. Each of these sections should be (( depth + 1 ) \* ( width + 1 )) bytes. Characters are read from the screen row by row for the depth + 1 rows and column by column within each row for width + 1 columns. If the specified alpha variable is too small to store the required information, the contents of the alpha variable are truncated at the last complete section. For example:

INPUT SCREEN screen_1\$, AT(5,5), BOX(5,5)

would enter rows 5 - 10 inclusive, columns 5 - 10 into the variable screen_1\$ . For all of the required information to be correctly stored, the alpha variable screen_1\$ must be dimensioned as follows:

|           |                                                       |
|-----------|-------------------------------------------------------|
|           |                                                       |
| 108       | Sections 1, 2 and 3 ((depth + 1) \* (width + 1)) \* 3 |
| Total 188 |                                                       |

To use INPUT SCREEN to store the entire contents of a standard 24x80 screen requires 6080 bytes

DIM screen\$(80 + 25 \* 80 \* 3 )\
INPUT SCREEN screen\$()

Though it is not possible to write on the 25th row of a screen it must still be recorded as [PRINT BOX(24,80)](PRINT_BOX(.htm) requires overscore box attributes on the 25th row.

A copy of a partitions screen can be saved to disk in INPUT SCREEN format either by pressing a special key or on receipt of a SIGUSR2\* signal. The screen is written to a file named scrndxxx in the current directory where xxx is the partition. This file can then be loaded from disk by another user and displayed on their screen with the [PRINT SCREEN](PRINT_SCREEN.htm) statement. This facility is intended for remote support. The special screen dumping key is identified by the ScreenDump TERMINFO clause.

\*      SIGUSR2 is a signal that can be sent to a process by issuing the Unix kill command.

<table>
<caption>The first 80 bytes returned by INPUT SCREEN</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Bytes</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>1-29</td>
<td>Terminal ID message received from terminal. Always returns `2236DE R03 19200BPS 8+O (USA)' in the DOS version.</td>
</tr>
<tr>
<td>30-65</td>
<td>Reserved - all HEX(00).</td>
</tr>
<tr>
<td>66</td>
<td>Binary number of the valid display sections. This depends on the size of the receiver variable.</td>
</tr>
<tr>
<td>67</td>
<td>Binary screen size (lines), normally 24, as determined by the Lines clause in the TERMINFO description of the terminal.</td>
</tr>
<tr>
<td>68</td>
<td>Binary screen size (columns), as determined by the Columns clause in the TERMINFO description of the terminal, defaults to 80.</td>
</tr>
<tr>
<td>69</td>
<td>Binary value of the row specified by AT.</td>
</tr>
<tr>
<td>70</td>
<td>Binary value of the column specified by AT.</td>
</tr>
<tr>
<td>71</td>
<td>Binary value of the depth specified by BOX.</td>
</tr>
<tr>
<td>72</td>
<td>Binary value of the width specified by BOX.</td>
</tr>
<tr>
<td>73-74</td>
<td>Reserved HEX(00).</td>
</tr>
<tr>
<td>75</td>
<td>Current attribute when enhanced mode is selected by HEX(0E)<br />
HEX(40) reverse video, HEX(20) blink<br />
HEX(10) bright, HEX(08) underline.</td>
</tr>
<tr>
<td>76</td>
<td>Video mode, HEX(00) if attributes turned off by HEX(0D), HEX(01) if permanently selected, HEX(02) if attribute is currently enabled.</td>
</tr>
<tr>
<td>77</td>
<td>Alternate character set status, HEX(00) for normal character set selected, HEX(02) for alternate character set.</td>
</tr>
<tr>
<td>78</td>
<td>Cursor status, HEX(00) cursor off, HEX(01) cursor on steady,<br />
HEX(02) cursor on blinking.</td>
</tr>
<tr>
<td>79</td>
<td>Binary cursor position (row).</td>
</tr>
<tr>
<td>80</td>
<td>Binary cursor position (column).</td>
</tr>
</tbody>
</table>

Character information - Section 1

The next set of bytes, after the 80 bytes of header information, contains the characters present within the range specified by AT and BOX. Characters are read from the specified area row by row for the specified range, and column by column within each row for the specified range.

Video attribute and box graphic information - Section 2

The second section contains a one byte attribute for each character. The code represents the video attribute mode, and information about box graphics if present. The code is structured as follows:

|         |                                            |
|---------|--------------------------------------------|
| HEX(80) | Alternate character set to be used         |
| HEX(40) | Reverse video attribute is on              |
| HEX(20) | Blink attribute is on                      |
| HEX(10) | Bright attribute is on                     |
| HEX(08) | Underline attribute is on                  |
| HEX(04) | Left horizontal box graphic segment is on  |
| HEX(02) | Right horizontal box graphic segment is on |
| HEX(01) | Vertical box graphic segment is on         |

Color attribute information - Section 3

This section stores a one byte code for each character. The code represents the background and foreground color attribute for the character. The background attribute is stored in the high order nibble and ranges from HEX(0x) to HEX(7x), while the foreground attribute is stored in the low order nibble and may have a value ranging from HEX(x0) to HEX(x7).

INPUT SCREEN will only record color information that is set with the special color sequence, HEX(020204 aa bb cc dd ee 0F) The BASIC-2C sequence HEX(02000605 aa bb cc dd ee 0F) is also supported though this sequence will only work if byte 22 of [\$OPTIONS]($OPTIONS.htm#BYTE22) is set to a non-zero value. Such sequences are only supported on certain terminal types, refer to the [Terminal support](TextTermIntro.htm) chapter for more information.

If color attributes are not in use each byte in section 3 is set to HEX(07) for black background and a white foreground.

Syntax examples:

INPUT SCREEN screen\$()\
INPUT SCREEN test\$,AT(row,col)\
INPUT SCREEN new\$, AT(2,4), BOX(7,7)\
INPUT SCREEN FLD(window\$.window_2\$),AT(4,4)

See also:

[PRINT SCREEN](PRINT_SCREEN.htm), [WINDOW OPEN/CLOSE](WINDOW.htm)
