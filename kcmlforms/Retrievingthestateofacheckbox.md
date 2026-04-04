Retrieving the state of a check box

------------------------------------------------------------------------

To retrieve the current state of a check box the

*State* property is used, for example the following would retrieve the current state of the check box:

CheckBoxState = .cbControl1.State

The *State* property returns 0 if the check box is unchecked, 1 if it is checked and 2 if the check box has the

*ThreeState* style set and the box is grayed out.
