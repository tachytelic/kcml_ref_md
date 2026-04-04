HasPictures (tree control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Set to show has pictures**

This property is used to enable the use of pictures for items within the tree. Normally plus and minus signs are ared to show open and closed directories, enabling this property will make use of a set of standard icons. Alternative icons can be set within the program with the [*Image* and](PROP_TREEITEM_IMAGE.htm) [*OpenImage* properties.](PROP_TREEITEM_OPENIMAGE.htm)

This property is a design time only property and can therefore only be set within the KCML forms designer.

##### Example:


     IF (.treeControl.HasPictures)
       ...
     END IF

##### See also:

Other [tree](tree.htm) properties, methods and events, [treeitem](treeitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
