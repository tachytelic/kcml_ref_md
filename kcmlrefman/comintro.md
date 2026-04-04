# Distributed objects

KCML supports several standards for distributed objects allowing KCML programmers to invoke objects, on the same or on other machines, written in KCML or written in some other programming language that supports these standards. In this mode KCML is said to be acting as a client. Similarly KCML objects can be made are accessible to other programming laguages in which case KCML is said to be acting as a server.

The OBJECT grammar in KCML provides a common, intuitive method for KCML server programs to create and manipulate objects.

### <span id="COM">COM support</span>

[COM](ObjCOM.htm) is a Microsoft standard for binary objects in Windows. It is available for Windows platforms only though Unix servers can use Kclient to acces COM servers. KCML can act as both a server and as a client.

CORBA support

[CORBA](ObjCorba.htm) is an industry standard for distributed objects. It is available for both Unix and Windows. KCML can act as both a server and as a client.

SOAP support

[SOAP](ObjSoap.htm) is an emerging standard for remote procedure calls over the Web using HTTP. It is available for both Unix and NT. KCML can act as a client currently.
