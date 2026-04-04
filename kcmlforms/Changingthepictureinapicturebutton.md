Changing the picture in a picture enabled control

To change the picture used by the KCML picture enabled control (such as a button, a form background, a grid cell or a tree node) you can either assign the [Picture](tmp/PROP_GENERIC_PICTURE.htm) property to an alternative picture object or you can change the existing picture objects local or server filename by modifying the [FileName\$](tmp/PROP_PICTURE_NAME.htm) or [Cache\$](tmp/PROP_PICTURE_CACHE.htm) property. For example, the following would allocate a different picture object to the picture button:

.picControl1.picture = &picture2

Note that changing properties for a picture object will effect all controls that use the picture object. For example if both a form and several picture buttons shared the *Picture1* object the following would change the picture used by the form and the buttons:

.picture1.cache\$ = "Library/House.jpg"

As a rule it is better to store pictures on the server and use caching to deliver a copy to the client as needed. Thus you should specify the filename with the [Cache\$](tmp/PROP_PICTURE_CACHE.htm) picture control property, for example:

.picture1.Cache\$ = "/user1/Pictures/House.BMP" .picControl1.picture = &picture1
