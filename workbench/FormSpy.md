## Spying on forms

This feature is implemented in the client and allows the programmer to see the properties of a control on a form in the debugger. For clarity only basic properties and properties that have been explictly set to values different from the default will be shown. This tool is particularly useful for inspecting grid and grid cell properties.

When a forms program is stopped in the debugger the form is still visible but is greyed out to make it clear that control has passed to the debugger. However if you invoke the forms windows system menu, by clicking the icon at the left of its toolbar, a Spy menu option will appear e.g.

<img src="bitmaps/spymenu.png" data-border="0" alt="Sytem menu showing spy option" />

If that option is selected then the mouse cursor will change to a gunsight and as it passes over the various controls on the form they will be edged in red as they are selected as the control to be spied upon. The next screen shot shows the gunsight cursor over the Quit button on a form (the cal.src demo from the KCML programming samples).

<img src="bitmaps/SpyClip.png" data-border="0" alt="Spy cursor over the Quit button" />

Clicking on the highlighted control will bring up a window listing basic properties such as position and properties of the control that differ from the default, i.e. they have been changed by the application.

<img src="bitmaps/SpyResults.png" data-border="0" alt="Results of spying on the Quit button" />

You can also spy on a running program but only if the workbench is active because you have previously interrupted it or because it was started from the workbench.
