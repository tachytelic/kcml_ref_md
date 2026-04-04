Working with TCP/IP sockets

The [OPEN#](OPENhash.htm) statement now supports opening TCP/IP sockets allowing a KCML program to act as either a client or a server on a TCP/IP network.

To act as a client a program can issue an open statement such as

OPEN \#1, "alpha.bigco.com :10000", "@"\
OPEN \#stream, "10.1.1.2:rexec", "@"

The " @" sign in the mode argument specifies that a socket is to be opened. The socket to use is specified in the filename argument with a colon separating the IP address from the port number. Port numbers may be supplied either as numbers or as known service names e.g. telnet or smtp. The server address may be either a numeric IP address in dot notation or a host name if there is a DNS or hosts file available to resolve this name. The OPEN will attempt to connect to that port and if there is no server available to accept the connection it will fail with a D82 error. However if a server does connect then the OPEN will succeed and the stream number may be used in subsequent [\$IF \#]($IF.htm), [READ#](READhash.htm) and [WRITE#](WRITEhash.htm) statements to exchange data with the server. To close the connection use [CLOSE \#](CLOSEhash.htm).

To act as a server a KCML program also issues a [OPEN#](OPENhash.htm) statement but this time it does not have to specify the host address as this is fixed to be the address of the machine on which the program is executing. E.g.

OPEN \#ConnectStream, " :8123", "@"

This [OPEN#](OPENhash.htm) will return immediately but the network layer will be primed to receive connections. You can check for a connection by using a [\$IF \#]($IF.htm) e.g.

a=\$IF \#ConnectStream, timeout

The [\$IF \#]($IF.htm) will return 1 in this example whenever a client connects and zero if the timeout expires. The stream in this form of the statement is reserved for connecting only and once a connection arrives the server program must then issue another [OPEN#](OPENhash.htm) to get the socket to use for sending messages. To get a working socket from a connection pass the initial stream as the filename in a further [OPEN#](OPENhash.htm) thus

OPEN \#MsgStream, \$PRINTF("#%d", ConnectStream), "@"

And then use \#MsgStream in [\$IF \#]($IF.htm), [READ#](READhash.htm), [WRITE#](WRITEhash.htm) and [CLOSE \#](CLOSEhash.htm). The connection stream should only be used in [\$IF \#]($IF.htm) and [CLOSE \#](CLOSEhash.htm). Acting as a server requires more careful programming if a service has to be provided for more than one client at a time. The message streams should be allocated from a pool array and a [\$IF \#]($IF.htm) used to test for messages that need to be processed. A [READ#](READhash.htm) will block if no data is available so use [\$IF \#]($IF.htm) first to see if there is any data available. The work done for each message should be completed as quickly as possible in order to provide a timely response for other clients.

**Note:** server programs on NT require KCML 6.0 or greater and Winsock version 2 to use \$IF to test for an available connection. KCML 5.02 only supported Winsock version 1.1 which provides no way to test for an accepted incoming connection and so a \$IF \#ConnectStream would always return 1. Winsock version 2 ships with NT4, Windows 98 and Windows 2000. It is also available from the Microsoft web site as an patch upgrade for Windows 95.

There is a similar issue with clients testing for the presence of a server using [\$ALARM]($ALARM.htm) and OPEN# which will only work on Unix (all versions) and Windows (\>= 6.0 with Winsock2). The use of a non-blocking socket and \$IF is also possible but again requires 6.0 to work under Windows.

An example of the use of sockets in a client application would be a program that uses the SMTP protocol to send an email message across the Internet. Simple Mail Transfer Protocol (SMTP) defined in [RFC821](http://www.ietf.org/rfc/rfc0821.txt) is the protocol used to transfer email across the internet. If you need to extend this to handle attachments you may find the MIME [RFC2045](http://www.ietf.org/rfc/rfc2045.txt) etc. relevant. Click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard.

REM simple STMP Internet mail program showing use of sockets REM A real program would handle errors better DIM msg\$80 DIM CRLF\$=HEX(0D0A) REM specify the SMTP host and protocol DIM MailHost\$="mail.someisp.com:smtp" REM identify our machine DIM OurHostname\$="me.myco.com" REM message sender and recipient DIM To\$="Jack@customer.com" DIM From\$="Jill@myco.com" DIM subject\$="Fetching a pail of water" REM connect to some SMTP host OPEN \#1, MailHost\$, "@" REM set line mode for replies STR(\$OPTIONS \#1, 2, 1) = HEX(07) REM get the welcome msg IF ('recv() == TRUE) REM say hello to start a conversation msg\$ = "HELO " & OurHostname\$ & CRLF\$ 'send(msg\$) IF ('recv() == TRUE) REM send who msg is from in RFC822 format \<fred@bigco.com\> msg\$ = "MAIL FROM: \<" & From\$ & "\>" & CRLF\$ 'send(msg\$) IF ('recv() == TRUE) REM send who it is for in that format, this can be repeated and REM may be rejected if no such user and host cannot forward msg\$ = "RCPT TO: \<" & To\$ & "\>" & CRLF\$ 'send(msg\$) IF ('recv() == TRUE) REM now send the message ending with a dot on a line of its own msg\$ = "DATA" & CRLF\$ 'send(msg\$) IF ('recv() == TRUE) REM the RFC822 header which ends in a blank line msg\$ = "To: " & To\$ & CRLF\$ & "From: " & From\$ & CRLF\$ 'send(msg\$) msg\$ = "Subject: " & subject\$ & CRLF\$ & CRLF\$ 'send(msg\$) REM send body of message REM a real program should escape singleton dots and the word From FOR i = 1 TO 5 msg\$ = "hello " & \$FMT("###", i) & CRLF\$ 'send(msg\$) NEXT i REM end msg\$ = "." & CRLF\$ 'send(msg\$) IF ('recv() == TRUE) REM we are done msg\$ = "QUIT" & CRLF\$ 'send(msg\$) 'recv() END IF END IF END IF END IF END IF END IF CLOSE \#1 END DEFSUB 'send(msg\$) a = WRITE \#1, RTRIM(msg\$) RETURN a END SUB DEFSUB 'recv() REM read responses in lines REM return mail error code, 2=OK, 3=info LOCAL DIM buf\$256, count, n, cont cont = FALSE WHILE TRUE DO count = READ \#1, buf\$ IF (count \<= 3) THEN RETURN PRINT STR(buf\$,, count) REM get reply code and check for continuation lines IF (NOT cont) THEN CONVERT STR(buf\$,, 3) TO n IF (STR(buf\$, 4, 1) \<\> "-") THEN BREAK cont = TRUE WEND n = INT(n / 100) RETURN (n == 2 OR n == 3 ? TRUE : FALSE) END SUB

See also:

[OPEN#](OPENhash.htm), [CLOSE#](CLOSEhash.htm), [READ#](READhash.htm), [WRITE#](WRITEhash.htm), [\$IF]($IF.htm), [\$OPTIONS#]($OPTIONShash.htm) [\$PRINTF(]($PRINTF.htm)
