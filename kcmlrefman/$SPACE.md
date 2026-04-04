\$SPACE

General Form:

\$SPACE

------------------------------------------------------------------------

The \$SPACE statement forces KCML to compact its dynamic memory heap and release as much memory as possible back to the operating system. The statement can be executed at any time however it will only be able to fully function if executed from the main line of a program and not from within a subroutine. Memory used for variables will not be examined if executed from a subroutine.

An implied \$SPACE is performed internally by KCML after a [LOAD](LOAD.htm) when there is maximum oportunity to reclaim unused memory.

You may wish to use this function explicitly, given the proviso about subroutines, if you have freed a large amount of user memory by setting array or string dimensions to zero with [REDIM](MAT_REDIM.htm).

See also:

[LIST SPACE](LIST_SPACE.htm)
