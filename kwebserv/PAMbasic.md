pam_unix.so configuration

This is the most basic PAM configuration which directly authenticates against the local password database, eg */etc/passwd* and */etc/shadow*.


    #%PAM-1.0
    auth       required     /lib/security/pam_unix2.so
    account    required     /lib/security/pam_unix2.so
    password   required     /lib/security/pam_unix2.so
    session    required     /lib/security/pam_unix2.so

Back to [Linux-PAM](pam.htm#pamLinux)
