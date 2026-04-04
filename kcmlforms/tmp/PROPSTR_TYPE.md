Type\$ (kcmledit control property)

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

**Specifies the format that the user will use to enter information**

This property may used by the Edit control and grid control cells to specify the style of the edit control or grid cell that will be presented on the form.

Starting with KCML 6.10 the use of this property is deprecated as the style can be deduced from the format information available in the [DataField](PROP_DATAFIELD.htm) property. KCML 6.10 allows a much richer selection of data aware [field types](mk:@MSITStore:kcmlrefman.chm::/tmp/xp.htm) and when these are used, the **Type\$** property is redundant.

Available types are detailed below. The second columns shows the new preferred field type for the DataField property.

|  |  |  |  |
|----|----|----|----|
| T | TIME | Time Format | Instructs the control to provide a time entry Edit control where data is entered in the format of HH:MM. |
| D | DATE | Date Format | Instructs the control to provide a date entry edit control. The format in which the date is displayed is detected from the Windows system settings. In the US this would be MM/DD/YYYY while in most other places it would be DD/MM/YYYY. |
| B | BOOL | Boolean | Instructs the control to act as a check box. |
| N*sn1.n2* | NUM() or UNUM() | Numeric | Instructs the control to permit only numbers to be entered. The field can accept both signed and unsigned values by specifying an optional plus or a minus sign immediately after the **N**. The first parameter ***n1*** restricts the length of the number while the second, optional, parameter ***.n2*** specifies the number of decimal places allowed. For example, specifying "N6.2" would allow a maximum value of 9999.99 to be entered. See the [.CanConvert](PROP_KCMLEDIT_CANCONVERT.htm) property for more information on how currency values should be specified. |
| S*n* | CHAR() or HEX() | String | Instructs the control to allow a string of up to *n* characters. |
| S*n1*x*n2* | TEXT() | Multi-line string | Instructs the control to act as a multiple line edit control allowing *n2* lines of *n1* characters. For example, an address field may require 5 lines of 35 characters therefore a type of "S35x5" would be specified. |
| I*sn* | INT() or UINT() | Integer value | Instructs the control to allow a signed or unsigned integer value to be entered. If required the optional plus or minus sign must be specified immediately after the **I**. If no sign specifier the number is assumed to be unsigned. The ***n*** parameter specified the number of storage bytes available. Allowed values are 1, 2 and 4. For example, specifying a type of "I1" would restrict the entry to a value ranging from 0 to 255 and a type of "I-1" would restrict the entry to a value ranging from -127 to +127. |

If a **Type\$** property is specified it will override the default type deduced from the DataField property.

##### Example:


     a$ = .editControl.Type$

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
