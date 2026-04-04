Designing forms in KCML

Forms are created and maintained using a [graphical editor](TheKCMLFormsDesigner.htm) built into the KCML Workbench and all the information about a form, including the form definition, its controls, methods and events, kept together in one **forms object** enforcing a highly structured approach. The text describing a form is verbose and normally hidden by the workbench withing the DEFFORM statement though it is visible if the program is saved in text form with SAVE ASCII. Right clicking the DEFFORM statement will invoke the editor.

All events for each control and all controls for each form are kept together in the program within a [DEFFORM ... FORM END](Formsprogramming.htm) pair. These statements are like machine written comments which do not do anything themselves but tell the Workbench where to put new event handling code.

Because everything to do with a form is contained between the pairs, the editor can suppress displaying all the statements between a pair greatly simplifying the appearance of a program and revealing its overall structure. Any collapsed section may be expanded simply left clicking on the DEFFORM statement. A similar approach is taken with event handler logic sandwiched between DEFEVENT and END EVENT pairs. The event handler logic can be hidden and revealed by clicking the DEFEVENT keyword.
