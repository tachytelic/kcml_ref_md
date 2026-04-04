KCML Form controls

------------------------------------------------------------------------

The following controls are the standard controls that are available with KCML forms.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Control</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Check box</td>
<td>A check box is used to allow the user to select an option as being either on or off.</td>
</tr>
<tr>
<td>Combo box</td>
<td>A combo box provides the user with a combination of a list box and an edit control. Selecting an item from the list updates the edit control area and text entered into the edit control are will update the list if appropriate.</td>
</tr>
<tr>
<td>Edit control</td>
<td>The KCML Edit control has all of the standard functionality of a regular Windows edit control along with some additional special functionality. The control can restrict the user to certain data ranges by setting the <a href="tmp/PROPSTR_TYPE.htm">Type$</a>property. This can be used to restrict the entry to single and multi-line strings of a fixed length, integer and floating point numeric values, date and time values etc. The control can also be instructed to act as a check box or a drop down list box.<br />
KCML Edit controls can also be linked to columns within a database table.<br />
Special properties also exist for European developers to allow the control to automatically convert the controls contents between the native and Euro currencies.</td>
</tr>
<tr>
<td>Gauge control</td>
<td>A special control allowing a simple progress bar to be placed onto the form.</td>
</tr>
<tr>
<td><p>Grid Control</p></td>
<td>The KCML grid control is a very flexible control allowing tables of information to be placed onto the form. Each grid cell can be programmed to have the same functionality as the regular KCML Edit control (See above).</td>
</tr>
<tr>
<td>List box</td>
<td>This control is used to display a list of items allowing the user to select one or more items from the list. Various properties are available to change the way in which the list is displayed, for example, the list can be automatically sorted as items are added.</td>
</tr>
<tr>
<td>Menus</td>
<td>A menu control can be created to appear at the top of the form. Popup menus can also be created to appear within a picture or grid control.</td>
</tr>
<tr>
<td>Picture Control</td>
<td>A special control allowing bitmap pictures to be placed onto a form. The pictures can be programmed to act as a static picture or as a button.</td>
</tr>
<tr>
<td>Push Button</td>
<td>A Button control is used as a simple push button allowing the user to click on the button face to perform a pre-defined task. The clicking of a button can be trapped with the <a href="tmp/PROP_BUTTON_CLICK.htm">Click()</a> event handler.</td>
</tr>
<tr>
<td>Radio Button</td>
<td>Radio buttons allow the user to select any one of a number of options.</td>
</tr>
<tr>
<td>Rich edit control (RTF Control)</td>
<td>The RTF control is a like an edit control with some basic word processing capabilities. The formatted text is returned to the program in RTF format. Some special methods and event handlers exist to make it possible to print the contents of the control to a Windows printer.</td>
</tr>
<tr>
<td>Static text control</td>
<td>These are simple labels used to place some text directly onto the form. They are often used to label controls such as edit controls and list boxes that do not have their own caption property.</td>
</tr>
<tr>
<td>Status Bar</td>
<td>A control allowing multiple panes of status information to be displayed on the form. As a control gets focus the text in the <a href="tmp/PROP_GENERIC_HELP.htm">Help$</a> property is automatically displayed in the status bar.</td>
</tr>
<tr>
<td>Tab control</td>
<td>The tab control allows multiple pages of controls to appear in one area of a form. A page is displayed by clicking on the tab section of the required page.</td>
</tr>
<tr>
<td>Tree control</td>
<td>The tree control allows the programmer to display hierarchical lists similar to the Windows file explorer.</td>
</tr>
</tbody>
</table>
