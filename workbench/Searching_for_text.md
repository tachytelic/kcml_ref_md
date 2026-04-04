## Searching For Text

A search facility is available to allow the program text, regardless of the display mode, to be searched for a specific string or symbol. The search dialog box can be brought up with the search key (F3 or CTRL-F), alternatively select the Find option from within the [Search menu](Search_Menu.htm). When a match is made the cursor is placed on the line containing the match. The Find Next (CTRL-N) and Find Previous (CTRL-P) keys can then be used to move between matched lines.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

*Find dialog box:*

<img src="bitmaps/FINDDLG.png" data-align="BASELINE" data-border="0" usemap="#FINDDLG" alt="Search dialog box" />

------------------------------------------------------------------------

</div>

When the dialog box is displayed the search text defaults to the last actioned object, i.e. the last object to be placed into the command/status line. The search text can contain regular expressions and may optionally be case insensitive. It is always case insensitive if the search is restricted to symbols only. The search text field has a drop down containing previous search strings. The following options are available from this dialog box.

A direction for the search must also be set.

| Search Direction | Action                               |
|------------------|--------------------------------------|
| Forwards         | The Search will proceeded top-down.  |
| Backwards        | The Search will proceeded bottom-up. |

One or more of the following options can be set.

| Search Option | Action |
|----|----|
| <span id="caseless">Caseless</span> | This option toggles the search type. If set a caseless search is performed and if unset only text exactly matching the search text will be found. Searching on symbols is always caseless. |
| <span id="wildcards">Regular Expression</span> | Allows pattern matching characters to be used as part of the search string. These may be true [regular expressions](regexp.htm). |
| <span id="modules"></span>All Modules | If set the search will proceed through all loaded modules. The direction it moves through the modules depends on your search direction. |
| <span id="selected">Selected Text</span> | If set the search will only be carried out on the currently highlighted text. |

Only one of the following Search types may be set.

| Search Type | Action |
|----|----|
| All text | Searches for matches in all text. The search is without any consideration for the meaning of the symbols in a program. All characters are searched with the searching being done in units of lines. |
| Symbols only | Searches for matches in symbols only. Different symbol types can be searched for by preceding the text with either a ( ' ) or a period to search for only subroutine labels or field variables respectively. Unix [regular expressions](regexp.htm) are not permitted but \* and ? are allowed as wild cards. Searching is done on the symbol table and will only match variable names, subroutine names, field names or labels. |
| Line numbers only | Searches for matches in line number references only. An alternative to LIST \#. This restricts the search to line numbers either at the start of a line or referenced in GOTO, GOSUB, LOAD etc statements. It is meaningful only to use numeric search strings and wild cards do not apply. |
| Literal strings | Matches simple quoted strings "....". If the checkbox for all occurrences is checked then the next string will be found irrespective of the contents. This can be used to systematically locate all the string literals in a program with a view to changing some to chevron international strings. If the checkbox is not checked then the literal string must match the text in the search box (which should be quoted). This mode of search will not match quoted text in comments. |
| Chevrons | Matches multilingual strings enclosed in \<\<\>\> chevrons. If the checkbox for all occurrences is checked then the next chevron string will be found irrespective of the contents otherwise the search string must be matched. |
