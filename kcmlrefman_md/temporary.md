# Temporary Files and Tables

> How KCML temporary files and KISAM tables are automatically cleaned up.

## Description

KCML temporary files and KISAM tables are identified by names starting with three hashes: `###`. They are designed to be automatically removed when a program finishes — even on abnormal termination.

### Platform behaviour

- **Unix**: Files are unlinked from the filesystem immediately after opening. They still exist and consume disk space (visible with `df`) but do not appear in directories (`ls`). 
- **Windows**: Files are flagged for deletion when closed; they remain visible in the filesystem until closed.

## Temporary sequential files

Create with `OPEN #` using a `###` filename; removed by `CLOSE #`:

```kcml
OPEN #stream, "###tempfile", "W", "0666"
REM ... write data ...
CLOSE #stream
```

## Temporary KISAM files

Create with `KI_CREATE`, open with `KI_OPEN`, removed by `KI_CLOSE`:

```kcml
CALL KI_OPEN ki_handle, "###tempkisam", "W" TO ki_status
REM ... use file ...
CALL KI_CLOSE ki_handle TO ki_status
```

## Temporary SQL tables

Create with `CREATE TABLE` using a `###` prefix:

```kcml
DIM sql$500
sql$ = "CREATE TABLE ""###temp"" (ID INTEGER(4), NAME VARCHAR(20))"
CALL KI_PREPARE ki_handle, sql$ TO ki_status
CALL KI_EXECUTE ki_handle TO ki_status
CALL KI_CLOSE ki_handle TO ki_status

REM Add index
sql$ = "CREATE UNIQUE INDEX ""###temp_A1"" ON ""###temp"" (ID)"
CALL KI_PREPARE ki_handle, sql$ TO ki_status
CALL KI_EXECUTE ki_handle TO ki_status
CALL KI_CLOSE ki_handle TO ki_status

REM Open the table (it is removed from the filesystem here on Unix)
CALL KI_OPEN ki_handle, "###temp", "W" TO ki_status
REM ... use table via handle ...
CALL KI_CLOSE ki_handle TO ki_status
```

**Note:** After `KI_OPEN`, the `###` table is removed from the filesystem but remains accessible via the open handle. It can be referenced by its `###` name or as `"#n"` where `n` is the handle number.

Tables created inside a temporary TABLESPACE automatically get the `###` prefix.

## See Also

- `OPEN #` — open sequential file streams
- `CLOSE #` — close and release streams
- `KI_CREATE` — create a KISAM file
- `KI_OPEN` — open a KISAM file
- `KI_CLOSE` — close a KISAM file
