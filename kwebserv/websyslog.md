Searching the System Log

System logs, especially on Unix systems, tend to very large. Finding a particular log message manually can be time consuming. The *View with filter* page can be used to find specific syslog messages.

### <u>Seach criteria</u>

The **View with filter** page will display a form where you can specify search criteria:

- **Source** : typically the machine name of the server. However, it can identify a remote machine if [syslogd](mk:@MSITStore:kcmlrefman.chm::/syslog.htm) has been setup to record messages from other machines.
- **Message** : the actual log message.
- **Date** & **Time** : when the message was logged.

All these fields accept a [KI_PMATCH](mk:@MSITStore:kdb.chm::/tmp/KI_PMATCH.htm) pattern.\
The **Case sesitive match** checkbox can be used to match the case, default is case-insensitive.

Any log message that matches one or more of these fields will be displayed, the latest log entry is displayed first. In general, you will usually just define a pattern for the **Message** field. Exclusions can be accomplished by prefixing a pattern with an exclamation mark.

### <u>Defining the scope of a seach</u>

The **Range of records to search** and **Maximum number of matches** values can be used to limit how much of the system log you want to search. The default is to find upto 100 matches in 1000 records. If log messages have been found then the **Range of records** value determines how many records the **<u>Next page</u>** will search. If the **Maximum number of matches** limit has been reached, then the **<u>Next page</u>** link will start from the last matching record. These limits can be disabled by setting their values to zero.\
However, it is **not advisable** to set both these values to zero as that would return an unlimited number of matches from a potentially large system log.

### <u>Examples</u>

**Example 1**: Find all records in the most recent 2000 messages that do not contain *cache file*

------------------------------------------------------------------------

\
**Source:**\

\
**Message:**\

\
**Date:**\

\
**Time:**\

\
**Range of records to search:**\

\
**Maximum number of matches:**\

\
Case sensitive match

\

------------------------------------------------------------------------

**Example 2**: Search the entire syslog for the first 10 records that contain *panic*:

------------------------------------------------------------------------

\
**Source:**\

\
**Message:**\

\
**Date:**\

\
**Time:**\

\
**Range of records to search:**\

\
**Maximum number of matches:**\

\
Case sensitive match

\

------------------------------------------------------------------------

##### See Also:

[Machine Type and Overview](overview.htm)\
[Configuring the syslog daemon](mk:@MSITStore:kcmlrefman.chm::/syslog.htm)\
man syslogd\
man syslog.conf
