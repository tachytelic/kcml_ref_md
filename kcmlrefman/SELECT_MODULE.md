SELECT LIBRARY

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\
1.      SELECT LIBRARY \[strexpr\]\
\
Where:\
\

<div class="indent">

strexpr = a string expression naming the library.\

</div>

</div>

------------------------------------------------------------------------

Selects a library for use in the [@LIST](LIST.htm) statements. The specified library name will be used for all future @LIST statements, the selected library is also set when a library is loaded. If you don't specify the optional library name then it will revert to selecting the traditional @ global.

Example:

SELECT LIBRARY\
SELECT LIBRARY "MyLib"

See also:

[Libraries](MODULE.htm)\
[List](LIST.htm)
