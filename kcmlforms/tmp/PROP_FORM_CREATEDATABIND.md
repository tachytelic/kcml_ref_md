CreateDataBind (form control method)

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
6.20+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> CreateDataBind(int, int) Method

**Create control in the Create event**

The CreateDataBind() method allows databinding pseudo-controls to be created dynamically during the [Create()](/tmp/PROP_FORM_CREATE.htm) event. The result is an object reference to the new control.

CreateDataBind() takes two parameters, the SYM of the data buffer to be used and the SYM of the find function for the record involved. If no record is involved, then 0 may be passed for the second parameter. For more information on the find function and records, refer to [DEF RECORD](mk:@MSITStore:kcmlrefman.chm::DEFRECORD.htm).

In this example a data bound edit control is added to a form. This form is presumed to already have a group callyed .mygroup, defined by the forms designer, which can take events from the control.


    DEF RECORD MyRecord
        FLD MyRecord_Fld1
        FLD MyRecord_Fld2$ = "CHAR(35)"
    END RECORD    

    DIM MyBuf$_MyRecord
    '_Init_MyRecord(BYREF MyBuf$)


    DEFFORM Form1
    ...
    DEFEVENT Form1.Create()
        LOCAL DIM OBJECT db
        LOCAL DIM OBJECT e

        REM Dynamically create a data bind pseudo-control
        OBJECT db = Form1.form.CreateDataBind(SYM(MyBuf$), SYM('_find_MyRecord))
        :         
        REM Create a dbedit and set the data-binding and DataField$
        OBJECT e = Form1.form.CreateControl(_CONTROL_DBEDIT, _STYLE_DBEDIT, OBJECT .mygroup)
        e.Left = 10
        e.Top = 10
        e.Width = 50
        e.Height = 13
        OBJECT e.DataBind = db
        e.DataField$ = "MyRecord_Fld2"
    END EVENT
    FORM END

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
