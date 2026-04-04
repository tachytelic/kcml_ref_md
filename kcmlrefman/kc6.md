The kc6 compiler

The kc6 utility is normally executed by [KMake](kmake.htm), so is not fully documented here. The purpose of kc6 is to take the source file components and combine them into a generated library, as produced by the KCML [SAVE](SAVE.htm) \<G\> method. The kc6 executable loads the KCML interpreter from the shared library *kserver.dll* (NT), *kserver.sl* (HP-UX) or *kserver.so*.

Usage


    kc6 [-s] [-v] -o library [-i import] prog1 [prog2 ...]

Note that there must be at least one component program specified.  A status report is written to standard output.  Any fatal errors are reported to standard error and an [exit code](#ExitCodes) is set.

Switches

| Switch | Purpose |
|----|----|
| -s | Operate silently, otherwise it will emit progess reports to standard output as it loads each component |
| -v | Print version number to standard output and terminate |
| -o library | This is a required switch that specifies the filename of the library to be created. |
| -i import | Specify another library that this library depends upon. The library must already exist and will be loaded before the library is resolved and saved thus allowing constants and fields to be given their correct values. This switch is optional and there can be more than one instance in which case the imported libraries will be loaded in the order specified. A list of these libraries is saved in the header of the new library. |
| -? | Produce a usage message on standard output |

Notes

Line numbers

Each source file has its own line number space. This means that the combined library does not need to be renumbered and the line numbers appearing in the library match those in the original source file. The target line of a GOTO must exist in that source file and it is irrelevant if this same line number also appears in other source files.

Source file information

Information about the source file components is embedded in the library. It is possible from the Workbench to determine the source file for the line of the cursor in a library and with a single keystroke load the appropriate source file into the foreground with the cursor at the same place.

Constructors

Library constructors are created. None, any or all source files may have a subroutine called **'Constructor**. In the generated library, each of these is renamed and a new 'Constructor is created for the entire library with calls to each component constructor. When the [LIBRARY ADD](MODULE.htm) statement is used in kcml, the 'Constructor function is called automatically, allowing library specific initialization to be called.

Assumptions made

- All libraries are created with [\$COMPLIANCE 1]($COMPLIANCE.htm).
- All ascii source files are loaded using [text source](NEWASCII.htm) conventions.
- All numeric variables starting with a leading underscore are assumed to be [constants](TutorialConstants.htm) and the dependent libraries will also be searched to find a definition. Similarly, [fields](TutorialFields.htm) are searched in the dependent libraries.

<span id="ExitCodes"></span>Exit codes

If kc6 encounters an error situation it will terminate setting its exit code to one of the following:

|     |                                                             |
|-----|-------------------------------------------------------------|
| 0   | Success                                                     |
| 1   | Reserved                                                    |
| 2   | Bad command line argument                                   |
| 3   | Unable to load a component source file                      |
| 4   | Missing -o flag to specify the output library               |
| 5   | An error occurred importing libraries or merging components |
| 6   | An error occurred writing the library                       |
| 7   | An error occurred opening the output file                   |

More details about any error can be found from the error message written to standard error and the context can be found from the status report sent to standard output.
