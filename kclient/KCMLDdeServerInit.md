KCMLDdeServerInit(flags)

This registers the KCML program with Windows as a DDE server. The flags argument is a bitmask of flags that condition the conversations we will accept. The useful flags are

| Constant | Value | Description |
|----|----|----|
| CBF_FAIL_EXECUTES | 0x8000 | Prevents the server from receiving XTYP_EXECUTE transactions. Any client that attempts this will be refused. |
| CBF_FAIL_POKES | 0x10000 | Prevents the server from receiving XTYP_POKE transactions. Any client that attempts this will be refused. |
| CBF_FAIL_REQUESTS | 0x20000 | Prevents the server from receiving XTYP_REQUEST transactions. Any client that attempts this will be refused. |

By ORing these together, transaction types that the program does not wish to handle can be passed back to Windows.

Syntax

\$DECLARE'KCMLDdeServerInit(INT())

Returns

If successful, the function returns an instance number otherwise it will return zero.

Example

See the [DDE server example](DDE_server_principles.htm).
