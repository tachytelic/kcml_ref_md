CurrencyChange (form control event)

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

**Called when user has changed selected currency on form**

This event will be triggered in a form if the user clicks the Alternative Currency button on the forms title bar or presses CTRL-E in a KCML edit control. The Client will display this button if a [\$CONVERT](mk:@MSITStore:kcmlrefman.chm::/$CONVERT.htm) exchange rate was set in the program and the form contains currency fields (that is KCML edit controls with a numeric [Type\$](PROPSTR_TYPE.htm) and with the [.CanConvert](PROP_KCMLEDIT_CANCONVERT.htm) property set to TRUE.) The button appear on the right of the titlebar and displays the three letter currency code for the currency in effect on the form. These codes and the exchange rate were defined by the value of the \$CONVERT string. Clicking the button toggles between the two currencies.

Whether or not this event is handled, the client will redisplay all the currency fields in the appropriate currency for the button state. Handling the event allows the programmer even more control over the appearance of the form allowing currency dependent static text to be changed perhaps.

See [Alternative Currency Support in KCML](/AlternativeCurrencysupport.htm) for more information.

##### Example:


     DEFEVENT Form1.Form.CurrencyChange()

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
