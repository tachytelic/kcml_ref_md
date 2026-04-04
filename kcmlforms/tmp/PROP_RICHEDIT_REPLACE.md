Replace (richedit control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Replace(string, string) Method

**Method to repalce all occurences of a field with the replacement text**

***Str1***      The search string\
***Str2***      The replacement string

This method is used to replace the contents of the first string with the second string within an RTF control. The method actually searches for the search string surrounded by two pairs of braces, for example "{{STRING}}".

This method is designed to allow functions such as a mail merge to be formed. Where a standard letter template is loaded into the control containing search text for each of the items to be merged, i.e. {{ADDRESSLINE1}}, {{TOWN}}, {{CITY}}, {{POSTCODE}} etc. The replace methods for this strings would then be something of the form: .rtfControl1.Replace("ADDRESSLINE1", dbAddressLine1\$) .rtfControl1.Replace("TOWN", dbTown\$) .rtfControl1.Replace("CITY", dbCity\$) .rtfControl1.Replace("POSTCODE", dbPostcode\$)

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
