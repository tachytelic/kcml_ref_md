CREATE WORD INDEX

CREATE WORD INDEX wsindexname ON tablename ( colname \[, colname ...\] ) ORDER BY indexname \[*indexparm* \[, *indexparm*\] ...\]

where the table name should match that in the preceding CREATE TABLE statement. The wsindexname should be the same as the table name with a suffix of "\_Wx" where x is the path number (1 to 4). The parentheses contain the columns (maximum of 8) defining the segments of the key. The coulmns specified should be of type VARCHAR, INTEGER, NUMERIC or IBMPACKED (if the field is one of the numeric types then NONAPLHA '0123456789' should be specified so that numbers are correctly included in the index). Data will be returned in the order defined by indexname which is an existing ordinary index on the table, and the *indexparm* list describes properties of the index e.g.

\[MAX integer\]\
\[MIN integer\]\
\[NONALPHA 'string'\]\
\[NOISE 'filename'\]\

|  |  |
|----|----|
| MAX | Maximum length of word to put into the index, longer words will be truncated (default 8, maximum 16) |
| MIN | Minimum length of word to put into the index (default 3, minimum 2) |
| NONALPHA | String of non alphabetic characters to be included in words |
| NOISE | Full path of file containing words that should be forced to be included or excluded from the index |

Note: Whilst it is possible to use a minimum word length of 2 this may cause the index to become undesirably large, so the default value of 3 is recommended for most applications.

The noise file is an XML file, which conforms to the following dtd: \<!ELEMENT NoiseWords (IncludeList?, ExcludeList?) \> \<!ELEMENT IncludeList (Word+) \> \<!ELEMENT ExcludeList (Word+) \> \<!ELEMENT Word (#PCDATA) \>

Examples

CREATE WORD INDEX SL00trans_W1 ON SL00trans (fname, sname) ORDER BY SL00trans_A09 MAX 15, MIN 5

See also:

[DROP WORD INDEX](DROP_W_INDEX.htm), [CREATE TABLE](CREATE_TABLE.htm) [CREATE INDEX](CREATE_INDEX.htm)
