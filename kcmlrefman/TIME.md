TIME function

------------------------------------------------------------------------

General Form:\

TIME

------------------------------------------------------------------------

The TIME alpha function returns the current system time as supplied by the operating system. This will be in [local time](timezone.htm), not GMT. The time is returned with two characters each for the hours, minutes, seconds and centiseconds "HHMMSScc" though the accuracy of this time depends on the operating system and in the worst case it may only be accurate to a second.

The TIME function is valid wherever an alpha expression is legal.

Syntax examples:

current\$ = TIME\
stamp\$ = DATE & TIME

See also:

[DATE](DATE.htm), [\$TIME]($TIME.htm), [\#TIME](_TIME.htm)
