selfid (Unix)

General Form:\
\
selfid \[-abcCdfsvwWx\] \[-t *ms*\] \[-k *kcmladdress*\]\

The *selfid* utility is used to determine and return the exact type of terminal being used. Normally UNIX will make sure that the value of the environment variable [TERM](EnvVars.htm#TERM) is appropriate to the type of terminal you are using. This is done with a terminal database file or by dynamic negotiation over *telnet*. Using *selfid* means that you do not need to maintain your own terminal type database for the value of [KTERM](EnvVars.htm#KTERM), as used by KCML to specify the terminal, if it is different from the TERM value assigned by UNIX.

The utility simply sends a series of sequences to the terminal to determine the terminal type and whether the terminal supports downloadable fonts. Once the type is determined it is echoed out on standard output, for example entering *selfid* on a generic Wyse 60 terminal would return wy60box, as generic Wyse terminals all support downloadable soft fonts. If the terminal did not support softfonts then only wy60 would be returned.

The utility tests for Kclient, WDW, DW, Wyse 60, 99, 120, 160 and 325 terminals, DEC VT100, 220, 320, 420 and 510 terminals, Wang, ACS, and Magna. ANSI and SCO ANSI can not be unambiguously detected this way as these terminals have no terminal identification capability.

As vt100 sequences can potentially hang Wyse terminals *selfid* will check for Wyse first but only if the value of \$TERM starts with 'wy'. If you know you don't have wyse terminals then use -w to avoid the test completely. If you may have wyse terminals but you can't rely on \$TERM being correct then use -W to force a test.

Starting with the KCML 5.03 version of Kclient, the client will negotiate the terminal type and answerback directly over telnet (if the server telnet daemon supports it) or will pass the values across as environment variables on the login prompt using a special feature in login supported on all Unix flavors.  This allows for the instant identification of a Kclient terminal from the existence of the special environment variables [\_KTERM](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#_KTERM) and [\_ANSWERBACK](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#_ANSWERBACK).

**Note:** When sending environment variables with the login prompt spaces are treated as separators. Thus it is not possible to have an answerback containing spaces sent by this method.

The selfid distributed with KCML 5.03 will first check for the environment variables \_KTERM and \_ANSWERBACK and if they are set will reply immediately with the appropriate value without attempting to query the terminal.  This allows existing .profile login scripts to be used unchanged.  If you are not running selfid you could have your scripts check for the \_KTERM and \_ANSWERBACK environment variables and set KTERM or the terminal number directly from them.

Some command line options (-c, -C and -f) only apply to Kclient clients and do not involve identification. See the [kclient manual](mk:@MSITStore:kclient.chm::/selfid.htm) for specifics about these commands.

The best place to use *selfid* would be within the users *.profile* to set the *KTERM* environment variable, and to test whether a softfont should be downloaded. For example:

KTERM=\`selfid\` case \$KTERM in wy60box) cat \$KCMLDIR/wyfont\[12\] ;; vt220box) cat \$KCMLDIR/vt220font ;; vt420box) cat \$KCMLDIR/vt420font ;; esac export KTERM

Note that for Wyse terminals that support downloadable softfonts, *selfid* will always return *wy60box*, and for DEC VT220 and VT320 it will return *vt220box*, and for VT420 and VT510 it will return *vt420box*. If you prefer not to use soft font boxes then use the *-b* flag with *selfid* to tell it not return the box suffix.

If *selfid* does not recognise the terminal then the value of the UNIX environment variable *TERM* is returned. This is what would happen for instance with an ANSI terminal.

If the Kerridge DW or Windows DW terminal emulator is in use then *selfid* will return *dw* regardless of the mode currently in use. This is particularly useful as KCML can automatically switch the emulator from say VT220 mode to KCML mode, thus allowing Wang style box graphics, function keys etc. to be used in KCML. Upon exit from KCML or if a UNIX shell command is executed from within a KCML program or at the immediate mode prompt, KCML will automatically switch back to the original mode. The magna and spx701 terminals also support this capability. To take advantage of this powerful capability make sure that *TERM* is left unaltered and set *KTERM* using *selfid*.

The *selfid* utility can also be used to return the contents of the terminals answerback string that many terminals including Wyse, DEC and the Kerridge range of terminal emulators support. Reading the terminals answerback field is particularly useful when connecting workstations over a network as normally you would not be able to allocate a unique terminal number, returned with the \#TERM function, to a physical terminal. By inserting the desired terminal number into the terminals answerback field, you can force KCML to use that number as its terminal number. This is done by specifying the *-a* flag with the *selfid* utility, for example

FORCETERM=\`selfid -a\` export FORCETERM

If an answerback is not set then *selfid -a* will return nothing, this is not a problem as *FORCETERM* will allocate a partition number counting down from 512 or it will count down from the value of the *BCDPART* environment variable if set.

The command line switches available with the *selfid* utility are as follows:

| Switch | Purpose |
|----|----|
| -a | Instructs *selfid* to return the contents of the terminals answerback field. |
| -b | Instructs *selfid* to only return the true terminal type regardless of font downloading capabilities. |
| -c | Request Kclient command line and echo it in a form that can be used to set environment variables KTERM, WDWVERSION, argc, arg1, arg2 ... using the shell eval command. No identification is performed. |
| -C *bookmark* | Pass the supplied bookmark to the kclient. This must be the last switch as what is left on the line is passed without any further parsing. |
| -f | Force a text window on a Kclient and exit. |
| -k *KCMLaddress* | By default *selfid* will test to see if the terminal type returned exists in the \$KCMLADDR/TERMINFO directory. An alternative directory may be specified after this flag. |
| -s | Run *selfid* in silent mode and set the return code only. It will not echo the terminal type. |
| -t *ms* | Sets a timeout specifies in milliseconds to force *selfid* to terminate. This does not work on some versions of Unix. |
| -v | Display *selfid* version number. |
| -w | Setting this flag instructs *selfid* not to send Wyse sequences, useful if you do not intend to use Wyse terminals as it then executes quicker. |
| -W | Force a check for Wyse terminals even if the value of \$TERM does not start with 'wy' |
| -x | Don't use select for delays. Do not use this unless specified. |
| -? | Display usage message. |

selfid will return the following terminal type strings and numbers

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>type<br />
string</th>
<th>return<br />
code</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr>
<td>unknown</td>
<td>0</td>
<td></td>
</tr>
<tr>
<td>vt100</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>vt220</td>
<td>2</td>
<td></td>
</tr>
<tr>
<td>vt320</td>
<td>3</td>
<td></td>
</tr>
<tr>
<td>vt420</td>
<td>4</td>
<td>vt510 returns this too</td>
</tr>
<tr>
<td>wy<em>xxx</em></td>
<td>6</td>
<td>where <em>xxx</em> is the model number e.g. wy60</td>
</tr>
<tr>
<td>wang</td>
<td>8</td>
<td></td>
</tr>
<tr>
<td>dw</td>
<td>9</td>
<td></td>
</tr>
<tr>
<td>wdw</td>
<td>9</td>
<td></td>
</tr>
<tr>
<td>Kclient</td>
<td>9</td>
<td></td>
</tr>
<tr>
<td>arabicwdw</td>
<td>9</td>
<td>wdw running under Arabic Windows</td>
</tr>
<tr>
<td>ACS</td>
<td>10</td>
<td></td>
</tr>
<tr>
<td>magna</td>
<td>11</td>
<td></td>
</tr>
<tr>
<td>spx701</td>
<td>12</td>
<td></td>
</tr>
</tbody>
</table>

Unless the -b switch is used the following Wyse terminal models will return *wy60box* as the type

60, 99, 120, 160, 325

See also:

Terminal support, [Kclient manual](mk:@MSITStore:kclient.chm::/selfid.htm)
