Using objects and properties

A form is essentially like any other KCML variable. Each form contains a number of controls (push button, edit box, list box etc.), and each control contains a number of properties (position, value etc.) and a number of events (such as clicking on a button). Thus the text in an edit box (say Edit1) in a form (say Form1) would be represented as:

Form1.edit1.text\$

To change the text of a control we would use

Form1.edit1.Text\$ = "New text"

It is worth noting that when the properties of a control are changed the control is not updated until the current event handler is complete. To force an update the

*Flush()* method is used.
