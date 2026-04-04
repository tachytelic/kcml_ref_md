Word indexing

KDB tables can be optionally word indexed allowing a rowset to be constructed where particuloar columns contain instances of the nominated words. An table can have multiple word indices and each index can involve one or more columns.

The index is created with a [CREATE WORD INDEX](CREATE_W_INDEX.htm) SQL statement. A word is defined as a run of alphabetic characters separated by whitespace or punctuation but it is possible to tell KCML to consider other characters such as digits using the NONALPHA clause. In particular numbers can be considered as words and INTEGER and NUMERIC columns can be indexed this way. The minimum and maximum length of a word can also be controlled.

Once a word index exists it will be kept up to date automatically. A program can search for rows that match given words using a [KI_WS_START](tmp/KI_WS_START.htm) to build a result set and then traverse it bideirectionally using [KI_WS_READ_NEXT](tmp/KI_WS_READ_NEXT.htm). When the result set is no longer required it should be dropped with a call to [KI_WS_END](tmp/KI_WS_END.htm).

Prior to KCML 6 and the type 7 table storage format there was an earlier word indexing implementation which is now considered obsolete. The API calls KI_WS_CREATE, KI_WS_OPEN, KI_WS_READ, KI_WS_WRITE, KI_WS_REWRITE and KI_WS_DELETE are not required in a KDB database and should not be used.
