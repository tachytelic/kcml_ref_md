MultiIndex\$ (listbox control property)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Read<br />
only</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Returns a multiple section as a list of indices in a string**

In a index with the Selection property set to allow multiple selections, a list of the currently selected item indices can be obtained from this read-only string property. They are returned as 16 bit integers in Intel byte ordering. There is no indictator for the end of the list so you must use the [SelCount](PROP_LISTBOX_MULTICOUNT.htm) property to see how many items are selected. Such a list can be extracted using something like LOCAL DIM a\$(\_MAXSEL)2, b\$\_MAXSEL\*4, i, x, maxi a\$() = .listControl1.MultiIndex\$ i = 1 maxi = MIN(\_MAXSEL, .listControl1.SelCount) WHILE i \<= maxi DO \$UNPACK(F=HEX(E002)) a\$(i) TO x IF (i == 1) b\$ = \$PRINTF("%d", x) ELSE b\$ = b\$ & \$PRINTF(",%d", x) END IF i++ WEND

This property is obsolete. Use [SelectedFirst](PROP_LISTBOX_GETSELECTEDFIRST.htm) instead.

##### See also:

Other [listbox](listbox.htm) properties, methods and events, [listitem](listitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
