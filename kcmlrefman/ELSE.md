ELSE

------------------------------------------------------------------------

General Form:\
\
     : ELSE statement\
\
Where:\
\
     statement           = any KCML statement\
\

------------------------------------------------------------------------

The ELSE statement is used immediately after an [IF ... THEN](IFTHEN.htm), [ON ... GOSUB](ONGOSUB.htm), [ON ... SELECT](ONSELECT.htm) statement, to conditionally execute a successive statement if the condition from the previous statement is false. If the previous condition was true then execution continues with the statement after the ELSE statement, assuming that the previous condition did not cause a branch. The ELSE statement can be followed by a [DO group](DO.htm) to execute a group of statements if the condition in the previous [IF ... THEN](IFTHEN.htm) statement was false.

See also:

[IF ... THEN](IFTHEN.htm), [DO group](DO.htm), [ON ... GOSUB](ONGOSUB.htm), [ON ... SELECT](ONSELECT.htm)

 
