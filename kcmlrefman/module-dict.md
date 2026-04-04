<div align="CENTER">

### Apache HTTP Server Version 1.3

</div>

# Terms Used to Describe Apache Modules

Each Apache module is described using a common format that looks like this:

<a href="#Status" rel="Help"><strong>Status:</strong></a> *status*\
<a href="#SourceFile" rel="Help"><strong>Source File:</strong></a> *source-file*\
<a href="#ModuleIdentifier" rel="Help"><strong>Module Identifier:</strong></a> *module-identifier*\
<a href="#Compatibility" rel="Help"><strong>Compatibility:</strong></a> *compatibility notes*

Each of the attributes, complete with values where possible, are described in this document.

## Module Terms

- [Status](#Status)
- [Source File](#SourceFile)
- [Module Identifier](#ModuleIdentifier)
- [Compatibility](#Compatibility)

------------------------------------------------------------------------

## <span id="Status">Status</span>

This indicates how tightly bound into the Apache Web server the module is; in other words, you may need to recompile the server in order to gain access to the module and its functionality. Possible values for this attribute are:

**Base**  
A module labeled as having "Base" status is compiled and loaded into the server by default, and is therefore normally available unless you have taken steps to remove the module from your configuration.

**Extension**  
A module with "Extension" status is not normally compiled and loaded into the server. To enable the module and its functionality, you may need to change the server build configuration files and re-compile Apache.

**Experimental**  
"Experimental" status indicates that the module is available as part of the Apache kit, but you are on your own if you try to use it. The module is being documented for completeness, and is not necessarily supported.

**External**  
Modules which are not included with the base Apache distribution ("third-party modules") may use the "External" status. We are not responsible, nor do we support such modules.

------------------------------------------------------------------------

## <span id="SourceFile">Source File</span>

This quite simply lists the name of the source file which contains the code for the module. This is also the name used by the `<IfModule>` directive.

------------------------------------------------------------------------

## <span id="ModuleIdentifier">Module Identifier</span>

This is a string which identifies the module for use in the `LoadModule` directive when dynamically loading modules. In particular, it is the name of the external variable of type module in the source file.

------------------------------------------------------------------------

## <span id="Compatibility">Compatibility</span>

If the module was not part of the original Apache version 1 distribution, the version in which it was introduced should be listed here.

------------------------------------------------------------------------

### Apache HTTP Server Version 1.3
