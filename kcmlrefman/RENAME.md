RENAME

------------------------------------------------------------------------

<div class="Generalform">

General Forms:

1.  RENAME label1 TO label2
2.  RENAME variable1 TO variable2
3.  RENAME OBJECT object1 TO object2

\
\
Where:\

|     |                      |                                 |
|-----|----------------------|---------------------------------|
|     | label1, label2       | = valid subroutine labels       |
|     | variable1, variable2 | = valid variable names          |
|     | object1, object2     | = valid DEFFORM or OBJECT names |

</div>

------------------------------------------------------------------------

The RENAME immediate mode command is used to rename all instances of label1 or variable1 to label2 or variable2 in the program currently held in memory. The RENAME OBJECT command can do the same for DEFFORN names or handle objects (defined by DIM OBJECT).

For example, to rename all of the '66 subroutines to 'open_file, and each occurrence of the a1\$ variable to lock1\$, the following two commands would be entered:

RENAME'66 TO 'open_file\
RENAME a1\$ TO lock1\$

To rename a form declared by DEFFORM you might use

RENAME OBJECT Form1 TO OrderForm\

This is an immediate mode command which cannot be used in a program. If used in a program halted in the workbench, the program will be marked as unresolved and execution cannot be resumed with CONTINUE. Furthermore the values associated with both the old and the new variables will be reset to their defaults even if the old variable was declared as common in a COM declaration.

To rename the same variables or labels in a number of files, create an ASCII file containing the RENAMEs with a text editor, [LOAD](LOAD.htm) the first program into memory and use [LOAD ASCII](LOAD_ASCII.htm) to load and execute the ASCII file.

An error will result if an attempt is made to change the variable type, for example, if an attempt is made to rename a global variable to a normal variable.

When renaming objects with RENAME OBJECT the new name must not be already used in the program.

Note that variables and subroutine labels can also be renamed by the KCML workbench Search and Replace function.

Syntax examples:

RENAME q\$ TO temp\$\
RENAME k\$() TO variable\$()\
RENAME '152 TO 'get_next_record\
RENAME OBJECT s TO SOAPsession

See also:

[LOAD ASCII](LOAD_ASCII.htm)
