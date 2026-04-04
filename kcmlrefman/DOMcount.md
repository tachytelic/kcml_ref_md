### A simple example of using the DOM

This is a contrived example to show the principles of using the [Xerces DOM object](tmp/dyndom.htm). It counts the number of instances a particular tag in the document then prints out associated values.

First we load the Xerces library into the dynamic object x. This may fail if you do not have both the KCML DOM library dyndom and the dependent xerces library on the PATH. See [CREATE](CREATE.htm) for more about this. We will unload the library when we are done by setting this object to NULL.

Next we create a object of type [Parser](tmp/dyndom.htm#Parser) with the .CreateParser() method. The Parser object owns all the memory used by the DOM and again should be set to NULL when done in order that this memory is freed. It is possible to set various parsing options on the object if you wish to expand namespaces or to validate against a DTD or schema.

The document is parsed and loaded into a DOM tree by the parse() method which takes a file or URL as its argument. You can also parse from memory as shown in this [example](DOMparsemem.htm).

If any error occurs at any point, for instance the xml file is not found or there is an XML syntax error parsing the document, an O30 error is thrown. A robust program should check using [ERROR](ERROR.htm) clauses but this example has omitted this essential precaution in the interests of clarity.

The DOM document is exposed by the document property of the parser object. We can use the getElemetsByTag method exposed by the [Document](tmp/dyndom.htm#Document) object to build a [NodeList](tmp/dyndom.htm#NodeList) collection object consisting of all the nodes that match the id. This can be done with two separate statements or they can be combined using the dot notation into one statment as shown.

The [NodeList](tmp/dyndom.htm#NodeList) collection object has a length property for the number of nodes in the list. You can also iterate over the list using the KCML [FOR OBJECT](FOR_OBJECT.htm) statements. In the example the titles are printed out by descending one level in the tree as its first child will be a [Text](tmp/dyndom.htm#Text) node containing the title string. Note you need to be careful about assumptions like this as the whitespace between tags is also included in the tree unless forbidden in a DTD or schema. In the example there will be an ignorable whitespace text node between the book and title tags so the title tag is actually the second child of the book node.

Finally we free up resources by setting the objects to NULL in the reverse order of creation. This is an essential step. In particular you must free the parser object before creating another one.

OBJECT x = CREATE "dynamic", "dyndom" OBJECT p = x.CreateParser() p.DoNamespaces = FALSE p.parse("books.xml") OBJECT list = p.Document.getElementsByTagName("title") PRINT "Number of books=";list.length FOR OBJECT i IN list PRINT i.firstChild.NodeValue\$ NEXT OBJECT i OBJECT list = NULL OBJECT p = NULL OBJECT x = NULL

A sample document is shown here. Copy this to the clipboard and paste into a file books.xml.

<span id="sample"></span> \<?xml version="1.0"?\> \<library\> \<book isbn="1001" cat="classics"\> \<title\>A Tale of two Cities\</title\> \<author\>Charles Dickens\</author\> \</book\> \<book isbn="1002" cat="classics"\> \<title\>Hamlet\</title\> \<author\>William Shakespeare\</author\> \</book\> \<book isbn="1003" cat="computers"\> \<title\>Inside OLE\</title\> \<author\>Kraig BrockSchmit\</author\> \</book\> \<book isbn="1004" cat="computers"\> \<title\>The C programming language\</title\> \<author\>Brian W Kernigan\</author\> \<author\>Dennis M Richie\</author\> \</book\> \</library\>

For other XML DOM examples click [here](xerces.htm).
