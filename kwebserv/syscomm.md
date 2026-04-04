<span id="syscomm"></span>

System Commands

This page allows an [Admin users](admusr.htm) to execute a simple non-interactive shell command.\
Examples of commands which are **interactive**, and should **NOT** be executed are.

- Any grahical user interface program, such as notepad.
- Any text based program which manipulates terminal attributes using terminal control (tty) protocols. Typical examples are system administration tools such as **smit** on AIX, **sam** on HP-UX, or **sysadm**
- The change password command **passwd**
- Certain versions of the **ping** command which send packets continuously until an interrupt key is pressed.

The command is executed and any output, along with the command's return code displayed. The command is also logged to a history file which can be viewed with the **View log file** link.

##### See Also:

[Remote Adminstration Functions](adminfns.htm)
