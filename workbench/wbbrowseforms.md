## Forms Browser

This uses a tree control to list the forms in the current program. By right clicking on a form in the tree you can jump to the form definition or invoke the forms editor. Expanding a form will display its controls and expanding a control will optionally display the events, methods and properties. A property that is enumerated, this is can only have a limited number of passable symbolic values, is further expandable to show the enumeration. Properties and methods are classified into basic and advanced and two check box options on the browsers menu controls whether only the basic or all the attributes are shown. Events which have handlers defined are flagged <img src="bitmaps/FlaggedEvent.png" data-border="0" />and you can use the Goto option of the right click [context menu](wbcontext.htm) to jump to the DEFEVENT for the handler.

The forms browser is linked to the forms help file so details of properties, methods and events for controls can be found using the help option on the right click context menu.

A down arrow button on the tool bar <img src="bitmaps/browsedownarrow.png" data-border="0" data-align="MIDDLE" alt="browser options menu button" />can bring up a menu controlling how the tree is shown and how forms are manipulated.

<div id="ClickDiv2">

<u>Click here to view the menu</u>

</div>

<div id="PicDiv2" style="Display:none">

<u>Click here to hide</u>

<img src="bitmaps/browseformmenu.png" data-border="0" data-align="TOP" width="272" height="216" alt="Forms browser menu" />

</div>

A new form can be added to the editor at the current cursor position by picking the 'Create new form...' option which will then ask you to name the form.

An existing form can be edited by first selecting it in the browser tree and then either using the right click context menu or taking the second menu option 'Edit form...'.

Properties, property enumerations and events can be dragged from the tree and dropped into the code in the editor window. In the case of an event this will create an empty event handler. A three-way persistent toggle on the browser menu determines whether it uses the full name, leading . or leading .. notation. When events are created either this way or by the forms editor, the workbench may put helpful REM statements into the body of the handler. A toggle on the forms browser menu controls whether this is done.

<div id="ClickDiv">

<u>Click here to view an example browser tree</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example</u>

An example browser tree

<img src="bitmaps/FormBrowseTree.png" data-border="0" alt="Typical form browser tree" />

</div>

If, while in the debugger, the current form is made visible with F4 then clicking on a control will switch the browser to forms mode, expand the subtree for that form and select the appropriate control allowing you to see its available methods, properties and events. This will also happen if you select a form reference in the code using SHIFT-F5 so for example if you SHIFT F5 on .treeControl1.text\$, the expression being inside an event handler for MyForm, then MyForm.treeControl1 will be selected and highlighted in the object browser
