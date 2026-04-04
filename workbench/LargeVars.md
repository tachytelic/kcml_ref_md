## Display Variables

This dialog is invoked from the right click [context menu](wbcontext.htm) when a string variable is being selected. You can also use the CTRL-F2 shortcut key. It has three types of display. The first is a mixed display which presents both an hexidecimal and ascii view of the varaible data. This is the view demonstarted below.

<div id="ClickDiv">

<u>Click here to see an example of a mixed view</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/LargeVars.png" data-border="0" alt="Display string variables dialog" />

In this example a 256 byte string *termfile\$* is being displayed in both hexadecimal and ascii. The mouse can be used to click on any of the bytes in either area and the offset into the string will be displayed. Here byte 23 is selected.

</div>

The second displays only the string by itself ignoring any charcters below 20 or ' '.

<div id="ClickDiv2">

<u>Click here to see an example of a string view</u>

</div>

<div id="PicDiv2" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/LargeVarsS.png" data-border="0" width="510" height="464" alt="Large Variable Display, String View" />

</div>

The third is only availble when the varaible you are looking at is a row buffer for a database table and there is an open connection to that database. This will display any data present in the row buffer, in a table format corresponding to field data.
