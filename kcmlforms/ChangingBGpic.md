Changing the background picture used by a form

------------------------------------------------------------------------

To change the background picture used by a form the [Picture](tmp/PROP_GENERIC_PICTURE.htm) property needs to be set to an existing picture control name. For example:

Form1.picture = &.picture1

Once the form has a picture control name set it is then possible to change the form background picture by modifying the picture controls filename property, for example:

.picture1.filename\$ = "C:\Library\Sheep.bmp"

The picture alignment can be changed with the

*PictureAlignment* property, for example:

.Form1.PictureAlignment = &.Tile
