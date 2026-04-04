Grid cell precedence rules

Each gridcell enumerated property has a **Default** value and you can set properties generically by row, column and for the whole grid. When determining the properties that apply to a particular cell the grid control applies some precedence rules. It checks to see if an explicit value has been assigned in the following order

1.  for that cell
2.  for its row
3.  for its column
4.  for the whole grid

Once it has found an explicit setting then any lesser precedence values are ignored. If none of these dimensions has been given an explicit value then the **Default** means that the next value in the enumeration is used.

**Note:** there are some notable special cases in that prior to KCML 6.00 the [.CanConvert](tmp/PROP_KCMLEDIT_CANCONVERT.htm) property had a default of FALSE so if any dimension set it to TRUE then it remained be TRUE even if some higher priority dimension had set it to FALSE. Furthermore *.text\$* can only be set for a cell.
