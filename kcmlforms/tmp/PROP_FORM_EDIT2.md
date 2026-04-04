EditForm (form control method)

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
<td>Advanced</td>
<td>KCML<br />
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> EditForm(int, int) Method

**Edit form with tables**

|  |  |
|----|----|
| int | The [SYM()](mk:@MSITStore:kcmlrefman.chm::/SYM(.htm) of a string that will define the controls to be added to the form |
| int | The SYM() of a two dimensional string array holding a table and column list |

This method extends the [Edit(int)](PROP_FORM_EDIT.htm) method to allow a form with data aware controls to be edited. The second SYM() specifies an (n,2) two dimensional array of pairs of table and column names available to populate the Tables window of the forms designer.

##### Example:


     .Form.EditForm(i, j)

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
