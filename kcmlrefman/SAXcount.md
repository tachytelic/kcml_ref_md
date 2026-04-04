### A simple example of using SAX2

This is a contrived example to show the principles of using the SAX parser in the [Xerces DOM object](tmp/dyndom.htm). It counts the number of instances of tag in the document then prints out the statistics.

First we load the Xerces library into the dynamic object x. This may fail if you do not have both the KCML DOM library dyndom and the dependent xerces library on the PATH. See [CREATE](CREATE.htm) for more about this. We will unload the library when we are done by setting this object to NULL.

Next we create a object of type [SAXParser](tmp/dyndom.htm#SAXParser) with the .CreateSAXParser() method.

SAX works by calling back to DEFSUBs in the KCML program whenever the parser identifies particular structuresin the document. You can get called for opening tags, closing tags, character data etc. The programmer informs the parser of the callback locations by creating a [ContentHandler](tmp/dyndom.htm#ContentHandler) object and using appropriate setter routines therein to pass the DEFSUB names e.g.

h.setStartElement(BYREF 'startElement)

The BYREF is absolutely necessary when passing locations like this. The DEFSUB must exist or an O30 error will be thrown. If the arguments to the callback function do not agree with those expected by the parser an O30 error will be thrown while parsing. A robust program should check using [ERROR](ERROR.htm) clauses but this example has omitted this essential precaution in the interests of clarity.

Once the KCML handlers have been defined the ContentHandler is assigned to the parser and the program can start parsing. The parser will then call back into the various DEFSUBs. Note that for character text the length is the number of Unicode characters in the string which may be less than the number of bytes which can be found using LEN(STR(text\$)). Also the character handler will be called for the whitespace between tags unless a DTD is used defining them as ignorable. The application must be able to handle multiple callbacks for one run of text between tags as can typically occur when the text contains entities like \&amp;.

SAX2 is namespace aware and when called for a tag, the tag name will be broken into the NS URI if applicable, the basic tag and the qname. If a tag is not namespaced then the uri string will be an empty string and the localname and qname will be the same.

Finally we free up resources by setting the objects to NULL in the reverse order of creation. This is an essential step. In particular you must free the parser object before creating another one.

REM example showing the use of SAX to parse a document DIM charcount, attrcount, tagcount, level, maxlevel, whitespace DIM OBJECT x, OBJECT p, OBJECT h REM create a SAX parser OBJECT x = CREATE "dynamic", "dyndom" OBJECT p = x.CreateSAXParser() REM create a Content handler and specify the callbacks OBJECT h = p.ContentHandler() h.setStartElement(BYREF 'startElement) h.setEndElement(BYREF 'endElement) h.setCharacters(BYREF 'chars) h.setStartDocument(BYREF 'startDoc) h.setEndDocument(BYREF 'endDoc) REM install it p.setContentHandler(OBJECT h) REM parse it p.parse("books.xml") REM tidy up OBJECT h = NULL OBJECT p = NULL OBJECT x = NULL END DEFSUB 'startDoc() REM zero counters at start of document charcount = 0 attrcount = 0 tagcount = 0 level = 0 maxlevel = 0 whitespace = 0 END SUB DEFSUB 'endDoc() REM print results at the end PRINT "tags =";tagcount PRINT "attributes=";attrcount PRINT "characters=";charcount PRINT "max depth =";maxlevel PRINT "whitespace=";whitespace END SUB DEFSUB 'startElement(uri\$, local\$, qname\$, OBJECT x) REM called for each opening tag attrcount += x.length tagcount++ level++ IF (level \> maxlevel) THEN maxlevel = level END SUB DEFSUB 'endElement(uri\$, local\$, qname\$) REM called on closing a tag level-- END SUB DEFSUB 'chars(text\$, len) REM called for any characters between tags, including whitespace REM note that len represents the Unicode chars in the string charcount += len REM track all whitespace nodes \$TRAN(text\$, HEX(200A 200D 2009))R IF (text\$ == " ") THEN whitespace++ END SUB

Use the sample document from the DOM example [here](DOMcount.htm#sample).

<span id="#progressive"></span>

##### Progressive parsing

To allow the application to abandon parsing in the middle of a document once it has extracted the necessary information you should use the progressive scan methods of parseFirst(), parseNext() and parseReset(). The parseFirst() method loads the document and returns TRUE if successful. The parseNext() method is called then to advance process each piece of markup in turn e.g.


    REM progessive scan
    OBJECT t = p.createScanToken()
    bOK = p.parseFirst("books.xml", OBJECT t)
    STOP
    WHILE bOK DO
        bOK = p.parseNext(OBJECT t)
    WEND
    p.parseReset(OBJECT t)

You can abandon parsing by not calling parseNext() again though to free parser memory you must call parseReset() when done.

For other XML DOM examples click [here](xerces.htm).
