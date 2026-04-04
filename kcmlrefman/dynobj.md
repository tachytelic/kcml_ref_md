### Accessing C++ objects from KCML

Arbitrary C++ objects can be accessed from KCML using its OBJECT notation provided the code is available as a shared library or DLL and provided the interfaces can be described using a KCML specific interface description language [KIDL](dynidl.htm). The KIDL description is an XML document and it is processed by XSLT tranforms to produce C++ code that acts as a wrapper for the basic object. This code is then compiled and linked with the original code to produce the library. The KIDL description is platform specific but the build process will be different certainly between NT and Unix and possibly between different Unix platforms.

KCML will track references automatically and can call object destructors when objects go out of scope. It will unload the library when the last object is destroyed. If any enumerated constants are declared in the library they will be added to the constants section of the Workbench functions browser.

Example

Here is an example of using the [Xerces DOM parser](xerces.htm) to count the number of tags with a given name in an XML document:

OBJECT x = CREATE "dynamic", "dyndom" OBJECT p = x.CreateParser() p.DoSchema = FALSE p.DoNamespaces = FALSE p.parse("books.xml") OBJECT list = p.Document.getElementsByTagName("book") PRINT list.length OBJECT list = NULL OBJECT p = NULL OBJECT x = NULL
