ColSize (gridcell control property)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Write<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, Type, Header, Largest, Stretch, Automatic)*

**Selects how column width is determined**

The **ColSize** property is used to specify how columns can be automatically sized according to their content. This is a cell based property, although it only has an effect if applied to a column. It is possible to set a grid-wide column sizing property which used on columns that have default sizing. For instance the following example will set the column sizing to be based on type for all columns except column 5 which is based on the largest entry. .gridControl1.Cell(0, 5).ColSize = &.Largest .gridControl1.ColSize = &.Type

The following ColSize options are available.

|  |  |
|----|----|
| Default | The column size is determined by the [ColWidth](PROP_GRIDCELL_COLWIDTH.htm) property or the default width for columns. |
| Type | The width is based on the [type](PROPSTR_TYPE.htm) of the column. Nearly all data types, such as D (date), T (time), Np.s (numeric) and In (integer) display all values with the same width. For small strings (S1, S2 and S3) the width is based on the largest single character (often, but not necessarily 'W'). For larger string types the average character width is used. |
| Header | The width is based on the [type](PROPSTR_TYPE.htm) of the column. However if the header string in the [Heading\$](PROP_GRIDCELL_HEADING.htm) property is wider, then the width of the header is used instead. |
| Largest | The column is sized to the largest entry. This means that no text will be truncated. This is the most computationally intensive of the options but this will not be a problem except in very large grids. |
| Stretch | The column will be at least its default width wide. After sizing all other column types if there is room for the grid to be wider without creating a horizontal scroll bar, then all columns that can stretch are widened proportional to make the grid as wide as possible |
| Automatic | Where there is a [type](PROPSTR_TYPE.htm) and it is not a long string then *Header* column sizing is used, otherwise *Stretch* is used. |

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
