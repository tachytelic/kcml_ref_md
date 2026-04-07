# kconf — Connection Manager Batch Utility

> Batch processing of access control lists in kconf.xml.

## Syntax

```
kconf -i importfile|-I importlist -f configfile -a|-c|-u [-b backup] [-s service] [-g] [-l] [-p]
```

## Description

`kconf` provides batch processing of the Connection Manager's `kconf.xml` access control lists. Useful for adding large numbers of users programmatically.

New users or valid clients are defined in an import list, either from:
- A plain text file (`-i` flag) — one entry per line; `#` starts a comment
- A comma-separated list on the command line (`-I` flag)

## Options

| Option | Description |
|--------|-------------|
| `-i importfile` | Read entries from a `.txt` file (one per line) |
| `-I importlist` | Comma-separated list of entries on command line |
| `-f configfile` | Path to `kconf.xml` |
| `-a` | Add to `adminusers` list (also adds to `validusers`) |
| `-c` | Add to `validclients` list |
| `-u` | Add to `validusers` list |
| `-b backup` | Create a backup of `kconf.xml` before modifying |
| `-s service` | Add entries to the access control list of a specific service |
| `-g` | Generate an access control list for the service if it doesn't exist |
| `-l` | (Unix) Create a `.kcmlLogin` for each new user |
| `-p` | Remove wildcard `*` entries from the access control list |

## Notes

- When adding `validusers` or `adminusers`, proper usernames are required — patterns are not allowed.
- `kconf` warns if a username has no account (`Warning: User fred has no account`) but adds it anyway (the account may be created later).

## Examples

```sh
# Add users from file to validusers in kconf.xml:
kconf -i newusers.txt -f kconf.xml -u

# Add to a specific service with backup:
kconf -i newusers.txt -f kconf.xml -u -s Live -b kconf.backup
```

### Example import file

```
# List of new users
jim
kath
john
alan
```

## See Also

- `kconf.xml` — Connection Manager configuration file
- `asp` — ASP multi-tenant configuration
- `dircon` — direct login mode
