# <span id="theconnectionwizard"></span> The connection Wizard

While it is possible to create a batch file or a shortcut to invoke KCML, the recommended technique is to use the connection Wizard. This uses the Windows Explorer shell to create a special connection file (a .kcc file) which defines the connection to the server and provides an easy to use icon in Explorer to invoke it.

To create a new connection to a KCML application you should right click in either the required Explorer folder or on the desktop. This brings up a popup menu one of whose options is 'New…'. Choose this and a further popup appears along side the first with a list of things that can be created at this location. One of these will be 'KCML client'. If you choose this you will invoke the Kclient connection Wizard property pages which allow the specification of how the client is to connect to its server.

There are 3 pages on a Windows 95 computer and 4 pages on NT. The extra NT page defines standard NT security properties for the connection file that are not implemented for Windows 95. The first page defines general file details for the connection file. The remaining pages [connection](connectionpage.htm) and [options](optionspage.htm) are explained later in this section.

There are two modes of operation depending on whether this is a direct connection to a local server or a networked connection over TCP/IP. The WKCML version of KCML for use on single PC's or on peer-to-peer LANs does not offer the Remote Connect option. Similarly the client installed on the PC's of a Client Server version of KCML for use with a Unix or NT server will not offer the local connect option.
