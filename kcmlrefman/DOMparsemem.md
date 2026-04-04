### XML DOM parsing from memory

This example shows the use of a [MemBufInputSource](tmp/dyndom.htm#MemBufInputSource) input stream object which allows the [parser](tmp/dyndom.htm#Parser) to parse a buffer rather than a file or URL.

DIM OBJECT x, OBJECT p, OBJECT Is, n REM create root object OBJECT x = CREATE "dynamic", "dyndom" REM create a parser object OBJECT p = x.CreateParser() p.DoSchema = FALSE p.DoNamespaces = FALSE REM fake up some XML DIM z\$="\<?xml version=""1.0""?\>\<root\>\<tag\>Hello\</tag\>\</root\>" REM create an input stream object OBJECT Is = p.MemBufInputSource(z\$, LEN(z\$), "test") REM parse it p.parseIS(OBJECT Is) OBJECT Is = NULL REM count the tags n = p.Document.getElementsByTagName("\*").length IF (n \<\> 2) THEN PRINT "Oops!" REM destroy the objects OBJECT p = NULL OBJECT x = NULL

For other XML DOM examples click [here](xerces.htm).
