# Direct Login Mode (Unix)

> How to configure KCML as a direct TCP/IP service via inetd, bypassing the telnet daemon.

## Description

Direct Login mode allows KCML to be a service available through the Unix `inetd` TCP/IP super-server. KCML is launched directly when a KClient connects, avoiding the performance overhead of the telnet daemon.

**Requirements:**
- End users must run KClient (not a generic terminal).
- Not available on Windows.
- The Connection Manager may be a more appropriate and general solution.

## How it works

1. A KClient connects to the configured port.
2. `inetd` launches KCML with the `-l` flag.
3. KCML prompts for login/password, authenticates against `/etc/passwd`, sets the security context, and changes to the user's home directory.
4. Because no shell or `.profile` is executed, environment variables must be loaded from `kconf.xml` using the `-S service_name` flag.

## Configuration

### `/etc/inetd.conf` entry

```
kcml  stream  tcp  nowait  root  /usr/lib/kcml/kcml  /usr/lib/kcml/kcml -l -S my_application
```

- The first argument must be the full path to `kcml`.
- One argument must be `-l`.
- The `-S my_application` flag loads environment variables from the `my_application` service in `kconf.xml`.

The service in `kconf.xml` should define a `START` environment variable pointing to the KCML startup program.

### `/etc/services` entry

```
kcml  777/tcp
```

Choose a port number not already in use (check `/etc/services` and `netstat -a`).

## Notes

- The original `kcmlprofile` method has been withdrawn. Add environment variables to `kconf.xml` `<general>` and `<service>` sections instead.
- After authentication, KCML runs the program named in the `START` environment variable.

## See Also

- `kconf` — Connection Manager and kconf.xml configuration
- `kcml` — KCML interpreter command-line flags
- `asp` — multi-tenant ASP configuration
