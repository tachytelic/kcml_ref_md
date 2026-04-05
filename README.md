# KCML Reference Documentation

This repository contains the reference documentation for **KCML** (Kerridge Computer Macro Language), a powerful multi-platform programming language descended from Wang BASIC-2.

## What is KCML?

KCML is an incremental compiler that combines the best features of compiled and interpreted languages. Originally developed by Kerridge Computer Company in 1985 to succeed the Wang 2200 BASIC-2 system, KCML has evolved through four generations into a modern Rapid Application Development (RAD) environment.

### Key Features

- **Cross-platform compatibility** - Programs and data files work unchanged across Windows, AIX, HP-UX, Solaris, Digital Unix, and more
- **Multi-user support** - True multi-user capabilities with automatic file/record locking and unique terminal numbering
- **Built-in database** - Integrated relational database with B-tree indexing, supporting both SQL and direct ISAM operations
- **Client-server architecture** - Designed for wide area networks and Internet connectivity
- **GUI and text applications** - Supports both modern forms-based interfaces and traditional text terminals

### History

- **1985** - Development began; first version written in C on Motorola 68000/XENIX
- **Late 1980s** - Second generation released with improved Wang compatibility
- **1991** - Third generation introduced DOS version, Windows terminal emulator
- **Present** - Fourth generation provides full RAD environment with integrated editor, debugger, and forms designer

## Documentation Structure

| Folder | Description |
|--------|-------------|
| [kcmlrefman/](kcmlrefman/) | **Language Reference Manual** - Core language statements, functions, operators, tutorials, and platform-specific information |
| [kclient/](kclient/) | **KCML Client** - Windows client application for connecting to KCML servers (forms and text display) |
| [kcmlforms/](kcmlforms/) | **Forms Designer** - GUI forms creation and management documentation |
| [kdb/](kdb/) | **Kerridge Database** - Built-in relational database, SQL reference, and data management utilities |
| [kwebserv/](kwebserv/) | **Web Server** - KCML web server configuration, authentication, and web services |
| [workbench/](workbench/) | **Workbench IDE** - Integrated development environment with editor, debugger, and program management |

## Language Reference Highlights

The language reference includes:

- **100+ statements and functions** - PRINT, INPUT, DIM, FOR/NEXT, WHILE, SELECT, and more
- **Matrix operations** - Built-in matrix arithmetic (MAT ADD, MAT INV, MAT TRN, etc.)
- **String handling** - Comprehensive string manipulation functions
- **File I/O** - Sequential and random access file operations
- **Error handling** - TRY/THROW/TRAP exception handling
- **COM/OLE automation** - Windows component integration
- **XML support** - DOM and SAX parsing capabilities
- **SOAP/CORBA** - Enterprise integration support

## Related Products

- **Kclient** - Freely distributable Windows client for displaying forms and text windows
- **Kprint** - Distributed printing system for rich document output over WANs
- **KMail** - Windows-based mail client for UNIX hosts

## Target Audience

KCML is used by 80,000+ end users worldwide for:
- General accounting and inventory management
- Vehicle dealership management systems
- Distribution and logistics
- Hotel management
- Travel booking and reservations
- And many other commercial applications

## KCML Code Execution Server

The `kcml_executor/` folder contains a Python-based execution server that allows Claude to write and test KCML code:

- **server.py** - HTTP server for remote KCML execution
- **mcp_server.py** - MCP protocol server for direct Claude integration

See [kcml_executor/README.md](kcml_executor/README.md) for deployment instructions.

## Origin

This documentation was converted from the original KCML HTML help files to Markdown format for improved accessibility and version control.

## License

Please refer to Kerridge Commercial Systems for licensing information regarding KCML software and documentation.
