# DEFOBJ

> Binds a database table to data-aware form controls (legacy, pre-KCML 6.10).

## Syntax

```
DEFOBJ objname$ ("REV7DD", ddname$, colprefix$)
```

| Parameter | Description |
|-----------|-------------|
| `objname$` | Name used as the `DataSource` property on data-aware controls |
| `"REV7DD"` | Literal keyword — must be exactly this case-insensitive string |
| `ddname$` | Path to the data dictionary file |
| `colprefix$` | Prefix prepended to column names in field definitions |

## Description

`DEFOBJ` was used prior to KCML 6.10 to declare database tables for binding to data-aware controls on forms. It is a **resolve-time declarative statement** and can appear anywhere in the program.

When a form is opened, data-aware controls are automatically populated (during `.Enter()`) and updated on OK. Only changed columns are sent back to the client.

The program is expected to:
1. Load the row buffers for the relevant tables
2. Establish field definitions
3. Write updated row buffers back to the database

The KCML Workbench forms designer can auto-generate `DEFOBJ` declarations and matching field definitions by scanning the program.

## Notes

- `DEFOBJ` is a **legacy** statement (pre-KCML 6.10). Newer KCML versions use a different mechanism for data binding.
- The first parameter must literally be `"REV7DD"` (case-insensitive).
- Column names in the program use `colprefix$ + column_name` to ensure uniqueness.

## See Also

- `DEFFORM` — define a form
- `DEFEVENT` — define form event handlers
- `FLD(` — access field variables in row buffers
