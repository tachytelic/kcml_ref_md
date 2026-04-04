Forms Designer - Working with tree controls

------------------------------------------------------------------------

Tree controls are used to provide hierachical lists of information. The look of the control is similar to that used by the MS Windows file explorer.

To add a tree control to the current form select the <img src="bitmaps/FDTreeTool.png" data-align="BOTTOM" data-border="0" alt="Tree control tool" /> icon from the controls palette and mark out on the form a rectangular area for the control. There is no special editor associated with the tree control. It is generally built at runtime using the [Add()](tmp/PROP_TREEITEM_ADD.htm) method. For more information on programming trees see [Introduction to Trees](IntroTree.htm).

There are however a number of useful styles that can be set in the forms designer, viz:

|  |  |
|----|----|
| [HasButtons](tmp/PROP_TREE_HASBUTTONS.htm) | A tree that has this style set adds a button to the left side of each parent item. The user can click the button once instead of double-clicking the parent item to expand or collapse the child. This style does not add buttons to items at the root of the hierarchy. To do so, you must also set [HasLines](tmp/PROP_TREE_HASLINES.htm) and LinesAtRoot to TRUE. |
| [HasLines](tmp/PROP_TREE_HASLINES.htm) | This style enhances the graphic representation of a tree view control's hierarchy by drawing lines that link child items to their parent item. This style does not link items at the root of the hierarchy. To do so, you need to also set [LinesAtRoot](tmp/PROP_TREE_LINESATROOT.htm) to TRUE. |
| [LinesAtRoot](tmp/PROP_TREE_LINESATROOT.htm) | This style is used in conjunction with [HasLines](tmp/PROP_TREE_HASLINES.htm) and [HasButtons](tmp/PROP_TREE_HASBUTTONS.htm) to make the root of the tree the same as the other nodes. |
| [HasPictures](tmp/PROP_TREE_HASPICTURES.htm) | This property is used to enable the use of pictures for items within the tree. Normally plus and minus signs are ared to show open and closed directories, enabling this property will make use of a set of standard icons. |
| [ShowSelAlways](tmp/PROP_TREE_SHOWSELALWAYS.htm) | Setting this style causes a selected item to stay selected when the tree view control loses focus. |
