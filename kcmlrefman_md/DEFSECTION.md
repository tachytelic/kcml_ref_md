# DEFSECTION

> Groups subroutines into named sections for organisational purposes in a library.

## Syntax

```
DEFSECTION sectionname
    DEFSUB 'sub1()
    ...
    END SUB
    DEFSUB 'sub2()
    ...
    END SUB
END SECTION
```

## Description

`DEFSECTION` is a purely organisational statement with **no effect at runtime**. It groups subroutines together so the KCML Workbench function browser can display them using section groupings, making large libraries easier to navigate.

`DEFSECTION` and `END SECTION` must always be balanced (paired).

`DEFSECTION` has an effect only within a library; it can be used in any program but only the Workbench benefits from it.

## Example

```kcml
DEFSECTION section_1
    DEFSUB 'sub1_1()
        ...
    END SUB
    DEFSUB 'sub1_2()
        ...
    END SUB
END SECTION

DEFSECTION section_2
    ...
END SECTION
```

## Notes

- Purely for code organisation — has no effect on program behaviour.
- Helps navigate large libraries in the KCML Workbench.
- `DEFSECTION` / `END SECTION` must be balanced; unbalanced pairs cause a resolve-time error.

## See Also

- `DEFSUB` — define a structured subroutine
- `LIBRARY ADD` — load a library into the foreground program
