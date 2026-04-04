Forms Designer - working with database tables

The forms designer can bind data aware controls automatically using drag and drop off a Table List. The Table List is displayed if ticked on in the View menu. It displays a tree with nodes for each of the [DEFOBJ](mk:@MSITStore:kcmlrefman.chm::/DEFOBJ.htm) defined tables in the calling program. If the nodes are expanded then the individual columns are shown. Alternatively if the Forms Designer is invoked by the [EditForm()](tmp/PROP_FORM_EDIT2.htm) method the programmer can supply the table list directly.

<div align="center">

<img src="bitmaps/TableList.png" data-border="0" alt="Example Table List" />

</div>

A column can be dragged from the list and dropped onto a form thus creating an edit control bound to that column. The Forms Designer will use the column information in the list to set the width of the control and its [DataSource](tmp/PROP_DATASOURCE.htm), [DataField](tmp/PROP_DATAFIELD.htm) and [Type\$](tmp/PROPSTR_TYPE.htm) properties. If the [Label\$](tmp/PROP_EDIT_EDITLABEL.htm) property is enabled (the default for KCML 6.00+, but set in the options dialog) it will also update the .Label\$ property using the column description from the list.
