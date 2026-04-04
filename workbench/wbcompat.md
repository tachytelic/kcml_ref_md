## Compatibility

The workbench is only available if you have a KCML6.00 or later client and server. In this combination the new workbench editor is the default, otherwise behaviour is much as before. The old editor can be re-enabled by checking the *Disable Workbench* checkbox in the connection properties or by using the -z flag on the kclient command line.

Very little functionality has disappeared with respect to the KCML4 full screen editor though some functions are now available though a different mechanism.

- Right double clicking in the editor to evaluate or to goto no longer has an effect because a single right click now brings up a popup menu. The functionality of the right double click in the old editor should always be available on this menu.
- The F2 status bar has moved to a combo box on the right hand side of the toolbar. The dropdown for this keeps a history of previous expressions or commands to facilitate recall. Error messages which used to appear on this status bar before now appear on a status line below the main workbench menu.

### Backward compatibility with KCML4 and earlier

The Workbench can be used to develop programs to run on earlier versions of KCML provided some compatibility constraints are understood.

The **COMPAT40**, **COMPAT32**, **COMPAT31** and **COMPAT30** environment variables can be used to warn about potential compatibility problems with the 4.0, 32., 3.1 or 3.0 versions when a program is saved. You should set one of these environment variables (use the lowest) if you are intending to develop for earlier KCML runtimes. Then when programs are SAVEd KCML will warn about any statements that will not be allowed in the earlier runtime.

The restriction of 1900 characters per line which was enforced in KCML 3.2 no longer applies in the Workbench though it is still imposed by the line oriented editor on the console window. This limit was imposed by the original editor rather than the KCML interpreter itself. In fact you could have an entire program consisting on several hundred statements all written with only one line number but this may however cause problems when taking code back to be edited by older KCML versions. The new editor will not enforce this 1900 character limit even if the COMPAT32 environment variable is set however **kat**, see below, can be used to check and warn of lines longer than 1900 characters.

The [kat](mk:@MSITStore:kcmlrefman.chm::/kat.htm) utility has new switches that can be used to check for compliance with earlier versions of KCML. This can be used to check whole directories in one go. It also checks line length. For example


    kat -r 32 progname

will check the file *progname* for compliance with version 3.22.09 KCML. The -r 31 switch checks for compliance with 3.10.12 and -r 30 for compliance with 3.00.18.
