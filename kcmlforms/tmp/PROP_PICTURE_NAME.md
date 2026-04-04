Filename\$ (picture control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Specifies a local client picture filename**

Specifies the full local filename of the [picture object](/PicObjects.htm) used by a [KCML picture-enabled control](/PicEnabledControls.htm). Using local filenames is not recommended as the filenames may differ between clients and client operating systems. To avoid this the Forms Designer [Open Picture dialog](/FormsDesignerPicBrowser.htm) will automatically inline small pictures using the [*.immediate\$*](/tmp/prop_picture_immediate.htm) property. The following example will only work if c:\Windows is the windows directory which is unlikely with an NT client. .Picture1.Filename\$ = "C:\Windows\Bubbles.BMP" .picButton.Picture = &.Picture1

Instead programs should store their pictures centrally on the server specifying them with the [.Cache\$](PROP_PICTURE_CACHE.htm) property. There will be no loss of performance here as the client will automatically download and locally cache the picture. If the picture is changed on the server it will be refreshed automatically.

##### See also:

Other [picture](picture.htm) properties, methods and events and [generic](generic.htm) properties and methods.
