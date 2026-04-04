pam_stack.so configuration

Some systems generate, from a configuration tool, an file that is a central definition of how to authenticate a user. This file is typically called *system-auth* which is included by *pam_stack.so*:


    #%PAM-1.0
    auth       required     /lib/security/pam_stack.so service=system-auth
    account    required     /lib/security/pam_stack.so service=system-auth
    password   required     /lib/security/pam_stack.so service=system-auth
    session    required     /lib/security/pam_stack.so service=system-auth

Back to [Linux-PAM](pam.htm#pamLinux)
