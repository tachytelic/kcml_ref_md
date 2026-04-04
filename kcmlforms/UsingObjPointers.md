Pointers to controls

There are a number of cases where it is useful to be able to reference a control by its symbol or pointer value instead of referencing it directly. This feature can be used to write generic subroutines that manipulate a control by its pointer value, i.e without knowing the actual control name. The pointer value for a control can be returned in two ways. Each control has a

*Sym* property which can be used to return the pointer value for the control. The value can be assigned to a variable and then later be used to reference the control. The control is referenced by replacing the controls name with an asterisk followed by the numeric variable containing the pointer value, for example to assign the pointer value of the control *btnControl1* to a variable the following would be used:

Pointer = .btnControl1.sym

and to reference the control using the pointer the following would be used:

.\*Pointer.Text\$ = "Some Text"

This feature is quite useful if you need to write a subroutine that needs to operate on controls without knowing their name. In the following example, a pointer to either a List box or a Combo box can be passed into the subroutine *'Fill()* which could be used to read in information from a data file and fill the control:

'Fill(.listControl1.sym) ... DEFSUB 'Fill(Pointer) LOCAL DIM Status Status = .\*Pointer.Add('GetNextRecord\$()) RETURN Status

Pointer values can also be used to assign property sets to controls, for example color and font sets. In this case the pointer value of the property set is referenced by placing an ampersand before the control name, for example to assign the color set *Color1* to the background color of a list box the following would be used:

.listControl1.backcolor = &.color1

The SYMNAME( function can be used to determine a control name from a pointer value, for example:

Name\$ = SYMNAME(Pointer) Control\$ = SYMNAME(..Sym)
