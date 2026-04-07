# KMake — KCML Library Build Utility

> Build KCML libraries from source files using an XML build descriptor.

## Description

KMake is a build utility for assembling KCML libraries. It uses an XML build file to describe libraries, their source file components, and dependencies. It invokes the `kc6` compiler to assemble each library, using file timestamps to rebuild only what has changed.

## Usage with kconf.xml

The recommended way to use KMake is via `kconf.xml`. If a system called `XYZ` is defined:

```sh
kmake -b XYZ
```

### Required kconf.xml elements

| Element/Variable | Description |
|-----------------|-------------|
| `<kcmltype>6</kcmltype>` | Declares the library type (always 6 currently) |
| `BUILD` env var | Filename of the XML build file |
| `SOFTWARE` env var | Directory of source files (relative paths are relative to this) |
| `LIBRARIES` env var | Destination directory for built libraries |

## Build file format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<build>
    <flag name="KCML6Keywords"/>
    <flag name="KCML6Decoration"/>
    <flag name="SearchVars"/>
    <flag name="SearchModuleVars"/>
    <flag name="ReplaceModuleVars"/>
    <flag name="CodeAnywhere"/>

    <library name="Boot">
        <src file="PROGRAMS/GB/MAING.src"/>
    </library>

    <library name="Constants">
        <src file="PROGRAMS/GB/CONST.src"/>
        <src file="PROGRAMS/CG/CONST.src"/>
        <src file="PROGRAMS/GB/CNW32.src"/>
    </library>

    <library name="DataStructure">
        <src file="GENPROGS/GB/IRECS.src" altfile="PROGRAMS/GB/IRECS.src"/>
    </library>
</build>
```

- `<flag>` — compiler flags affecting all libraries
- `<library name="...">` — defines a library and its source components
- `<src file="...">` — source file component
- `altfile` — alternative source path if the primary is not found

Missing directories for libraries are created automatically.

## See Also

- `kc6` — library compiler invoked by KMake
- `compile` — compile individual programs
- `kconf` — Connection Manager configuration
