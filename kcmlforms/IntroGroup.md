Group control overview

Controls can be organized into named groups using the [Forms Designer](FormsDesignerGroupingControls.htm). The name given to the group becomes the name of a pseudo control at run time and certain methods can be applied to the group which then apply to the group members individually. In this way it is possible to disable or make invisible a number of controls on a form with one call as the form changes mode.

Group methods include

- Enabling and Disabling
- Making visible or invisible
- Making read-only
- Switching focus to the first element

A control can be a member of only one group. You cannot change group membership programmatically at run time.

Group methods do not modify the server-side properties of controls. If a property of a control has been modified by applying a group method, inspecting that property will not return the value being used by the client.
