# Libraries

> How to package reusable KCML code into shared libraries that can be loaded by any program.

## Overview

Libraries are the modern KCML mechanism for sharing code, constants, and field definitions between programs. They replace the older [global partition](TutorialGlobal.md) concept and should be used in all new applications.

A library is a compiled p-code file (`.klib`) that is loaded into a running KCML program's address space with `LIBRARY ADD`. Once loaded, the library's public functions, constants, and fields are immediately available to the program as if they had been defined locally.

```kcml
LIBRARY ADD "CoreFunctions" = "../libraries/CoreFunctions.klib"
```

The string before `=` is the **friendly name** used to refer to the library in diagnostics and `LIST M` output. The string after `=` is the file path to the compiled `.klib` file.

## Loading and Unloading Libraries

### Loading

```kcml
LIBRARY ADD "MyLib" = "/usr/lib/myapp/MyLib.klib"
```

Libraries can be loaded at any point in a program. The load order matters: when KCML resolves a reference to a function, constant, or field, it searches the currently executing program first, then libraries in the order they were loaded.

There is no limit on the number of loaded libraries.

### Inspecting loaded libraries

```kcml
LIST M
```

Lists all currently loaded libraries in search order.

### Unloading

```kcml
LIBRARY REMOVE "MyLib"
LIBRARY REMOVE ALL
```

Unloading is generally not recommended because library variables are not destroyed — they persist in the foreground program's variable space. Use `LIBRARY REMOVE` only if you have a specific reason.

### Automatic lifecycle

- `CLEAR` and `LOAD RUN` unload all libraries.
- `LOAD` (without `RUN`) does **not** unload libraries. This is intentional: it allows a library to be resident while different programs are loaded and run.

## Encapsulation

Libraries are the primary encapsulation mechanism in KCML. A well-structured library:

1. **Declares its data** in `COM` statements (creating library variables in the foreground).
2. **Initializes its data** in a `'Constructor()` function, which KCML calls automatically after the library loads.
3. **Exposes behaviour** through `PUBLIC DEFSUB` functions.
4. **Hides internals** with `PRIVATE`.

### Library variables

Variables declared in a library's `COM` statement are called **library variables**. When the library is loaded, KCML creates these variables in the foreground program's namespace. Unlike ordinary `DIM` variables, library variables survive `LOAD` statements (they behave like `COM`). If the library is unloaded with `LIBRARY REMOVE`, these variables revert to being ordinary `DIM`-style variables.

### The Constructor function

If a library defines a `DEFSUB 'Constructor()`, that function runs immediately after the library is loaded. Use it to initialize library variables.

### PUBLIC and PRIVATE

```kcml
PUBLIC DEFSUB 'GetPrice$(item_code$)
    REM callable from any program that has loaded this library
    ...
RETURN price$

PRIVATE DEFSUB 'FormatInternal$(raw$)
    REM only callable from within this library
    ...
RETURN formatted$

PUBLIC DIM MAX_ITEMS = 1000    REM exported constant
PRIVATE DIM BUFFER_SIZE = 256  REM internal constant only
```

If neither `PUBLIC` nor `PRIVATE` is specified, `PUBLIC` is assumed. However, explicitly marking scope is strongly recommended — it prevents name clashes between libraries and makes the interface clear.

> **Future compatibility:** In a future version of KCML, `PRIVATE` will become the default. Write new libraries with explicit `PUBLIC` on every exported symbol.

`PUBLIC` and `PRIVATE` can be used with `DIM`, `DEFRECORD`, and `DEFSUB`.

## Creating a Library

Libraries are compiled from KCML source files using the `kc6` command-line compiler:

```bash
kc6 -o MyLib.klib myprog.src anotherprog.src
```

If your library depends on constants or field definitions from another library, specify it with `-i`:

```bash
kc6 -o MyLib.klib -i BaseLib.klib myprog.src anotherprog.src
```

Multiple `-i` flags can be used for multiple dependencies.

### Multiple source components

A library can be built from multiple `.src` files. Each component is compiled independently and can have overlapping line number ranges without conflict. Each component can also have its own `'Constructor()` — all constructors are called in order when the library loads.

### Automating builds with kmake

For applications with multiple libraries and complex dependencies, use the `kmake` utility. It reads an XML build file that specifies libraries, their source components, and their dependencies. `kmake` uses filesystem timestamps to rebuild only what has changed.

## Sharing Data Between Partitions

A library can share data across KCML partitions by using `@`-prefixed (global) variable declarations:

```kcml
DIM @shared(10)    REM marks library as containing shared data
```

The first such library to be loaded is mapped read-write and its `@` variables are writable. Only one shared-data library is supported at a time — if a second is loaded, its variables will not be visible from the foreground.

## Notes

- **Libraries replace global partitions.** For any new application needing shared code, use `LIBRARY ADD` rather than the `-g` kcml switch and `SELECT @PART`.
- **Load order determines search order.** If two libraries define a function with the same name, the one loaded first wins. Use `PRIVATE` to avoid exposing internal functions that could cause clashes.
- **`DIM` in a library** is only for declaring constants (and occasionally fields). Variables that need to exist in the foreground should use `COM`.
- **Fields should use `DEFRECORD`**, not raw `DIM` field declarations, in almost all cases.
- See also: `LIBRARY ADD`, `LIBRARY REMOVE`, `LIST M`, `DEFSUB`, `DEFRECORD`, `kc6`, `kmake`, [TutorialGlobal](TutorialGlobal.md)
