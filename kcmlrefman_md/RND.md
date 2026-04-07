# RND(

> Generates a pseudo-random number between 0 and 1.

## Syntax

```
RND(0)     — return first value in the sequence (reset sequence)
RND(n)     — return next value (n != 0)
```

## Description

Returns a pseudo-random floating-point number in the range `[0, 1)`.

- `RND(0)` — returns the **first** value of the random number sequence. Using `RND(0)` at program start ensures the same sequence every run (deterministic).
- `RND(non-zero)` — returns the **next** value in the sequence.

To generate a random integer in a range: `INT(RND(1) * range) + lower_bound`.

## Examples

```kcml
REM Random number [0,1)
PRINT RND(1)
REM  e.g.  0.1584625767084
```

```kcml
REM Random integer 1–100
DIM roll
roll = INT(RND(1) * 100) + 1
PRINT roll
```

```kcml
REM Deterministic sequence (same on each run)
PRINT RND(0)    : REM  always the same first value
PRINT RND(1)    : REM  next value
PRINT RND(1)    : REM  next value
```

```kcml
REM Shuffle: pick a random element from an array
DIM idx
idx = INT(RND(1) * size) + 1
PRINT arr$(idx)
```

## Notes

- The argument to `RND(` only matters for 0 vs non-zero — the actual value of a non-zero argument does not affect the sequence.
- There is no built-in seed function; `RND(0)` always restarts at the same first value.

## See Also

- `INT(` — floor integer (used to get integer random numbers)
