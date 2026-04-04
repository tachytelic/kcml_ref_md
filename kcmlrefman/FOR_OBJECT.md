FOR OBJECT ... IN ... NEXT OBJECT

------------------------------------------------------------------------

General Form:

FOR OBJECT *object_ref* IN *collection_object*\
...\
NEXT OBJECT *object_ref*

------------------------------------------------------------------------

The FOR OBJECT ... IN statement is used in conjunction with the NEXT OBJECT statement to iterate over all the elements of a **collection**. A collection is a special class of object that provides First() and Next() methods returning object references. Each FOR OBJECT ... IN statement must be paired with a NEXT OBJECT statement. Both statements must use the same index object reference.

When the FOR OBJECT ... IN statement is first executed the index object reference variable is set to point to the first object in the collection. If the collection is now empty then execution resumes at the statment after the NEXT OBJECT. Otherwise program execution continues within the loop body until the corresponding NEXT OBJECT statement is executed whereupon execution will resume at the top of the loop with the next object, if any. If the collection was empty then the loop body may never be executed. This differs from the classic [FOR ... NEXT](FOR.htm) loop where the body is always executed at least once.

Example:

FOR OBJECT col IN Rowset.Fields()\
    PRINT col.name\$,col.precision\
NEXT OBJECT col

In this example the collection object is returned by a method call into its parent object. This method is only invoked once when the FOR OBJECT is first executed and it is not reevaluated on each later iteration of the loop.

Jumping into a FOR OBJECT ... IN loop will cause an error at the first use of the index object.

Jumping out of a FOR OBJECT ... IN loop is allowed but should be avoided as it is considered bad programming practice and terminating loops incorrectly can cause stack overflow errors. If a program has to jump out of a loop then a [BREAK](BREAK.htm) statement should be used to abandon the loop entirely or the [CONTINUE](CONTINUE.htm) statement may be used skip the remaining body of the loop. E.g.

FOR OBJECT c IN countries\
    IF c.source == 1 THEN BREAK\
    .static1.Text\$ = c.name\$\
    IF c.language \<\> "En" THEN CONTINUE\
    EnSpeakers += c.population\
NEXT OBJECT c

FOR OBJECT loops are automatically indented by the KCML editor provided that, when the program is resolved, each FOR OBJECT ... IN statement has exactly one corresponding NEXT OBJECT

An example of a collection used within KCML is the collection of controls on a form which can be enumerated thus

DIM f=2\
DEFEVENT Form1.help.Click()\
FOR OBJECT i IN Form1\
     i.Height = i.Height \* f\
NEXT OBJECT i\
f = 1 / f\
END EVENT

in this example clicking this help button will toggle the size of the form and all its controls to twice normal and back.

See also:

[FOR](FOR.htm), [BREAK](BREAK.htm), [CONTINUE](CONTINUE.htm), [RETURN CLEAR](RETURN_CLEAR.htm)
