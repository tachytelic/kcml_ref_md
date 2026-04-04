Date and Time functions in KCML

KCML generally uses [Julian dates](JulianDate.htm) to represent a date in a database as an integer day number in a standardized epoch. Todays Julian date is available with the [\#DATE](_DATE.htm) function. To represent the date in a string you can use [CONVERT DATE](CONVERT_DATE.htm) to get an [ISO-8601](http://www.iso.ch/markete/8601.pdf) date in YYYY-MM-DD format. It is also available as a YYYYMMDD with the \$TODAY function. The deprecated DATE function returned todays date as YYMMDD. These date functions all use local time.

Times are represented by a count of the number of seconds since midnight local time. The [\#TIME](_TIME.htm) function will return the time this way. To get the same infomation in a HHMMSS string the [TIME](TIME.htm) function can be used or [CONVERT TIME](CONVERT_TIME.htm) can be used to convert \#TIME to an ISO-8601 time string with the format of HH:MM:SS. These times are all local times.

Time stamps are best implemented using the [\$TIMESTAMP]($TIMESTAMP.htm) function which returns the current date and time in terms of the number of milliseconds since 0000 GMT year 0000 (one day before 1 January 0001). Note that this is not a local time and is with respect to GMT on operating systems that implement timezones. This is an unsigned binary integer returned as a six byte string.

Both Unix and NT understand the concept of timezones and can be setup to use GMT time internally with local time available by specifying the timezone. This means that system times such as timestamps on files are held in GMT. Unix systems can use the TZ environment variable to do this per process, usually setting it in the .profile login script if different from the system default. On NT the timezone can be set per user with a profile. Windows 95 and 98 do not distinguish internally between GMT and local time and always operate on local time.

The difference in minutes between local time in the timezone and GMT is stored in bytes 43 and 44 of [\$MACHINE]($MACHINE.htm#BYTE43) as a two byte signed value. This will be negative for timezones east of Greenwich Prime Meridian. Any daylight saving time bias will be negative e.g. in the UK, where TZ=GMT0BST, the value of this \$MACHINE field will be -60 in the summer, reflecting the one hour BST bias, and in winter it will be zero. In the eastern part of the US and Canada, where TZ=EST5EDT, in summer it will be 240 and in winter 300. The timezone offset in \$MACHINE is recalculated each time the TIME, DATE or \$TIME functions are executed. If KCML is running across a change of daylight saving time then this will be taken into account only if TIME, DATE or \$TIME is first called.

TZoffset = VAL(STR(\$MACHINE,43),-2)

See Also

[\#DATE](_DATE.htm)\
[DATE](DATE.htm)\
[\$TODAY]($TODAY.htm)\
[\#TIME](_TIME.htm)\
[TIME](TIME.htm)\
[\$TIME]($TIME.htm)\
[\$TIMESTAMP]($TIMESTAMP.htm)\
[CONVERT TIME](CONVERT_TIME.htm)\
[CONVERT DATE](CONVERT_DATE.htm)\
[\$MACHINE]($MACHINE.htm)\
