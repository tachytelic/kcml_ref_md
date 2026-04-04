XML support in KCML

XML is a standard markup language under development at the World Wide Web Consortium ([W3C](http://www.w3.org/TR/REC-xml)) which can be used to describe data in a very general way. It is a subset of SGML and has many similarities to HTML, an application of SGML, but is more general and is extensible. The XML standard is of growing importance for data on web pages and in particular for Business to Business (B2B) exchange of data via the Web or email.

- KCML has a built in XML 1.0 [non-validating parser](XMLExpat.htm) which can build a tree from XML supplied either in a file ([XML_OPEN](tmp/XML_OPEN.htm)) or in a string buffer ([XML_PARSE_BUFFER](tmp/XML_PARSE_BUFFER.htm)). A program can then traverse the tree from top to bottom by calling [XML_NEXT](tmp/XML_NEXT.htm) repeatedly to get the next element together with its value and any attributes.
- There is also support for accessing a third party [XML DOM parser](mk:@MSITStore:kcmlrefman.chm::/xerces.htm). This allows programs to build and manipulate XML trees in a program and is recommended for more complex applications.
- This parser also support [SAX2](mk:@MSITStore:kcmlrefman.chm::/SAXcount.htm) which is best suited to reading large documents and is a better choice than the built in parser for such tasks.
