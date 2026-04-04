KCML Constants

Base registry keys

These constants are some of the predefined, base, registry keys that can be used when [\$DECLARE'ing](../$DECLARE.htm) the RegOpenKeyEx() Windows API. For Example: DIM hkey, rtn \$DECLARE 'RegOpenKeyEx(INT(),STR(),INT(),INT(),RETURN INT()) \$DECLARE 'RegCloseKey(INT()) hkey = 0 rtn = 'RegOpenKeyEx(\_HKEY_LOCAL_MACHINE, keyname\$, 0, \_KEY_READ, BYREF hkey) IF (rtn == 0 AND hkey \<\> 0) PRINT "Registry key " ; keyname\$ ; " has been opened" 'RegCloseKey(hkey) END IF

| Constant name        | Value      | Description                        |
|----------------------|------------|------------------------------------|
| \_HKEY_CLASSES_ROOT  | 0x80000000 | File extensions and associations   |
| \_HKEY_CURRENT_USER  | 0x80000001 | Logged on user's registry settings |
| \_HKEY_LOCAL_MACHINE | 0x80000002 | Global System settings             |

Back to list of [Constants](constindex.htm)
