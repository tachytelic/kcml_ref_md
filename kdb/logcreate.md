Creating the KDB Journal

The performance of the KDB journal depends heavily on the systems performance when writing to the log device. Log writes to a dedicated device require little or no head movement which can help performance. If the disk used for the log device is also used for some other purpose, such as a filesystem then this situation can be spoilt by the disk having to seek to some other part of the disk, and then back to the log device. The log device should be a high performance disk devoted to the purpose of logging.

Two device names are used for the KDB journal. One is used by the KCML processes to write synchronously to the log. This is a raw character (c) device. The second is used by [krecover](krecover.htm) to read from the log. This is a block (b) device. The use of a block device for reading should give optimum [krecover](krecover.htm) performance as block devices benefit from the disk cache and read ahead.

A raw partition should be available. The block (b) and character (c) entries for this device should be linked to /dev/kisamlogread (b) and /dev/kisamlogwrite (c). Different names may be used if [krecover](krecover.htm) is informed of the fact via its -r and -w options. For example on one Unix machine the disk c1t0d0 is being used.

\$ \$ ls -l /dev/\*/c1t0d0 brw-r----- 1 bin sys 31 0x010000 Feb 2 15:48 /dev/dsk/c1t0d0 crw-r----- 1 bin sys 188 0x010000 Feb 2 15:48 /dev/rdsk/c1t0d0 \$ \$ /sbin/mknod /dev/kisamlogread b 31 0x010000 \$ /sbin/mknod /dev/kisamlogwrite c 188 0x010000 \$ \$ ls -l /dev/kisam\* brw-rw-rw- 1 root sys 31 0x010000 Feb 3 09:37 /dev/kisamlogread crw-rw-rw- 1 root sys 188 0x010000 Feb 4 10:28 /dev/kisamlogwrite \$

To initialize the journal:

\$ \$ krecover -m 500 -v 2 -l /tmp/myLog \$

This will create and initialise the required shared memory and log file. In this case a maximum size of 500Mb has been set. The verbosity level set to 2, and any output will go to /tmp/mylog rather than the default of *stdout*. As the *-n* option is not used, we have elected to use a small looping log. This will also start the background syncing daemon.

verbose values used by [krecover](krecover.htm):

|       |     |                            |
|-------|-----|----------------------------|
| == 0  |     | silent - no error messages |
| \>= 1 |     | error messages - default   |
| \>= 2 |     | status and file names      |
| \>= 3 |     | headers                    |
| \>= 4 |     | sub headers                |

KCML processes can now be started and their database updates will be logged. To close the log ALL foreground KCML processes should be terminated, then a SIGTERM or SIGHUP should be sent to the daemon. This may be done by 'shutdown'. This can also be done by [krecover](krecover.htm) –k, which gets the daemons PID from shared memory, and sends a SIGTERM to it. More details of initialisation, startup and shutdown follow.
