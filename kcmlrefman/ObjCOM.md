### COM support in KCML

COM, or [Component Object Model](http://www.microsoft.com/com/about.asp), is a Microsoft standard for binary objects in Windows. Ditributed object support is available with DCOM. While there is some support for DCOM under Unix with Software AG's [EntireX](http://www.softwareag.com/entirex) this has limited platform support and compromised functionality and is not currently available for KCML for Unix. Therefore KCML COM support is limited to Windows NT and Windows 9x. However by using the COM support in Kclient any Unix server can still invoke COM objects either in the client PC or, by using DCOM, on other NT servers. KCML can also act as a [COM server](comserver.htm) exposing its subroutines to other COM clients which may be written in any langauge that supports COM including KCML.

COM is a stategic technology for Microsoft and it provides access to all of its products through COM objects. Using COM you can access data in a database though ADO, you can arrange meetings and send email using CDO, and you can access Word and Excel documents.

KCML clients can only access objects with so-called Dual Interfaces which expose an IDispatch interface and which have a type library associated with them. The type library defines the available objects methods and properties. This IDispatch support is also known as OLE Automation and is used by many languages such as Java, VB, Windows scripting etc. KCML acting as a COM server only exposes an IDispatch interface and can only be accessed by products that support this automation standard.

COM objects can be either DLLs loaded into the KCML address space or separate processes. Using DCOM support in NT objects on other servers can be accesses across the network in a transparent way.

The OBJECT grammar in KCML provides a common, intuitive method for KCML server programs to create and manipulate COM objects existing in their own right and COM controls (aka OCXs) embedded in forms. It is a client server implementation and the objects can exist on the client machine under the control of kclient (to allow for Unix servers) or they can be on the KCML server machine (provided the O/S is Windows 9x or NT).

For more information see the page on [CREATE](CREATE.htm) and on [OLE Automation](comautomation.htm).
