Resize (form control event)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
<td>Advanced</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when the user resizes the form**

The **Resize** event is triggered when a resizable form is resized by the user. This will happen when the user resizes the form by dragging the edges, maximizes the form, or when the form is initially sized on startup. In the case of drag resizing, only one event is sent when the drag is finished (by releasing the mouse button). On startup a Resize event is guaranteed to be triggered. The order of events will be that the [Show()](mk:@MSITStore:kcmlforms.chm::/PROP_FORM_SHOW.htm) event will occur before the Resize event, but that the form will not be visible until the Resize event has completed, giving the programmer an opportunity to res-arrange the controls first.

A form can only be resized if the [Resize](PROP_DLG_RESIZEDLG.htm) design time property is TRUE.

The appropriate [Left](mk:@MSITStore:kcmlforms.chm::/PROPNUM_X.htm), [Top](mk:@MSITStore:kcmlforms.chm::/PROPNUM_Y.htm), [Width](mk:@MSITStore:kcmlforms.chm::/PROPNUM_W.htm)and [Height](mk:@MSITStore:kcmlforms.chm::/PROPNUM_H.htm) properties for the form and individual controls are up to date when the event triggers.

Control sizes and positions only change automatically if [anchoring](/FormsDesignerAnchoringthecontrolsonaform.htm) is used. If not, controls can be moved manually by changing these properties within the Resize event.

See this [example program](/ExampleResize.htm) for more about how a Resize event handler can be used to move buttons when a form is resixed at runtime.

##### Example:


     DEFEVENT Form1.Form.Resize()

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
