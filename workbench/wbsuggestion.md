## Suggestion

The suggestion command allows for the quick completion of names for convenience or where the programmer is unsure of the exact name. The suggestion comand is invoked with ALT-DOWN ARROW and produces a menu of suitable selections. Use the mouse to click on the chosen item or the cursor keys to navigate (unlike normal menus the left and right arrow keys can be used as well) and press return to choose an item. Escape or clicking outside the menu dismisses the menu with no change.

Suggestions can be used with variables, form entities and functions. In the case of form entities, the context (usually an event handler) can help in building the suggestion. For functions any selected global partition is also searched for suitable suggestions.

There is a maximum size for the suggestion list so it may be necessary to refine the code being suggested on.

How suggestions work depends to some extent on the context. Here are some example of suggestions being used in typical cases:

<span id="autocomplete"></span>

### Empty Line

When used on an empty line the workbench will use preceding program lines to suggest likely keywords. Thus scanning up the program, if there is an incomplete IF statement, the suggestion list will contain ELSE, ELSE IF and END IF. This works with IF, WHILE, FOR, REPEAT

For example, entering

FOR i = 1 TO 10 <span class="key">\<CR\> \<ALT-DOWN ARROW\></span>

will result in the suggestion of NEXT i. Selecting this suggestion will enter NEXT i and then move to a new blank edit line.

### Variables

Assume we have a variable called numusers or num_users or NumberUsers (we are not quite sure). Entering

numu <span class="key">\<ALT-DOWN ARROW\></span>

will produce a list taken from the current programs symbol table including num_users which we click to select and this replaces the text with num_users.

### Functions

Suppose the user enters

'gb\_<span class="key">\<ALT-DOWN ARROW\></span>

then the suggestion box will list all functions in the program starting 'gb\_. There may be a few but it will be easy to spot 'gb_open (say, which is defined in the global) in the list and select it. The code will now appear as

'gb_open(

### Forms

Suppose we are in an event handler called MyForm.MyButton.Click(). Entering

. <span class="key">\<ALT-DOWN ARROW\></span>

will produce a suggestion list containing all the controls on MyForm. Entering

.myb <span class="key">\<ALT-DOWN ARROW\></span>

will produce a suggestion list of controls starting .myb, including .MyButton. Selecting this one will replace the text with .MyButton. Entering

.MyButton <span class="key">\<ALT-DOWN ARROW\></span>

will not suggest controls as the control is already a control name on the form. Instead possible properties will appear in the suggestion list, and we could select .Text\$ from the list. This would change the text in the editor to .MyButton.text\$. Entering

..<span class="key">\<ALT-DOWN ARROW\></span>

will also produce a list of properties for the .MyButton control (as mentioned earlier we are supposing we are in the MyForm.MyButton.Click() event handler).
