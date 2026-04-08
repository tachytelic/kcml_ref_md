# KDB Utility Programs

## kconvdd — Dictionary Conversion Utility

Converts a legacy `.dd` dictionary file back to SQL `CREATE TABLE` statements. Tables created in KCML 6.00 or later with `CREATE TABLE` have their dictionary embedded in the table file itself; earlier tables had a separate `.dd` file.

```bash
kconvdd [switches] file1 [file2 ...]
```

Output is emitted on stdout.

| Switch | Purpose |
|--------|---------|
| `-b` | Print byte offsets in the row buffer against each column |
| `-f` | Force output even if the dictionary record size is incorrect |
| `-s` | Output dictionary from embedded schema in a type 6+ table file |
| `-t` | Set trace level for debugging |

**Examples:**
```bash
kconvdd /dicts/SL00trans.dd > SL00trans.sql
kconvdd -s /data/SL00trans > SL00trans.sql
```

---

## kconvert — Table Conversion Utility

Converts type 6 (or earlier) tables to type 7 format. Type 7 is required for KDB database connections, embedded schemas, and BLOB support.

- Tables must be in a catalog (unless `-f -s` flags are used) and must have a valid dictionary or `.sq` file entry
- The original file is renamed with a `.kdb` extension appended
- The new file is created in the same directory with the name `oldfilename.kdb`
- If an error occurs, the catalog is reverted to point to the old file

```bash
kconvert [switches] table1 [table2 ...]
```

| Switch | Purpose |
|--------|---------|
| `-d database` | Use the catalog belonging to `database` |
| `-i` | Create indices on the type 7 table matching those on the type 6 table (non-unique indices gain ROWID as last key segment) |
| `-l logfile` | Write output to `logfile` (default: stderr) |
| `-f filename` | Convert single file `filename` without a catalog |
| `-s dictionary` | Dictionary to use with `-f` option (`.sq` or `.dd` file) |
| `-t` | Set trace level for debugging |

Tablenames may include wildcard characters (quote them to prevent shell expansion).

**Examples:**
```bash
# Convert all tables in the BUGS database with index creation
kconvert -i -l /tmp/kconvert.log -d BUGS "*"

# Convert specific tables
kconvert -d LIVE "00*" "01*" 02_BR_BRANC

# Convert a single file without a catalog
kconvert -i -f /data/MK/00/00.MK.Accnts -s /dicts/MK/Accnts.dd
```

---

## krebuild — Index Rebuild Utility

Rebuilds a table's index directly from the data. Faster than dropping and recreating indices via SQL, especially for large tables.

- **Fast rebuild** (default): Uses the existing sequence set, only rebuilds the index set to compact and rebalance. If inconsistency is found, automatically falls back to full rebuild.
- **Full rebuild** (`-f`): Re-reads all data rows and rebuilds the complete index from scratch.

```bash
krebuild [switches] tablefile
```

| Switch | Purpose |
|--------|---------|
| `-c` | Consolidate extents |
| `-f` | Force full rebuild |
| `-p partno` | Specify partition number for locking |
| `-s` | Silent mode |
| `-u` | Open table in `U` (unchecked) mode |
| `-v` | Print version number only |
| `-V level` | Set verbose level |
| `-4` | Rebuild type 3 tables as type 4 |
| `-6` | Rebuild as type 6 index |

**To convert to type 7, use `kconvert` instead** — `krebuild` only goes up to type 6.

Temporary workspace up to twice the index size is required. Use the `WORKSPACE` environment variable to redirect temp files to a larger filesystem if needed.

**Example:**
```bash
WORKSPACE=/tmp/bigspace krebuild -f /data/SL/00/SL00trans
```

---

## krecover — Journal Control Daemon

Manages the KDB journal. See [11-journaling.md](11-journaling.md) for full journal setup and examples.

```bash
krecover [switches]
```

| Switch | Purpose |
|--------|---------|
| `-i` | Show logging information from shared memory and log header |
| `-e` | Enable logging |
| `-n` | Enable huge log mode |
| `-d` | Disable logging |
| `-D` | Delete shared memory |
| `-k` | Shutdown daemon (SIGTERM) |
| `-K` | Kill daemon (SIGKILL) |
| `-s` | Force a sync |
| `-S` | Force syncing mode |
| `-f` | Force recovery of recent logs (< 6 hours old) |
| `-F` | Force recovery regardless of log age |
| `-T` | Force total recovery of huge log |
| `-g num` | Use `num` processes for per-file journal recovery |
| `-j dir` | Use `dir` for per-file journals |
| `-J name` | Tail per-file journal |
| `-l name` | Logging output filename |
| `-m num` | Set maximum log size |
| `-p num` | Set sync pause interval |
| `-r name` | Use `name` as log read device |
| `-w name` | Use `name` as log write device |
| `-v num` | Verbose level (0=silent, 1=errors, 2=status+files, 3=headers, 4=sub-headers) |
| `-x num` | Set transaction mode bit field |
| `-u` | Unlock semaphore |
| `-h` | List command line switches |
| `-t` | Tail journal log |
| `-z` | Disable check for running KCMLs |
| `-Z` | Zap current log file to nulls |

Returns `0` on success, `99` on failure — always check the return code in scripts.

---

## kverify — Table Integrity Verification

Verifies the integrity of table indices. Can also list table properties.

```bash
kverify [switches] file [file ...]
```

Five verification levels (default is level 3):

| Level | What is checked |
|-------|----------------|
| 1 | Control blocks only — super-quick |
| 2 | Controls + sequence set in order + free chains account for all blocks |
| 3 | Level 2 + all data area keys can be looked up in the index |
| 4 | For each ROWID in the index, the row is loaded and its key segments verified |
| 5 | Like level 3 but with exhaustive duplicate checking (very slow on large tables) |

| Switch | Purpose |
|--------|---------|
| `-c` | Print write user count only |
| `-d` | Print table properties only |
| `-e` | Print extent table only |
| `-l level` | Set verification level (1–5) |
| `-p partno` | Specify partition number for locking |
| `-r` | Open in mode `R` (default is `X`) |
| `-s` | Silent mode |
| `-u` | Open in mode `U` |
| `-v` | Print version number only |

**Examples:**
```bash
# Quick check
kverify -l 1 /data/SL/00/SL00trans

# Full verify, read-only mode
kverify -r /data/SL/00/SL00trans

# Print table properties
kverify -d /data/SL/00/SL00trans
```
