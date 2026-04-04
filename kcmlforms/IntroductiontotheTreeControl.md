Introduction to the Tree Control

------------------------------------------------------------------------

The tree control is used to present hierarchical information to the user in much the same way as the Windows 95/NT file explorer does. Items can be added to the control at multiple branches. The user can then later expand and collapse these branches by clicking on the folder icons.

<span id="Adding_items_to_the_tree" adding_items_to_the_tree=""></span>Adding items to the tree

Tree control items are added with the [*Add()* method. The](tmp/PROP_TREE_ADD.htm) [*Add()* method returns a unique identifier for each item that is added. The identifier is then used in conjunction with the](tmp/PROP_TREE_ADD.htm) [*Item()* method to change the properties of the item or to call a method for the item. A combination of the](tmp/PROP_TREE_ITEM.htm) [*Item()* and](tmp/PROP_TREE_ITEM.htm)

*Add()* methods is used to create multiple branches. For example:

treeItem = .treeControl1.Add("A Folder", 3)

would add an item to the tree. The numeric parameter specifies the type of item, in this case the item will be added as a parent item, i.e. a folder item that can be expanded by the user. Other numeric parameters are available to change the sort order used by tree branches, see the

*Add()* method for more information.

To add child items to the folder created in the example above the return variable is used with the

*Item()* method, for example:

.treeControl1.Item(treeItem).Add("A Child item", 0) .treeControl1.Item(treeItem).Add("Another child item", 0) .treeControl1.Item(treeItem).Add("A third child item", 0)

To add another folder with another level of child items the following would be used:

treeItem = .treeControl1.Item(treeItem).Add("Another Folder", 3) .treeControl1.Item(treeItem).Add("A Child item at a different level", 0) .treeControl1.Item(treeItem).Add("Another child item at a different level", 0) .treeControl1.Item(treeItem).Add("A third child item at a different level", 0)

<span id="Deferred_population_of_branches" deferred_population_of_branches=""></span>Deferred population of branches

When working with large trees, as would be the case with a file/directory browser, it would be inefficient to fill all levels of the tree in this way. To defer the population of tree branches the [*Expand()* event is used. This event is called the first time the user expands a new tree branch. If the branch is collapsed and re-expanded the event is not called. The](tmp/PROP_TREE_EXPAND.htm)

*ExpandItem* property is used to retrieve the index of the item that is being expanded, this property can then be used to populate the branch. For example, the following would populate the newly expanded branch with 10 items:

\- DEFEVENT Form1.treeControl1.Expand() FOR a = 1 TO 10 CONVERT a TO abc\$, (#####) ..Item(..ExpandItem).Add(abc\$, 0) NEXT a END EVENT

Obviously the above example is somewhat contrived as you would need to be a little bit more precise as to the information added to a particular branch.

The [*ExpandChange()* event is called each time a branch is expanded or collapsed. This is particularly useful if the contents of a level need to be refreshed. Note that if a tree branch is being expanded for the first time, the](tmp/PROP_TREE_EXPANDCHANGE.htm) [*ExpandChange()* event will be called immediately after the](tmp/PROP_TREE_EXPANDCHANGE.htm)

*Expand()* event.

[Click here](Exampledirectorybrowser.htm) to see an example program

 
