Inheriting forms

A new KCML form can be instructed to inherit controls, properties, methods, events and event handlers from an existing form. This allows forms to be created as templates that are subsequently used by other forms within the program. The template form must be available in memory at the time the inheriting form is opened and therefore must either reside in the same program or be available in a module or global partition.

In the KCML6 Workbench if you create a form through the [forms browser](mk:@MSITStore:workbench.chm::/wbbrowseforms.htm) menu you will get a dialog box allowing you to both name the new form and specify the name of any form that you wish to inherit from. A dropdown list shows the names of the other forms in the current program. In the KCML5 editor the required form template is selected when the **Add Form Object** option is selected from within the KCML5 Object Browser.

Form definitions that have inherited information from another form have the parent form name specified within the definition statement. The form name is inserted by the browser when the new form is created and cannot be added at a later date. For example:

-DEFFORM Form1() ... FORM END -DEFFORM Form2(Form1) ... FORM END ... Form2.Open()

When editing forms in the Forms Designer the controls that were inherited are marked with a red cross indicating their parentage and the fact that you cannot edit them. The basic form with its title bar and any inherited controls always come from the template form. The inheriting form just adds extra controls and events.
