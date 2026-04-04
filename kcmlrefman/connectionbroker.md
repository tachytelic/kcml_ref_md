Connection Broker

Introduction

The connection broker is a utility which allows KClient and KCML to be used over an unreliable network. When the network link is broken the broker will seamlessly restore the connection once the link is back up. Additionally a mobile device can use a broker-protected connection to enable it to be suspended to save battery power without having to restart a KCML application.

In operation there are two connection brokers, one at the server end and one at the client end. The brokers act as proxies with KClient & KCML remaining unaware of any network disconnections. The server broker runs as a single daemon process handling all connections. It need not be on the same server as the KCML application it protects but it must have a reliable connection to that server. The client broker functionality is built into KClient and needs no additional installation.

In a typical connection scenario KClient will initiate a connection using its internal broker. This broker will then connect to the server-side broker which will in turn connect to the appropriate KCML service. Each session is given a unique ID and also each client computer has a persistent unique ID. If then for some reason the network connection is broken and say, KClient attempts to send some data to KCML the socket send will fail. KClient's broker will attempt to reconnect to the server broker. Once this is successful the server broker will use the session ID to restore the original connection and resend any data lost when the connection was broken.

If the client computer is shut down while the network is disconnected the server broker will be unaware of this and keep the KCML session running. The next time KClient connects the server broker will identify the client computer from its persistent ID and attempt to restore all broken sessions for that computer. Any sessions which no longer exist in the client will then be destroyed in the server.

**Note:**

The connection broker performs no authentication. It simply acts as an unbreakable piece of network cable. Thus it should never be exposed on a public network.

The connection broker acts as a proxy so the client connections will appear to originate from the host running the broker. For this reason the connection broker should not be used where enforcement of the [connection manager](mk:@MSITStore:kwebserv.chm::/connmgr.htm)'s [valid clients](mk:@MSITStore:kwebserv.chm::/systemconf.htm#validip) list is a requirement.

See also:

[Setting up the connection broker](connectionbrokersetup.htm)

[Connection broker options for a KClient connection](mk:@MSITStore:kclient.chm::/optionspage.htm#broker)
