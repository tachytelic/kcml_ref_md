# KDB SQL Functions

SQL functions can be used inline in any SQL statement. They can also be invoked using ODBC function escape syntax `{fn functionname()}` but the plain inline form is preferred.

```sql
SELECT UCASE(name) FROM customers
SELECT {fn UCASE(name)} FROM customers   -- ODBC form, also works
```

---

## Set Functions (Aggregate)

Used in queries with `GROUP BY`. Can also be used without `GROUP BY` to aggregate all rows.

| Function | Description |
|----------|-------------|
| `COUNT()` | Number of rows in the group |
| `SUM()` | Sum of the column within the group |
| `AVG()` | Average value of the column within the group |
| `MIN()` | Minimum value of the column within the group |
| `MAX()` | Maximum value of the column within the group |

**Examples:**
```sql
SELECT COUNT(*) FROM SL00trans
SELECT color, COUNT(*), SUM(quantity) FROM SL00test GROUP BY color
SELECT AccountCode, SUM(AmountPaid) FROM TRANSACTIONS GROUP BY AccountCode
SELECT MIN(quantity), MAX(quantity), AVG(quantity) FROM SL00test
```

---

## String Functions

String expressions must have a predictable length at prepare time.

| Function | Description |
|----------|-------------|
| `ASCII(string_exp)` | ASCII code of the leftmost character |
| `BLOBDATA(column, length)` | Returns `length` characters from a BLOB or CBLOB column |
| `CHAR(code)` | Character with the given ASCII code |
| `CONCAT(str1, str2)` | Concatenate two strings |
| `DIFFERENCE(str1, str2)` | Integer difference between SOUNDEX values of two strings |
| `INSERT(str1, start, length, str2)` | Delete `length` chars from `str1` at `start`, insert `str2` there |
| `LCASE(string_exp)` | Convert to lower case |
| `LEFT(string_exp, count)` | Leftmost `count` characters (count must be a constant) |
| `LENGTH(string_exp)` | Number of characters excluding trailing blanks |
| `LOCATE(str1, str2 [, start])` | Starting position of `str1` within `str2` (returns 0 if not found) |
| `LTRIM(string_exp)` | Remove leading blanks |
| `REPEAT(string_exp, count)` | String repeated `count` times (count must be a constant) |
| `REPLACE(str1, str2, str3)` | Replace all occurrences of `str2` in `str1` with `str3` |
| `RIGHT(string_exp, count)` | Rightmost `count` characters (count must be a constant) |
| `RTRIM(string_exp)` | Remove trailing blanks |
| `SOUNDEX(string_exp)` | Standard Soundex four-character value |
| `SPACE(count)` | String of `count` spaces (count must be a constant) |
| `SUBSTRING(str, start, length)` | Substring (start and length must be constant expressions) |
| `UCASE(string_exp)` | Convert to upper case |

**Examples:**
```sql
SELECT UCASE(sname), LCASE(fname) FROM SL00trans
SELECT LENGTH(RTRIM(color)) FROM SL00test
SELECT CONCAT(fname, CONCAT(' ', sname)) AS fullname FROM SL00trans
SELECT * FROM SL00trans WHERE UCASE(sname) LIKE 'SMI%'
SELECT SUBSTRING(color, 1, 3) FROM SL00test
```

---

## Numeric Functions

| Function | Description |
|----------|-------------|
| `ABS(numeric_exp)` | Absolute value |
| `ACOS(float_exp)` | Arccosine (radians) |
| `ASIN(float_exp)` | Arcsine (radians) |
| `ATAN(float_exp)` | Arctangent (radians) |
| `ATAN2(float_exp1, float_exp2)` | Arctangent of x,y coordinates (radians) |
| `CEILING(numeric_exp)` | Smallest integer >= numeric_exp |
| `COS(float_exp)` | Cosine (float_exp in radians) |
| `COT(float_exp)` | Cotangent (float_exp in radians) |
| `DEGREES(numeric_exp)` | Convert radians to degrees |
| `EXP(float_exp)` | Exponential value |
| `FLOOR(numeric_exp)` | Largest integer <= numeric_exp |
| `LOG(float_exp)` | Natural logarithm |
| `LOG10(float_exp)` | Base-10 logarithm |
| `MOD(int1, int2)` | Remainder of int1 / int2 |
| `PI()` | Value of pi |
| `POWER(numeric_exp, int_exp)` | numeric_exp to the power of int_exp |
| `RADIANS(numeric_exp)` | Convert degrees to radians |
| `RAND([integer_exp])` | Random floating point (optional seed) |
| `ROUND(numeric_exp, integer_exp)` | Round to integer_exp decimal places (negative = left of decimal) |
| `SIGN(numeric_exp)` | -1, 0, or 1 |
| `SIN(float_exp)` | Sine (float_exp in radians) |
| `SQRT(float_exp)` | Square root |
| `TAN(float_exp)` | Tangent (float_exp in radians) |
| `TRUNCATE(numeric_exp, integer_exp)` | Truncate to integer_exp decimal places |

**Examples:**
```sql
SELECT ABS(quantity - 100) FROM SL00test
SELECT ROUND(price, 2) FROM products
SELECT MOD(pid, 10) FROM SL00trans
```

---

## Date Functions

Note: KISAM does not support a TIME data type; only DATE functions are available.

| Function | Description |
|----------|-------------|
| `CURDATE()` | Current date as a date value |
| `DAYNAME(date_exp)` | Name of the day (e.g. `Sunday`) |
| `DAYOFMONTH(date_exp)` | Day of month (1–31) |
| `DAYOFWEEK(date_exp)` | Day of week (1=Sunday, 7=Saturday) |
| `DAYOFYEAR(date_exp)` | Day of year (1–366) |
| `MONTH(date_exp)` | Month (1–12) |
| `MONTHNAME(date_exp)` | Name of month (e.g. `January`) |
| `NOW()` | Current date and time as a timestamp |
| `QUARTER(date_exp)` | Quarter (1–4, where 1 = Jan–Mar) |
| `TIMESTAMPADD(interval, int_exp, ts_exp)` | Add `int_exp` intervals to timestamp |
| `TIMESTAMPDIFF(interval, ts1, ts2)` | Number of intervals by which ts2 > ts1 |
| `WEEK(date_exp)` | Week of year (1–53) |
| `YEAR(date_exp)` | Year as integer |

Valid interval values for `TIMESTAMPADD` / `TIMESTAMPDIFF`:
- `SQL_TSI_DAY`
- `SQL_TSI_WEEK`
- `SQL_TSI_MONTH`
- `SQL_TSI_QUARTER`
- `SQL_TSI_YEAR`

**Examples:**
```sql
SELECT * FROM SL00trans WHERE created = CURDATE()
SELECT YEAR(batchdate), MONTH(batchdate), COUNT(*) FROM SL00trans GROUP BY 1, 2
SELECT DAYNAME(created) FROM SL00trans
```

---

## System Functions

| Function | Description |
|----------|-------------|
| `DATABASE()` | Name of the current database (from the sources file / kconf.xml) |
| `IFNULL(exp, value)` | Returns `value` if `exp` is NULL, otherwise returns `exp` |
| `USER()` | Server login ID of the current user |

**Examples:**
```sql
SELECT DATABASE()
SELECT IFNULL(color, 'unknown'), quantity FROM SL00test
```

---

## Type Conversion

No explicit type conversion functions are currently supported. The KCML SQL engine performs implicit conversions where plausible (e.g. numeric to string for display).
