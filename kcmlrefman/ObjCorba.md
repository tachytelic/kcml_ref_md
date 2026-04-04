### CORBA support in KCML

[CORBA](http://www.omg.org/gettingstarted/corbafaq.htm), or Common Object Request Broker Architecture, is an industry standard for distributed objects which as been evolving for some time. It is language independent (mappings exist for Java, C, C++ smalltalk and COBOL as well as for KCML) and, unlike COM, it runs on both UNIX platforms and NT. The specification is controlled by the Object Management Group, or OMG, and the [OMG web site](http://www.omg.org) contains information about CORBA as a standard. CORBA implementations for various platforms are available commercially from companies such as [Iona Orbix](www.iona.com) and [VisiBroker](www.inprise.com/visibroker) from Inprise. There are also a number of Open Source implementations available such as [MICO](http://www.mico.org) which supports Corba 2.3 and is interoperable with other commercial ORBs.

KCML can acts as both a *client* and a *server* for CORBA. This means that you can use the CORBA industry standard rather than say custom socket listeners, to communicate between KCML processes on different machines, and also call your KCML programs from other programming languages such as Java, C and C++.

In CORBA, an interface repository serves the same purpose as a COM type library. KCML only supports objects which can describe their interfaces (that is they support the **get_interface()** method), so an interface repository must be deployed.

CORBA support is through a shared library *kcorba.so*. In this initial release this is being compiled only for MICO 2.3.3 and is available only on certain platforms (Linux, Unixware 7). Environmental information such as the location of the repositories is passed to KCML using the -q command line switch.
