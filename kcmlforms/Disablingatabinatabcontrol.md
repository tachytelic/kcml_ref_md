Disabling a tab in a tab control

To disable an individual tab in a tab control use the [*Enabled* property. Once a tab has been disabled the can see the tab caption but will not be able to use any of the items on the tab iteself. For example, the following would disable a tab in the control *tabControl1*, note that the tab names are created by the](tmp/PROPNUM_ENABLED.htm) [Tab control editor](FormsDesignerTabcontrols.htm):

.tabControl1.MainTab.Enabled = FALSE

Note that the current enabled state of a tab can also be returned by this property, for example:

TabState = .tabControl1.MainTab.Enabled
