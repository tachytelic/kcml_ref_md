KCML special file extensions

KCML recognizes some special file extensions viz

.asc

This was used in KCML2 to denote an ascii program. It is now considered obsolete but it is recognized for input files for the [compile](compile.htm) utility. Use .src instead.

.kcml

Starting with KCML 6.0 this extension is recognized for compiled KCML programs. Program files with this extension are displayed in the [Workbench File Browser](mk:@MSITStore:workbench.chm::/wbbrowsefiles.htm). On Windows this extension is automatically registered in the registry and the IIS3 ScriptMap so that KCML can be used for web server [CGI scripts](cgi.htm). See article on [scripting](script.htm).

.src

This denotes an ascii program file. It is specially recognized by LOAD when [\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 40 is set to load/save ascii and compiled programs together. Programs with this extension are listed in the [Workbench File Browser](mk:@MSITStore:workbench.chm::/wbbrowsefiles.htm) and can be saved using its save feature with the extension.
