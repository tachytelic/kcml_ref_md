Libraries

Introduction

Libraries are a way of sharing common code libraries between instances of KCML. They replace the original [global partition](TutorialGlobal.htm) concept.

The KCML environment consists of a running program (called the forground) augmented by zero or more shared libraries containing functions or defining fields and constants. In KCML 6.x libraries are loaded dynamically with the [LIBRARY ADD](MODULE.htm) statement but you should keep in mind that on future versions of KCML libraries may be loaded automatically with the program that depends on them. Libraries exist as files containing executable p-code images and when loaded with LIBRARY ADD they are given a friendly name as in:


        LIBRARY ADD "CoreFunctions" = "../libraries/CoreFunctions.klib"

The library is mapped into the KCML programs address space making its public functions, constants and fields available to the program. The mapping is generally a read-only mapping though it is possible to use one particular library to share data.

There is no particular limit to the number of libraries a program may add. The order of loading is important as it determines the order in which the libraries are searched when resolving references to functions, constants or fields. An ordered list of the loaded libraries is shown in the functions browser window of the KCML workbench. The immediate mode statement [LIST M](LIST_M.htm) will also list out the currently loaded libraries in the search order.

Libraries will be unloaded by [CLEAR](CLEAR.htm) or [LOAD RUN](LOAD_RUN.htm) but they are unaffected by LOAD. A library may be unloaded with LIBRARY REMOVE or LIBRARY REMOVE ALL though this is not recommended as library variables are not destroyed.

<span id="encapsulation"></span>

Encapsulation

A major strength of libraries is based in their ability to encapsulate code for a component. A library can contain the functions that operate on its data and the data itself can be instantiated by defining it in [PUBLIC DIM](DIM.htm#scope) statements within the library. Variables defined this way are called **library variables** and they get created in the foreground programs with the special attribute of persisting across LOAD statments as if they were in common. Any initialization required can be performed by the library **constructor function** 'Constructor() which, if defined in the library, gets executed immediately after the library is loaded. Library variables created in the foreground by a LIBRARY ADD revert to being regular DIMed variables if the library is unloaded by LIBRARY REMOVE.

The only way code encapsulated in a library can be executed is through a DEFSUB call into the library. The variables used in these functions will generally be local variables. If globally scoped variables are referenced then they must have been declared in the foreground or copied there as library variables because they were COMed in the library. DIM is only used in a library to declare [constants](TutorialConstants.htm) or possibly fields though, in almost all cases, fields should be declared with DEFRECORD.

The **PRIVATE** keyword can be used with [DIM](DIM.htm), [DEFRECORD](DEFRECORD.htm) and [DEFSUB](DEFSUB.htm) to limit the visibility of constants, records, fields and functions to just the library that defines them. This is good practice and strongly recommended as it can prevent name clashes between libraries. To declare that an object should be exported the the **PUBLIC** qualifier should be used. If no PUBLIC or PRIVATE qualifier is used with DIM, DEFRECORD or DEFSUB then PUBLIC is assumed but it is again a good practice to explicitly declare scope by putting PUBLIC on functions, fields or constants that are to be exported outside the library. In a future version of KCML PRIVATE will be the default.

Creating a library

Libraries are created from source program files in batch mode using the [kc6](kc6.htm) compiler utility. If a library depends on another library for constant or field definitions then this needs to be specified to the compiler. For example:


        kc6 -o MyLib.klib -i BaseLib.klib myprog.src anotherprog.src

will build the MyLib library using constants and fields from the BaseLib library. The new library was build from the two components *myprog.src* and *anotherprog.src*. These components are loaded independently and can have overlapping line number ranges without affecting one another. They can also have independent constructor functions which will called in turn when the library is loaded.

The [kmake](kmake.htm) utility can be used to automate the build process when a number of libraries are involved and which have with complex interdependencies. This utility is driven by an XML file specifying the libraries to build, their components and their dependencies. It uses filesystem timestamps to determine if a library has to be rebuild because of a change in a supporting library.

Sharing data with a library

If a library defines @ variables, e.g. DIM @shared(10), it is marked as containing shared data. The first library to be loaded that is marked this way will be mapped read-write so that these variables can be modified. If you attempt to load more than one such shared data library then the variables of the second and later libraries will not be visible from the foreground program.
