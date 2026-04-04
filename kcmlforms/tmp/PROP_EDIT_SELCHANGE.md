SelChange (kcmledit control event)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when a new item is selected in the drop down portion of the control**

This event handler is called each time the current selection changes in a drop down listbox associated with the edit control. This is usually due to the user picking from the list but it can also be invoked when

- items are programmatically added to the list with .Add() and they happen to agree with the text currently in the edit control
- the currently selected item is programmatically removed from the list with Delete()
- the [text\$](PROPSTR_TITLE.htm) property is changed and a similar match occurs

For this, and other reasons to do with change of focus, the use of this event is strongly discouraged and you are advised to set the [ValidateSelChange](PROP_KCMLEDIT_VALIDATESELCHANGE.htm) property instead. This causes a [Validate()](PROP_KCMLEDIT_VALIDATE.htm) event to be triggered only when the user makes a selection either by entering text in the edit control or by selecting from the list and it can't be triggered by the action of the program.

##### Example:


     DEFEVENT Form1.editControl.SelChange()

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
