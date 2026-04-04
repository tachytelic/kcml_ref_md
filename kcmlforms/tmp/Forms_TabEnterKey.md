TabEnterKey method

<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> TabEnterKey(Enable)

The **TabEnterKey(Enable)** method allows the user to remap the num-pad Enter key to a Tab key in dbedit and grid controls. The default behaviour is to work as a Tab key. An Enter key will be sent for a multiline edit control even if this behaviour is enabled.

This method only has an effect if called before a form is created. REM Disable use of num-pad enter key as TAB forms.TabEnterKey(FALSE)

##### See also:

[PersistFormSize](/tmp/Forms_PersistFormSize.htm), [SetToolBarSize](/tmp/Forms_SetToolBarSize.htm), [SpoofGraph](/tmp/Forms_SpoofGraph.htm), [TabReturnKey](/tmp/Forms_TabReturnKey.htm), [UserColor](/tmp/Forms_UserColor.htm)
