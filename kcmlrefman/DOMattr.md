### XML DOM accessing attributes

This example shows the use of a [NamedNodeList](tmp/dyndom.htm#NamedNodeList) collection for accessing the attributes of an [element](tmp/dyndom.htm#Element) mode. Using the XML sample from the first [example](DOMcount.htm#sample) it makes up a [NodeList](tmp/dyndom.htm#NodeList) collection of the various books and then picks out those that have a category of 'classics' printing the isbn reference for each.

A NodeList is generated for all the \<book\> nodes. Each node has an Attribute property which is a NamedNodeList of attribute nodes. This is checked using the getNamedItem() method to select those that have the right value for the *cat* attribute and if it matches the value of the isbn attribute is printed.

Note that the attribute collection was referenced by OBJECT a first rather than used in two inline expressions which would have involved evaluating the expression twice.

OBJECT x = CREATE "dynamic", "dyndom" OBJECT p = x.CreateParser() p.parse("books.xml") FOR OBJECT i IN p.Document.getElementsByTagName("book") OBJECT a = i.Attributes IF (a.getNamedItem("cat").NodeValue\$ == "classics") PRINT a.getNamedItem("isbn").NodeValue\$ END IF NEXT OBJECT i OBJECT a = NULL OBJECT p = NULL OBJECT x = NULL

For other XML DOM examples click [here](xerces.htm).
