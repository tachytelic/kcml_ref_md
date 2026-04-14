#!/bin/sh
#
# kcml-live.sh - SysV init script to start a KCML Global Partition
#
# A KCML Global Partition is a long-running background process that acts as a
# shared execution environment for KCML programs. It loads a set of library
# partitions (USERLIB) and a start program (STARTFILE) at boot, and remains
# resident to service user sessions and inter-partition calls.
#
# BCDPART (here: 256) sets the maximum partition number KCML may allocate;
# background partitions are assigned downward from this ceiling. The partition
# holds shared COM variables, global subroutines, and database handles
# accessible to all connected users.
#
# This script is intended to be placed in /etc/init.d/ and enabled via
# update-rc.d or a systemd compatibility layer. It uses start-stop-daemon
# to launch KCML in the background and tracks the process via a PID file.
#
### BEGIN INIT INFO
# Provides:          kcml-live
# Required-Start:    $local_fs $remote_fs $network $syslog
# Required-Stop:     $local_fs $remote_fs $network $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start KCML live in background
# Description:       Starts the KCML Global Partition at boot
### END INIT INFO

PATH=/sbin:/bin:/usr/bin:/usr/lbin:/usr/local/kcml:/usr/sbin
NAME=kcml-live
DESC="KCML live"

PIDFILE=/run/${NAME}.pid
LOGFILE=/user1/kcmlbg_live.log
DAEMON=/usr/local/kcml/kcml

HEAPINIT=2048
TERMFILE=/usr/local/kcml/TERMFILE
BCDPART=256
LIBRARY=KOPEN3GB
PROGRAMS=/user1/kopen/D40
USERLIB="GB/libVI,GB/ANSON"

# Uncomment if needed
# LD_PRELOAD=/etc/libmacspoof.so.1.0.1
# MAC_ADDRESS=00:50:04:57:78:D7

STARTFILE="${PROGRAMS}/GB/START"

export PATH HEAPINIT TERMFILE BCDPART LIBRARY PROGRAMS USERLIB
# export LD_PRELOAD MAC_ADDRESS

. /lib/lsb/init-functions

do_start() {
    if [ ! -x "$DAEMON" ]; then
        log_failure_msg "$DAEMON not found or not executable"
        return 1
    fi

    if [ ! -r "$STARTFILE" ]; then
        log_failure_msg "$STARTFILE not found"
        return 1
    fi

    umask 000

    /usr/sbin/start-stop-daemon --start --quiet --background \
        --make-pidfile --pidfile "$PIDFILE" \
        --startas /bin/sh -- -c \
        "exec \"$DAEMON\" -g \"$STARTFILE\" >>\"$LOGFILE\" 2>&1"
    return $?
}

do_stop() {
    /usr/sbin/start-stop-daemon --stop --quiet --retry=TERM/30/KILL/5 --pidfile "$PIDFILE"
    RETVAL=$?
    [ $RETVAL -eq 0 ] && rm -f "$PIDFILE"
    return $RETVAL
}

case "$1" in
    start)
        log_daemon_msg "Starting $DESC" "$NAME"
        if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
            log_progress_msg "already running"
            log_end_msg 0
            exit 0
        fi
        do_start
        log_end_msg $?
        ;;
    stop)
        log_daemon_msg "Stopping $DESC" "$NAME"
        do_stop
        log_end_msg $?
        ;;
    restart|force-reload)
        log_daemon_msg "Restarting $DESC" "$NAME"
        do_stop
        sleep 1
        do_start
        log_end_msg $?
        ;;
    status)
        status_of_proc -p "$PIDFILE" "$DAEMON" "$NAME"
        exit $?
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|force-reload|status}"
        exit 1
        ;;
esac

exit 0
