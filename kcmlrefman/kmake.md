The KMake utility

KMake is a utlity program to build KCML libraries. It uses an XML based file to describe the libraries, the source file components for each library and the library dependencies. It then executes the [kc6 compiler](kc6.htm) to assemble each library from its source files.

KMake uses the file times of source files to determine whether a library needs rebuilding allowing a single source file to be changed, kmake executed and only the minimum rebuilding done.

Using kconf.xml

KMake can run using a simple build file, but is best run using kconf.xml as part of a system. If a system called XYZ is defined in kconf.xml, then the libraries may be built with

kmake -b XYZ

A number of elements and environment variables need to be defined in kconf.xml:

kcmltype

The service must indicate the type of libraries to be built, by adding the following element to that service (currently the kcmltype is always 6):

\<kcmltype\>6\</kcmltype\>

Environment variables

|  |  |
|----|----|
| BUILD | This defines the filename of the xml build file. |
| SOFTWARE | This defines the directory of source files. Where absolute filenames are not specified in the build file, they are relative to this directory. |
| LIBRARIES | This defines the destination for where libraries are built. Library names may include separator characters to place them in sub-directories. Where directories do not exist for libraries they are created automatically. |

The XML build file

A simple XML containing all the key elements is presented here:


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
        <library name="CoreFunctions">
            <usemodule name="Constants"/>
            <usemodule name="DataStructure"/>
            <usemodule name="Boot"/>
            <src file="PROGRAMS/GB/libGN.src"/>
            <src file="PROGRAMS/GB/libKI.src"/>
            <src file="PROGRAMS/GB/libKD.src"/>
            <src file="PROGRAMS/GB/libR8.src"/>
            <src file="PROGRAMS/GB/libSF.src"/>
            <src file="PROGRAMS/GB/libPR.src"/>
        </library>
        <library name="Administrator">
            <usemodule name="Constants"/>
            <usemodule name="CoreFunctions"/>
            <src file="PROGRAMS/GB/ADMIN.src"/>
            <src file="PROGRAMS/GB/libAD.src"/>
        </library>
        <program name="GB/INIT">
            <usemodule name="CoreFunctions"/>
            <src file="programs/GB/INIT.src"/>
        </program>
        <program name="GB/LDMOD">
            <usemodule name="CoreFunctions"/>
            <src file="programs/GB/LDMOD.src"/>
        </program>
        <program name="GB/MENU">
            <usemodule name="CoreFunctions"/>
            <usemodule name="Administrator"/>
            <usemodule name="CommercialGlobal"/>
            <src file="programs/GB/MENU.src"/>
        </program>
    </build>

Elements

<table data-frame="void">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="10%">Element</th>
<th width="50%">Description and attributes</th>
</tr>
</thead>
<tbody>
<tr>
<td>build</td>
<td>Always the root element</td>
</tr>
<tr>
<td>library</td>
<td>Define a library. The library may contain usemodule and src elements
<table width="100%">
<thead>
<tr>
<th width="10%">Attribute</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>name</td>
<td>Name of library. It must be a valid relative filename. The extension ".mod" is applied automatically.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>program</td>
<td>Define a program. May contain the same elements as a library. In KCML 6.10 program elements are ignored, but may be defined for use by future versions of KCML sharing a common build file.
<table width="100%">
<thead>
<tr>
<th width="10%">Attribute</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>name</td>
<td>Name of program. It must be a valid relative filename. The extension ".mod" is applied automatically.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>src</td>
<td>Specifies a KCML source file (either ascii or compiled) that is a component of this library or program.
<table width="100%">
<thead>
<tr>
<th width="10%">Attribute</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>file</td>
<td>Source file component. If a relative pathname is specified, then it is relative to the environment variable SOFTWARE.</td>
</tr>
<tr>
<td>altfile=</td>
<td>Optional. Alternative source file if the specified source file does not exist. Unless the -i option is specified it is an error if neither of these files exits.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>usemodule</td>
<td>Name a library that this program or library depends upon at the time of building. This must specify the name of a library within the build file. When kmake executes, it will always build a library's dependencies before building the library itself. The order of the libraries in the build file does not matter. KMake will fail if there are circular dependencies in the build file.
<table width="100%">
<thead>
<tr>
<th width="10%">Attribute</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>name</td>
<td>Library name. Will match the name attribute of a library element.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>flag</td>
<td>There are no flags in KCML6.10 and these flag elements are ignored. They may be specified to allow a common source file between KCML6.10 and future KCML systems.
<table width="100%">
<thead>
<tr>
<th width="10%">Attribute</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>name</td>
<td>Name the flag.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>modulegroup</td>
<td>Library groups allow for more complicated dependencies where two libraries depend on each other. This is not applicable to KCML6.10 but allows specification of grouping for future versions of KCML. Future versions will allow the generation of export information for each library in the group, followed by building each member of the group with access to the other group members' export information. Each member library has the same set of dependencies and so the usemodule element should be a direct child of the modulegroup element and not individual libraries. In KCML6.10 the modulegroup is ignored and each member library is built individually, using the usemodule information for the modulegroup to specify its dependencies. This allows systems using future versions of KCML to share the same build file as one using KCML6.10.
<table width="100%">
<thead>
<tr>
<th width="10%">Attribute</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>name</td>
<td>Name the modulegroup. No files are created using this name.</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

KMake flags

These may be listed with kmake -?

<table data-frame="VOID">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Option</th>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>-a</td>
<td> </td>
<td>Build all. All targets in the system are rebuilt, regardless of file times.</td>
</tr>
<tr>
<td>-b</td>
<td>system</td>
<td>Build system. Build using the specified system from kconf.xml. It is recommended that this method is used.</td>
</tr>
<tr>
<td>-i</td>
<td> </td>
<td>Ignore missing source files rather than error. If this option is specified, then even where neither the file= or optional altfile= exists then no error will be generated. The library is built using the other files that do exist. If no components exist then the library is not built.</td>
</tr>
<tr>
<td>-k</td>
<td> </td>
<td>Continue after errors. Normally kmake stops at an error. This option allows it to continue as far as possible, building libraries that do not depend on other libraries that have failed to build.</td>
</tr>
<tr>
<td>-n</td>
<td> </td>
<td>Rebuild all targets. Given one or more named targets, this file builds the given targets having built all target dependencies regardless of filetime</td>
</tr>
<tr>
<td>-q</td>
<td> </td>
<td>Build using temporary files. This allows the building of libraries while some library files are currently in use. Without this option the build would normally fail because of the files being in use. Using this option, libraries are built to temporary files and then moved over the library file in an operating-system specific manner to avoid this error.<br />
<br />
<strong>NB</strong> This option is not recommended. An existing process may end up using previous and new libraries as an inconsistent set leading to random and unpredictable problems. It is intended for use where background processes need to continue executing and are known never to load extra libraries after they have started.</td>
</tr>
<tr>
<td>-t</td>
<td>target</td>
<td>Build targets. This option may be specified many times. If no targets are specified on the commmand-line then all libraries and programs are built. If targets are specified then only these libraries (and any libraries they depend on) are built. This allows for faster build times during the software development process.</td>
</tr>
</tbody>
</table>
