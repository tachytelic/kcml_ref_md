CanConvert (kcmledit control property)

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
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, Enable, Disable, Always)*

**Determines whether value can be converted to alternative currency**

The CanConvert property property is used to define a dbedit field as being a currency field. It requires the [Type\$](PROPSTR_TYPE.htm) property to be set to a Numeric type (e.g. N13.4). When displaying values, the Kclient's current locale currency settings are used (decimal and thousands separator character, and the number of decimal places to the right of the decimal).

A currency field can also be displayed in an alternative currency form (especially to support the Euro). See [Alternative currency support](/AlternativeCurrencysupport.htm) for more information. In versions of KCML prior to 6.00 this property has a Boolean type; in 6.00 it is an enumeration, although TRUE and FALSE will still work.

|  |  |
|----|----|
| Default (FALSE) | This is not a currency field |
| Enable (TRUE) | This is a currency field. It is displayed in the normal or alternative currency according to the current display mode |
| Disable | This is a currency field. It is always displayed in the normal currency |
| Always | This is a currency field. It is always displayed in the alternative currency |

.editControl1.CanConvert = TRUE

Note:

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
