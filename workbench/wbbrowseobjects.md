## Object browser

There are two parts to the Object Browser. One part displays objects that have been instantiated in a running program, the other allows you to store references to objects that need not have been instantiated. One is useful for debugging the other for development. The first is able to display [COM](mk:@MSITStore:KCMLrefman.chm::/comintro.htm#COM), [Corba](mk:@MSITStore:KCMLrefman.chm::/comintro.htm#CORBA), or [SOAP](mk:@MSITStore:KCMLrefman.chm::/comintro.htm#SOAP) object type. The second section allows COM Type Libraries and SOAP Object definitions to be displayed.

<div id="ClickDiv">

<u>Click here for an example browser tree browsing an ADO collection object</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example</u>

<img src="bitmaps/ObjBrowseTree.png" data-border="0" alt="COM browser for ADO objects" />

</div>

For each instantiated object a tree control displays its methods, properties, events and enumerations. Some objects may have subsidiary objects such as collections. Expanding methods will show any arguments required together with their types. If the type is an enumeration then it too can be expanded to see the enumerated values. Optional arguments are surrounded by \[\] characters.

<div id="ClickDiv2">

<u>Click here for an example browser tree browsing the References Section</u>

</div>

<div id="PicDiv2" style="Display:none">

<u>Click here to hide the example</u>

<img src="bitmaps/ObjBrowseTreeRef.png" data-border="0" alt="COM browser for References" />

</div>

The objects in the references section are displayed in exactly the same way. To place an object definition in the references section you will need to use the [Object Management Dialog](wbbrowseobjman.htm) that can be opened using the down arrow icon in the Browser Window Toolbar.

Selecting a method or property of a COM object which has *HelpString* comments attached will display the comment at the bottom of the browser. The right click context menu can be used to display any available help file information. For Soap Objects there may be help documentation included in he WSDL definition. This documentation will also be displayed at the bottom of the browser.

The types of parameters and the return values of functions are shown for informational purposes in lower case inside parentheses after the variable name. These generally follow the COM conventions e.g. int(4) for a four byte signed integer. A variant type can be a string or a number depending on the requirements of the function.

For some parameters passed by reference the BYREF keyword will prefix the name indicating that it is required when passing the parameter from KCML. Additionally for numbers if the data type required is a double then the browser will display BYREF NUM(*param name*) to indicate that doubles have to be distinguished this way to KCML as numeric arguments passed by reference are otherwise assumed to be signed four byte integers.

Methods can be presumed to return an integer result unless the names is modified with a \$ suffix implying a string result or a type, such as void for no result, is shown.

In the references section there are several different functions provided by either drag&drop or context menus. They depend upon which node you have selected. Below is a table that outlines these functions.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Node Type</th>
<th>Context Menu Options</th>
<th>Drag&amp;Drop functionality</th>
</tr>
</thead>
<tbody>
<tr>
<td>SOAP Object</td>
<td><ol>
<li>Help.</li>
</ol></td>
<td>Will create an object definition in the code.</td>
</tr>
<tr>
<td>SOAP Method</td>
<td><ol>
<li>Help.</li>
<li>Copy Method name to windows clipboard.</li>
</ol></td>
<td>None.</td>
</tr>
<tr>
<td>COM Type Library or COM Object</td>
<td><ol>
<li>Help.</li>
</ol></td>
<td>Will create an object definition in the code.</td>
</tr>
<tr>
<td>COM Method</td>
<td><ol>
<li>Help.</li>
<li>Copy Method name to windows clipboard.</li>
<li>Copy a $Declare statement to windows clipboard. The $Declare statement is automatic built from this objects methods. This is intended for use with the Windows API type library.</li>
</ol></td>
<td>None.</td>
</tr>
<tr>
<td>Object Enumeration</td>
<td><ol>
<li>Help.</li>
<li>Copy enumeration name to windows clipboard.</li>
</ol></td>
<td>Insert the enumeration name in your program code.</td>
</tr>
</tbody>
</table>
