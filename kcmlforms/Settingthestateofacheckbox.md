Setting the state of a check box

------------------------------------------------------------------------

To set the state of a check box either set the [*State*](tmp/PROP_BUTTON_STATE.htm) property within the Forms Designer or modify this property directly within the program. Normally a check box has two states, either unchecked or checked. These states can be set with the *State* property, for example the following would be used to check the check box:

.cbControl1.State = TRUE

to uncheck the check box the state is set back to FALSE. If the check box has the

*ThreeState* property set then there is a third state, known as Checked and Grayed. This state can be set by setting the state property to 2, for example:

cbControl1.State = 2
