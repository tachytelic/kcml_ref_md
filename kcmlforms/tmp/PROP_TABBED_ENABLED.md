Enabled (tabbeditem control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Enables/disables tab page items**

This property is used to disable the specified tab page within a tab control. Tabs are initially enabled unless disabled by the tab editor in the Forms Designer. A disabled tab cannot become the visible page and is shown with its tab ear text greyed out. If the target tab page is the currently visible page then it will be moved to the back and replaced by the next tab in order. For example: .TabControl1.tab1.Enabled = FALSE

To grey out all the tabs together, thus stopping the user navigating the control, use the Enabled property of the control itself e.g. .TabControl1.Enabled = FALSE

Note that this will not disable the controls on the visible page.

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
