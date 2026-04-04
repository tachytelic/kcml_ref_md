The text program format is a new source format for program files that supports conditional loading of code. To load source programs using the new rules, set byte 46 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE46) to HEX(05) or set the OPTIONS_RUN_46 [environment variable](EnvVars.htm#options_run). The characteristics of this new format are:

- One statement per line presumed.
- Colons are now optional and needed only if there are multiple statements per line.
- Line numbers are optional. KCML will auto-number.
- Support for conditional loading.
- First check for file with a .src extension before loading the file as specified (except in \$COMPILE).

The text form of [SAVE](SAVE.htm) and [SAVE ASCII](SAVE_ASCII.htm) continue to generate colons and line numbers for backward compatibility and to avoid gratuitous source control deltas. However files are always saved as source with a .src extension in this mode either by the workbench [Save/Save As](mk:@MSITStore:workbench.chm::/saveprog.htm) options or by a SAVE statement. This presumes that [\$COMPILE]($COMPILE.htm) will be used to produce binary version of programs for deployment. If so enabled, \$COMPILE will accept the new format when loading programs to be compiled but it does not apply the convention for appending a .src extension when loading as it is controlled by it's own [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE40) byte 40.

Developing using source programs

KCML developers are strongly urged to use this feature and to keep all the programs in text format during the development. The programs should be stored in directories as separate files using the .src extension to identify the programs as being in source format.

For deployment the programs should be compiled using \$COMPILE or kcml -c. Libraries should be compiled with [kmake](kmake.htm). At this time any translation can be applied and the compiled programs may be encrypted.

Keeping programs in source format during development incurs only a magininal performance overhead during a LOAD. On the other hand a source format makes the use of [source control](mk:@MSITStore:workbench.chm::/cvs.htm) possible and allows text processing tools like sed, grep or UltraEdit to be applied to the programs.

Conditional loading

Conditional loading is done using \#if, \#ifver, \#ifdef, \#ifndef, \#else and \#endif operators in the code. Code that is conditionally compiled out has no effect on the execution and will appear greyed out in the workbench and cannot be edited. For example:


      REM
      #ifdef CUSTOMER_A
      'SpecialCall()
      #else
      'NormalCall()
      #endif

If the conditional value CUSTOMER_A is defined then function 'SpecialCall() will be called. If not, then function 'NormalCall() will be called. The \#ifdef, \#ifndef, \#else and \#endif only affect loading. The \#ifdef, \#ifndef, \#else, \#endif and the code excluded all behave exactly like REM statements. This means that excluded code does not need to be syntactically correct or can use features only supported in later versions of KCML.

Conditional values are currently defined using environment variables. They are TRUE if and only if the environment variable exists and is empty string, the string "TRUE" or the string "1". Otherwise they are FALSE.

\#ifdef X is used to include code wanted if X is defined. \#ifndef has the opposite logic and will include code only if X is not defined. \#else is optional. All \#ifdef or \#ifndef must be ended by a closing \#endif. They may also be nested.

You can test against a string for a particular value with \#if as in


      REM
      #if ACCOUNTS_SUPPORT == "GAAP"
      'SetExtraOpts(1);
      #else
      #if ACCOUNTS_SUPPORT == "LATIN"
      'SetExtraOpts(2);
      #endif
      #endif

Finally you can conditionally load code depending on a minimum version number of the KCML used to compile it as in


    #ifver 6.2
    PRIVATE DEFRECORD r
       FLD f1$32
    END RECORD
    #else
    DIM .f1$ = (1,32), ...
    #endif

The version number is a minimum version so in the example the record version would also be compiled for KCML 7.0. Only one significant digit in the minor version is considered thus 6.11 and 6.10 are both considered as 6.1.

Conditional loading and the KCML Workbench

It is important to understand that the conditions are applied only as the text format program is being compiled in a LOAD or a \$COMPILE. The conditions are not applied (at least not at this time) by the KCML Workbench as programs are being edited. To make this clear the Workbench editor will flag any conditional operators entered into a program with an A08.40 error leaving the line colored as if in error. Any statements inside the conditional block will be compiled into the program whatever the condition. However if the program is saved in text format and later loaded then the conditions will be applied and code generated as appropriate.

Compatibility

This format was introduced in KCML 6.10. To enable it in this version byte 46 of \$OPTIONS RUN must be set to HEX(05).
