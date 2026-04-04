Adding pictures to forms in the Forms Designer

This option of the Tools menu is used to explicitly create [picture objects](PicObjects.htm) in a form. Normally pictures are created automatically when the *.Picture* property of a [picture enabled control](PicEnabledControls.htm) is set. This option allows pictures to exist independently of a control so that they can be manipulated at runtime perhaps.

<img src="bitmaps/AddPic.png" width="450" height="210" alt="Add picture dialog" />

|  |  |
|----|----|
| Pictures | A list of the pictures currently in the form |
| Preview | A preview thumbnail of the curretly selected picture |
| Add Local... | This will bring up a standard Windows Open File dialog allowing you to browse and select a local file from an accessible filesystem. The picture will be named automatically |
| Add Remote... | This brings up a simple dialog asking for a name for the picture and a server based filename for the file. This is used to set the [*.cache\$*](tmp/PROP_PICTURE_CACHE.htm) property of the picture object. There is no attempt to verify this filename is valid on the server and there will be no preview. The filename may contain environment variables which will be expanded at runtime when the form is opened. |
| Add FTP... | This allows you to FTP a file from a server down onto your workstation so that it can be inlined as a local file. It invokes an [FTP Open dialog](FormsDesignerFtpPics.htm). |
| Delete | This deletes the selected picture from the form. |
