Configuring the syslog daemon

KCML uses the Unix syslog to log warnings and error messages. Additionally KCML applications can use the [WRITE LOG](WRITE_LOG.htm) statement to generate their own log entries. In exceptional circumstances Kclient will directly raise log messages on its servers syslog.

What happens to a log entry is determined by the configuration file */etc/syslog.conf* that the syslog daemon reads on stating up. This is an ascii script file that can be edited with any editor. Blank lines are ignored and lines in which the first nonwhite character is a \# are treated as comments. The configuration file can filter by facility and priority level and can write the message to a logfile, write to the console screen or redirect to another server. KCML 6.00 and later uses a facility code of LOG_LOCAL1, while KCML 5.02 uses the LOG_USER facitity. Both versions use priority levels of LOG_INFO, LOG_WARNING and LOG_ERR. Kclient also uses the LOG_DEBUG level for GPF stack dumps.

A configuration entry in this file is composed of two TAB-separated fields, one for the **selector** and one for the **action**. The selector field contains a semicolon-separated list of priority specifications of the form *facility.level* where **facility** is a system facility, or comma-separated list of facilities, and **level** is the minimum severity of the condition being logged. There are a number of built in codes such as kern, mail, etc. KCML 6 uses the facility code of **local1** and KCML 5.02 uses the **user** facility code for their messages. The facility symbol \* can be used to represent all facilities and the level none means do not send messages from the indicated facility to the selected file. So for example, a selector of \*.debug;mail.none will send all messages except mail messages to the selected file.

The action field indicates where to forward the message. Values for this field can have various forms of which only two are relevant to a KCML site, viz:

- A filename, beginning with a leading slash, which indicates that messages specified by the selector are to be written to the specified file. The file will be opened in append mode.
- The name of a remote host, prefixed with an @, e.g. @server, which indicates that messages specified by the selector are to be forwarded to the syslogd on the named host.

A KCML site could use local1.info;user.info /var/adm/log/kcml.log

to pick up all KCML messages. To get KClient dumps it should log \*.debug /var/adm/log/debug.log

For more about syslog configuration see the man page for syslogd on your system. As logs get bigger with time you may need to add a cron script to rotate the logs on a daily basis though many modern Unix systems will do this automatically.
