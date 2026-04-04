# <span id="cachesettings"></span> Cache settings

The cache holds form definitions and bitmaps. It is by default a subdirectory of the directory from which kclient is executed but you can use this dialog to change this to another directory. By default the maximum cache size is based on a proportion of free disk space capped at 50MB. Larger sizes can be set manually if required but the default will generally be more than adequate. Kclient will drop unused forms to manage the space automatically.

This tab allows the location and maximum size to be altered. The size can be specified as a fixed value or as a percentage of available space.

The cache can emptied via a button.

When connected to the server over a slow link, say a dialup PPP connection, performance can be improved by unchecking the 'Download pictures' checkbox. This will stop the client downloading bitmaps. Already cached bitmaps will still be displayed but no new ones will be downloaded.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/cache.gif" data-border="0" width="535" height="336" alt="Cache settings dialog" />

</div>
