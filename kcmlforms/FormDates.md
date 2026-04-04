Dates and times on forms

Forms have special handling in grids and kcmledit controls for the date and time [data types](mk:@MSITStore:kdb.chm::/datatypes.htm) of KCML through the use of the [.type\$](tmp/PROPSTR_TYPE.htm) property. For a date the type is 'D' and for a time it is 'T'. Both these types can be [data aware](DataAwareForms.htm).

The client will format the date according to the locale of client using the settings specified by the user in the Regional Settings option of the Windows Control Panel. Thus a date of 2000-07-20 might be rendered as 20/7/2000 in the UK, 20-07-2000 in Germany and 07/20/2000 in the USA. The Gregorian calendar is always used with a full four digit year and the ability in Far Eastern versions of Windows to set an Era is ignored.

When editing a date the client will skip over the separator automatically w. A zero or out of range date will display as blank and date controls can be set to blank by the user to indicate a null date (i.e. a Julian date value of zero). The client will internally validate the date to be a legal value using a Y2K compliant leap year algorithm and will not allow the focus to leave the control if the date is illegal. A legal year must fall between 1601 and 2199 in the Gregorian calendar. When editing a date entering the character 't' will set the date to todays date. The up and down arrows will adjust the date by +1 and -1 days respectively.

Times are also displayed using the locale and validated by the control with the proviso that 24h notation is always used i.e. 13:00 not 1:00p. There is no null time and blank is not allowed. When editing a time entering 't' will set the time to the current time. The Up and down arrows will adjust the minute field by +1 and -1 minutes respectively and the page up and page down keys will adjust the time by +1 and -1 hours respectively.

There is no attempt to adjust the time to compensate for a time zone difference between the client and the server. The server local timezone is always used.

See the section [Date and Time functions in KCML](mk:@MSITStore:kcmlrefman.chm::/timezone.htm) programs for more about converting dates and times in KCML programs.
