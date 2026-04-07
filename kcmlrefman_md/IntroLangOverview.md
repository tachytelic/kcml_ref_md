# KCML Language Overview

> KCML is an incremental-compiler language that combines the portability of an interpreter with the performance of a compiled language, providing more than a hundred built-in statements and functions for business application development.

## Overview

KCML is an **incremental compiler**: each line of a program is compiled into an efficient internal form as it is entered, yet KCML can reconstruct the original source at any time to allow editing. This gives you the fast execution of a compiled language and the interactive flexibility of an interpreted one.

The language ships with over a hundred built-in statements and functions. Tasks that require significant effort in other languages — sorting, string searching, matrix arithmetic — are handled by single KCML statements.

## Runtime and Development

KCML makes no distinction between a runtime and a development version. Both are present in a single installation. Developers can selectively disable development features (the interactive editor, debugger, etc.) by setting flag bytes inside `$OPTIONS`, hiding those capabilities from end users without needing a separate runtime package.

## Multi-User Features

KCML is a true multi-user language regardless of platform:

- Each KCML process has a unique terminal number.
- File and record locking is maintained automatically within the built-in KISAM database.
- Explicit lock statements are available for external files and devices.
- In client/server configurations, shared business logic can be made available to all KCML processes running on the server via the global partition mechanism.

## Compatibility and Portability

Programs and data files written on any KCML-supported platform can generally run unchanged on any other. KCML runs on Unix variants (AIX, HP-UX, Solaris, SCO UnixWare, Digital Unix), Windows (NT, 95, 98), and DOS. Developing on a Windows laptop and deploying to a Unix server is a normal workflow.

## BASIC-2 Compatibility

KCML was designed to preserve the best features of the Wang 2200 BASIC-2 environment. It remains essentially fully compatible with all BASIC-2 releases through version 3.4, including the global partition multi-user model. It also maintained compatibility with the BASIC-2C (NPL) dialect up to release 3.2, though recent NPL versions have diverged enough that future compatibility is not a goal.

## Compatibility Across KCML Versions

Upgrade tools are provided to help move from older KCML generations to the current version. Backward compatibility between KCML versions has always been a design commitment.

## Notes

- The incremental compilation model means syntax errors are reported line-by-line as code is entered, rather than at build time.
- The ability to reconstruct source from the compiled internal form is what makes the Workbench editor possible.
- The `$OPTIONS` system variable controls many language and security features; consult the `$OPTIONS` reference for details.
