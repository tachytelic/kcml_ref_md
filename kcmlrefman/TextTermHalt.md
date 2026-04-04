HALT and RESET keys

The HALT key is used to interrupt a running program and force it into the [KCML debugger](mk:@MSITStore:workbench.chm::/Debug_mode.htm). If the program was blocked waiting for input then it might be necessary to press some key to satisy the input request before the program will actually halt.

RESET is a more drastic way of halting a program. Unlike HALT it is not possible to continue execution after a RESET. RESET will interrupt programs blocked reading from devices or blocked on a lock. HALT, on the other hand, will generally expect the operation to complete before it stops the program.

When using WKCML, Kclient or when using the WDW32 terminal emulator in its extended KCML mode, the HALT and RESET keys are set to CTRL+BREAK and CTRL+ALT+BREAK respectively and cannot be changed.

HALT and RESET are disabled if programming is disabled and the keys can be separately disabled using bytes 13 and 12 respectively in [\$OPTIONS]($OPTIONS.htm#BYTE12).

Text mode terminals

If you use a text mode terminal such as a VT100 with the client server version of KCML on NT then HALT is fixed as CTRL-C and RESET is fixed as CTRL-\\

In UNIX versions of KCML the HALT and RESET keys are not defined with the *TERMINFO* mechanism but are mapped onto the UNIX interrupt and quit keys. These keys are defined with the UNIX *stty* command which should be placed in the users *.profile* so that it is executed when they log on. For instance to define HALT as CTRL-C and RESET as CTRL-R use the UNIX *stty* command thus

stty intr '^c' quit '^r'

The caret notation is used for CTRL keys.

Several other control assignments may be defined with the *stty* command but generally they should be disabled to prevent problems. One example is the *susp* parameter which suspends the current foreground task.

A full list of the *stty* control assignments currently set for a particular terminal can be found with the *stty -a* command:

\$ stty -a speed 9600 baud; intr = ^y; quit = ^r; erase = ^h; kill = ^u; eof = ^d; eol = \<undef\>; eol2 = \<undef\>; swtch = \<undef\>; start = ^q; stop = ^s; susp = ^z; dsusp = \<undef\>; rprnt = ^r; flush = ^o; werase = ^w; lnext = ^v; -parenb -parodd cs8 -cstopb hupcl cread -clocal -loblk -parext -ignbrk brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl -iuclc ixon -ixany -ixoff imaxbel isig icanon -xcase echo echoe echok -echonl -noflsh-tostop -echoctl -echoprt -echoke -defecho -flusho -pendin -iexten opost -olcuc onlcr -ocrnl -onocr -onlret -ofill -ofdel tab3

The output from the *stty* command will vary considerably from machine to machine, the above example was taken from UNIX 5.4 system. The first line and the last eight lines determine the general configuration of the port, i.e. the line speed and parity etc. The other five lines are the *stty* control assignments. The only two that effect KCML are the *intr* and *quit* keys which change the HALT and RESET keys respectively. The *erase* and *eof* keys should be left unchanged as they specify the keys that are to be used as BACKSPACE and EOF which are useful when working within the UNIX shell. The rest can be disabled by setting them to \`^-' as follows:

stty kill '^-' swtch '^-' start '^-' stop '^-' stty susp '^-' dsusp '^-' rprnt '^-' flush '^-' stty werase '^-' lnext '^-'

The next time that you enter the *stty -a* command all of the above options would then be listed as \`\<UNDEF\>'. The above lines should be entered into the users *.profile* to disable these keys on all terminals.

For more information about *stty* see the stty(1) entry in your UNIX documentation.
