LOAD ASCII <span style="font-size: 16pt ; ">command</span>

------------------------------------------------------------------------

General Form:\
\
     LOAD ASCII strexpr\
\
Where:\
\
     strexpr                = the name of a file\
\

------------------------------------------------------------------------

This command allows the loading and compiling of an ASCII file into memory, merging it with any program text already there. It is a command and is therefore not programmable however since KCML 3.0 [LOAD](LOAD.htm) itself can load programs in source form.

The file names are searched for in the current working directory irrespective of any [SELECT DISK](SELECT_DISK.htm) or [SELECT \#0](SELECT_DISK.htm). However, full Unix/DOS pathnames may be used.

Such files may contain immediate mode statements and commands; these will be executed line by line as the file is read during the [LOAD ASCII](LOAD_ASCII.htm) command. However you should not use RUN, LOAD (of an ascii program), \$COMPILE or LOAD ASCII in such scripts. The command is more or less equivalent to [SELECT CI](SELECT_CI.htm) and redirects the keyboard to a file.

Example:

Using a Unix or Windows editor, e.g 'vi' or 'NOTEPAD', a script is created containing the following lines:

RENAME EACH\$ TO RECORD\$\
RENAME QUICK\$ TO WORK\$\
RENAME '100 TO 'GET_NEXT_RECORD

Then when editing a program, entering [LOAD ASCII "map"](LOAD_ASCII.htm) will execute the [RENAME](RENAME.htm) commands for the program currently in memory.

See also:

[LOAD](LOAD.htm), [SAVE ASCII](SAVE_ASCII.htm)
