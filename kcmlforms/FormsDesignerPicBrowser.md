Forms Designer - Browsing pictures

------------------------------------------------------------------------

Pictures are [objects](PicObjects.htm) on a form which can be associated with controls such as menu toolbars, trees and picture buttons using the picture browser. The forms designer picture browser is invoked from the [menu editor](FormsDesignerMenubars.htm) or from the ellipsis on the picture property of a control displayed in the property browser.

For information about the format of pictures see [Picture Formats](PicFormats.htm).

<img src="bitmaps/PicBrowse.gif" data-border="0" width="402" height="387" alt="Picture browser dialog" /> <span id="table"></span>

<span id="picselect"></span>

Select a name for the picture

Select the name of the picture from the drop list of pictures already the form and stock pictures. To add a new picture to this list you can use the [Add Picture dialog](FormsDesignerAddPictures.htm) on the tools menu.

<span id="picclear"></span>

Clear picture

Click this button to return no picture as the selection.

<span id="remotefile"></span>

Remote file

Check this radio button setting and enter the name of a file containing the picture. This file must be on the server and is in server format. It should be a relative file name and may include environment variables that will be expanded by the server. It is used to set the [.cache\$](tmp/PROP_PICTURE_CACHE.htm) property of the control. Be aware that the forms designer will not validate that the name is correct.

<span id="localfile"></span>

Local PC file

Click this radio button to use a file that is present on the client as the picture. The name of the file is taken from the File Open box below. The Forms Designer will read that file and inline the contents as the [.immediate\$](tmp/PROP_PICTURE_IMMEDIATE.htm) property provided the file size is less than 2kb. If it is bigger than that threshold a message box will appear showing the size and asking if it should still be inlined or whether a reference to the original filename should be saved as the value of the [.filename\$](tmp/PROP_PICTURE_NAME.htm) property. Generally the use of such a local filename is to be discouraged as it cannot be guaranteed that a file of that name will be available on all clients at all times. Furthermore some clients (e.g. CE KTerms) have no local file storage.
