Transaction Logging and the KDB Journal

The KCML database access layer, KISAM, supports two important features of databases, transactions and a journal. The transactions can be used to guarantee that a group of changes to several KDB tables are atomic. The journal can be used to protect the KDB tables from loss of data or corruption due to a system failure. These two features can be enabled separately or together. It is not necessary to have a journal to use transactions.

KDB Journal

The KDB journal can be configured with two possible disaster scenarios in mind. The first is to protect KDB tables from possible loss of data or corruption caused by an interruption to the normal running of a system, such as an operating system crash or power failure. Updates to tables can be held in disk buffers for some time. These updates are not written if the system crashes. To improve this situation, but retain the performance advantage of delayed writes and cached reads, copies of all database writes are made to a log file. In the event of a system crash the utility program [krecover](krecover.htm) reads this log and re-writes the logged entries

The second scenario is an interruption to the normal running of a system where the data has to be retrieved from a backup, due perhaps to a hard disk failure. After the hardware has been repaired and the backup restored the utility program [krecover](krecover.htm) reads the log and re-writes the logged entries.

In both cases this log file should be a raw disk partition, with no buffering. This ensures that everything written to the log really is recorded on the disk. For best performance the log partition should be on a disk of its own. This will minimize disk head movement.

When only a minor interruption to normal running is envisaged, a smaller log device is adequate. When the end of the log is reached KCML loops back to the beginning and reuses the log. Replaying the log over this loop back period is catered for. It is important to ensure that the operating system performs a given delayed write before that write’s log entry is overwritten. To this end KCML starts a daemon process that periodically flushes the operating system buffers and notes the fact in the log. This syncs the disk buffers a default of every 5 minutes. In the event of a system crash the [krecover](krecover.htm) utility replays the log from the last but one sync entry. It is assumed that every write older than this has really been performed.

When a more serious hardware failure is envisaged a much larger log is required to record all database writes since the last backup. The log obviously can’t be reused until another successful backup has been performed.

A small area of shared memory is used to co-ordinate the sharing of the log file, and to indicate that a journal exists and is enabled. It also indicates the current end of the log file. This allows KCML processes to find the current end of the log and write to it with no disk head movement.

It is possible to use the KDB journal to protect against both the above disaster scenarios at the same time. A large log is required, which can’t be reused until another successful backup has been taken. In addition a daemon process periodically flushes the operating system buffers and notes the fact in the log.

After a failure of the first type, a temporary interruption to the normal running of a system, the [krecover](krecover.htm) utility replays the log from the last but one sync entry. The log is not restarted, it continues to be used as before – ensuring continued protection from both scenarios.

After a failure of the second type the hardware is repaired and the backup restored. The [krecover](krecover.htm) utility is then used to read the whole log and re-write the logged entries. Again, the log is not restarted, ensuring continued protection from both scenarios.
