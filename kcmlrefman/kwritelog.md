kwritelog

General Form:\
\
kwritelog \[-l level\] message

------------------------------------------------------------------------

The kwritelog utility writes a message to the [system log](syslog.htm). It provides the same functionality [WRITE LOG](WRITE_LOG.htm) KCML statement, but can be used in command shell scripts. This can be useful for scripts which are executed during system startup or are used to start and stop background daemons.

The optional *-l level* flag can be used to log the message at different severity level. These are

| Level | Purpose             | Unix level code |
|-------|---------------------|-----------------|
| 0     | Information message | LOG_INFO        |
| 1     | Warning message     | LOG_WARNING     |
| 2     | Error message       | LOG_ERR         |

\
If no level is specified the message will be logged at level 0.

Example:



    kwritelog -l 1 "Starting background deamon ..."

    # Start the daemon
    /usr/app/start_daemon.ksh
    rc=$?
    if [ "$rc" = "0" ]
    then
        kwritelog "Daemon has started"
    else
        kwritelog -l 2 "Daemon failed to start, error code $rc"
    fi
