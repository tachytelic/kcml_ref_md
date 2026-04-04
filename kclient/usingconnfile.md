# <span id="usingaclientconnectionfile"></span> Using a client connection file

Once the file has been created you can log into the application by just clicking the icon in Explorer.

On a remote connection you can use a connection file defined for one particular user with another userid by right clicking the icon and choosing the *'Connect as user…'* option. This causes the client to disregard any user or password information stored in the connection file and reprompt for login details.

If the connection is set to cache the password and you have changed it on the server then the next login attempt will fail and reprompt for a password. If the new password is correct it will be cached for use by subsequent logins. Alternatively the password on the [Connection page](connectionpage.htm) can simply be corrected prior to logging in.

Connection files are regular files and can be copied, renamed and linked using explorer. If renaming be careful to preserve the special hidden .kcc extension.
