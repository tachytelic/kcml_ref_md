# <span id="downloadingfromtheinternet"></span> Downloading from the Internet

The kclient components are available packaged as a downloadable CAB file and digitally signed by Kerridge from our ftp site. The CAB download protocol is supported in Internet Explorer version 3 and later. It is not supported by Netscape.

ftp://ftp.kerridge.com/pub/kcml502/activex/kclient.cab

This public URL can be referenced in your script using the CODEBASE property of the object together with a minimum version number. Kclient version numbers normally take the form 05.02.00.xxxx where xxxx is a build number e.g. 5.02.00.4245 was the current version at the time of writing. In the CODEBASE definition leading zeroes are not required and the minor number is swapped so that 5.2.0 represents 5.0.2. The following clause will ensure that at least version 5.0.2.4245 is installed on the users PC.

CODEBASE="ftp://ftp.kerridge.com/pub/kcml502/ActiveX/kclient.cab#Version=5,0,2,4245"

Internet Explorer checks to see if kclient is already registered on the PC and if not it will fetch the cab file from the URL. If it is registered then it will compare versions and will update if the installed version is less than that specified.
