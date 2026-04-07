# KCML Reserved Words

> Keywords that cannot be used as variable names in KCML.

## Description

Because KCML allows multi-character variable names, there is a potential conflict between language keywords and possible variable names. The following words are **reserved** and may not be used as variable names.

## Reserved word list

```
ABS(        ADD         ADD(        ADDC        ADDC(
ALARM       ALERT       ALL         ALL(        AND
AND(        ARC         ARCCOS(     ARCSIN(     ARCTAN(
ASCII       AT(         ATN(        BA          BAT
BEG         BIN(        BM          BOOL        BOOL(
BOX(        BREAK       BU          BYREF       CALL
CASE        CI          CLEAR       CLOSE       CO
COM         CON         CON(        COND(       CONTINUE
CONVERT     COPY        COS(        CREATE      DA
DAC         DATA        DATALOAD    DATASAVE    DATE
DBACKSPACE  DC          DCT         DEFCOMOBJ   DEFEVENT
DEFFN       DEFFORM     DEFOBJ      DEFSUB      DEGREES
DELETE      DESELECT    DIM         DIM(        DIR
DISK        DO          DRIVER      DSC         DSKIP
DT          EDIT        ELEMENT     ELSE        ELSEDO
END         ENDDO       ENDEVENT    ENDIF       ENDSUB
ENUM        ENV(        ERR         ERR(        ERROR
EXP(        EXTEND      FALSE       FIX(        FLD(
FN          FOR         FORM        FROM        FSORT
GOLDKEY     GOSUB       IDN         IDN(        IF
INDEX(      INIT(       INPUT       INT(        INV(
ISNULL(     KEY         KEY(        KEYIN       LEN(
LET         LGT(        LIMITS      LIMITST     LINE
LINPUT      LIST        LOAD        LOADDC      LOADT
LOCAL       LOCK        LOG         LOG(        LOOP
LS          LTRIM(      MAT         MAX(        MERGE
MIN(        MOD(        MODULE      MOVE        NEEDS
NEXT        NOROUND     NOT         NUM(        OBJECT
OFF         ON          OPEN        OR          OR(
PACK        PACK(       PANIC       PART        PASSWORD
PAUSE       PI          PLOT        POS(        PRECISION
PREV        PRINT       PRINTUSING  PTR(        RADIANS
RBACKSPACE  READ        RECNO       RECNO(      REDIM
REM         REMOVE      RENAME      RENAMET     RENUMBER
REPEAT      RESAVE      RESAVET     RESTORE     RETURN
REWRITE     RND(        ROTATE(     ROTATEC(    ROUND
ROUND(      RSKIP       RTRIM(      RUN         SAVE
SAVEDCT     SAVET       SAVET(      SBACKSPACE  SCRATCH
SCRATCHT    SCREEN      SEARCH      SEEK        SELECT
SET         SGN(        SHELL       SIN(        SORT
SPACE       SPACEF      SPACEK      SPACEP      SPACEV
SPACEW      SQR(        SSKIP       START       STAT
STEP        STOP        STR(        SUB         SUBC
SYM(        SYMNAME(    TAB(        TAN(        TAPE
TC          TERM        TERMINAL    THEN        THENDO
TIME        TO          TRACE       TRAP        TRN(
TRUE        UNLOCK      UNPACK      UNPACK(     UNSCRATCH
UNTIL       VAL(        VER(        VERIFY      WEND
WHILE       WINDOW      WRITE       XOR         XOR(
ZER         ZER(
```

## Notes

- Reserved words are **case-insensitive** — `PRINT`, `Print`, and `print` are all reserved.
- Function reserved words include `(` — e.g. `ABS(` is reserved but `ABS` (without the paren) is not.
- `MODULE` and `OBJECT` became reserved in KCML 6.
- `BYREF`, `RTRIM(`, `LTRIM(` became reserved in KCML 5.

## See Also

- `compatver` — KCML version compatibility
