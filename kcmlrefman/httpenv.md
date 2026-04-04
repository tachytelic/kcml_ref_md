| Variable | Meaning |
|----|----|
| AUTH_TYPE | Contains the authentication method used to validate the Web browser, if any is used. An example of an authentication method is a username/password scheme. |
| CONTENT_LENGTH | The length of the user-provided content from the Web page requesting the CGI script, which is sent via the user's Web browser. Because the user-provided content is passed to the CGI script as a string, this value is in bytes, with each byte representing one character. |
| DOCUMENT_ROOT | The directory from which the web documents are served. |
| CONTENT_TYPE | Contains the type of the data that accompanies the browser's request for the CGI script. Examples are text/html or image/jpeg. |
| GATEWAY_INTERFACE | Holds the version of the Common Gateway Interface being used. For version 1.1 of the CGI specification, this variable would be CGI/1.1. |
| PATH_INFO | Holds additional path information for the CGI script. This is usually the virtual path to another document in the document root that the CGI script will use. This value is set from the information appended to the URL requesting the CGI script. |
| PATH_TRANSLATED | Holds additional path information for the CGI script. This is usually the virtual path to another document in the document root that the CGI script will use. This value is set from the information appended to the URL requesting the CGI script. |
| QUERY_STRING | Contains the user-provided data when the request method is GET. This data is appended along with a question mark to the referenced URL. For example, in the URL http://www.kcml.com/cgi-bin/who.kcml?State=UK, the QUERY_STRING would be "state=UK." |
| REMOTE_ADDR | Stores the IP address of the machine running the Web browser requesting the CGI script. |
| REMOTE_HOST | Stores the domain name of the machine running the Web browser requesting the CGI script. If this information is unavailable to the Web server, REMOTE_ADDR will be set and REMOTE_HOST will not be set. |
| REMOTE_IDENT | Stores the user's login name only if the Web server supports identification. |
| REMOTE_USER | Stores the username the Web browser specified for authentication. This is only set if the server supports authentication and the CGI script is protected. |
| REQUEST_METHOD | Contains the request method used to request the CGI script. This can contain any of the valid HTTP request methods such as GET, HEAD, POST, PUT, and so on. |
| SCRIPT_NAME | Stores the virtual path and name of the CGI script being executed. This is used for self-referencing URLs. |
| SERVER_NAME | Contains the name, either domain name or IP address, of the machine running the Web server. |
| SERVER_PORT | Contains the port number on which the Web browser sent the request to the Web server. |
| SERVER_PROTOCOL | Contains the name and version of the protocol being used to make the request for the CGI script. In most cases, this will be the HTTP protocol and will look something like HTTP/1.0. |
| SERVER_SOFTWARE | Stores the name and version of the Web server software that executed the CGI script. For example, for the Microsoft IIS5 on Win2k it would be set to "Microsoft-IIS/5.0" |

**CGI Environment Variables** {border="0" cellpadding="5" width="100%"}

In addition to the CGI environment variables, the Web server makes available all the HTTP request headers received from the Web browser. These are also placed in environment variables, all of which have the prefix HTTP\_. Table 2 lists the HTTP request header environment variables.

**HTTP Request Header Environment Variables**

HTTP Request Header

Meaning

HTTP_ACCEPT

Contains a comma-separated list of media types the browser can accept in response from the Web server. Examples are audio/basic, image/gif, text/\*, \*/\*. The last two examples contain the wildcard \*, which is a stand-in for any string of characters. text/\* means that all forms of text can be accepted; \*/\* means that the browser will accept any content type.

HTTP_ACCEPT_LANGUAGE

Contains the browser's preferred language for a response from the Web server. However, responses in any language not specified in this variable are allowed. An example is en_UK, which is UK English.

HTTP_AUTHORIZATION

Contains authorization information from the Web browser. Its value is used for the browser to authenticate itself with the Web server. There is not a single specific format for possible values of this field, and new formats may be added. One example is the user/password scheme, where the value, in my case, would be user fred:mypassword.

HTTP_FROM

Contains the name of the requesting user as supplied by the Web browser in an e-mail address format. Current browsers do not send this for reasons of privacy.

HTTP_PRAGMA

Holds the value of any special directives for the Web server. For instance, a proxy Web server has one valid value for a pragma request header, no-cache, which means that the proxy server should always request the document from the real Web server instead of returning a nonexpired cached copy.

HTTP_REFERER

Contains the URI (uniform resource identifier, which is a superset of URLs) of the document that contained the link to the currently requested document. An example would be http://www.thepalace. com/web-pages.html.

HTTP_USER_AGENT

Contains the name of the Web browser software that requested the document. An example is "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)" for IE5.5 running on Windows 2000.
