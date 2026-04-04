## Browsing files

This tree control displays the files and directory in the source directory. The Workbench determines the directory to use by first inspecting the environment variable PROGRAMS. If this does not exist or is not a plausible directory path then it will look for the environment variable HOME and if that does not exist then the current working directory is used. Only files with no extension or with an extension of .src or .asc are displayed.

There is a small menu supporting this mode with options to go up a directory, specify the directory to start from and an option to return to the original home directory.

<img src="bitmaps/browsefilemenu.png" data-border="0" width="140" height="51" alt="Up, specify dir and home menu opts with Home selected" />

Double clicking on a suitable file will LOAD the file into the editor replacing whatever is in memory. Right clicking will bring up a context menu with options to **Load**, **View** or display **properties**. **Load** is the default and has the same effect as double clicking. **View** will load the file into a new window for display only. **Properties** is currently non-functional.

If there are any platter files [\$DEVICE](mk:@MSITStore:kcmlrefman.chm::/$DEVICE.htm)d in the program then they will appear at the end of the tree. Expanding the platter will show the files. Though platters do not have directories and have a flat namespace, the browser attempts to display the files in a hierarchy using the NSG naming convention of using space as a separator. Files on platters can also be LOADed by clicking them.

<div id="ClickDiv">

<u>Click here to view an example of browsing a Rev8 directory</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example</u>

##### Browsing a Rev8 directory

<img src="bitmaps/FileBrowseTree.png" data-border="0" alt="Browsing a Rev8 directory" />

</div>
