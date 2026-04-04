Group event handlers

It is sometimes useful to group controls and have an event handler that is called if a particular event occurs for any of the controls in the group. For example, you may have a [*Click()* event handler for a group of push buttons so that if any of the buttons in the group are clicked the event handler is called (Refer to](tmp/PROP_BUTTON_CLICK.htm) [Grouping controls](FormsDesignerGroupingControls.htm) for information on adding controls to a group.) Once the event handler is called the methods and properties for the control can be referenced directly by leaving out the form and control name from the variable. For example, *Form1.btnControl1.Enabled* is replaced with *..Enabled*. Assume that a group called *grpControl1* has been created with four push buttons in the group labelled *btnControl1, button2, button3* and *button4.* To change the text on the face of a button in the group when it is clicked, the following event handler could be used:

-DEFEVENT Form1.grpControl1.Click() ..Text\$ = "New Text" END EVENT

To determine exacty which control triggered the event you should test the contents of the controls [*Text\$* or](tmp/PROPSTR_TITLE.htm) [*Tag\$* properties. The tag\$ property is useful for controls that do not have any label text, for example list boxes and combo boxes. The following example tests for the](tmp/PROPSTR_TAG.htm) [*GetFocus()* event for the controls in the group *Main1*. Note that the](tmp/PROP_EDIT_SETFOCUS.htm)

*GetFocus()* event can be triggered from several different control types including Edit controls, List boxes and Combo boxes.

-DEFEVENT Form1.Main1.GetFocus() SELECT CASE ..Tag\$ CASE "Display" ... CASE "Update" ... CASE ELSE ... END SELECT END EVENT
