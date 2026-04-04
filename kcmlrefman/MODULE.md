LIBRARY

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

LIBRARY ADD strexpr1 = strexpr2\
LIBRARY REMOVE strexpr1\
LIBRARY REMOVE ALL

</div>

Where:

<div class="indent">

strexpr1 = a string expression naming the module\
strexpr2 = a string expression representing the module filename

</div>

</div>

------------------------------------------------------------------------

The LIBRARY statement allows the mapping in and out of shared KCML libraries, commonly called [globals](TutorialModules.htm). It is a generalization of the original [SELECT @PART](SELECT_@PART.htm) process global in the following ways

- more than one global can be available at any time
- the shared text is read directly from a memory mapped file so no dedicated shared memory partition is required
- libraries can be added and dropped at any time

LIBRARY ADD is used to add a new library onto the end of the list of current libraries. This list is presumed to start with the original foreground program which can be considered as the main library module. A library is named with a name which can later be used in a LIBRARY REMOVE to unload the library. The second string expression is the name of the file containing the library image. This must have been previous created either with the [kc6](kc6.htm) compiler or in immediate mode with a [SAVE](SAVE.htm) \<G\> statement on a system running the same type of KCML.

Once loaded with a LIBRARY ADD, a library stays mapped into memory until explicitly dropped with a LIBRARY REMOVE or until a CLEAR. In particular they are preserved across a LOAD or a CLEAR P. All the currently loaded libraries can be dropped by LIBRARY REMOVE ALL.

When searching for a [DEFSUB'](DEFSUB.htm) routine, KCML will look first in the currently executing library (which may be the foreground). If not found there it will search the library list from the start looking for the routine. Remember the foreground process is considered to be the first library in the list so routines placed in the foreground can override secondary library routines.

Libraries can also be used to hold definitions of [fields](TutorialFields.htm) and [constants](TutorialConstants.htm) to be looked up using the same algorithm.

Certain variables declared in the library using the [PUBLIC DIM](DIM.htm#scope) statement will be copied to the foreground symbol table when the library is loaded and marked as persistent so they do not get dropped after a program LOAD. Such variables are called **library variables** and they can be numerics, strings or objects. Fields, records and constants are not considered as library variables and are looked up only when referenced. If the library is later unloaded its library variables revert to being normal foreground symbols and they may well be dropped from the program on the next LOAD.

Variables declared as [PRIVATE DIM](DIM.htm#scope) are not visible from outside the library.

A library can have a **constructor** function with the special reserved name of '\_Constructor() which will be automatically invoked by LIBRARY ADD in order to perform any initialization required by the libraries.

Libraries can be comprised of more than one program and compiled together using the [kmake](kmake.htm) utility which will only rebuild a library if one of its components is out of date. The component programs can have their own line number spaces. Each program can have their own constructor function and the compiler will arrange for each to be called in turn when the library is loaded. The make system is driven by a XMLbuild file that enumerates the libraries and their components.

Libraries are generally mapped in as read-only memory to facilitate sharing. An exception is the first global which will be mapped in as read-write if and only if KCML spotted a DIM or COM of an @ variable at the time it was SAVEd. Thus only the first global will support shared data.

Libraries have hardware dependencies on byte ordering, word size and and alignment and while they can be exchanged between similar platforms, e.g. Linux and Unixware, or NT and Windows 95, they are not generally interopable.

Compatibility

The LIBRARY statement was originally called MODULE and was renamed in KCML 6.20. Both keyworks are acceptible but KCML will always use LIBRARY when recreating program source

The MODULE statement was introduced in KCML 6.0 and is supported on both Unix and NT. It is an interim stage and will be replaced by a new implementation in the next major release of KCML. This next implementation will withdraw access to the variables of a global. All access will be through subroutine calls. You should start now on the assumption that you cannot change foreground variables using a function in a global. Make all variables in the library local if possible.

Library variables and constructors were introduced in KCML 6.10.

Optional PRIVATE and PUBLIC keywords for [DEFSUB](DEFSUB.htm) limiting visibility outside of a library were introduced in KCML 6.10.

Library variables in KCML 6.10 were defined with COM but this has been superseded by PUBLIC DIM. COM is still allowed in a library in 6.20 but it will raise an error in future versions of KCML.

Syntax examples:

LIBRARY ADD "MK/libGb" = "./PROGS/MK/libGb"\
LIBRARY REMOVE "MK/libGb"\
LIBRARY REMOVE ENV("LIBRARY")\

See also:

[SELECT @PART](SELECT_@PART.htm), [LIST M](LIST_M.htm)\
[Tutorial on libraries](TutorialModules.htm)
