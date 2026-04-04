### <span id="FormObjects">Objects in forms</span>

In KCML 5.02 and earlier versions of KCML 5 there was support for a limited subset of OCX controls conforming to the original pre-OCX96 specification. The full specification of the control was extracted from its type library by the Forms Editor and was saved inside the form definition. The encoding scheme did not handle controls with a hierarchy of component objects nor did it handle OCX96 spec property methods.

KCML 6.00 implements the full OCX96 specification by treating OCXs like any other [COM object](ObjCOM.htm) except that the forms Open() method will automatically instantiate it within the form container. It will not be necessary for the form to contain a specification of the properties and methods available as this can be discovered by KCML at runtime. Old forms will be accepted by the new KCML 6.00 forms designer though this information will be ignored if the OCX controls are accessed as objects. New forms created with the KCML 6.00 forms designer will not contain these property and method specifications which for some controls will be a significant space saving.

OBJECT myOCX=form1.controlOCX myOCX.redraw()

See the page on [OCX controls](mk:@MSITStore:kcmlforms.chm::/IntroOCX.htm) for more on how to use OCX controls on forms.

Object notation can also be used inside event handlers to simplify access to controls, grid cells, tabs, listbox items and tree nodes. For example a gridcell can be referenced as an object:

OBJECT thiscell = .grdDB.cell(row, col) thiscell.text\$="Hello"

as can the entire grid control e.g.

OBJECT grid = Form1.gridControl1 'InitGrid(OBJECT grid)

Special enumerator properies allow easy access to the elements of list boxes ([First](mk:@MSITStore:kcmlforms.chm:://tmp/PROP_LISTBOX_GETFIRST.htm), [Next](mk:@MSITStore:kcmlforms.chm:://tmp/PROP_LISTBOX_GETNEXT.htm), [SelectedFirst](mk:@MSITStore:kcmlforms.chm:://tmp/PROP_LISTBOX_GETSELECTEDFIRST.htm), [SelectedNext](mk:@MSITStore:kcmlforms.chm:://tmp/PROP_LISTBOX_GETSELECTEDNEXT.htm), [Index](mk:@MSITStore:kcmlforms.chm:://tmp/PROP_GENERIC_ODATAPTR.htm)), tabs ([TabFirst](mk:@MSITStore:kcmlrefman.chm:://tmp/PROP_TABBED_GETFIRST.htm), [TabNext](mk:@MSITStore:kcmlrefman.chm:://tmp/PROP_TABBED_GETNEXT.htm)) and trees ([Parent](mk:@MSITStore:kcmlrefman.chm:://tmp/PROP_TREEITEM_GETOPARENT.htm), [Child](mk:@MSITStore:kcmlrefman.chm:://tmp/PROP_TREEITEM_GETOCHILD.htm), [Next](mk:@MSITStore:kcmlrefman.chm:://tmp/PROP_TREEITEM_GETONEXT.htm)).

There is special support in FOR OBJECT that allows all the controls on a form to be enumerated with objects as in

FOR OBJECT ctrl IN Form1 ... NEXT OBJECT ctrl

See this [example](mk:@MSITStore:kcmlforms.chm::/ExampleFormObjects.htm) for more about using OBJECT notation on forms.
