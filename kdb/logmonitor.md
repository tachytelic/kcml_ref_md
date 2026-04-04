Monitoring Logging Activity

The [krecover](krecover.htm) utility allows a system administrator to monitor the journalling subsystem and its log. Issuing krecover –i shows the settings held in the shared memory and then in the header of the log. These will only be the same just after the shared memory has been synced with the log.

Points of interest in this output include the maximum size of the log and the current offset into it. When set up as a large log this will tell how full the log is. From the previous and last sync offsets, and the sync pause, the rate of output to the log can be calculated. The last PID indicates the last process to perform a database update. The enabled and transaction mode flags indicate the mode of operation. These flags are bit fields where,

transaction mode byte is built up from:

|      |                                   |
|------|-----------------------------------|
| 0x01 | KDB transaction logging ON        |
| 0x02 | check that tables are locked      |
| 0x04 | take transaction system lock      |
| 0x08 | take KDB logging system lock      |
| 0x10 | ERR if transaction locking is off |
| 0x20 | automatic KI_ROLLBACK on error    |
|      |                                   |

enabled byte is built up from:

|      |                                         |
|------|-----------------------------------------|
| 0x01 | KDB transactions enabled                |
| 0x02 | also write to log – sync daemon         |
| 0x04 | large log, no sync daemon               |
| 0x08 | force sync daemon, even with a huge log |

The current daemon PID indicates that the syncing daemon, if present, is alive and well. The daemon can also be checked by ps –eaf \| fgrep krecover

Issuing krecover –t –v 2 will tail the log, giving details of tables that are being written to. Increasing the verbosity level to 3 will show where in the tables the changes are being made. An interrupt will be required to stop the [krecover](krecover.htm) output.

It is possible to issue krecover –d to disable and krecover –e to enable the log while KCML processes are running. This will obviously invalidate the log, as while the log is disabled database writes are not recorded in the log. It can, however, be useful for testing the relative performance with and without the log.

Again for testing purposes, krecover –d –k –D ‘d’isables logging, ‘k’ills off the daemon, and ‘D’eletes the shared memory. This leaves a clean sheet from which to restart logging. Issuing krecover –s forces a sync, from shared memory to the log.
