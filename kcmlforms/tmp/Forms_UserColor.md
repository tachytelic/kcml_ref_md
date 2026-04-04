UserColor method

<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> UserColor(Name\$, Red, Green, Blue, Description\$)

The **UserColor()** method allows the application to define a set of user preference colors for an application. These colors are named by the application but a mechanism is provided in the kclient forms preferences dialog for the user to set teh actual color according to his or her preferences. This allows the application to use colors other than the Windows system colors without hard-wiring colors into forms and giving users no control.

These colors should be allocated on an application wide basis to be consistent. The colors can then be defined at application startup, and then used within the various forms as appropriate. They will appear in the forms designer for the programmer to select.

To define a user color, it must have a name (this will appear in the forms designer), for example "Highlight", default RGB color values (e.g. 255, 0, 0 for bright red), and a description string that will appear in the KClient Forms Preferences page. This last string should be internationalized if appropriate.

The default RGB value is used initially, but may be modified by the user in the same manner as built in special colors such as EditReadOnlyColor. A list of user colors appear in the Forms Preferences page in kclient and if edited by the user they will be saved to the registry for persistance.

forms.UserColor("Highlight", 255, 0, 0, \<\<"Highlight color"\>\>)

##### See also:

[PersistFormSize](/tmp/Forms_PersistFormSize.htm), [SetToolBarSize](/tmp/Forms_SetToolBarSize.htm), [SpoofGraph](/tmp/Forms_SpoofGraph.htm), [TabEnterKey](/tmp/Forms_TabEnterKey.htm), [TabReturnKey](/tmp/Forms_TabReturnKey.htm)
