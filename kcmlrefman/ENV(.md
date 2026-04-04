ENV(

------------------------------------------------------------------------

<div class="Generalform">

General Form:

> ENV(alpha_expression)

</div>

------------------------------------------------------------------------

The ENV( function sets the contents of a native operating system [environment variable](EnvVars.htm). This function is particularly useful for passing parameters to child processes created with either [SHELL](SHELL.htm), [\$RELEASE]($RELEASE.htm) and [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm).

ENV( can also be used as a function returning the current contents of an environment variable. In this case if the requested variable has not been defined then spaces are returned. ENV( is valid wherever an alpha expression is legal.

The [LIST E](LIST_E.htm) statement displays a list of environment variables which have been locally modified.

To unset an environment variable set it to spaces. This reverts it to its original value if it was inherited from the KCML tasks parent.

From KCML 6.20 onwards the following environment variables are read only:

- LOGIN
- LOGNAME
- KCMLDIR
- SYSTEMID
- TERMFILE

Any attempt to set the variables will be ignored.

Examples:

In this example the contents of the Unix environment variable TERM will be stored into the alpha receiver terminal\$:

terminal\$ = ENV("TERM")

Compatibility:

In KCML 5.0 and later versions, setting an environment variable with ENV() will put that variable into the environment that is inherited by child processes. If you do not wish to do this in oder to be compatible with earlier verions of KCML then then set byte 39 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE39) to HEX(00).

Syntax example:

ENV("PROG") = new\$

See also:

[LIST E](LIST_E.htm)
