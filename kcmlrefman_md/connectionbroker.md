# Connection Broker

> Utility that provides seamless reconnection for KClient/KCML over unreliable networks.

## Description

The connection broker is a utility that protects KClient/KCML connections against network interruptions. When the network link breaks, the broker automatically restores the connection once the link is restored. Mobile devices can use the broker to suspend without restarting the KCML application.

## Architecture

Two broker instances work together:
- **Server-side broker**: a daemon process handling all connections. Does not need to be on the same host as KCML, but must have a reliable connection to it.
- **Client-side broker**: built into KClient — no separate installation needed.

KClient connects to its internal broker → the client broker connects to the server broker → the server broker connects to the KCML service.

## How reconnection works

Each session has a unique ID; each client computer has a persistent unique ID.

1. If the network breaks and KClient attempts to send data, the socket fails.
2. KClient's broker attempts to reconnect to the server broker.
3. On success, the server broker uses the session ID to restore the connection and resend any lost data.

If the client computer shuts down while disconnected, the server broker keeps the KCML session running. When KClient reconnects, the server broker uses the persistent client ID to restore broken sessions; sessions that no longer exist on the client are destroyed on the server.

## Security notes

- The connection broker performs **no authentication** — it acts as an unbreakable network cable.
- **Never expose the broker on a public network.**
- Client connections appear to originate from the broker host — do not use the broker where enforcement of the Connection Manager's valid-clients list is required.

## See Also

- `connectionbrokersetup` — setting up the connection broker
- `kconf` — Connection Manager configuration
