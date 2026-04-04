SetFocus (tabbeditem control method)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> SetFocus(int) Method

**Moves the tab into focus**

This method can be applied to a page on a tab control and will have the effect of selecting that page and exposing its controls. If a value of TRUE is passed input focus is set to the the tab's ear otherwise focus is left unchanged. The Forms Designer can set a separate [tabstop order](/FormsDesignerSettingTheTabOrder.htm) for the controls on each tab page.

##### Example:


     .tabbeditem.SetFocus(i)

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
