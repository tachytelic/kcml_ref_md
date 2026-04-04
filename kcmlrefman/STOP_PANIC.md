STOP PANIC

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/stoppanic.gif" data-align="BOTTOM" data-border="0" alt="stoppanic.gif" />\
\

------------------------------------------------------------------------

The STOP PANIC ON statement is used to instruct KCML to consider all subsequent [STOP](STOP.htm) statements as [PANIC](PANIC.htm) statements. This avoids having to change existing code if you already used [STOP](STOP.htm) only in places where [PANIC](PANIC.htm) might be appropriate. The STOP PANIC OFF statement restores to the original meaning of [STOP](STOP.htm).

If the NOPROG environment variable is set and STOP PANIC is in force, subsequently entering immediate mode will cause a [PANIC](PANIC.htm) to occur.

See also:

[PANIC](PANIC.htm), [STOP](STOP.htm)
