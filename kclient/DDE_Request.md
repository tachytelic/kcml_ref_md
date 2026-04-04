DDE Requests

A DDE request is when a client application wants the server to pass it a chunk of data. The client application will connect to the server on a particular topic, and then will request data associated with a particular "item" of the topic. Item’s do not need to be registered with the DDML like topics, but the DDE server will need to check the item string that was passed and return the appropriate data. For example, a DDE client application may specify a record name as the topic, and a particular field it is interested in as the item. The DDE server will check this item string and pass back the relevant field. Hence, the DDE structure of a server may look a little like this:

<img src="bitmaps/DDE_Request.gif" data-align="BOTTOM" data-border="0" alt="DDE object heirarchy" />

In this example, the DDE server supports 2 topics, and "Topic 1" has two data items associated with it. If a client wishes to obtain data on "Item 2" it will connect to the server called "Server", on the topic "Topic 1". It will then make a DDE request for data on item "Item 2", which in turn the DDE server will return.
