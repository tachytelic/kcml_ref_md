## Objects and actions

An **object** is a piece of text such as a variable, a function, a condition or a subroutine label. The object may copied to the command/status line and evaluated or actioned with the function being performed depending on the object type.

Objects are selected in one of three ways: by moving the cursor to the object and pressing F5, by left double-clicking with the mouse on the object in the program or by moving the cursor and then using the menu option *Select Object*. Using a simple algorithm, the variable, function, condition, subroutine label or number under the cursor or mouse pointer is selected, i.e. displayed in reverse video, and copied to the command/status line at the bottom of the screen.

Once in the status line an object can be actioned by first moving the cursor to the status line with F2, then pressing RETURN. The action performed depends on the object:

| Object                 | Action                                           |
|------------------------|--------------------------------------------------|
| Integer                | List code from that line-number                  |
| Integer,integer        | Move cursor to specific line and statement       |
| Variable               | Performs a LIST DIM output for the variable      |
| Function               | Evaluates the function and displays the result   |
| Condition              | Evaluates the condition as TRUE or FALSE.        |
| Subroutine Label       | Performs a LIST FROM 'label                      |
| Expression in brackets | Evaluates the expression and displays the result |

Issuing a right double-click with the mouse on an object will both select and action the object.

Objects copied to the command/status line are stored in a buffer which contains the last 16 analyzed objects. Once in the command/status line the North and South cursor movement keys can be used to search through this buffer.
