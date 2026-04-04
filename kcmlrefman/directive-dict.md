<div align="CENTER">

### Apache HTTP Server Version 1.3

</div>

# Terms Used to Describe Apache Directives

Each Apache configuration directive is described using a common format that looks like this:

<a href="#Syntax" rel="Help"><strong>Syntax:</strong></a> *directive-name* *some args*\
<a href="#Default" rel="Help"><strong>Default:</strong></a> *`directive-name default-value`*\
<a href="#Context" rel="Help"><strong>Context:</strong></a> *context-list*\
<a href="#Override" rel="Help"><strong>Override:</strong></a> *override*\
<a href="#Status" rel="Help"><strong>Status:</strong></a> *status*\
<a href="#Module" rel="Help"><strong>Module:</strong></a> *module-name*\
<a href="#Compatibility" rel="Help"><strong>Compatibility:</strong></a> *compatibility notes*

Each of the directive's attributes, complete with possible values where possible, are described in this document.

## Directive Terms

- [Syntax](#Syntax)
- [Default](#Default)
- [Context](#Context)
- [Override](#Override)
- [Status](#Status)
- [Module](#Module)
- [Compatibility](#Compatibility)

------------------------------------------------------------------------

## <span id="Syntax">Syntax</span>

This indicates the format of the directive as it would appear in a configuration file. This syntax is extremely directive-specific, so refer to the text of the directive's description for details.

------------------------------------------------------------------------

## <span id="Default">Default</span>

If the directive has a default value (*i.e.*, if you omit it from your configuration entirely, the Apache Web server will behave as though you set it to a particular value), it is described here. If there is no default value, this section should say "*None*".

------------------------------------------------------------------------

## <span id="Context">Context</span>

This indicates where in the server's configuration files the directive is legal. It's a comma-separated list of one or more of the following values:

**server config**  
This means that the directive may be used in the server configuration files (*e.g.*, `httpd.conf`, `srm.conf`, and `access.conf`), but **not** within any `<VirtualHost>` or \<Directory\> containers. It is not allowed in `.htaccess` files at all.

**virtual host**  
This context means that the directive may appear inside `<VirtualHost>` containers in the server configuration files.

**directory**  
A directive marked as being valid in this context may be used inside `<Directory>`, `<Location>`, and `<Files>` containers in the server configuration files, subject to the restrictions outlined in How Directory, Location and Files sections work.

**.htaccess**  
If a directive is valid in this context, it means that it can appear inside *per*-directory `.htaccess` files. It may not be processed, though depending upon the <a href="#Override" rel="Help">overrides</a> currently active.

The directive is *only* allowed within the designated context; if you try to use it elsewhere, you'll get a configuration error that will either prevent the server from handling requests in that context correctly, or will keep the server from operating at all -- *i.e.*, the server won't even start.

The valid locations for the directive are actually the result of a Boolean OR of all of the listed contexts. In other words, a directive that is marked as being valid in "`server config, .htaccess`" can be used in the `httpd.conf` file and in `.htaccess` files, but not within any \<Directory\> or \<VirtualHost\> containers.

------------------------------------------------------------------------

## <span id="Override">Override</span>

This directive attribute indicates which configuration override must be active in order for the directive to be processed when it appears in a `.htaccess` file. If the directive's <a href="#Context" rel="Help">context</a> doesn't permit it to appear in `.htaccess` files, this attribute should say "*Not applicable*".

Overrides are activated by the `AllowOverride` directive, and apply to a particular scope (such as a directory) and all descendants, unless further modified by other `AllowOverride` directives at lower levels. The documentation for that directive also lists the possible override names available.

------------------------------------------------------------------------

## <span id="Status">Status</span>

This indicates how tightly bound into the Apache Web server the directive is; in other words, you may need to recompile the server with an enhanced set of modules in order to gain access to the directive and its functionality. Possible values for this attribute are:

**Core**  
If a directive is listed as having "Core" status, that means it is part of the innermost portions of the Apache Web server, and is always available.

**Base**  
A directive labeled as having "Base" status is supported by one of the standard Apache modules which is compiled into the server by default, and is therefore normally available unless you've taken steps to remove the module from your configuration.

**Extension**  
A directive with "Extension" status is provided by one of the modules included with the Apache server kit, but the module isn't normally compiled into the server. To enable the directive and its functionality, you will need to change the server build configuration files and re-compile Apache.

**Experimental**  
"Experimental" status indicates that the directive is available as part of the Apache kit, but you're on your own if you try to use it. The directive is being documented for completeness, and is not necessarily supported. The module which provides the directive may or may not be compiled in by default; check the top of the page which describes the directive and its module to see if it remarks on the availability.

------------------------------------------------------------------------

## <span id="Module">Module</span>

This quite simply lists the name of the source module which defines the directive.

------------------------------------------------------------------------

## <span id="Compatibility">Compatibility</span>

If the directive wasn't part of the original Apache version 1 distribution, the version in which it was introduced should be listed here. If the directive has the same name as one from the NCSA HTTPd server, any inconsistencies in behaviour between the two should also be mentioned. Otherwise, this attribute should say "*No compatibility issues.*"

------------------------------------------------------------------------

### Apache HTTP Server Version 1.3
