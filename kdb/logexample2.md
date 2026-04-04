Example Two

In this example a huge log is used to protect against both the temporary interruption to the normal running of the system, by an operating system crash or power failure, and the interruption to the normal running of a system where the data has to be retrieved from a backup, due perhaps to a hard disk failure. The log can be initialised by:

krecover –n –m 9000 -S –v 2 –l /tmp/krecover.log

This uses a disk partition of at least 9Gb, and two device names /dev/kisamlogread and /dev/kisamlogwrite It uses -n to indicate a huge log and –S to indicate that although a huge log is being used, a syncing daemon is also required.

The log could be opened by the following script: krecover –e –n –S –v 2 –l /tmp/krecover.log if \[ \$? != 0 \] then echo Failed to open KDB journal successfully echo Could not enable logging – see log file else echo KDB logging started fi

If there has been a simple system crash then [krecover](krecover.htm) will first replay the log, then start up normally. It is possible that there is a more serious hardware problem, perhaps some of the disks are unavailable, [krecover](krecover.htm) will report errors writing to some files and startup as normal. The log is not lost. Manual intervention will be required however. Once the hardware has been repaired, and any data has been retrieved from a backup, the following is required to force [krecover](krecover.htm) to restore from the start of the log.

Stop the daemon, leaving the log open with

krecover -K

Restore from the open log with: krecover –T –n –S –v 2 –l /tmp/krecover.log echo \$?

The return code should be 0. The log could be closed by the following script:

krecover –d –v 2 –l /tmp/krecover.log if \[ \$? != 0 \] then echo Failed to close KDB journal successfully echo Could not disable logging – see log file else \# OK, so far, now try to kill the old daemon krecover –k –v 2 –l /tmp/krecover.log if \[ \$? != 0 \] then echo Failed to close KDB journal successfully echo Could not terminate daemon – see log file else echo KDB logging stopped fi fi

In this example the log would have to be initialised after every successful backup had been performed, by closing down the log, with the above script, and then,

krecover –n –m 9000 -S –v 2 –l /tmp/krecover.log
