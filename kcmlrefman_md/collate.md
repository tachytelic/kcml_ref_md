# Collating Sequences

> How KCML orders strings when sorting and comparing.

## Description

When sorting strings, KCML uses a collating sequence to determine character ordering. The default (US ASCII) is straightforward — the ASCII code value determines sort order. However, Latin1 and other code pages break this relationship (e.g. `Ä` has code 196, which sorts after `Z` rather than between `A` and `B`).

## Selecting a collating sequence

Set byte 50 of `$OPTIONS RUN` to select the active collating sequence:

| Value | Sequence |
|-------|----------|
| `HEX(00)` | Default — US ASCII (code page order) |
| `HEX(01)` | Latin1 — correct ordering for accented Western European characters |
| `HEX(02)` | User-defined — via a shared library |

This byte also controls how `$UPPER` and `$LOWER` determine case, and how `$STRCOLL` compares characters.

## Effect on SORT

`SORT` uses collating sequences when key segments are specified with the `KEY` option clause. Without the `KEY` option, the default binary comparison is used regardless of byte 50.

## User-defined collating sequences

Setting byte 50 to `HEX(02)` enables a custom collating sequence loaded from a shared library. This allows any arbitrary character ordering to be implemented (e.g. for East Asian or other non-Latin character sets).

## See Also

- `SORT` — sort arrays
- `$STRCOLL` — string collation comparison
- `$UPPER` — convert to uppercase
- `$LOWER` — convert to lowercase
- `$OPTIONS` — runtime options byte array
