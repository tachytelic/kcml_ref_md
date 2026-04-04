# Xerces DOM object

------------------------------------------------------------------------

Usage:


    OBJECT x = CREATE "dynamic", "dyndom"

For further information see <http://xml.apache.org/xerces-c/index.html>

------------------------------------------------------------------------

[root](#root)\
[SAXParser](#SAXParser)\
[ContentHandler](#ContentHandler)\
[ScanToken](#ScanToken)\
[Attributes](#Attributes)\
[Parser](#Parser)\
[Document](#Document)\
[Node](#Node)\
[Implementation](#Implementation)\
[DocumentType](#DocumentType)\
[Text](#Text)\
[CDATASection](#CDATASection)\
[Comment](#Comment)\
[DocumentFragment](#DocumentFragment)\
[EntityReference](#EntityReference)\
[ProcessingInstruction](#ProcessingInstruction)\
[CharacterData](#CharacterData)\
[Attr](#Attr)\
[Element](#Element)\
[NamedNodeMap](#NamedNodeMap)\
[NodeList](#NodeList)\
[TreeWalker](#TreeWalker)\
[NodeIterator](#NodeIterator)\
[NodeFilter](#NodeFilter)\
[MemBufInputSource](#MemBufInputSource)\
[Writer](#Writer)\
[MemBufOutput](#MemBufOutput)\
[WriterFilter](#WriterFilter)\
[ImplementationLS](#ImplementationLS)\

------------------------------------------------------------------------

<span id="root"></span>

## root

Xerces XML root object

This product includes software developed by the Apache Software Foundation (http://www.apache.org/).

| Method | Returns | Purpose | Status |
|----|----|----|----|
| createParser() | [XercesDOMParser](#XercesDOMParser) | Creates DOM parser object | KCML |
| createSAXParser() | [SAXParser](#SAXParser) | Creates a SAX2 parser object | KCML |
| getDOMImplementation(name\$) | [Implementation](#Implementation) | Return an Implementation ref from DOM Implementation Registry | KCML |

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| Implementation | R | [Implementation](#Implementation) | Return an Implementation ref | KCML |

------------------------------------------------------------------------

<span id="SAXParser"></span>

## SAXParser

SAX2 Parser object

| Method | Returns | Purpose | Status |
|----|----|----|----|
| ContentHandler() | [ContentHandler](#ContentHandler) | Constructor for a SAX2 ContentHandler object | KCML |
| createScanToken() | [ScanToken](#ScanToken) | Allocate a ScanToken for use in a progressive parse | KCML |
| getFeature(name\$) | bool | Query the state of a SAX2 feature |  |
| getProperty\$(name\$) | string | Query the state of a SAX2 property |  |
| parse(URI\$) | void | Parse a URI |  |
| parseFirst(URI\$, [token](#ScanToken)) | bool | Start a progressive parse of a URI |  |
| parseNext([token](#ScanToken)) | bool | Continue a progressive parse |  |
| parseReset([token](#ScanToken)) | void | Reset the parser after a progressive parse |  |
| setContentHandler([handler](#ContentHandler)) | void | Specify the SAX2 ContentHandler |  |
| setFeature(name\$, value) | void | Specify the state of a SAX2 feature |  |
| setProperty(name\$, value\$) | void | Specify the state of a SAX2 property |  |

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| ErrorCount | R | int | Get error count from last parse |  |
| ExitOnFirstFatalError | RW | bool | Get/set Exit On First Fatal Error flag |  |
| ValidationConstraintFatal | RW | bool | Get/set Validation Constraint Fatal flag |  |

------------------------------------------------------------------------

<span id="ContentHandler"></span>

## ContentHandler

Object that receives callbacks from SAX2 events

| Method | Returns | Purpose | Status |
|----|----|----|----|
| SetCharacters(fn) | void | Set KCML handler subroutine for characters |  |
| SetEndDocument(fn) | void | Set KCML handler subroutine for end of document |  |
| SetEndElement(fn) | void | Set KCML handler subroutine for end of element |  |
| SetIgnorableWhitespace(fn) | void | Set KCML handler subroutine for DTD defined ignorable whitespace |  |
| SetResetDocument(fn) | void | Set KCML handler subroutine for restart of document |  |
| SetStartDocument(fn) | void | Set KCML handler subroutine for start of document |  |
| SetStartElement(fn) | void | Set KCML handler subroutine for start of element |  |

| Callback | Returns | Purpose | Status |
|----|----|----|----|
| characters(text\$, length) | void | Receive notification of text. Note that the length is the number of UTF-16 characters in the string. To get the length in bytes use LEN(STR(text\$)). This handler may be called more than once for a text string which contains entities. |  |
| endDocument() | void | Receive notification of end of document |  |
| endElement(uri\$, localname\$, qname\$) | void | Receive notification of end of every element |  |
| ignorableWhitespace(text\$, length) | void | Receive notification of DTD defined ignorable whitespace |  |
| resetDocument() | void | Receive notification of restart of document |  |
| startDocument() | void | Receive notification of start of document |  |
| startElement(uri\$, localname\$, qname\$, [attributes](#Attributes)) | void | Receive notification of start of every element, uri\$ is the combination of the NS and the tag as a URI, localname\$ is the bare tag name, qname\$ is the tag with its prefix,attributes is an object containing any attributes for the tag |  |

------------------------------------------------------------------------

<span id="ScanToken"></span>

## ScanToken

Scan state token for progressive parsing

------------------------------------------------------------------------

<span id="Attributes"></span>

## Attributes

A list of attributes for an element as returned by SAX2

| Method | Returns | Purpose | Status |
|----|----|----|----|
| Index(qname\$) | integer | Returns the index of an attribute in the list by qualified name |  |
| Index(uri\$, localpart\$) | integer | Returns the index of an attribute in the list by namespace name |  |
| LocalName\$(index) | string | Returns the local name of an attribute in the list by index (0 based) |  |
| QName\$(index) | string | Returns the qualified name of an attribute in the list by index (0 based) |  |
| Type\$(qname\$) | string | Returns the type of an attribute in the list by qualified name. The attribute type is one of the strings 'CDATA', 'ID', 'IDREF', 'IDREFS', 'NMTOKEN', 'NMTOKENS', 'ENTITY', 'ENTITIES', or 'NOTATION' (always in upper case). |  |
| URI\$(index) | string | Returns the namespace URI of an attribute in the list by index (0 based) |  |
| Value\$(index) | string | Returns the value of an attribute in the list by position |  |

| Property | Type | Returns      | Purpose                                    | Status |
|----------|------|--------------|--------------------------------------------|--------|
| Length   | R    | unsigned int | Returns the number of elements in the list |        |

------------------------------------------------------------------------

<span id="Parser"></span>

## Parser

Parser object

| Method | Returns | Purpose | Status |
|----|----|----|----|
| MemBufInputSource(buf, buflen, id) | [MemBufInputSource](#MemBufInputSource) | Constructor for a memory buffer input stream |  |
| adoptDocument() | [Document](#Document) | Adopt DOM document, caller now responsible for releasing memory |  |
| parse(URI\$) | void | Parse a URI |  |
| parseIS([stream](#MemBufInputSource)) | void | Parse from an inputstream | KCML |
| reset() | void | Reset parser state ready for another parse |  |
| resetDocumentPool() | void | Free parser memory |  |

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| CreateEntityReferenceNodes | RW | bool | Get/set flag controlling expansion of entities |  |
| DoNamespaces | RW | bool | Get/set process namespaces flag |  |
| DoSchema | RW | bool | Get/set Process schemas flag |  |
| Document | R | [Document](#Document) | Return document object |  |
| ErrorCount | R | int | Get error count from last parse |  |
| ExitOnFirstFatalError | RW | bool | Get/set Exit On First Fatal Error flag |  |
| ExternalNoNamespaceSchemaLocation\$ | RW | string | Get/set location of an external schema or DTD |  |
| ExternalSchemaLocation\$ | RW | string | Get/set location of an external schema or DTD. There can be a list of more than one. It matches the target namespace of the instance document. |  |
| IncludeIgnorableWhitespace | RW | bool | Get/set flag controlling how whitespace is treated (requires DTD) |  |
| LoadExternalDTD | RW | bool | Get/set flag to control loading of an external DTD. If the DTD is referenced only for consistency checking and is not needed during the parse, say to supply entities, then set this flag to FALSE. |  |
| ValidationConstraintFatal | RW | bool | Get/set Validation Constraint Fatal flag |  |
| ValidationScheme | RW | ValScheme | Get/set validation scheme |  |

------------------------------------------------------------------------

<span id="Document"></span>

## Document

DOM Document object

Multiply inherits from among the following interfaces:

[Node](#Node)\

| Method | Returns | Purpose | Status |
|----|----|----|----|
| createAttribute(name\$) | [Attr](#Attr) | Create a new attribute node with given name |  |
| createAttributeNS(namespaceURI\$, qualname\$) | [Attr](#Attr) | Create a new attribute node with given name |  |
| createCDATASection(data\$) | [CDATASection](#CDATASection) | Create a new CDATA node for given data |  |
| createComment(text\$) | [Comment](#Comment) | Create a new Comment node for given text |  |
| createDocumentFragment() | [DocumentFragment](#DocumentFragment) | Create an empty DocumentFragment object |  |
| createElement(tagname\$) | [Element](#Element) | Create a new Element node |  |
| createElementNS(namespaceURI\$, qualname\$) | [Element](#Element) | Create a new Element node |  |
| createEntityReference(name\$) | [EntityReference](#EntityReference) | Create a new Entity reference node |  |
| createNodeFilter() | [NodeFilter](#NodeFilter) | Create a node filter object | KCML |
| createNodeIterator([root](#Node), whatToShow, [filter](#NodeFilter), entityReferenceExpansion) | [NodeIterator](#NodeIterator) | Create a flat tree NodeIterator |  |
| createProcessingInstruction(target\$, data\$) | [ProcessingInstruction](#ProcessingInstruction) | Create a new Processing Instruction node |  |
| createTextNode(data\$) | [Text](#Text) | Create a new Text node |  |
| createTreeWalker([root](#Node), whatToShow, [filter](#NodeFilter), entityReferenceExpansion) | [TreeWalker](#TreeWalker) | Import a node from another document |  |
| createWriterFilter() | [WriterFilter](#WriterFilter) | Create a serialization WriterFilter object | KCML |
| getElementById(id\$) | [Element](#Element) | Return element matching an ID |  |
| getElementsByTagName(pattern\$) | [NodeList](#NodeList) | Make node list of elements matching a tag name or '\*'. It does not support XPath. |  |
| getElementsByTagNameNS(NsURI\$, localname\$) | [NodeList](#NodeList) | Get a node list object of descendent objects by name |  |
| importNode([importnode](#Node), deep) | [Node](#Node) | Import a node from another document |  |

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| Doctype | R | [DocumentType](#DocumentType) | Returns the document type declaration |  |
| DocumentElement | R | [Element](#Element) | Returns the documents root element |  |
| Implementation | R | [Implementation](#Implementation) | Returns the implementation object that handles the doc |  |

------------------------------------------------------------------------

<span id="Node"></span>

## Node

DOM Node object

Downcastable from the following interfaces:

[Text](#Text)\
[Element](#Element)\
[CharacterData](#CharacterData)\
[DocumentType](#DocumentType)\
[Attr](#Attr)\

| Method | Returns | Purpose | Status |
|----|----|----|----|
| appendChild([newChild](#Node)) | [Node](#Node) | Add child to list of children |  |
| cloneNode(deep) | [Node](#Node) | Clone this node |  |
| hasChildNodes() | bool | Return true if node has children |  |
| insertBefore([newChild](#Node), [refChild](#Node)) | [Node](#Node) | Insert node before existing child node |  |
| isSupported(feature\$, version\$) | bool | Supports a specified function |  |
| normalize() | void | Normalize children |  |
| release() | void | Free resources | Xerces |
| removeChild([oldChild](#Node)) | [Node](#Node) | Delete child oldchild from the list of children and return it |  |
| replaceChild([newChild](#Node), [oldChild](#Node)) | [Node](#Node) | Replace existing child with newchild and return oldChild |  |

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| Attributes | R | [NamedNodeMap](#NamedNodeMap) | Return a list of the attributes of the node or NULL |  |
| ChildNodes | R | [NodeList](#NodeList) | Return all children in a nodelist |  |
| FirstChild | R | [Node](#Node) | Return first child of a node |  |
| LastChild | R | [Node](#Node) | Return last child of a node |  |
| LocalName\$ | R | string | Return local part of the qualified name of this node |  |
| NamespaceURI\$ | R | string | Return namespace URI for node tag |  |
| NextSibling | R | [Node](#Node) | Return next sibling of a node |  |
| NodeName\$ | R | string | Return name of a node |  |
| NodeType | R | int | Return type of a node |  |
| NodeValue\$ | R | string | Return value of a node, depending on type |  |
| OwnerDocument | R | [Document](#Document) | Get the document associated with this node |  |
| ParentNode | R | [Node](#Node) | Return parent of a node |  |
| Prefix\$ | RW | string | Get/set namespace prefix of this node |  |
| PreviousSibling | R | [Node](#Node) | Return previous sibling of a node |  |

------------------------------------------------------------------------

<span id="Implementation"></span>

## Implementation

DOM Implementation object

Downcastable from the following interfaces:

[ImplementationLS](#ImplementationLS)\

| Method | Returns | Purpose | Status |
|----|----|----|----|
| createDocument(NamespaceURI\$, qualifiedName\$, [doctype](#DocumentType)) | [Document](#Document) | Creates a new XML Document object |  |
| createDocument() | [Document](#Document) | Creates a nameless XML document object |  |
| createDocumentType(qualifiedName\$, publicId\$, systemId\$) | [DocumentType](#DocumentType) | Creates a new XML DocumentType object |  |
| hasFeature(feature\$, version\$) | bool | returns TRUE if a feature is supported |  |

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| Implementation | R | [Implementation](#Implementation) | Return a Implementation ref for this object |  |

------------------------------------------------------------------------

<span id="DocumentType"></span>

## DocumentType

DOM Document type object

Extends [Node](#Node)

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| Entities | R | [NamedNodeMap](#NamedNodeMap) | Return a NamedNodeMap of the entities declared in the DTD |  |
| InternalSubset\$ | R | string | Return internal subset as a string |  |
| Name\$ | R | string | Return name of the DTD |  |
| Notations | R | [NamedNodeMap](#NamedNodeMap) | Return a NamedNodeMap of the notations declared in the DTD |  |
| PublicId\$ | R | string | Return public ID of external subset |  |
| SystemId\$ | R | string | Return system ID of external subset |  |

------------------------------------------------------------------------

<span id="Text"></span>

## Text

DOM Text object

Extends [CharacterData](#CharacterData)

| Method | Returns | Purpose | Status |
|----|----|----|----|
| isIgnorableWhitespace() | bool | Returns TRUE if node contains only ignorable whitespace (requires a DTD) |  |
| isWhitespace() | bool | Returns TRUE if node contains only whitespace | KCML |
| splitText(offset) | [Text](#Text) | Splits node into two at offset |  |

------------------------------------------------------------------------

<span id="CDATASection"></span>

## CDATASection

DOM CDATA object

Extends [Text](#Text)

------------------------------------------------------------------------

<span id="Comment"></span>

## Comment

DOM Comment object

Extends [CharacterData](#CharacterData)

------------------------------------------------------------------------

<span id="DocumentFragment"></span>

## DocumentFragment

DOM DocumentFragment object

**DocumentFragment** is a lightweight [Document](#Document) object allowing a program to extract part of a document tree or create a small object that looks like a [Node](#Node) without the overhead of a [Document](#Document) object.

In operations, such as inserting Nodes as children of other [Nodes](#Nodes), that take Nodes as arguments, a DocumentFragment may be passed resyulting in all the child nodes of the DocumentFragment being moved to the child list of this node.

DocumentFragment nodes do not need to be well-formed XML documents (although they do need to follow the rules imposed upon well-formed XML parsed entities, which can have multiple top nodes). For example, a DocumentFragment might have only one child and that child node could be a [Text](#Text) node. Such a structure model represents neither an HTML document nor a well-formed XML document.

When a DocumentFragment is inserted into a [Document](#Document) (or indeed any other [Node](#Node) that may take children) the children of the DocumentFragment and not the DocumentFragment itself are inserted into the [Node](#Node). This makes the DocumentFragment very useful when the user wishes to create nodes that are siblings; the DocumentFragment acts as the parent of these nodes so that the user can use the standard methods from the [Node](#Node) interface, such as **insertBefore()** and **appendChild()**.

Extends [Node](#Node)

------------------------------------------------------------------------

<span id="EntityReference"></span>

## EntityReference

DOM EntityReference object

Extends [Node](#Node)

------------------------------------------------------------------------

<span id="ProcessingInstruction"></span>

## ProcessingInstruction

DOM ProcessingInstruction object

Extends [Node](#Node)

| Property | Type | Returns | Purpose                      | Status |
|----------|------|---------|------------------------------|--------|
| Data\$   | RW   | string  | Get/set data of the element  |        |
| Target\$ | R    | string  | Return target of the element |        |

------------------------------------------------------------------------

<span id="CharacterData"></span>

## CharacterData

DOM Character object

Extends [Node](#Node)

| Method | Returns | Purpose | Status |
|----|----|----|----|
| appendData(newdata\$) | void | Appends character data to end of node |  |
| deleteData(offset, count) | void | Deletes character data at the offset in the node |  |
| insertData(offset, newdata\$) | void | Inserts character data at the offset in the node |  |
| replaceData(offset, count, newdata\$) | void | Replaces character data at the offset in the node |  |
| substringData\$(offset, count) | string | Returns a substring of character data for node |  |

| Property | Type | Returns      | Purpose                           | Status |
|----------|------|--------------|-----------------------------------|--------|
| Data\$   | R    | string       | Return data of the element        |        |
| Length   | R    | unsigned int | Return count of chars in the text |        |

------------------------------------------------------------------------

<span id="Attr"></span>

## Attr

DOM Attribute object

Extends [Node](#Node)

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| Name\$ | R | string | Return name of the attribute |  |
| OwnerElement | R | [Element](#Element) | Return Element node the attribute is attached to or NULL if none |  |
| Specified | R | bool | Return TRUE if the attribute was explicitly specified rather than assumed from the DTD default |  |
| Value\$ | RW | string | Get/set value of the attribute |  |

------------------------------------------------------------------------

<span id="Element"></span>

## Element

DOM Element object

Extends [Node](#Node)

| Method | Returns | Purpose | Status |
|----|----|----|----|
| getAttribute\$(name\$) | string | Get attribute of element by name |  |
| getAttributeNS\$(NsURI\$, localname\$) | string | Get attribute of element by name |  |
| getAttributeNode(name\$) | [Attr](#Attr) | Get a Attr node object by name |  |
| getAttributeNodeNS(NsURI\$, localname\$) | [Attr](#Attr) | Get a Attr node object by name |  |
| getElementsByTagName(name\$) | [NodeList](#NodeList) | Get a node list object of descendent objects by name |  |
| getElementsByTagNameNS(NsURI\$, localname\$) | [NodeList](#NodeList) | Get a node list object of descendent objects by name |  |
| removeAttribute(name\$) | void | Remove attribute of element by name |  |
| removeAttributeNS(NsURI\$, localname\$) | void | Remove attribute of element by name |  |
| removeAttributeNode([name](#Attr)) | [Attr](#Attr) | Remove specified Attr node |  |
| setAttribute(name\$, value\$) | void | Set attribute of element by name |  |
| setAttributeNS(NsURI\$, qualname\$, value\$) | void | Set attribute of element by name |  |
| setAttributeNode([newattr](#Attr)) | [Attr](#Attr) | Adds or replaces an Attr node |  |
| setAttributeNodeNS([newattr](#Attr)) | [Attr](#Attr) | Adds or replaces an Attr node |  |

| Property  | Type | Returns | Purpose                    | Status |
|-----------|------|---------|----------------------------|--------|
| TagName\$ | R    | string  | Return name of the element |        |

------------------------------------------------------------------------

<span id="NamedNodeMap"></span>

## NamedNodeMap

DOM Named Node Map object

This collection can be iterated with FOR OBJECT ... NEXT OBJECT

| Method               | Returns       | Purpose                      | Status |
|----------------------|---------------|------------------------------|--------|
| getNamedItem(name\$) | [Node](#Node) | Return node with given name  |        |
| item(index)          | [Node](#Node) | Return node with given index |        |

| Property | Type | Returns      | Purpose                          | Status |
|----------|------|--------------|----------------------------------|--------|
| Length   | R    | unsigned int | Return count of nodes in the map |        |

------------------------------------------------------------------------

<span id="NodeList"></span>

## NodeList

DOM Node List object

This collection can be iterated with FOR OBJECT ... NEXT OBJECT

| Method      | Returns       | Purpose                      | Status |
|-------------|---------------|------------------------------|--------|
| item(index) | [Node](#Node) | Return node with given index |        |

| Property | Type | Returns      | Purpose                              | Status |
|----------|------|--------------|--------------------------------------|--------|
| Length   | R    | unsigned int | Return count of nodes in a node list |        |

------------------------------------------------------------------------

<span id="TreeWalker"></span>

## TreeWalker

DOM TreeWalker object

| Method | Returns | Purpose | Status |
|----|----|----|----|
| firstChild() | [Node](#Node) | Moves to first child and returns the node |  |
| getCurrentNode() | [Node](#Node) | Get node at which the NodeWalker is positioned |  |
| lastChild() | [Node](#Node) | Moves to last child and returns the node |  |
| nextNode() | [Node](#Node) | Moves to and returns next node in list |  |
| nextSibling() | [Node](#Node) | Moves to next sibling and returns the node |  |
| parentNode() | [Node](#Node) | Moves to and returns the closest visible ancestor node of the current node in list |  |
| previousNode() | [Node](#Node) | Moves to and returns previous node in list |  |
| previousSibling() | [Node](#Node) | Moves to previous sibling and returns the node |  |
| setCurrentNode([node](#Node)) | void | Set node at which the NodeWalker is positioned |  |

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| ExpandEntityReferences | R | bool | Return original ExpandEntityReferences flag |  |
| WhatToShow | R | integer | Return bitmap of node types included |  |

------------------------------------------------------------------------

<span id="NodeIterator"></span>

## NodeIterator

DOM NodeIterator object

| Method         | Returns       | Purpose                      | Status |
|----------------|---------------|------------------------------|--------|
| nextNode()     | [Node](#Node) | Return next node in list     |        |
| previousNode() | [Node](#Node) | Return previous node in list |        |

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| ExpandEntityReferences | R | bool | Return original ExpandEntityReferences flag |  |
| WhatToShow | R | integer | Return bitmap of node types included |  |

------------------------------------------------------------------------

<span id="NodeFilter"></span>

## NodeFilter

Object that receives filter callbacks from NodeIterator and TreeWalker

The acceptNode() callback function returns one of the following enumeration\
DIM \_FILTER_ACCEPT=1, \_FILTER_REJECT=2, \_FILTER_SKIP=3

| Method        | Returns | Purpose                                | Status |
|---------------|---------|----------------------------------------|--------|
| SetFilter(fn) | void    | Set KCML callback for filtering a node |        |

| Callback                  | Returns | Purpose | Status |
|---------------------------|---------|---------|--------|
| acceptNode([node](#Node)) | integer |         |        |

------------------------------------------------------------------------

<span id="MemBufInputSource"></span>

## MemBufInputSource

Memory buffer based input stream object

------------------------------------------------------------------------

<span id="Writer"></span>

## Writer

Used to serialize a document

**Features supported**

This table is taken from the Apache Xerces documentation

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>normalize-characters</td>
<td>true [ optional] (default) Perform the W3C Text Normalization of the characters in document as they are written out. Only the characters being written are (potentially) altered. The DOM document itself is unchanged.<br />
false [required] do not perform character normalization.</td>
</tr>
<tr>
<td>split-cdata-sections</td>
<td>true [required] (default) Split CDATA sections containing the CDATA section termination marker ']]&gt;' or characters that can not be represented in the output encoding, and output the characters using numeric character references. If a CDATA section is split a warning is issued.<br />
false [ required] Signal an error if a CDATASection contains an unrepresentable character.</td>
</tr>
<tr>
<td>validation</td>
<td>true [ optional] Use the abstract schema to validate the document as it is being serialized. If validation errors are found the error handler is notified about the error. Setting this state will also set the feature use-abstract-schema to true.<br />
false [ required] (default) Don't validate the document as it is being serialized.</td>
</tr>
<tr>
<td>expand-entity-references</td>
<td>true [ optional] Expand EntityReference nodes when serializing.<br />
false [required] (default) Serialize all EntityReference nodes as XML entity references.</td>
</tr>
<tr>
<td>whitespace-in-element-content</td>
<td>true [required] ( default) Output all white spaces in the document.<br />
false [ optional] Only output white space that is not within element content. The implementation is expected to use the isWhitespaceInElementContent flag on Text nodes to determine if a text node should be written out or not.</td>
</tr>
<tr>
<td>discard-default-content</td>
<td>true [required] (default ) Use whatever information available to the implementation (i.e. XML schema, DTD, the specified flag on Attr nodes, and so on) to decide what attributes and content should be serialized or not. Note that the specified flag on Attr nodes in itself is not always reliable, it is only reliable when it is set to false since the only case where it can be set to false is if the attribute was created by a Level 1 implementation.<br />
false [required] Output all attributes and all content.</td>
</tr>
<tr>
<td>format-canonical</td>
<td>true [optional] This formatting writes the document according to the rules specified in DOM3. Setting this feature to true will set the feature "format-pretty-print" to false.<br />
false [required] (default) Don't canonicalize the output.</td>
</tr>
<tr>
<td>format-pretty-print</td>
<td>true [optional] Formatting the output by adding whitespace to produce a pretty-printed, indented, human-readable form. The exact form of the transformations is not specified by this specification. Setting this feature to true will set the feature "format-canonical" to false.<br />
false [required] (default) Don't pretty-print the result.</td>
</tr>
</tbody>
</table>

| Method | Returns | Purpose | Status |
|----|----|----|----|
| canSetFeature(feature\$, value) | bool | Indicates whether setting a feature to a particular value will be supported | DOM3 |
| getFeature(feature\$) | bool | Get the value of a standardized feature | DOM3 |
| release() | void | Free resources | Xerces |
| setFeature(feature\$, value) | void | Set the value of a standardized feature | DOM3 |
| setFilter([filter](#WriterFilter)) | void | Apply a WriterFilter object to filter the serialized output | DOM3 |
| writeDocToString(doc) | [MemBufOutput](#MemBufOutput) | Serialize a UTF-8 encoded document to a string object | KCML |
| writeToString\$([node](#Node)) | string | Serialize a node or document to a string | DOM3 |
| writeToStringObject(node) | [MemBufOutput](#MemBufOutput) | Serialize a node to a string object | DOM3 |

| Property | Type | Returns | Purpose | Status |
|----|----|----|----|----|
| Encoding\$ | RW | string | Get/Set encoding to use when serializing. NULL means UTF-8. | DOM3 |
| NewLine\$ | RW | string | Get/Set end-of-line sequence to use when serializing. Only HEX(0A), HEX(0D) and HEX(0D0A) are acceptable. NULL means OS default. | DOM3 |

------------------------------------------------------------------------

<span id="MemBufOutput"></span>

## MemBufOutput

String object

| Property | Type | Returns | Purpose           | Status |
|----------|------|---------|-------------------|--------|
| Text\$   | R    | string  | Return UTF-8 text | KCML   |

------------------------------------------------------------------------

<span id="WriterFilter"></span>

## WriterFilter

Object that receives filter callbacks during serialization

The acceptNode() callback function returns the same enumeration as the NodeFilter callbacks namely\
DIM \_FILTER_ACCEPT=1, \_FILTER_REJECT=2, \_FILTER_SKIP=3

| Method        | Returns | Purpose                                | Status |
|---------------|---------|----------------------------------------|--------|
| SetFilter(fn) | void    | Set KCML callback for filtering a node |        |

| Callback                  | Returns | Purpose | Status |
|---------------------------|---------|---------|--------|
| acceptNode([node](#Node)) | integer |         |        |

| Property   | Type | Returns | Purpose                                 | Status |
|------------|------|---------|-----------------------------------------|--------|
| WhatToShow | RW   | integer | Get/Set types of nodes to be serialized |        |

------------------------------------------------------------------------

<span id="ImplementationLS"></span>

## ImplementationLS

Factory methods for DOM Writer object

Extends [Implementation](#Implementation)

| Method | Returns | Purpose | Status |
|----|----|----|----|
| createDOMWriter() | [Writer](#Writer) | Create a Writer serializing object | DOM3 |
