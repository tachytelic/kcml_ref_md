# <span id="printerpreferences"></span> Printer preferences

Kclient implements a Local Printer facility that allows the controlling KCML process to route raw ascii text for printing to the client. The client can then pass this through to an appropriate device set by the Print Output Device list box.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

## <img src="bitmaps/printpref.gif" data-border="0" alt="Printer preferences dialog" />

</div>

| **Device** | **Purpose** |
|----|----|
| \[None\] | Print output is discarded |
| Printer | Text is routed to a Windows printer through the normal Windows spooler. If this device is selected then the radio buttons to select the printer are enabled. You can select either the current Windows default or pick a specific printer known to Windows. You can only print to printers whose drivers can resolve generic text. This may rule out some fax printers which require rasterized input from the GDI. Screen dumps can be color or monochrome bitmaps to reproduce all the attributes. |
| File | Text is sent unaltered to the named file. A text box is enabled allowing the filename to be specified. Alternatively a browse button can be used to select an existing file. Screen dumps are text only. |
| Clipboard | Text is copied to the Windows clipboard. Screen dumps are text only. |

\

Kclient supports a screen dump mode in its Text Windows using the PrintScreen button.
