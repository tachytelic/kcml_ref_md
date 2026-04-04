### Printing a DOM tree in DOM3

Support for serialization is defined in the as yet unreleased DOM3 specification and Xerces 2.x supports an initial implementation of this which should be considered experimental though unlikely to change substantially.

To serialize a DOM tree you will need to create a [DOM Writer object](tmp/dyndom.htm#Writer) using the registered [LS Implementation](tmp/dyndom.htm#ImplementationLS), e.g.


    OBJECT x = CREATE "dynamic", "dyndom"
    REM get the DOM LS implementation
    OBJECT impls = x.getDOMImplementation("LS")
    OBJECT writer = impls.createDOMWriter()

The specification allows for multiple registered implementation objects.

Once you have a writer object you can specify the encoding to use with the read/write property [Encoding\$](tmp/dyndom.htm#Writer) (UTF-8 by default) and how new lines are to be handled with the [newline\$](tmp/dyndom.htm#Writer) read/write property (O/S specific default such as HEX(0A) on Unix or HEX(0D0A) on Windows). The feature mechananism allows some control over how the serialization is to be done. E.g. to enable a formatted output you could set this feature on


    writer.setFeature("format-pretty-print", TRUE)

A list of the feature strings can be found [here](tmp/dyndom.htm#Writer).

To generate a string containing the text of the document use the following.


    REDIM z$ = writer.writeToString$(OBJECT root)

The object passed can be the document node or any node in the tree. The tree below the node is serialized. The [WriterFilter](tmp/dyndom.htm#WriterFilter) object can be used to setup a callback function allowing the KCML program to filter the nodes included in the serialized output and to specify classes of nodes to be included.

This example processes the books.xml file and strips out the \<author\> tags when it serializes it to a string:


    DIM z$, OBJECT x, OBJECT p, OBJECT impls, OBJECT writer, OBJECT filter
    DIM _FILTER_ACCEPT=1, _FILTER_REJECT=2, _FILTER_SKIP=3
    OBJECT x = CREATE "dynamic", "dyndom"

    REM parse the file
    OBJECT p = x.CreateParser()
    p.DoNamespaces = FALSE
    p.parse("books.xml")
    OBJECT root = p.Document.DocumentElement

    REM create a writer object
    OBJECT impls = x.getDOMImplementation("LS")
    OBJECT writer = impls.createDOMWriter()

    REM setup for serialization
    writer.setFeature("format-pretty-print", TRUE)
    writer.NewLine$ = HEX(0D0A)

    REM add a filter to strip the <author> tags
    OBJECT filter = p.Document.createWriterFilter()
    filter.SetFilter(BYREF 'accept)
    writer.SetFilter(OBJECT filter)

    REM print to a string
    REDIM z$ = writer.writeToString$(OBJECT root)
    END

    DEFSUB 'accept(OBJECT node)
    REM filter callback function
    RETURN (node.NodeName$ == "author" ? _FILTER_REJECT : _FILTER_ACCEPT)
    END SUB

For other XML DOM examples click [here](xerces.htm).
