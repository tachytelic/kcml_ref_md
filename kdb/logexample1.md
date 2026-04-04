Example One

In this example a small log is used to protect against the temporary interruption to the normal running of the system, by an operating system crash or power failure. The log can be initialised by: krecover –m 512 –v 2 –l /tmp/krecover.log

This uses a disk partition of at least 512Mb, and two device names /dev/kisamlogread and /dev/kisamlogwrite

The log could be opened by the following script:

krecover –e –v 2 –l /tmp/krecover.log if \[ \$? != 0 \] then echo Failed to open database journal successfully echo Could not enable logging – see log file else echo Database logging started fi

If there has been a system crash then [krecover](krecover.htm) will first replay the log, then start up normally.

The log could be closed by the following script,

krecover –d –v 2 –l /tmp/krecover.log if \[ \$? != 0 \] then echo Failed to close KDB journal successfully echo Could not disable logging – see log file else \# OK, so far, now try to kill the old daemon krecover –k –v 2 –l /tmp/krecover.log if \[ \$? != 0 \] then echo Failed to close KDB journal successfully echo Could not terminate daemon – see log file else echo Database logging stopped fi fi
