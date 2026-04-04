## Source control

KCML has specific support for the RCS and CVS source control systems which can be used to track changes in KCML programs. RCS is a basic file oriented stsyem for tracking changes using reverse deltas. It is available from GNU and commercially a number of suppliers such as [MKS](http://www.mks.com). CVS is a superset of RCS that allows large projects with multiple developers to be managed and is the recommended source control system for use with KCML. For more about CVS and how to obtain it see the [CVS FAQ](http://www.cvshome.org). There are implementations for Unix and Windows ([client](http://www.wincvs.org) and [server](http://www.cvsnt.org)).

Programs cannot be on platters - they must be discrete files kept in their source form at least during development. Before release the directories can be compiled using \$COMPILE.

- Developers can keep both the compiled and the master source versions of their programs in the same directory without conflict as ascii programs have a distinctive .src extension. By setting byte 46 of [\$OPTIONS RUN](mk:@MSITStore:kcmlrefman.chm::/$OPTIONS_RUN.htm#BYTE46) to BIN(4) KCML can be instructed to load the compiled version of a file unless there is an ascii version with a .src extension which is newer. In that case it will compile the ascii program first and load the compiled version. With this setting KCML will SAVE both ascii and compiled forms of the program.
- An even better convention is to just use source format while developing and to compile programs only for testing and deployment. This allows the developer to take advantage of the [conditional compilation](mk:@MSITStore:kcmlrefman.chm::/NEWASCII.htm) features introduced with KCML 6.2. Setting byte 46 of [\$OPTIONS RUN](mk:@MSITStore:kcmlrefman.chm::/$OPTIONS_RUN.htm#BYTE46) to BIN(5) enables this mode as as with the previous mode, where a .src extension will be added to filenames but there will be no check for a compiled version nor will one be saved..

Source control systems store the master copies of programs in a repository, usually on a server and developers check out a copy of the system with all its programs onto their own machines or their own directory on the server. They can modify the programs, test them and then commit their changes back to the repository. CVS will allocate and track the versions and is capable of reconstructing the system for any given date or build tag.

A unique and powerful feature of CVS is that it allows several developers to work on the same sources at the same time and it delays conflict resolution until checkin. If modifications do not conflict then it can merge both sets of changes together but if the same statements are changed then it marks the program lines in question with chevrons showing the repository version and the developers version and asks the developer to resolve the conflict before allowing the commit e.g.


    <<<<<<
    IF (a == b) THEN c = x+y
    ======
    IF (a == b) THEN c = y+x
    >>>>>>

KCML will parse the chevrons allowing a program with a conflict to be loaded into the Workbench but they are considered to be resolve time errors so the program cannot be executed until the conflict is resolved. The F7 shortcut key can be used to find the first line in conflict and the the CTRL-W CVS match key can toggle between the alternatives. The SHIFT-CTRL-W key will select the alternative containing the cursor and the CTRL-Q shortcut will delete the selected text and the matching chevrons.

The [\$Id](mk:@MSITStore:kcmlrefman.chm::/$ID.htm) keyword can be used to tag a program with its CVS version number and date last edited. This tag is expanded whenever a program is checked out of the respository.
