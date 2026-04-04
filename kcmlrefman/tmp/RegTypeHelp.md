KCML Constants

Registry value types

These constants match the type passed back from RegQueryValueEx() Windows API. For Example: REM Get the PANIC file directory using server-side \$DECLAREs \$DECLARE 'RegQueryValueEx(INT(),STR(),INT(),RETURN INT(),RETURN STR(),RETURN INT())="\*" \$DECLARE 'RegOpenKeyEx(INT(),STR(),INT(),INT(),RETURN INT())="\*" \$DECLARE 'RegCloseKey(INT())="\*" DIM pandir\$256 pandir\$ = 'RegGetPanicDir\$() PRINT "Panic directory is ";pandir\$ END REM Find the PANIC directory from the registry DEFSUB 'RegGetPanicDir\$() LOCAL DIM path\$256 LOCAL DIM hkey, valsize, valtype, rtn rtn = 'RegOpenKeyEx(\_HKEY_LOCAL_MACHINE, "Software\Kerridge\KCML", 0, \_KEY_READ, BYREF hkey) IF (rtn == 0 AND hkey \<\> 0) valsize = LEN(STR(path\$)) rtn = 'RegQueryValueEx(hkey, "panicdir", 0, BYREF valtype, BYREF path\$, BYREF valsize) IF (rtn \<\>0 OR valtype \<\>\_REG_SZ) REM Failed to read value or value isn't a string path\$ = " " END IF 'RegCloseKey(hkey) END IF RETURN path\$ END SUB

| Constant name | Value | Description |
|----|----|----|
| \_REG_NONE | 0 | No defined value type |
| \_REG_SZ | 1 | Null terminated string |
| \_REG_EXPAND_SZ | 2 | String value with embedded environment variables |
| \_REG_BINARY | 3 | Binary data in any form |
| \_REG_DWORD | 4 | A 32-bit integer value |
| \_REG_DWORD_BIG_ENDIAN | 5 | A 32-bit integer value, byte-swapped REG_DWORD |
| \_REG_LINK | 6 | Symbolic-link, to be only used by the Operating system. |
| \_REG_MULTI_SZ | 7 | Array of null-terminated strings, terminated by a double null. |
| \_REG_RES_LIST | 8 | Device-driver resource list |
| \_REG_QWORD | 11 | A 64-bit number |

Back to list of [Constants](constindex.htm)
