### <span id="Properties">Object properties</span>

Objects can have properties (often called attributes in the Corba world) which can be inspected or altered (though some properties may be read only). E.g.

count = Table.RowCount

String valued properties have a trailing \$ as in

m\$ = Obj.HelpText\$

Generally a property can be used anywhere where an equivalent variable was allowed.

Properties are actually implemented as a special type of method but this is handled internally by KCML. The properties applicable to an object can be seen using the [Object Browser](combrowse.htm) in the workbench.
