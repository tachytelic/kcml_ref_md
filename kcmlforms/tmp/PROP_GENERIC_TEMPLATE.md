Template (generic property)

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
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Control is a template**

A control with this property set to **TRUE** is hidden invisible to the user and is generally used as a template control for the [Duplicate()](PROP_GENERIC_DUPLICATE_2.htm) method. This property is a design time only property and can therefore not be changed under program control.

##### Example:


     IF (.tabbeditem.Template)
       ...
     END IF

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
