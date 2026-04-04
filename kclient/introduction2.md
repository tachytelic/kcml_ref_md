# <span id="introduction2"></span> Introduction

The Kerridge KCML client application or Kclient provides the user interface for a KCML program. It is capable of displaying Forms or GUI dialogs under the control of KCML logic executing on a server. The KCML server can be on the same machine (a direct connection) or at the other end of a TCP/IP socket link.

Kclient implements a thin client computing model in that it contains no business logic of its own -- all business logic executes in the KCML server. The client is solely responsible for displaying forms and limits itself to simple functions such as checking the validity of dates or the size of numbers. Generally the client will only interrupt the server in response to user events that the server has declared an interest in handling, e.g. the clicking of a button.

The client implements a local persistent cache held on disk so that once a form definition, or a form component such as a bitmap, has been sent to the client then it can be held locally and need not be resent if that form is redisplayed subsequently. This makes very efficient use of bandwidth on a WAN connection which at the same time giving a rich GUI interface.

For legacy applications Kclient is also capable of displaying Text Forms reproducing a 25x80 terminal emulation inside of a window. It supports both VT220 and KCML Extended emulations.
