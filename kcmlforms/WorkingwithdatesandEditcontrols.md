Working with dates and Edit controls

------------------------------------------------------------------------

An Edit control that has been created with a type of "D", as specified by the

*Type\$* property, can be used to display dates and accept date input from the user. The control automatically inserts forward slash characters to separate the day, month and year. Once the control has been displayed the up and down arrow keys can be used to move to the next an previous days changing the month and year accordingly. The exact date format used by the control is read from the Windows system settings, therefore in Europe the date would be displayed as DD/MM/YYYY and in the United States the format would be MM/DD/YYYY.

The date is sent to the control as a Julian date value. To calculate a Julian Date use the CONVERT DATE statement which converts an ISO date string ("YYYY-MM-DD") into a Julian value and vice verse, for example:

MyDate\$ = "1998-12-25" CONVERT DATE MyDate\$ TO JDate .EditControl1.Text\$ = JDate

The \#DATE function returns today's date as a Julian value. Therefore, to display today's date in the control the following would be used:

.EditControl1.Text\$ = \#DATE

The value entered is returned in the

*Text\$* property as an alpha value, therefore you will need to convert this value to a numeric before it can be reconverted, for example:

CONVERT J_Date\$ TO J_Date CONVERT DATE J_Date TO MyDate\$
