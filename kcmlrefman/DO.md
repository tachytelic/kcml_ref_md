DO group

------------------------------------------------------------------------

General Form:\
\
     DO \[statement\] ... ENDDO\
\
Where:\
\
     statement           = a group of KCML statements\
\

------------------------------------------------------------------------

A do group is a set of statements which is to be treated as a single statement in [IF THEN](IFTHEN.htm), [ELSE](ELSE.htm) and [ERROR](ERROR.htm) statements. Do groups may themselves contain other do groups up to a depth of over 50. The KCML editor will automatically indent do groups to highlight the complete structure. Each DO is paired with its corresponding ENDDO at resolve time. A do group may extend over more than one line. Jumping into a DO group is allowed but it is a very bad programming practice.

Example:

OPEN \#stream, "MainFile","r+"\
ERROR DO\
     'DisplayError()\
     'Prompt()\
END DO

See also:

[IF ... THEN](IFTHEN.htm), [ELSE](ELSE.htm), [ERROR](ERROR.htm)

 
