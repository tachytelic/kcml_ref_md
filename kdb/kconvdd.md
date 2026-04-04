Dictionary conversion utility

Database tables will only contain embedded data dictionary information if they were type 6 or higher and were created using an SQL CREATE TABLE statement in KCML 6.00 or later. Earlier tables required a separate dictionary table to define their structure. Conventionally these dictionaries had the same name as the table they described but with a .dd extension. The *kconvdd* utility can be used to convert one of these dictionaries back to SQL. The general usage is

kconvdd \[switches\] file1 \[ file2 ...\]

The SQL is emitted on standard output. The optional switches are

| Switch | Purpose |
|----|----|
| -b | Print byte offsets in the table row buffer against each column. Generally these are deduced by CREATE TABLE. |
| -f | Force kconvdd to produce some output even if the data dictionary record size is incorrect. |
| -s | Output dictionary from embedded dictionary in table |
| -t | Set trace level for debugging. |
