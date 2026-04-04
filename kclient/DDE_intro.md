Dynamic data exchange (DDE)

Microsoft Windows has included from the earliest versions a system that allows Windows applications to communicate with each other in order to transfer data. This system is known as Dynamic Data Exchange or DDE for short. In recent years DDE has been replaced by more modern (and reliable) technologies such as OLE Automation and COM but many applications still offer a DDE interface. In general Automation is to be preferred and Kclient supports acting as an OLE automation client. As a rule only use DDE if that is all the application will support.

Applications that request data from others are known as DDE 'clients', whereas applications that can supply data on request are known as DDE 'servers'. Some applications support DDE in both directions, typical examples of which are Microsoft's Word and Excel. The Windows Program Manager is DDE compliant, allowing other DDE applications to request information about program groups and items - even allowing other applications to create new program groups and items. This will then be reflected in the Win9x or NT4 shell.

Because coding applications to use DDE is not straightforward, a number of functions exist as part of the KCML Client that can simplify matters. These functions can be accessed from KCML using the [\$DECLARE](mk:@MSITStore:kcmlrefman.chm::/$DECLARE.htm) statement, and allow you to send or receive data using DDE with just a few lines of code. For example, a KCML program could start a DDE conversation with Excel, and instruct it to perform a particular task - such as drawing a graph for example. Likewise, a macro written in Excel could request data from KCML, demonstrating the transfer of data in two directions.

The following pages will list the available DDE commands that can be accessed from KCML, using the \$DECLARE statement.

|  |  |
|----|----|
| [KCMLAddTopic](KCMLAddTopic.htm) | Register KClient as a DDE server application |
| [KCMLDdeClose](KCMLDdeClose.htm) | Close conversation |
| [KCMLDdeDestroy](KCMLDdeDestroy.htm) | Unregister Kclient as a DDE client/server application |
| [KCMLDdeExec](KCMLDdeExec.htm) | Execute DDE command |
| [KCMLDdeInit](KCMLDdeInit.htm) | Register Kclient as a DDE client application |
| [KCMLDdeLoad](KCMLDdeLoad.htm) | Check/launch DDE server application |
| [KCMLDdeOpen](KCMLDdeOpen.htm) | Open DDE conversation |
| [KCMLDdePoke](KCMLDdePoke.htm) | Insert a value on the DDE conversation channel |
| [KCMLDdeRequest](KCMLDdeRequest.htm) | Transfer data from a DDE server to a KCML program |

See also [Writing a DDE Server Application in KCML](DDE_Server_principles.htm).
