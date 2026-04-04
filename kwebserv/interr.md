<span id="interr"></span>

Interrogate Services

The interrogate services page displays the table of [services](systemconf.htm#services). The first, *Connect to Service*, column is link which will invoke KClient to connect to the selected service, provided that the service's [connection](systemconf.htm#services) property is set to **true**.\
If the service defines a database *catalogue*, then the catalogue's filename will be a link to a page which displays all contained database tables.\
A *permissions* file is used by a service, then it is shown as a link to display the contents of that table.\
Services may also define a *tablespace*, a directory where database tables are stored. Selecting the tablespace name will produce a [directory listing](dirlist.htm).

After a link to create a new [service](systemconf.htm#services), there is a table showing the list of global tablespaces, each of the links will produce a [directory listing](dirlist.htm).\
If the [current service](currentsrv.htm) defines it own private tablespaces, then these are shown in a table as well.

Note that if a service defines its own [valid user](systemconf.htm#validusr) and [valid client](systemconf.htm#validip) access control lists, then some of these links may be disabled or missing.

##### See Also:

[Connecting to a Service](connserv.htm), [Kerridge System Configuration](systemconf.htm)
