### Xerces XML DOM parser

This is a product of the [Apache XML project](http://xml.apache.org) available as a shared library and implemented in KCML using [dynamic objects](DynObj.htm). It allows an XML Document Object Model or DOM tree to be created in the memory of a KCML program with nodes corresponding to the tags, text, attributes, comments etc from the XML document. The DOM model is a [W3C standardized](http://www.w3.org) object model used to programmatically manipulate XML. Xerces implements [DOM level 2](http://www.w3.org/TR/DOM-Level-2-Core/) as well as [SAX2](http://sax.sourceforge.net/) and partially implements [Schema](http://www.w3.org/TR/xmlschema-0/). There is also initial support for [DOM3](http://www.w3.org/TR/2002/WD-DOM-Level-3-Core-20020409/) features such as [serialization](http://www.w3.org/TR/2002/WD-DOM-Level-3-ASLS-20020409/)

The DOM parser is ideal for applications that need to load a document in memory and manipulate or access its components randomly.

The SAX2 parser interface is more suitable for applications that wish to stream large documents without building an in-memory DOM tree. This is faster and uses significantly less memory than the DOM approach but once a tag has been parsed it is lost unless the application preserves the information.

An Apache DOM object is created with [CREATE](CREATE.htm) using the dyndom shared library e.g.


    OBJECT x = CREATE "dynamic", "dyndom"

Documentation for the objects created may be found at the Xerces web site [here](http://xml.apache.org/xerces-c/api.html) and their implementation in KCML is documented [here](tmp/dyndom.htm). Note that KCML does not implement all the features of the Xerces model at this time.

There are some examples of using the DOM and SAX in this manual

- [A simple example of counting and printing specific tags](DOMcount.htm)
- [Parsing from a memory buffer](DOMparsemem.htm)
- [Printing a DOM tree using DOM2 methods](DOMprint.htm)
- [Printing a DOM tree using DOM3 methods](DOM3print.htm)
- [Accessing attributes](DOMattr.htm)
- [Creating XML documents](DOMcreate.htm)
- [Using SAX2 to count tags](SAXcount.htm)
