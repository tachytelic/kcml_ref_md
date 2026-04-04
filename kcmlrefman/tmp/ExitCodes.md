KCML return codes

The following values can be returned by KCML in certain circumstances. The same values could also be returned by \$END, using the syntax:


    $END return_value

It is therefore sensible to restrict application program return values to the range 1-100, so as not to confuse their return values with those from KCML.

If KCML terminates with one of these exit codes you can also consult the system log (the application event log for NT or syslog for Unix) to see if KCML reports any more specific information.

| Exit code | Reason                                    |
|-----------|-------------------------------------------|
| 0         | Normal successful termination             |
| 101       | Error during initialization               |
| 102       | KCML license expired                      |
| 103       | Client disconnected                       |
| 104       | RETURN CLEAR ALL screen saver             |
| 105       | RETURN CLEAR in screen saver              |
| 106       | Memory error cannot panic                 |
| 107       | Licensing problem                         |
| 108       | CORBA initialization error                |
| 109       | Internal error                            |
| 110       | Internal error                            |
| 111       | Internal error                            |
| 112       | KTERM terminal not in terminal database   |
| 113       | PANIC due to runtime error                |
| 114       | Program error or forced panic             |
| 115       | PANIC statement executed                  |
| 116       | Internal error                            |
| 117       | Internal error                            |
| 118       | Internal error                            |
| 119       | Internal error                            |
| 120       | Internal error                            |
| 121       | Internal error                            |
| 122       | Internal error                            |
| 123       | Internal error                            |
| 124       | Internal error                            |
| 125       | Internal error                            |
| 126       | Unable to open TERMFILE                   |
| 128       | KCML checksum failed                      |
| 129       | Screen saver terminated                   |
| 130       | Terminated on SIGTERM signal              |
| 131       | Runtime only system                       |
| 132       | Wrong grace password                      |
| 133       | Recursive PANIC                           |
| 134       | Unable to find error file                 |
| 135       | Unable to find terminal file              |
| 136       | Error in shm or semaphore                 |
| 137       | Read failed - disconnected                |
| 138       | Select failed - read disconnected         |
| 139       | Write failed - disconnected               |
| 140       | Select failed - write disconnected        |
| 141       | Internal error during startup             |
| 142       | Unable to load CORBA shared lib           |
| 143       | Unable to allocate heap                   |
| 144       | Unable to allocate \#PART                 |
| 145       | Unable to allocate \#TERM                 |
| 146       | Unable to determine ttyname               |
| 147       | Memory error creating \$PSTAT             |
| 148       | Invalid KCML command line                 |
| 150       | Unable to open registry TERMFILE key      |
| 151       | Internal error, session chain enter       |
| 152       | Internal error, session chain exit        |
| 153       | PANIC statement                           |
| 154       | Client version not supported, upgrade     |
| 155       | Terminated on SIGKILL signal              |
| 156       | PANIC while in SOAP method call           |
| 157       | Keep running conection problem            |
| 158       | Unable to find configuration file         |
| 159       | We think we can't write the error message |
| 160       | Exception handler closed the program      |
| 161       | Failed to load environment from kconf.xml |
| 162       | KCML terminated due to signal             |
