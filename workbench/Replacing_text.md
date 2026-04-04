## Replacing text and symbols

The replace facility has all the same options as the [search](Searching_for_text.htm) facility. In addition a replacement string is supplied and each instance of the search string will be replaced by an instance of the replacement string.

The replace dialog is only available in edit mode in the foreground program. It can be invoked from the keyboard with SHIFT F3. A count of the number of substitutions made will appear on the status bar.

The search text can contain regular expressions and may optionally be case insensitive. It is always case insensitive if the search is restricted to symbols only. Currently [wildcard](regexp.htm) characters are supported in the search string only and not in the replacement string. Also searches on symbols don't use regular expressions but use only \* and ? wildcards. Therefore performing a symbol search and replace from "\*gb\*" to "\*xy\*" would replace all variables containing the characters "gb" with "\*xy\*".

The search text is saved and previous search strings can be retrieved from the combo box by pressing down arrow or clicking on the combo box button to the right of the search box. These strings are common between the [Search](Searching_for_text.htm) and The Replace dialogs.

<div id="ClickDiv">

<u>Click here to view an example replace dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

*Replace dialog box:*

<img src="bitmaps/REPLDLG.png" data-align="BASELINE" data-border="0" usemap="#ReplaceDlg" alt="Replace dialog box" />

</div>

The Options check boxes and the Search type radio buttons are the same as in the [Find dialog](Searching_for_text.htm).
