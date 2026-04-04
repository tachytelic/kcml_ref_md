& (Concatenation) operator

------------------------------------------------------------------------

<div class="Generalform">

General Form:\
\

<div class="indent">

alpha_receiver = \[alpha_operand\] & alpha_operand ...

</div>

</div>

\

------------------------------------------------------------------------

The concatenation alpha operator combines the contents of the first alpha operand with the contents of the second alpha operand, without intervening characters. The combined strings are then assigned to the receiver variable. The concatenation alpha operator can only be used in alpha expression portion of an alpha assignment statement.

Blank spaces are ignored if they appear at the end of a variable, however if a variable is initialised to contain only spaces only one space is actually used. For example:

test\$ = "A"\
sample1\$ = sample1\$ & test\$

If sample1\$ contained only spaces, then sample1\$ would be set to a space followed by the letter \`A'. Note the above example is the same as:

sample1\$ = & test\$

Several concatenation operators can be used in one statement. They can also be mixed with other alpha operators such as [AND](AND.htm) in the same alpha expression. Multiple receivers are not allowed on the left of the shorthand =&.

Special cases:

Concatenated strings can be used as arguments to a function e.g.

'update(prefix\$ & suffix\$)

and also in strings returned from a string function as in

DEFSUB 'tagit(tag\$)\
RETURN = "\<" & tag\$ & "\>"\
END SUB

Syntax examples:

map\$ = page\$ & chapter\$(1) AND HEX(4F)\
name\$ = & new\$
