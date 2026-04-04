Picture objects

Picture objects encapsulate the pictures used in [picture enabled controls](PicEnabledControls.htm) such as toolbars and picture buttons. Such controls have a [picture](tmp/PROP_GENERIC_PICTURE.htm) property which can be set to the name of a picture object e.g.

.picObj1.cache\$="clouds.bmp" .picButton1.picture = &.picObj1

User defined picture objects can reference either a local picture on the client (not recommended) using the objects [*.filename\$*](tmp/PROP_PICTURE_NAME.htm) property or they can reference a server filename using the [*.cache\$*](tmp/PROP_PICTURE_CACHE.htm) property. Small pictures can also be inlined in the form using the [*.immediate\$*](tmp/PROP_PICTURE_IMMEDIATE.htm) property. This will be done automatically by the Forms Designer for local pictures less than 2kb in size and can be optionally done for pictures larger than that up to a maximum of 8kb.

Picture objects must be created and named in the forms designer but their properties can be changed at runtime by server logic. There are a number of [stock picture objects](Acompletelistofstockpics.htm) built into the client which can also be selected.

.picButton1.picture = &.Stop

The usual way to create an object is to highlight the control in the Forms Designer's property browser and to click on the picture property. This will bring up a [Picture Open dialog](FormsDesignerPicBrowser.htm) allowing the selection of a picture already defined in the form, a stock picture or allow the definition of a new picture.

You can also add a picture object to a form directly with the [Add Picture](FormsDesignerAddPictures.htm) option from the Tools menu in the Forms Designer. This has the additional capability of being able to FTP a picture from your workstation to the server. Picture objects added this way must be referenced in the [*.Picture*](tmp/PROP_GENERIC_PICTURE.htm) property of some control or they will be stripped from the form when it is saved back into the program in the workbench.
