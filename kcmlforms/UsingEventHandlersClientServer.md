Client server operation

Event processing needs access to the form to read back fields and maybe to modify the form itself. Thus when a user clicks on a button we may want to know the text in an associated edit box. This is all handled automatically by KCML, even in the client-server mode, so there is no need to request further information from the form. (Even on TCP/IP, which has high bandwidth, a request and response can take several hundred milliseconds.) This is achieved for all basic Windows controls by close integration of client and server functionality.
