Network printing

Kprint<sup>TM</sup> is a Kerridge product that acts as an LPD print server taking raw text as input and producing rich printer output by merging the output with locally cached forms specifications. For more about the product see <http://www.kcml.com/kprint>. LPD is a network printing protocol supported on both Unix and NT and also natively by many network connected printers.

You can access Kprint queues from a KCML program running on a Unix server by [\$DEVICE]($DEVICE.htm#)ing them as a [spooled Unix printer](UnixPrinting.htm#Spooler) thus

\$DEVICE /015="\|lp -d kprintq"

assuming that *kprintq* is the name of a Kprint queue previously setup with lpadmin.

However it may be better to access the printer directly over the LPD protocol as this will work with both Unix and NT environments. When accessing a kprint server from NT you will need to either using a LPD printer driver or, more usually, access the queue directly from the program using the LPD=Y qualifier in [\$DEVICE]($DEVICE.htm) e.g. \$DEVICE /015="kprintq@kprintserver LPD=Y" \$DEVICE /016="queue2@10.0.1.10,LPD=Y"

The server hostname after the @ and the @ character itself are not required if the server is on the same computer as the KCML process.

The LPD=Y mechanism may also work with some network connected printers that support LPR/LPD. Usually the printer queue name is arbitrary (check with your printer documentation).
