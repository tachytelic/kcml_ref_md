Tree control overview

A tree view control displays a hierarchical list of items using lines to connect related items in a hierarchy. Each item consists of a label and an optional picture. Furthermore each item can have a list of subitems associated with it making up the hiearchy. By clicking an item, the user can expand or collapse the associated list of subitems. Microsoft Windows Explorer uses a tree view control to display directories. This help file uses a tree control for its contents pane.

KCML distinguishes between the tree itself and the tree items that form the nodes of the structure.

Tree styles

The tree control has a number of design time set boolean style properties that determine the look of the overall tree:

|  |  |
|----|----|
| [HasButtons](tmp/PROP_TREE_HASBUTTONS.htm) | A tree that has this style set adds a button to the left side of each parent item. The user can click the button once instead of double-clicking the parent item to expand or collapse the child. This style does not add buttons to items at the root of the hierarchy. To do so, you must also set [HasLines](tmp/PROP_TREE_HASLINES.htm) and LinesAtRoot to TRUE. |
| [HasLines](tmp/PROP_TREE_HASLINES.htm) | This style enhances the graphic representation of a tree view control's hierarchy by drawing lines that link child items to their parent item. This style does not link items at the root of the hierarchy. To do so, you need to also set [LinesAtRoot](tmp/PROP_TREE_LINESATROOT.htm) to TRUE. |
| [LinesAtRoot](tmp/PROP_TREE_LINESATROOT.htm) | This style is used in conjunction with [HasLines](tmp/PROP_TREE_HASLINES.htm) and [HasButtons](tmp/PROP_TREE_HASBUTTONS.htm) to make the root of the tree the same as the other nodes. |
| [HasPictures](tmp/PROP_TREE_HASPICTURES.htm) | This property is used to enable the use of pictures for items within the tree. Normally plus and minus signs are ared to show open and closed directories, enabling this property will make use of a set of standard icons. |
| [ShowSelAlways](tmp/PROP_TREE_SHOWSELALWAYS.htm) | Setting this style causes a selected item to stay selected when the tree view control loses focus. |

OBJECT notation for tree nodes

Because of the nested parent child relationships between tree nodes, the OBJECT notation is very useful for manipulating tree objects. In particular for each tree item the objects representing the parent, first child, and next sibling (element at the same level) are readily available as attributes of the tree item object, respectively the [Parent](tmp/PROP_TREEITEM_GETOPARENT.htm), [Child](tmp/PROP_TREEITEM_GETOCHILD.htm) and [Next](tmp/PROP_TREEITEM_GETONEXT.htm) properties.

For example, to make all the child items of a tree item bold, the Child property is used to find the first property, and the Next property is used thereafter to find the next child. This example only acts on immediate children, but recursion could easily be used to make it act on all descendents.

DEFSUB 'MakeBold(OBJECT c) LOCAL DIM x x = c.Child WHILE OBJECT x \<\> NULL DO x.Bold = TRUE OBJECT x = x.Next WEND
