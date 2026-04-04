Making all controls in a group readonly

------------------------------------------------------------------------

As well as being able to disable the controls in a group it is also possible to make the controls read only. The difference being that the user can gain access to a readonly contol but they cannot change the contents. This property is only relevant when used with edit controls.

To make all the controls in a group read only the

*ReadOnly()* method is used. Passing a value of *TRUE* means that the controls in the group are made read only while a value of *FALSE* resets the default edit mode for the controls.. For example, the following would make all the controls in the group *grpControl1* read only:

.grpControl1.ReadOnly(TRUE)

To reset the controls back to the normal edit mode following would be used:

.grpControl1.ReadOnly(FALSE)
