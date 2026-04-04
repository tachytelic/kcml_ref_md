# <span id="authenticationoptions"></span> Authentication options

To log into a Unix server the client need only supply a userid and a password from the servers password file. With an NT server this is still the case but there is a further option of authentication transparently using the clients security credentials if the client is logged into the same domain.

| Method | Purpose |
|----|----|
| Always require password | A dialog asking for a userid and password will always appear when a connection is made. The userid can be defaulted from the connection but the password must always be supplied at connection time. The details of the login process are not visible. |
| Text window on connect | Similar to the 'Always require password' but it will force out a text window as soon as the server accepts the connection so that the user can see the login process. Set this to see any error messages if you fail to authenticate using the previous type. |
| Cache Password | You must supply the userid and password which the client will encrypt and save in the current users registry under the server key. They will be used to transparently log in to the server on future connections provided the user has been authenticated locally by logging into Windows on the client PC. |
| NT domain authentication | This assumes an NT server and a client that is securely logged into the same domain using the NTLM protocol. The client is then able to exchange security credentials with the server and be implicitely logged in. |
| NT no logon | This assumes an NT server and a KCML server program that is responsible for its own authentication and security (e.g. Kerridge V8). Not currently implemented. |
