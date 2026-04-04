KCML Constants

Registry access flags

This controls the mode in which a Registry key is opened when using a [\$DECLARE](../$DECLARE.htm) of the RegOpenKeyEx() Windows API.

| Constant name        | Value   | Description                         |
|----------------------|---------|-------------------------------------|
| \_KEY_READ           | 0x20019 | Read-only access                    |
| \_KEY_WRITE          | 0x20006 | Can set a value or create a sub-key |
| \_KEY_CREATE_SUB_KEY | 0x4     | Can add a sun-key                   |
| \_KEY_ENUM_KEYS      | 0x8     | Can enumerate sub-keys              |
| \_KEY_QUERY_VALUE    | 0x1     | Can inspect a value data            |
| \_KEY_SET_VALUE      | 0x2     | Can set value data                  |
| \_KEY_ALL_ACCESS     | 0xF003F | Full access to the key              |

Back to list of [Constants](constindex.htm)
