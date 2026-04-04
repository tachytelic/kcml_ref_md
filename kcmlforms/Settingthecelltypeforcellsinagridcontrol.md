Setting the cell type for cells in a Grid control

------------------------------------------------------------------------

To make it easier to format data within a Grid control various types are available by setting the [*Type\$* property. For example, you may want an entire row or column to be formatted to display dates or numeric values etc. If formatting is not used then it is unlikely that columns of numeric information will line up correctly. For details of the available types refer to the](tmp/PROPSTR_TYPE.htm)

*Type\$* property.

The following example first sets the format type of column 6 so that it will automatically format dates. It would then place a number of random dates into each cell in the column:

.GridControl1.Cell(0, 6).Type\$ = "D" FOR Count = 1 TO .GridControl1.Rows CONVERT \#DATE - INT(RND(1) \* 300) TO abc\$, (########) .GridControl1.Cell(Count, 6).Text\$ = abc\$ NEXT Count

Note: The \#DATE function is used to return today's date as a julian value. The date cell type automatically converts Julian values into the local date format used by the PC.
