ChangeRowCol (grid control method)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> ChangeRowCol(int, int, int, int) Method

**Allows new rows and columns to be added to the grid**

|      |                                    |
|------|------------------------------------|
| Int1 | Row position                       |
| Int2 | Column position                    |
| Int3 | Number of rows to insert/delete    |
| Int4 | Number of columns to insert/delete |

This method is used to insert and delete rows and columns in a Grid control. The method arguments specify the row and column position where the new cells are to be inserted and the number of rows and columns to add. Negative values are used to remove rows and columns. For example, the following would insert a single new row at row 3 moving the old row 3 to row 4: .GridControl1.ChangeRowCol(3, 1, 1, 0)

When inserting a row the insert row and any rows below it are moved down together with their contents and properties and a new row with default attributes is created at the insert point. When adding columns at and to the right of the insert column are similarly shifted.

**Note 1:** The rows or columns affected are those **before** the nominated row and column position. Thus, inserting 1 row with a row position of 2 means that a new row will be inserted between rows 1 and 2. Deleting 1 row with a row position of 2 means removing the row just before row 2, which means deleting row 1.

**Note 2:** Prior to version 6.00 of KCML the effect of the ChangeRowCol() method was only in the client. Even if server side text storage was enabled, the contents would not be updated and they would no longer reflect the state of the grid in the client. This anomaly was corrected in KCML 6.00 where server side text storage is implicit.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
