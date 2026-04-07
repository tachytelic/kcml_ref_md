# Setting Up the Connection Broker

> How to install and configure the KCML connection broker.

## Installation

The broker is installed as part of KCML. It is **not enabled by default**. To start it automatically, uncomment the relevant lines in the KCML startup script:

```sh
if [ /usr/local/kcml/broker ]
then
    /usr/local/kcml/broker &
fi
```

## Configuration

The broker reads its configuration from `kconf.xml`, inside a `<broker>` block:

```xml
<broker>
    <logfile>broker.log</logfile>
    <loglevel>0</loglevel>
</broker>
```

The broker re-reads its configuration when sent `SIGHUP`.

### Configuration options

| Tag | Type | Default | Description |
|-----|------|---------|-------------|
| `listenport` | integer | 14600 | Port the broker listens on for connections |
| `logfile` | string | `broker.txt` | Path to the log file |
| `loglevel` | integer | 1 | Log verbosity: 0 = critical events only, 9 = every connection event |
| `idletimeout` | hours | 48 | How long a session must be idle before becoming a candidate for disconnection when session slots are full |

## Version flag

The only command-line option is `-v` which prints the version number.

```sh
broker -v
```

## See Also

- `connectionbroker` — connection broker overview
- `kconf` — Connection Manager configuration
