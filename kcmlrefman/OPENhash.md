OPEN \#

General form:\
\
     OPEN \[#stream,\] filename \[,mode\] \[,perms\] \[,buffersize\]\
\

------------------------------------------------------------------------

The OPEN \#statement is used to open and/or optionally create the specified file on the specified *stream*. If the stream is specified it must have previously been selected to a native operating system directory with the [SELECT \#](SELECT_DISK.htm) statement. Any file previously open on the stream is first closed.

It is also possible to have KCML allocate the stream from a pool of free streams and return it as the value of the function. In this case you do not specify the stream and you must use OPEN in the context of a numeric function. Such streams will be automatically closed on a [RUN](RUN.htm) or [LOAD](LOAD.htm) to permit interactive development. The stream allocated will be the highest free stream in the pool.

The *mode* parameter determines how the file is to be treated once opened. The valid settings for the mode parameter are show in the table below.

The *perms* parameter specifies the default permissions to be set on the file when it is created. The permissions are specified as a string with a leading zero followed by three octal digits following the format of the Unix umask command. The three trailing octal digits represent the user, group and public permissions for the file. Each digit can be set as follows:

| Permission | Octal digit |
|------------|-------------|
| Read       | 4           |
| Write      | 2           |
| Execute    | 1           |

\
Therefore, to make the file readable and writeable by the owner and the members of the owners group, but only readable to all other users you would set the permissions to "0664". Although the execution bit can be set it is clearly not relevant here. The permissions mask is also ignored on Windows versions.

OPEN \# file modes.

| Mode | Description |
|----|----|
| r | Open for read operations only. Writing to the file will give an error. Open will fail if the file does not exist. |
| w | Open for write operations only. If the file exists then its contents are destroyed. |
| a | Open file for appending. A new file is created if the file does not exist. |
| r+ | Open for both read and write operations. Error if the file does not exist. |
| w+ | Open for both read and write operations. If the file exists then its contents are destroyed. |
| a+ | Open for reading and appending. Create a new file if the file does not exist. |

Additional mode flags

An optional translation flag of "b" or "t" may be appended to the mode to specify how newline translation is to be performed under Windows. These flags are ignored under UNIX. The default is "b" for binary i.e. no translation. The "t" flag tells Windows to translate 0x0A newline characters to the 0x0D 0x0A combination when writing to the file and to drop the 0x0D from the combination when reading from the file.

For both Windows and Unix flags of "s", for synchronous I/O (O_SYNC), and "n", for polling or non-blocking I/O (O_NDELAY), are allowed. These flags were ignored in Windows environments prior to KCML 6.0.

For UNIX and Windows NT it is possible to create and open a named pipe or FIFO by specifying "p" in the mode string.

Both Windows and Unix can open a TCP/IP socket if "@" is used in the mode string. For more about socket support see [Working with TCP/IP sockets](sockets.htm).

| Flag | Description         |
|------|---------------------|
| t    | Windows text mode   |
| b    | Windows binary mode |
| s    | Synchronous writes  |
| n    | Non-blocking reads  |
| p    | Named pipes         |
| @    | TCP/IP socket       |

Under Windows NT named pipes must begin with \\.\pipe\\ Named pipes are not supported by Windows 9x. The process creating the pipe must specify the 'p' mode but the client processes must not. The client processes will block until the server process creates the pipe as pipes do not have any independent existence in NT.

If the mode parameter is not specified then "r+b" is assumed, for open for both read and write operations in Windows binary mode, error if the file does not exist.

The buffersize, if specified, is used to fix the size the buffer used for READ \#. If not specified then a default size is chosen by KCML. Setting an explicit size of zero disables buffering. Byte 3 of \$OPTIONS \# can be inspected to determine whether a buffer has been allocated for a particular stream.

Temporary files

Temporary files can be created with OPEN. For more information see [temporary files](temporary.htm).

Socket options

Options that apply only to sockets can be specified using three letter codes directly following the filename and separated by commas. An option is enabled by being set equal to Y and disabled by being set equal to N e.g.

OPEN \#n, ":8080,RUA=N", "@"

Available options are

| Option | Default | Purpose |
|----|----|----|
| RUA | Y | Reuse a port for a server. The default is Y to allow a server to be restarted within the 4m TIME_WAIT delay time of a half closed socket. Set this to N if you want to error an attempt to restart a server on a port that is in use. |

For more about socket programming see [Working with TCP/IP sockets](sockets.htm).

Example:

OPEN \#1,"./DATAFILE","a+b","0666"\
ERROR mesg\$ = "Error opening file"

In this example the file "DATAFILE" is opened in the current working directory and will be created if it does not already exist. The permissions specify that the file is readable and writable by all users.Example:

SELECT \#1 "."\
OPEN \#1,"DATAFILE","a+b","0666"\
ERROR mesg\$ = "Error opening file"

In this example the file "DATAFILE" is opened in the current working directory and will be created if it does not already exist. The permissions specify that the file is readable and writable by all users.

Syntax examples:

OPEN \#45,filename\$, mode\$\
OPEN \#stream, "DATA1",,mode\$\
OPEN \#9, "NEWFILE", "r+b", "0600", buffer\
stream = OPEN filename\$, mode\$

See also:

[CLOSE#](CLOSEhash.htm), [READ#](READhash.htm), [WRITE#](WRITEhash.htm), [SEEK#](SEEKhash.htm), [\$OPTIONS#]($OPTIONShash.htm)
