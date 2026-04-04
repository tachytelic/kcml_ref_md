Wyse 60,65,99,120,160,325

KTERM=wy*nn*

These are common terminals supporting many emulation’s. All Wyse terminals upward and including the Wyse 60 (except for the Wyse75 and the Wyse 370) are supported by the default *TERMINFO*, although *TERMINFO* itself only has entries for Wyse60, 99, 120, 160 and 325. If your terminal is not one of these then set it in its highest Wyse mode, and configure it in UNIX as a Wyse 160 (wy160). Alternatively add the terminal to the *TERMINFO* file by modifying the section that defines the Wyse 60, Wyse 160 etc. The line to change will be similar to the following:

\[wy60\|wy99\|wy120\|wy160\]

This line instructs the *TERMINFO* compiler [tik](tik.htm) to compile the following source section into the file TERMINFO/wy60 and create UNIX links to the files TERMINFO/wy99, TERMINFO/wy120 etc. To add another Wyse terminal to this line, for example the Wyse 325, which by default is already there, change the line to the following:

\[wy60\|wy99\|wy120\|wy160\|wy325\]

These differ from the cheaper Wyse 30 and Wyse 50 terminals in that they have a soft font capability that **KCML** can exploit to give box graphics (see [Wyse60 with boxes](TextTermWy60box.htm)). It is also available with a 16 key keyboard as well as an industry standard AT keyboard.

Because these terminals generally have no bright attribute but have a dim capability, the standard *TERMINFO* uses dim for normal text and normal for bright text. This may require a slight adjustment of the brightness controls. Alternatively the TERMINFO section for Wyse terminals contains two pairs of *AttribOn* and *AttribOff* sequences one of which is disabled with comment characters. Simply uncomment the required pair and comment out the previous definition as required, remembering to re-compile the database with the *tik* utility.

The default *TERMINFO* for these terminals assume that a full 16 function key keyboard is being used. It will need to be modified for the 12 function key AT keyboard if you wish to access SF12 to SF15 and SF28 to SF31.
