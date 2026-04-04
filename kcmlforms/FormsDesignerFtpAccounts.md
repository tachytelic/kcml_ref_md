Managing FTP accounts in the Forms Designer

This dialog allows the management of FTP accounts. It is invoked from the FTP Open dialog as part of creating a picture object. An FTP account defined the userid and password to be used to access a specified server which must be offering an FTP service.

The dialog lists all the accounts currently defined, (together with the server, userid and default directory,) and allows the creation of a new account or the editing or deletion of an existing one.

<img src="bitmaps/FtpAccounts.png" data-border="0" width="401" height="209" alt="FTP accounts dialog" />

Both the New and the Edit buttons will invoke the dialog below. The delete button deletes the selected account.

<img src="bitmaps/NewFtpAccount.png" data-border="0" width="315" height="253" alt="Edit FTP account dialog" />

|  |  |
|----|----|
| Account name | A suitable name for the account that will be referenced in the [FTP open dialog](FormsDesignerFtpPics.htm). |
| Host | The hostname of the server as either a numeric IP address or a TCP/IP host name defined in a DNS or a local hosts file. |
| Username | A valid user account name for that server. |
| Password | A corresponding password for the account |
| Anonymous | Some servers may allow anonymous access (logging in with a userid of anonymous and a special password). Checking this box will do this without you having the supply a userid or password. The files available with this sort of access may be restricted. |
| Initial Directory | If you do not wish to start from the usual home directory corresponding to the supplied userid then you can specify another directory here. This should be available to that user though this will not be checked until the account is used. |
