# HASH(

> Hashes an alpha expression to produce a bucket number in the range `0` to `n-1`.

## Syntax

```
HASH( alpha_expression, numeric_expression )
```

Returns a numeric value. Valid wherever a numeric function is legal.

| Argument | Description |
|----------|-------------|
| `alpha_expression` | The key to hash |
| `numeric_expression` | The modulus (typically a prime number); result is in range 0 to n−1 |

## Description

`HASH(` applies a hash function to the entire first argument and reduces the result modulo the second argument. The result is a number in the range **0 to n−1**.

The modulus is typically a prime number to minimise collisions. Repeated calls with different keys produce approximately uniformly distributed values.

## Examples

```kcml
: DIM result, key$20
: key$ = "Hello"
: result = HASH(key$, 131)
: PRINT "HASH(Hello,131)="; result
: $END
```

Output:
```
HASH(Hello,131)= 32
```

Typical uses:

```kcml
Bucket = HASH(Key1$, 131)
IF (HASH(Index$, Location) < New)
```

## Notes

- The modulus should generally be a **prime number** to spread keys evenly.
- `HASH(` is useful for implementing in-memory hash tables or distributing records across buckets.
- The result is always non-negative (0 to n−1).

## See Also

- `STR(` — substring extraction
- `LEN(` — string length
